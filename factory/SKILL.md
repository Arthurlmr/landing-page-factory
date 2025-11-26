# Landing Page Factory Skill

## Purpose

This skill enables Claude to generate multiple high-quality, production-ready SaaS landing pages from a single brief. Each generation produces 3-4 distinct visual variants while maintaining consistent content and brand identity.

## How It Works

1. **Input**: A YAML brief file containing brand info, content, and preferences
2. **Process**: Claude reads the brief + factory config and generates landing pages
3. **Output**: Multiple HTML files, each with a different visual theme

## File Structure

```
factory/
├── SKILL.md                 # This file
├── structure.md             # Section templates and content structure
├── design-system.md         # Design rules, spacing, typography
└── themes/
    ├── modern-dark.json     # Dark theme (Stripe-like)
    ├── light-minimal.json   # Light minimalist theme
    ├── bold-gradient.json   # Bold with gradients
    └── corporate-clean.json # Professional corporate
```

## Generation Rules

### 1. Read the Brief
Parse the YAML brief to extract:
- `brand`: Company name, colors, fonts, logo
- `content`: Hero text, features, use cases, methodology, CTAs
- `preferences`: Which themes to generate, animation level, sections to include

### 2. Apply Structure
Follow `structure.md` to ensure each landing page has:
- Consistent section ordering
- Required content blocks
- Proper semantic HTML structure
- Accessibility standards (ARIA labels, contrast ratios)

### 3. Apply Themes
For each requested theme in `themes/`:
- Load the theme JSON
- Apply color palette via CSS variables
- Apply typography (font families, sizes, weights)
- Apply component styles (cards, buttons, badges)
- Apply animation presets

### 4. Generate Variants
Each variant should feel distinctly different:
- **modern-dark**: Dark backgrounds, subtle glows, glassmorphism
- **light-minimal**: White space, clean lines, subtle shadows
- **bold-gradient**: Vibrant gradients, bold typography, dynamic shapes
- **corporate-clean**: Professional, grid-based, conservative colors

### 5. Output Format
Generate complete, standalone HTML files:
- All CSS inline in `<style>` tags
- All JS inline in `<script>` tags
- Google Fonts loaded via CDN
- Fully responsive (mobile-first)
- No external dependencies

## Content Injection Points

The brief YAML maps to these content areas:

```yaml
brand:
  name: → Logo text, footer, meta title
  colors:
    primary: → CTAs, accents, highlights
    secondary: → Backgrounds, headings
    accent: → Hover states, badges
  fonts:
    heading: → H1-H6 font-family
    body: → Body text font-family

content:
  hero:
    badge: → Hero badge text
    title: → H1 main title
    highlight: → Gradient/colored word in title
    description: → Hero paragraph
    cta_primary: → Main button text
    cta_secondary: → Secondary button text
    stats: → Array of {value, label}
  
  problems:
    title: → Section title
    description: → Section intro
    items: → Array of {icon, title, description}
    stat: → {value, text} highlight box
  
  solution:
    title: → Section title
    description: → Section intro
    items: → Array of {icon, title, description, badge}
  
  features:
    title: → Section title
    items: → Array of {icon, title, description, color}
  
  use_cases:
    title: → Section title
    tabs: → Array of {icon, title, benefits[]}
  
  methodology:
    title: → Section title
    steps: → Array of {number, title, description}
  
  complementary:
    title: → Section title
    items: → Array of {icon, title, description, link}
  
  cta:
    title: → Final CTA title
    description: → CTA paragraph
    button: → Button text
    features: → Array of trust indicators
```

## Quality Checklist

Before outputting, verify each landing page:

- [ ] All brand colors correctly applied
- [ ] All content from brief injected
- [ ] Responsive at 1200px, 900px, 600px breakpoints
- [ ] Animations smooth and performant
- [ ] Links have hover states
- [ ] Buttons have focus states
- [ ] Semantic HTML structure
- [ ] No console errors
- [ ] Lighthouse score > 90

## Example Prompt to Claude

```
Read the brief at briefs/todo/client-brief.yaml and generate landing pages.

Use the factory skill at factory/SKILL.md.
Apply themes: modern-dark, light-minimal, bold-gradient.

Output files to outputs/{brand-name}/:
- {brand-name}-dark.html
- {brand-name}-light.html  
- {brand-name}-bold.html
```

## Customization

### Adding New Themes
1. Create a new JSON file in `themes/`
2. Follow the schema in existing themes
3. Reference it in the brief's `preferences.themes` array

### Adding New Sections
1. Update `structure.md` with the new section template
2. Add content mapping in this SKILL.md
3. Update brief template with new fields

### Modifying Design System
Edit `design-system.md` to change:
- Spacing scale
- Typography scale
- Border radius values
- Shadow definitions
- Animation timings
