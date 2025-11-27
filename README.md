# Landing Page Factory

Génération automatique de landing pages en 10 minutes.

## 🔄 Workflow complet

```
┌─────────────────────────────────────────────────────────────────┐
│                        FORMULAIRE                                │
│         (utilisateur remplit infos sur son produit)             │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                          N8N                                     │
│                                                                  │
│  1. Firecrawl → Scrape site existant (branding, screenshot)     │
│  2. Perplexity → Recherche contexte marché                       │
│  3. Gemini Vision → Analyse screenshot                           │
│  4. Gemini → Génère le brief YAML (avec PROMPT_GEMINI_N8N.md)   │
│  5. Push le fichier briefs/{client}.yaml sur GitHub             │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                     GITHUB ACTION                                │
│                                                                  │
│  Trigger automatique quand nouveau fichier dans briefs/         │
│                                                                  │
│  1. Détecte briefs/ouisay.yaml                                  │
│  2. Lance: python scripts/generate.py briefs/ouisay.yaml        │
│  3. Claude API génère la landing page (~30 sec)                 │
│  4. Sauvegarde dans outputs/ouisay/test-001/landing.html        │
│  5. Commit + Push                                                │
│  6. Notif Slack (optionnel)                                     │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                        OUTPUT                                    │
│                                                                  │
│  outputs/                                                        │
│  └── ouisay/                                                    │
│      ├── test-001/          ← Premier test                      │
│      │   ├── landing.html                                       │
│      │   └── manifest.json                                      │
│      ├── test-002/          ← Deuxième test (auto-incrémenté)  │
│      │   ├── landing.html                                       │
│      │   └── manifest.json                                      │
│      └── ...                                                    │
└─────────────────────────────────────────────────────────────────┘
```

## 📁 Structure du projet

```
landing-page-factory/
├── briefs/                    # ← N8N upload ici
│   ├── _TEMPLATE.yaml         # Template de référence
│   └── {client}.yaml          # Brief généré par Gemini
│
├── outputs/                   # ← Landings générées ici
│   └── {client}/
│       └── test-{N}/
│           ├── landing.html
│           └── manifest.json
│
├── factory/                   # Instructions pour Claude
│   ├── SKILL.md
│   ├── structure.md
│   ├── design-system.md
│   └── themes/
│       └── light-minimal.json
│
├── scripts/
│   └── generate.py            # Script de génération
│
├── .github/workflows/
│   └── generate.yml           # GitHub Action
│
├── PROMPT_GEMINI_N8N.md       # Prompt pour ton noeud Gemini
└── README.md
```

## 🚀 Setup

### 1. Cloner/Forker le repo

```bash
git clone https://github.com/Arthurlmr/landing-page-factory.git
cd landing-page-factory
```

### 2. Configurer les secrets GitHub

Settings → Secrets and variables → Actions → New repository secret

| Secret | Valeur |
|--------|--------|
| `ANTHROPIC_API_KEY` | `sk-ant-...` |
| `SLACK_WEBHOOK_URL` | (optionnel) |

### 3. Configurer n8n

1. Dans ton workflow n8n, après avoir collecté toutes les données
2. Ajoute un noeud Gemini avec le contenu de `PROMPT_GEMINI_N8N.md`
3. Ajoute un noeud GitHub pour push le YAML généré dans `briefs/{client}.yaml`

## 📝 Format du brief

Le brief YAML doit suivre le format dans `briefs/_TEMPLATE.yaml`.

**Champs obligatoires :**
- `project.name` : Slug du client (ex: "ouisay")
- `brand.company_name` : Nom de l'entreprise
- `brand.colors.primary` : Couleur principale
- `content.hero.title` : Titre principal
- `content.hero.subtitle` : Sous-titre
- `content.features.items` : Liste des features (3-6)

## 💰 Coûts

- **~$0.30** par landing page (Claude API)
- Temps de génération : ~30-60 secondes

## 🔧 Usage manuel (debug)

```bash
# Générer une landing page localement
export ANTHROPIC_API_KEY="sk-ant-..."
python scripts/generate.py briefs/ouisay.yaml

# Ouvrir le résultat
open outputs/ouisay/test-001/landing.html
```

## 🎨 Thème

Actuellement : **Light Minimal**
- Fond blanc (#ffffff)
- Ombres subtiles
- Design épuré et professionnel
- Responsive mobile-first

## 📊 Versioning automatique

Si un client génère plusieurs landings :
- Premier test → `outputs/ouisay/test-001/`
- Deuxième test → `outputs/ouisay/test-002/`
- etc.

Cela permet de faire de l'A/B testing en gardant l'historique.
