# Landing Page Structure Template

## Overview

This document defines the standard structure for all generated landing pages. Each section has a specific purpose, content requirements, and HTML structure.

## Section Order (Default)

1. Navigation (fixed)
2. Hero
3. Problems / Pain Points
4. Solution Overview
5. Features (detailed)
6. Use Cases / Benefits by Role
7. Methodology / How It Works
8. Complementary Offerings (optional)
9. Final CTA
10. Footer

---

## Section 1: Navigation

### Purpose
Fixed navigation bar for branding and quick access to sections.

### Required Elements
- Logo (text or image)
- Navigation links (4-5 max)
- Primary CTA button

### HTML Structure
```html
<nav class="nav">
  <a href="#" class="nav-logo">{brand.name}</a>
  <div class="nav-links">
    <a href="#solution" class="nav-link">Solutions</a>
    <a href="#features" class="nav-link">Fonctionnalités</a>
    <a href="#usecases" class="nav-link">Cas d'usage</a>
    <a href="#" class="nav-link">Ressources</a>
    <a href="#cta" class="btn btn-primary">{content.hero.cta_primary}</a>
  </div>
</nav>
```

### Design Rules
- Position: fixed, top: 0
- Background: semi-transparent with blur
- Z-index: 1000
- Height: 70-80px
- Padding: 20px 60px

---

## Section 2: Hero

### Purpose
Capture attention immediately. Present the main value proposition.

### Required Elements
- Badge/pill (social proof or positioning)
- H1 title with highlighted word
- Description paragraph (2-3 sentences)
- Primary CTA button
- Secondary CTA button (optional)
- Stats row (3 metrics)
- Visual element (dashboard preview, illustration, or image)

### HTML Structure
```html
<section class="hero">
  <!-- Background elements -->
  <div class="hero-bg-orb"></div>
  <div class="hero-grid"></div>
  
  <div class="hero-container">
    <div class="hero-content">
      <div class="hero-badge">
        <span class="hero-badge-dot"></span>
        <span class="hero-badge-text">{content.hero.badge}</span>
      </div>
      
      <h1 class="hero-title">
        {content.hero.title} <span class="gradient">{content.hero.highlight}</span>
      </h1>
      
      <p class="hero-description">{content.hero.description}</p>
      
      <div class="hero-buttons">
        <a href="#cta" class="btn btn-primary btn-large">{content.hero.cta_primary}</a>
        <button class="btn btn-secondary btn-large">{content.hero.cta_secondary}</button>
      </div>
      
      <div class="hero-stats">
        <!-- Repeat for each stat -->
        <div class="hero-stat">
          <div class="hero-stat-value">{stat.value}</div>
          <div class="hero-stat-label">{stat.label}</div>
        </div>
      </div>
    </div>
    
    <div class="hero-visual">
      <!-- Dashboard preview or illustration -->
    </div>
  </div>
</section>
```

### Design Rules
- Min-height: 100vh
- Padding-top: 140px (account for fixed nav)
- Two-column layout on desktop (content | visual)
- Single column on mobile
- Title: 48-72px, font-weight 800
- Description: 18-22px, opacity 0.7

---

## Section 3: Problems / Pain Points

### Purpose
Create empathy by identifying customer pain points. Build urgency.

### Required Elements
- Section title
- Section description
- 4-6 problem cards with icon, title, description
- Highlight stat (optional but recommended)

### HTML Structure
```html
<section id="problems" class="problems-section">
  <div class="section-container">
    <div class="section-header">
      <h2 class="section-title">
        {content.problems.title} <span class="gradient">{highlight}</span>
      </h2>
      <p class="section-description">{content.problems.description}</p>
    </div>
    
    <div class="problems-grid">
      <!-- Repeat for each problem -->
      <div class="problem-card">
        <div class="problem-card-icon">{icon}</div>
        <h3 class="problem-card-title">{title}</h3>
        <p class="problem-card-desc">{description}</p>
      </div>
    </div>
    
    <div class="stat-highlight">
      <div class="stat-highlight-value">{content.problems.stat.value}</div>
      <p class="stat-highlight-text">{content.problems.stat.text}</p>
    </div>
  </div>
</section>
```

### Design Rules
- 3-column grid on desktop, 1 column on mobile
- Card hover: lift + border color change
- Stat highlight: gradient background, centered

---

## Section 4: Solution Overview

### Purpose
Present how the product solves the problems. High-level benefits.

### Required Elements
- Section title
- Section description (2-3 paragraphs allowed)
- 4 solution pillars with icon, badge, title, description

### HTML Structure
```html
<section id="solution" class="solution-section">
  <div class="section-container">
    <div class="section-header">
      <h2 class="section-title">{content.solution.title}</h2>
      <p class="section-description">{content.solution.description}</p>
    </div>
    
    <div class="solution-grid">
      <!-- Repeat for each pillar -->
      <div class="solution-card">
        <div class="solution-card-accent"></div>
        <div class="solution-card-icon">{icon}</div>
        <span class="solution-card-badge">{badge}</span>
        <h3 class="solution-card-title">{title}</h3>
        <p class="solution-card-desc">{description}</p>
      </div>
    </div>
  </div>
</section>
```

### Design Rules
- 4-column grid on desktop, 2 on tablet, 1 on mobile
- Cards have accent bar at top
- Background orb for depth

---

## Section 5: Features (Detailed)

### Purpose
Detail specific features. Show depth of product.

### Required Elements
- Section title
- 6 feature blocks with icon, title, description
- Each feature can have unique accent color

### HTML Structure
```html
<section id="features" class="features-section">
  <div class="section-container">
    <div class="section-header">
      <h2 class="section-title">{content.features.title}</h2>
    </div>
    
    <div class="features-grid">
      <!-- Repeat for each feature -->
      <div class="feature-card">
        <div class="feature-card-icon" style="--accent: {color}">{icon}</div>
        <div class="feature-card-content">
          <h3 class="feature-card-title">{title}</h3>
          <p class="feature-card-desc">{description}</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

### Design Rules
- 2-column grid with icon + content layout
- Icons in colored containers
- Longer descriptions allowed (2-3 sentences)

---

## Section 6: Use Cases

### Purpose
Show how different roles/departments use the product.

### Required Elements
- Section title
- Tab navigation (4 tabs)
- Tab content panels with icon, title, benefits list, CTA, visual

### HTML Structure
```html
<section id="usecases" class="usecases-section">
  <div class="section-container">
    <div class="section-header">
      <h2 class="section-title">{content.use_cases.title}</h2>
    </div>
    
    <div class="usecases-tabs">
      <!-- Repeat for each tab -->
      <button class="usecase-tab" data-tab="{index}">
        <span>{icon}</span> {title}
      </button>
    </div>
    
    <div class="usecase-content">
      <!-- Repeat for each panel -->
      <div class="usecase-panel" data-panel="{index}">
        <div class="usecase-content-grid">
          <div>
            <div class="usecase-icon">{icon}</div>
            <h3 class="usecase-title">{title}</h3>
            <ul class="usecase-benefits">
              <!-- Repeat for each benefit -->
              <li class="usecase-benefit">
                <span class="usecase-benefit-check">✓</span>
                {benefit}
              </li>
            </ul>
            <button class="btn btn-primary">Voir la démo</button>
          </div>
          <div class="usecase-visual">
            <!-- Abstract visual representation -->
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

### Design Rules
- Tabs horizontally centered
- Active tab: gradient background
- Panel: card with two-column layout
- Include JavaScript for tab switching

---

## Section 7: Methodology

### Purpose
Reassure prospects about ease of implementation.

### Required Elements
- Section title
- 4 numbered steps with title and description
- Visual connecting line between steps

### HTML Structure
```html
<section id="methodology" class="methodology-section">
  <div class="methodology-container">
    <div class="section-header">
      <h2 class="section-title">{content.methodology.title}</h2>
    </div>
    
    <div class="methodology-steps">
      <div class="methodology-line"></div>
      
      <!-- Repeat for each step -->
      <div class="methodology-step">
        <div class="methodology-step-circle">
          <span class="methodology-step-number">{number}</span>
        </div>
        <h3 class="methodology-step-title">{title}</h3>
        <p class="methodology-step-desc">{description}</p>
      </div>
    </div>
  </div>
</section>
```

### Design Rules
- 4-column layout for steps
- Horizontal line connecting circles (hidden on mobile)
- Numbers in circular badges with gradient

---

## Section 8: Complementary Offerings (Optional)

### Purpose
Cross-sell other products/services. Show breadth.

### Required Elements
- Section title
- 4-6 cards with icon, title, description, link

### HTML Structure
```html
<section id="complementary" class="complementary-section">
  <div class="section-container">
    <div class="section-header">
      <h2 class="section-title">{content.complementary.title}</h2>
    </div>
    
    <div class="complementary-grid">
      <!-- Repeat for each item -->
      <div class="complementary-card">
        <div class="complementary-card-icon">{icon}</div>
        <h3 class="complementary-card-title">{title}</h3>
        <p class="complementary-card-desc">{description}</p>
        <a href="#" class="complementary-card-link">
          En savoir plus <span>→</span>
        </a>
      </div>
    </div>
  </div>
</section>
```

### Design Rules
- 3-column grid
- Cards hover: lift + gradient background

---

## Section 9: Final CTA

### Purpose
Convert. Strong call-to-action.

### Required Elements
- Large title
- Description paragraph
- Primary CTA button
- Trust indicators

### HTML Structure
```html
<section id="cta" class="cta-section">
  <div class="cta-bg-glow"></div>
  <div class="cta-container">
    <h2 class="cta-title">
      {content.cta.title} <span class="gradient">{highlight}</span>
    </h2>
    <p class="cta-description">{content.cta.description}</p>
    
    <div class="cta-buttons">
      <a href="#" class="btn btn-primary btn-xl">{content.cta.button}</a>
    </div>
    
    <p class="cta-features">
      <!-- Repeat for each feature -->
      ✓ {feature}
    </p>
  </div>
</section>
```

### Design Rules
- Centered layout
- Large glowing background orb
- Title: 48-56px
- Max-width: 800px

---

## Section 10: Footer

### Purpose
Legal links, branding, copyright.

### Required Elements
- Logo
- Navigation links
- Copyright text

### HTML Structure
```html
<footer class="footer">
  <div class="footer-container">
    <a href="#" class="footer-logo">{brand.name}</a>
    <div class="footer-links">
      <a href="#" class="footer-link">À propos</a>
      <a href="#" class="footer-link">Blog</a>
      <a href="#" class="footer-link">Contact</a>
      <a href="#" class="footer-link">Mentions légales</a>
    </div>
    <div class="footer-copyright">
      © {year} {brand.name}. Tous droits réservés.
    </div>
  </div>
</footer>
```

### Design Rules
- Dark background
- Three-part layout: logo | links | copyright
- Subtle top border
