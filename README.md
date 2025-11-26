# 🏭 Landing Page Factory

> Générez automatiquement des landing pages SaaS premium à partir d'un simple brief YAML.

![Landing Page Factory](https://img.shields.io/badge/Powered%20by-Claude%20API-orange)
![License](https://img.shields.io/badge/license-MIT-blue)

## 🎯 Concept

Déposez un fichier brief YAML dans `briefs/todo/` → GitHub Actions génère automatiquement 3-4 versions de landing pages avec différents thèmes → Vous êtes notifié sur Slack quand c'est prêt.

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Brief YAML    │ ──▶ │  Claude API     │ ──▶ │  Landing Pages  │
│   (briefs/todo) │     │  + Factory      │     │  (outputs/)     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
                                                        ▼
                                                ┌─────────────────┐
                                                │  Slack Notif    │
                                                │  🚀 C'est prêt! │
                                                └─────────────────┘
```

## 📁 Structure du Projet

```
landing-page-factory/
├── .github/
│   └── workflows/
│       └── generate.yml          # GitHub Action automatique
├── briefs/
│   ├── templates/
│   │   └── brief-template.yaml   # Template à copier
│   ├── todo/                     # 📥 Déposez vos briefs ici
│   └── done/                     # 📤 Briefs traités (archivés)
├── factory/
│   ├── SKILL.md                  # Instructions pour Claude
│   ├── structure.md              # Structure des sections
│   ├── design-system.md          # Règles de design
│   └── themes/
│       ├── modern-dark.json      # Thème sombre (Stripe-like)
│       ├── light-minimal.json    # Thème clair minimaliste
│       ├── bold-gradient.json    # Thème vibrant avec gradients
│       └── corporate-clean.json  # Thème corporate pro
├── outputs/                      # 📦 Landing pages générées
│   └── {project-name}/
│       ├── {project}-modern-dark.html
│       ├── {project}-light-minimal.html
│       └── manifest.json
├── scripts/
│   └── generate.py               # Script de génération
└── README.md
```

## 🚀 Quick Start

### 1. Fork & Clone

```bash
git clone https://github.com/YOUR_USERNAME/landing-page-factory.git
cd landing-page-factory
```

### 2. Configurer les Secrets GitHub

Dans votre repo GitHub → Settings → Secrets and variables → Actions :

| Secret | Description |
|--------|-------------|
| `ANTHROPIC_API_KEY` | Votre clé API Anthropic |
| `SLACK_WEBHOOK_URL` | (Optionnel) Webhook Slack pour notifications |

### 3. Créer un Brief

```bash
cp briefs/templates/brief-template.yaml briefs/todo/mon-projet-brief.yaml
```

Éditez le fichier avec vos informations.

### 4. Push & Enjoy

```bash
git add briefs/todo/mon-projet-brief.yaml
git commit -m "Add brief for mon-projet"
git push
```

Le workflow GitHub Actions se déclenche automatiquement. En ~2 minutes, vos landing pages sont dans `outputs/mon-projet/`.

## 📝 Format du Brief

```yaml
project:
  name: "mon-projet"              # Nom du dossier output
  language: "fr"                  # Langue du contenu

brand:
  name: "Ma Startup"
  colors:
    primary: "#f06422"            # Couleur principale
    primary_light: "#f29f4b"      # Variante claire
    secondary: "#0e1624"          # Couleur secondaire
  fonts:
    heading: "Outfit"             # Police titres (Google Fonts)
    body: "Outfit"                # Police corps

preferences:
  themes:                         # Thèmes à générer
    - "modern-dark"
    - "light-minimal"
    - "bold-gradient"
  animations: "full"              # full | subtle | minimal | none

content:
  hero:
    badge: "..."
    title: "..."
    # ... voir template complet
```

📄 **[Voir le template complet](briefs/templates/brief-template.yaml)**

## 🎨 Thèmes Disponibles

| Thème | Description | Inspiration |
|-------|-------------|-------------|
| `modern-dark` | Sombre avec glows et glassmorphism | Stripe, Linear, Vercel |
| `light-minimal` | Blanc épuré, ombres subtiles | Notion, Figma |
| `bold-gradient` | Gradients vibrants, typo bold | Framer, Webflow |
| `corporate-clean` | Professionnel, conservateur | Salesforce, HubSpot |

### Créer un Thème Custom

1. Dupliquez un thème existant dans `factory/themes/`
2. Modifiez les couleurs, fonts, effets
3. Ajoutez le nom dans votre brief

## ⚙️ Utilisation Locale

### Prérequis

```bash
pip install anthropic pyyaml
export ANTHROPIC_API_KEY="votre-clé"
```

### Générer manuellement

```bash
python scripts/generate.py briefs/todo/mon-brief.yaml
```

## 🔔 Notifications Slack

Pour recevoir une notification Slack :

1. Créez un [Slack Webhook](https://api.slack.com/messaging/webhooks)
2. Ajoutez-le comme secret `SLACK_WEBHOOK_URL`

Vous recevrez :

```
🚀 Landing Pages générées!

Projet: mon-projet
Fichiers générés:
- mon-projet-modern-dark.html
- mon-projet-light-minimal.html
- mon-projet-bold-gradient.html

[📂 Voir sur GitHub]
```

## 🛠️ Personnalisation

### Modifier la Structure

Éditez `factory/structure.md` pour :
- Ajouter/supprimer des sections
- Modifier l'ordre
- Changer le HTML template

### Modifier le Design System

Éditez `factory/design-system.md` pour :
- Spacing scale
- Typography scale
- Border radius
- Shadows
- Animations

### Modifier le Comportement de Claude

Éditez `factory/SKILL.md` pour :
- Règles de génération
- Mapping contenu → HTML
- Quality checklist

## 📊 Coûts Estimés

Avec Claude claude-sonnet-4-20250514 :
- ~$0.10-0.15 par landing page générée
- Brief moyen → 3 thèmes → ~$0.35

## 🤝 Contribution

1. Fork le projet
2. Créez une branche (`git checkout -b feature/amazing`)
3. Commit (`git commit -m 'Add amazing feature'`)
4. Push (`git push origin feature/amazing`)
5. Ouvrez une Pull Request

## 📄 License

MIT License - Utilisez librement pour vos projets !

---

<p align="center">
  Made with 🧡 using Claude API
</p>
