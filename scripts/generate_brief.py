#!/usr/bin/env python3
"""
Generate creative brief from raw onboarding data using Claude Opus 4.5
"""

import anthropic
import json
import sys
import os

OPUS_PROMPT = """
RÔLE
Tu es directeur artistique senior et stratège conversion. Tu rédiges des briefs créatifs pour la génération de landing pages haute conversion.

DONNÉES DISPONIBLES

## BRANDING (extrait par Firecrawl)
{firecrawl}

## CONTENU & POSITIONNEMENT (extrait par Perplexity)
{perplexity}

## RECHERCHES COMPLÉMENTAIRES (Gemini Search)
{gemini_search}

## ANALYSE VISUELLE PAGE ACTUELLE (Vision)
{vision}

## RÉPONSES CLIENT (formulaire onboarding)
{user_answers}

---

TÂCHE
Génère un brief YAML complet et créatif pour la génération d'une landing page.

TU DOIS DÉCIDER :
1. Le style de background adapté au tone (gradient-mesh, texture, geometric, glassmorphism, noise, solid)
2. Le niveau d'animation (subtle, moderate, bold) selon le secteur
3. La structure des sections (ordre, présence/absence selon données disponibles)
4. Les angles copywriting (hooks percutants, CTA wording)
5. Les éléments de réassurance à prioriser
6. La densité visuelle (airy pour premium, balanced pour B2B, dense pour startup)

RÈGLES CRITIQUES
- Ne JAMAIS inventer de données non présentes dans le contexte
- Si témoignages absents → ne pas inclure la section testimonials
- Si stats absentes → ne pas inclure la section stats
- Adapter la structure au contenu réellement disponible
- Le brief doit être AUTO-SUFFISANT (le générateur de code ne verra QUE ce brief)
- Les textes (headline, subheadline, CTA) doivent être prêts à l'emploi, pas des placeholders

ANTI-SLOP
- Éviter les headlines génériques ("Bienvenue", "Découvrez notre solution")
- Éviter les CTA faibles ("En savoir plus", "Cliquez ici")
- Privilégier des hooks spécifiques au métier du client

FORMAT OUTPUT
Génère UNIQUEMENT le YAML ci-dessous, rien d'autre (pas de ```yaml, pas d'explication) :

client: [nom de l'entreprise]
url_source: [url analysée]
generated_at: [timestamp ISO]

design_system:
  colors:
    primary: "[hex exact de Firecrawl]"
    accent: "[hex exact de Firecrawl]"
    background: "[hex exact de Firecrawl]"
    text_primary: "[hex]"
    text_secondary: "[hex]"
  fonts:
    heading: "[font exacte de Firecrawl]"
    body: "[font exacte de Firecrawl]"
    google_fonts_import: "[URL Google Fonts complète]"
  border_radius:
    buttons: "[valeur de Firecrawl]"
    cards: "[valeur]"
  tone: "[tone de Firecrawl]"

creative_direction:
  background_style: "[gradient-mesh | texture | geometric | glassmorphism | noise | solid]"
  background_details: "[description précise : couleurs du gradient, type de texture, etc.]"
  animation_level: "[subtle | moderate | bold]"
  visual_density: "[airy | balanced | dense]"
  mood: "[description en 3-5 mots]"
  inspiration_notes: "[notes créatives pour le générateur]"

structure:
  - section: hero
    headline: "[8 mots max, percutant, spécifique au métier]"
    subheadline: "[20 mots max, bénéfice principal]"
    cta_primary:
      text: "[texte du bouton]"
      url: "#contact"
    cta_secondary:
      text: "[texte optionnel]"
      url: "[url]"
    visual_type: "[illustration | gradient-shape | product-mockup | none]"
    
  - section: social_proof
    type: "[logos | stats | badges | mixed]"
    headline: "[optionnel]"
    items:
      - "[item 1]"
      - "[item 2]"
    
  - section: problem_solution
    headline: "[titre de section]"
    problems:
      - icon: "[emoji]"
        text: "[problème 1]"
    solutions:
      - icon: "[emoji]"
        text: "[solution 1]"
        
  - section: features
    headline: "[titre]"
    subheadline: "[sous-titre optionnel]"
    layout: "[grid-3 | grid-2 | list | cards]"
    items:
      - icon: "[emoji]"
        title: "[titre feature]"
        description: "[description courte]"
        
  - section: testimonials
    headline: "[titre]"
    layout: "[slider | grid | single]"
    items:
      - quote: "[citation exacte si disponible]"
        author: "[nom]"
        role: "[fonction, entreprise]"
        
  - section: cta_final
    headline: "[titre percutant]"
    subheadline: "[sous-titre]"
    cta_text: "[texte bouton]"
    form_fields: "[email | email+name | email+name+phone | none]"
    
  - section: footer
    style: "[minimal | standard | expanded]"
    links:
      - text: "[lien]"
        url: "[url]"

content:
  company_name: "[nom]"
  tagline: "[baseline si disponible]"
  value_proposition: "[proposition de valeur principale]"
  services:
    - "[service 1]"
    - "[service 2]"
  benefits:
    - "[bénéfice 1]"
    - "[bénéfice 2]"
  target_audience: "[cible principale]"
  differentiators:
    - "[différenciateur 1]"
    - "[différenciateur 2]"

seo:
  title: "[60 chars max]"
  description: "[155 chars max]"
  
notes_for_generator: |
  [Instructions spéciales pour le générateur de code HTML.
  Exemples : "Utiliser un dégradé mesh avec les couleurs primary vers accent",
  "Les cards doivent avoir un effet glassmorphism subtil",
  "Animation fade-in au scroll sur chaque section"]
"""

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_brief.py <path_to_raw_data.json>")
        sys.exit(1)
    
    raw_data_path = sys.argv[1]
    
    # Charger les données brutes
    with open(raw_data_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
    
    client_name = raw_data.get('client_name', os.path.basename(raw_data_path).replace('.json', ''))
    
    # Préparer le prompt
    prompt = OPUS_PROMPT.format(
        firecrawl=json.dumps(raw_data.get('firecrawl', {}), indent=2, ensure_ascii=False),
        perplexity=raw_data.get('perplexity', 'Non disponible'),
        gemini_search=json.dumps(raw_data.get('gemini_search', {}), indent=2, ensure_ascii=False),
        vision=json.dumps(raw_data.get('vision', {}), indent=2, ensure_ascii=False),
        user_answers=json.dumps(raw_data.get('user_answers', {}), indent=2, ensure_ascii=False)
    )
    
    # Appeler Opus 4.5
    client = anthropic.Anthropic()
    
    print(f"Génération du brief pour {client_name}...")
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=8192,
        messages=[{"role": "user", "content": prompt}]
    )
    
    brief_yaml = response.content[0].text
    
    # Nettoyer si nécessaire (enlever ```yaml si présent)
    if brief_yaml.startswith("```"):
        brief_yaml = brief_yaml.split("\n", 1)[1]
    if brief_yaml.endswith("```"):
        brief_yaml = brief_yaml.rsplit("```", 1)[0]
    
    # Créer le dossier briefs si nécessaire
    os.makedirs("briefs", exist_ok=True)
    
    # Sauvegarder
    output_path = f"briefs/{client_name}.yaml"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(brief_yaml.strip())
    
    print(f"Brief généré : {output_path}")
    
    # Afficher stats
    usage = response.usage
    print(f"Tokens utilisés : {usage.input_tokens} in / {usage.output_tokens} out")

if __name__ == "__main__":
    main()
