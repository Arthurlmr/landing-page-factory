#!/usr/bin/env python3
"""
Landing Page Factory - Generation Script (with Streaming)

This script reads a brief YAML file and generates multiple landing page
variants using the Claude API with streaming for long requests.

Usage:
    python generate.py briefs/todo/project-brief.yaml
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
FACTORY_PATH = Path("factory")
OUTPUT_PATH = Path("outputs")


def load_yaml(file_path: str) -> dict:
    """Load and parse a YAML file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def load_file(file_path: Path) -> str:
    """Load a text file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def load_factory_context() -> str:
    """Load all factory files into a context string."""
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
    
    # Load all themes
    themes_path = FACTORY_PATH / "themes"
    if themes_path.exists():
        for theme_file in themes_path.glob("*.json"):
            theme_content = load_file(theme_file)
            context_parts.append(f"# Theme: {theme_file.name}\n\n```json\n{theme_content}\n```")
    
    return "\n\n---\n\n".join(context_parts)


def generate_landing_page(client: anthropic.Anthropic, brief: dict, theme: str, factory_context: str) -> str:
    """Generate a single landing page variant using Claude with streaming."""
    
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
1. Le thème "{theme}" (applique toutes ses couleurs, fonts, effets)
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
            # Print progress dots
            if len(response_text) % 1000 == 0:
                print(".", end="", flush=True)
    
    print()  # New line after progress dots
    
    # Clean up if wrapped in markdown code blocks
    if response_text.startswith("```html"):
        response_text = response_text[7:]
    if response_text.startswith("```"):
        response_text = response_text[3:]
    if response_text.endswith("```"):
        response_text = response_text[:-3]
    
    return response_text.strip()


def process_brief(brief_path: str):
    """Process a single brief file and generate all theme variants."""
    
    print(f"\n{'='*60}")
    print(f"Processing: {brief_path}")
    print(f"{'='*60}")
    
    # Load brief
    brief = load_yaml(brief_path)
    project_name = brief.get('project', {}).get('name', 'unnamed')
    themes = brief.get('preferences', {}).get('themes', ['modern-dark'])
    
    print(f"Project: {project_name}")
    print(f"Themes: {', '.join(themes)}")
    
    # Create output directory
    output_dir = OUTPUT_PATH / project_name
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Load factory context
    factory_context = load_factory_context()
    
    # Initialize Claude client
    client = anthropic.Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY")
    )
    
    generated_files = []
    
    # Generate each theme variant
    for theme in themes:
        print(f"\n→ Generating {theme} variant...")
        
        try:
            html_content = generate_landing_page(client, brief, theme, factory_context)
            
            # Validate we got HTML
            if not html_content.strip().startswith("<!DOCTYPE") and not html_content.strip().startswith("<html"):
                # Try to find HTML in the response
                doctype_pos = html_content.find("<!DOCTYPE")
                if doctype_pos != -1:
                    html_content = html_content[doctype_pos:]
                else:
                    html_pos = html_content.find("<html")
                    if html_pos != -1:
                        html_content = html_content[html_pos:]
            
            # Save file
            output_file = output_dir / f"{project_name}-{theme}.html"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print(f"  ✓ Saved: {output_file}")
            generated_files.append(str(output_file))
            
        except Exception as e:
            print(f"  ✗ Error generating {theme}: {str(e)}")
    
    # Create manifest
    manifest = {
        "project": project_name,
        "generated_at": datetime.now().isoformat(),
        "brief_file": brief_path,
        "themes": themes,
        "files": generated_files
    }
    
    manifest_file = output_dir / "manifest.json"
    with open(manifest_file, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"\n✓ Manifest saved: {manifest_file}")
    print(f"✓ Generated {len(generated_files)} landing page(s)")
    
    return generated_files


def main():
    """Main entry point."""
    
    if len(sys.argv) < 2:
        print("Usage: python generate.py <brief1.yaml> [brief2.yaml] ...")
        sys.exit(1)
    
    # Check for API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
    
    brief_files = sys.argv[1].split()
    
    all_generated = []
    
    for brief_file in brief_files:
        brief_file = brief_file.strip()
        if brief_file and os.path.exists(brief_file):
            generated = process_brief(brief_file)
            all_generated.extend(generated)
        else:
            print(f"Warning: Brief file not found: {brief_file}")
    
    print(f"\n{'='*60}")
    print(f"COMPLETE - Generated {len(all_generated)} total file(s)")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
