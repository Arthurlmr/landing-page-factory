# Design System

## Overview

This design system defines the visual language for all generated landing pages. It ensures consistency while allowing theme-specific customization.

---

## Spacing Scale

Use consistent spacing based on an 8px grid:

```css
--space-1: 4px;
--space-2: 8px;
--space-3: 12px;
--space-4: 16px;
--space-5: 20px;
--space-6: 24px;
--space-7: 32px;
--space-8: 40px;
--space-9: 48px;
--space-10: 60px;
--space-11: 80px;
--space-12: 100px;
--space-13: 120px;
```

### Application
- **Section padding**: `120px 60px` (desktop), `80px 24px` (mobile)
- **Card padding**: `32px` or `36px`
- **Grid gaps**: `24px` or `32px`
- **Element margins**: Use scale values

---

## Typography Scale

### Font Sizes

```css
--text-xs: 11px;
--text-sm: 13px;
--text-base: 15px;
--text-lg: 17px;
--text-xl: 20px;
--text-2xl: 24px;
--text-3xl: 32px;
--text-4xl: 40px;
--text-5xl: 48px;
--text-6xl: 56px;
--text-7xl: 64px;
--text-8xl: 72px;
```

### Font Weights

```css
--font-light: 300;
--font-regular: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;
--font-extrabold: 800;
```

### Line Heights

```css
--leading-tight: 1.1;
--leading-snug: 1.25;
--leading-normal: 1.5;
--leading-relaxed: 1.7;
--leading-loose: 1.8;
```

### Application

| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| H1 (Hero) | 48-72px | 800 | 1.1 |
| H2 (Section) | 40-52px | 800 | 1.2 |
| H3 (Card) | 18-24px | 700 | 1.3 |
| Body | 15-17px | 400 | 1.6-1.7 |
| Small | 13-14px | 500 | 1.5 |
| Badge | 11-13px | 600 | 1.4 |

### Letter Spacing

```css
--tracking-tighter: -2px;  /* H1 titles */
--tracking-tight: -1px;    /* H2 titles */
--tracking-normal: 0;      /* Body text */
--tracking-wide: 0.5px;    /* Badges, buttons */
```

---

## Border Radius

```css
--radius-sm: 4px;
--radius-md: 8px;
--radius-lg: 12px;
--radius-xl: 16px;
--radius-2xl: 20px;
--radius-3xl: 24px;
--radius-full: 100px;
```

### Application

| Element | Radius |
|---------|--------|
| Buttons | 8-14px |
| Cards | 16-24px |
| Badges/Pills | 100px |
| Icons containers | 12-16px |
| Inputs | 8-12px |

---

## Shadows

### Light Theme Shadows

```css
--shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 12px rgba(0, 0, 0, 0.08);
--shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.1);
--shadow-xl: 0 16px 48px rgba(0, 0, 0, 0.12);
--shadow-2xl: 0 24px 64px rgba(0, 0, 0, 0.15);
```

### Dark Theme Shadows

```css
--shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.2);
--shadow-md: 0 4px 12px rgba(0, 0, 0, 0.3);
--shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.4);
--shadow-xl: 0 16px 48px rgba(0, 0, 0, 0.5);
--shadow-2xl: 0 24px 64px rgba(0, 0, 0, 0.6);
```

### Colored Shadows (for CTAs)

```css
--shadow-primary: 0 8px 40px rgba(var(--primary-rgb), 0.4);
--shadow-primary-hover: 0 12px 50px rgba(var(--primary-rgb), 0.5);
```

---

## Transitions

### Durations

```css
--duration-fast: 150ms;
--duration-normal: 300ms;
--duration-slow: 500ms;
--duration-slower: 800ms;
```

### Easings

```css
--ease-out: cubic-bezier(0.16, 1, 0.3, 1);
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
--ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
```

### Common Transitions

```css
/* Buttons */
transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);

/* Cards hover */
transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);

/* Links */
transition: color 0.3s ease;

/* Scroll animations */
transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
```

---

## Animations

### Keyframes Library

```css
@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(2deg); }
}

@keyframes pulse-glow {
  0%, 100% { box-shadow: 0 0 40px rgba(var(--primary-rgb), 0.3); }
  50% { box-shadow: 0 0 80px rgba(var(--primary-rgb), 0.5); }
}

@keyframes slide-up {
  from { opacity: 0; transform: translateY(60px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes fade-in {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes pulse-dot {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.7; transform: scale(1.2); }
}

@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}
```

### Animation Classes

```css
.animate-on-scroll {
  opacity: 0;
  transform: translateY(40px);
  transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

.animate-on-scroll.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Staggered delays */
.stagger-1 { transition-delay: 0.1s; }
.stagger-2 { transition-delay: 0.2s; }
.stagger-3 { transition-delay: 0.3s; }
.stagger-4 { transition-delay: 0.4s; }
.stagger-5 { transition-delay: 0.5s; }
.stagger-6 { transition-delay: 0.6s; }
```

---

## Component Patterns

### Buttons

```css
.btn {
  border: none;
  padding: 12px 28px;
  border-radius: 8px;
  font-weight: 600;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  font-family: inherit;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 10px;
}

.btn-primary {
  background: linear-gradient(135deg, var(--primary), var(--primary-light));
  color: white;
  box-shadow: var(--shadow-primary);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-primary-hover);
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: white;
}

.btn-large {
  padding: 18px 36px;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 700;
}

.btn-xl {
  padding: 20px 48px;
  border-radius: 14px;
  font-size: 18px;
}
```

### Cards

```css
.card {
  background: rgba(255, 255, 255, 0.03);
  border-radius: 20px;
  padding: 32px;
  border: 1px solid rgba(255, 255, 255, 0.06);
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.card:hover {
  background: rgba(var(--primary-rgb), 0.08);
  border-color: rgba(var(--primary-rgb), 0.2);
  transform: translateY(-8px);
}
```

### Badges

```css
.badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(var(--primary-rgb), 0.1);
  border: 1px solid rgba(var(--primary-rgb), 0.3);
  padding: 8px 16px;
  border-radius: 100px;
  font-size: 13px;
  font-weight: 500;
}
```

### Gradient Text

```css
.gradient-text {
  background: linear-gradient(135deg, var(--primary), var(--accent));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

---

## Responsive Breakpoints

```css
/* Desktop first approach */
@media (max-width: 1200px) {
  /* Large tablets, small desktops */
}

@media (max-width: 900px) {
  /* Tablets */
}

@media (max-width: 600px) {
  /* Mobile */
}
```

### Responsive Rules

| Breakpoint | Section Padding | Grid Columns | Title Size |
|------------|-----------------|--------------|------------|
| > 1200px | 120px 60px | As designed | 48-72px |
| 900-1200px | 100px 40px | Reduce by 1-2 | 40-56px |
| 600-900px | 80px 24px | 1-2 columns | 36-48px |
| < 600px | 60px 20px | 1 column | 32-40px |

---

## Accessibility Standards

### Color Contrast
- Text on backgrounds: minimum 4.5:1 ratio
- Large text (>18px bold): minimum 3:1 ratio
- Interactive elements: minimum 3:1 ratio

### Focus States
All interactive elements must have visible focus states:

```css
.btn:focus-visible {
  outline: 2px solid var(--primary);
  outline-offset: 2px;
}

a:focus-visible {
  outline: 2px solid var(--primary);
  outline-offset: 2px;
}
```

### Motion Preferences

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## Dark vs Light Theme Adjustments

### Dark Theme (default for modern-dark, bold-gradient)
- Background: #0e1624 to #131d2e
- Text: #ffffff (headings), rgba(255,255,255,0.7) (body)
- Cards: rgba(255,255,255,0.03) with rgba(255,255,255,0.06) border
- Hover: Add glow effects

### Light Theme (for light-minimal, corporate-clean)
- Background: #ffffff to #f8f9fa
- Text: #1a1a1a (headings), #4a5568 (body)
- Cards: #ffffff with rgba(0,0,0,0.08) border
- Hover: Add subtle shadows
