#!/usr/bin/env python3
"""
Landing Page Factory - Single Page Generator

Workflow:
1. n8n uploads brief to: briefs/{client-name}.yaml
2. GitHub Action triggers on push
3. Generates: outputs/{client-name}/test-{N}/landing.html
4. Auto-increments test number if client folder exists

Cost: ~$0.30 per landing page (Claude API)
"""

import os
import sys
import yaml
import json
import anthropic
from pathlib import Path
from datetime import datetime


# Configuration
CLAUDE_MODEL = "claude-sonnet-4-20250514"
MAX_TOKENS = 32000

# Paths
SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent
FACTORY_PATH = ROOT_DIR / "factory"
OUTPUTS_PATH = ROOT_DIR / "outputs"


def load_yaml(file_path: str) -> dict:
    """Load and parse a YAML file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def load_file(file_path: Path) -> str:
    """Load a text file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def load_factory_context() -> str:
    """Load factory instructions."""
    context_parts = []
    
    # Load SKILL.md
    skill_path = FACTORY_PATH / "SKILL.md"
    if skill_path.exists():
        context_parts.append(f"# SKILL.md\n\n{load_file(skill_path)}")
    
    # Load structure.md
    structure_path = FACTORY_PATH / "structure.md"
    if structure_path.exists():
        context_parts.append(f"# structure.md\n\n{load_file(structure_path)}")
    
    # Load design-system.md
    design_path = FACTORY_PATH / "design-system.md"
    if design_path.exists():
        context_parts.append(f"# design-system.md\n\n{load_file(design_path)}")
    
    # Load ONLY light-minimal theme
    theme_path = FACTORY_PATH / "themes" / "light-minimal.json"
    if theme_path.exists():
        theme_content = load_file(theme_path)
        context_parts.append(f"# Theme: light-minimal.json\n\n```json\n{theme_content}\n```")
    
    return "\n\n---\n\n".join(context_parts)


def get_next_test_number(client_dir: Path) -> int:
    """Get next test number for a client (test-001, test-002, etc.)."""
    if not client_dir.exists():
        return 1
    
    existing_tests = [d for d in client_dir.iterdir() if d.is_dir() and d.name.startswith("test-")]
    if not existing_tests:
        return 1
    
    # Extract numbers and find max
    numbers = []
    for test_dir in existing_tests:
        try:
            num = int(test_dir.name.replace("test-", ""))
            numbers.append(num)
        except ValueError:
            continue
    
    return max(numbers) + 1 if numbers else 1


def generate_landing_page(client: anthropic.Anthropic, brief: dict, factory_context: str) -> str:
    """Generate landing page using Claude with streaming."""
    
    brief_yaml = yaml.dump(brief, allow_unicode=True, default_flow_style=False)
    
    prompt = f"""Tu es un expert en création de landing pages SaaS ultra-premium.

## CONTEXTE - FACTORY

{factory_context}

---

## BRIEF CLIENT

```yaml
{brief_yaml}
```

---

## INSTRUCTIONS

Génère une landing page HTML complète en utilisant:
1. Le thème "light-minimal" (fond blanc, design épuré, ombres subtiles)
2. La structure définie dans structure.md
3. Les règles du design-system.md
4. Tout le contenu du brief ci-dessus

IMPORTANT:
- Génère un fichier HTML COMPLET et AUTONOME
- Inclus tout le CSS dans une balise <style>
- Inclus tout le JavaScript dans une balise <script>
- Charge les Google Fonts via CDN
- Le design doit être responsive (mobile-first)
- Ajoute les animations scroll avec Intersection Observer
- Le résultat doit être production-ready
- Style LIGHT : fond blanc (#ffffff), textes gris foncé, accents avec la couleur primaire du client

Réponds UNIQUEMENT avec le code HTML complet, sans explications ni markdown autour. Commence directement par <!DOCTYPE html>
"""

    # Use streaming for long requests
    response_text = ""
    
    with client.messages.stream(
        model=CLAUDE_MODEL,
        max_tokens=MAX_TOKENS,
        messages=[
            {"role": "user", "content": prompt}
        ]
    ) as stream:
        for text in stream.text_stream:
            response_text += text
            if len(response_text) % 1000 == 0:
                print(".", end="", flush=True)
    
    print()  # New line after progress
    
    # Clean up markdown wrappers if present
    if response_text.startswith("```html"):
        response_text = response_text[7:]
    if response_text.startswith("```"):
        response_text = response_text[3:]
    if response_text.endswith("```"):
        response_text = response_text[:-3]
    
    return response_text.strip()


def process_brief(brief_path: str):
    """Process a brief and generate landing page."""
    
    brief_file = Path(brief_path)
    client_name = brief_file.stem  # "ouisay.yaml" → "ouisay"
    
    print(f"\n{'='*60}")
    print(f"Processing: {brief_path}")
    print(f"Client: {client_name}")
    print(f"Theme: light-minimal")
    print(f"{'='*60}")
    
    # Load brief
    brief = load_yaml(brief_path)
    
    # Determine output directory with versioning
    client_dir = OUTPUTS_PATH / client_name
    test_number = get_next_test_number(client_dir)
    test_dir = client_dir / f"test-{test_number:03d}"
    test_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Output: {test_dir}/landing.html")
    
    # Load factory context
    factory_context = load_factory_context()
    
    # Initialize Claude client
    client = anthropic.Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY")
    )
    
    # Generate landing page
    print(f"\n→ Generating landing page...")
    
    try:
        html_content = generate_landing_page(client, brief, factory_context)
        
        # Validate HTML
        if not html_content.strip().startswith("<!DOCTYPE") and not html_content.strip().startswith("<html"):
            doctype_pos = html_content.find("<!DOCTYPE")
            if doctype_pos != -1:
                html_content = html_content[doctype_pos:]
            else:
                html_pos = html_content.find("<html")
                if html_pos != -1:
                    html_content = html_content[html_pos:]
        
        # Save landing page
        output_file = test_dir / "landing.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"  ✓ Saved: {output_file}")
        
        # Save manifest
        manifest = {
            "client": client_name,
            "test_number": test_number,
            "generated_at": datetime.now().isoformat(),
            "brief_file": str(brief_path),
            "theme": "light-minimal",
            "output": str(output_file)
        }
        
        manifest_file = test_dir / "manifest.json"
        with open(manifest_file, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2)
        
        print(f"  ✓ Manifest: {manifest_file}")
        
        return str(output_file)
        
    except Exception as e:
        print(f"  ✗ Error: {str(e)}")
        return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate.py briefs/{client}.yaml")
        print("Example: python generate.py briefs/ouisay.yaml")
        sys.exit(1)
    
    # Check for API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
    
    brief_path = sys.argv[1]
    
    if not os.path.exists(brief_path):
        print(f"Error: Brief file not found: {brief_path}")
        sys.exit(1)
    
    result = process_brief(brief_path)
    
    print(f"\n{'='*60}")
    if result:
        print(f"✓ SUCCESS - Landing page generated")
        print(f"  {result}")
    else:
        print("✗ FAILED - See errors above")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
