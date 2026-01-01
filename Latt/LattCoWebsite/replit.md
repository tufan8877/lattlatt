# Latt & Co GmbH Website

## Overview

This is a static, multi-page marketing website for Latt & Co GmbH, an electrical and plumbing services company based in Vienna, Austria. The site is designed to showcase their services, enable customer contact, and provide information about career opportunities. It operates as a purely client-side application with no backend infrastructure, focusing on fast load times, SEO optimization, and accessibility compliance.

The website serves both B2C customers (homeowners needing electrical/plumbing work) and B2B clients (property management companies), with dedicated pages for each audience segment.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Technology Stack:**
- **HTML5** - Semantic markup for all pages
- **Tailwind CSS (CDN)** - Utility-first CSS framework loaded via CDN (`https://cdn.tailwindcss.com`)
- **Vanilla JavaScript** - No frameworks; minimal JS for mobile navigation

**Design Decisions:**
- **Static Site Approach**: No build process or bundlers required. All pages are standalone HTML files that can be served directly from any web server or static hosting platform.
- **CDN-Based Styling**: Tailwind CSS is loaded from CDN with inline configuration to define custom brand colors (`latt-red: #E30613`, `latt-blue: #0066B3`). This eliminates the need for a build step while maintaining design consistency.
- **Mobile-First Responsive Design**: Uses Tailwind's responsive utilities with breakpoints for mobile/tablet/desktop views.

**Accessibility Features:**
- WCAG 2.1 AA compliance target
- Skip-to-content links on all pages
- ARIA labels and roles for navigation elements
- Focus management for interactive elements
- Semantic HTML structure

**Page Structure:**
- `index.html` - Homepage with service overview and CTAs
- `dienstleistungen.html` - Services catalog
- `hausverwaltungen.html` - B2B property management services
- `notdienst.html` - 24-hour emergency service information
- `sanierung.html` - Renovation services
- `jobs.html` - Career opportunities
- `lehrlinge.html` - Apprenticeship program
- `kontakt.html` - Contact information
- `impressum.html` - Legal imprint (required in Austria)
- `datenschutz.html` - Privacy policy

### Navigation System

**Implementation:**
- Sticky header navigation on all pages
- Mobile hamburger menu with JavaScript toggle
- Close-on-outside-click functionality
- Consistent navigation structure across all pages

**JavaScript Functionality (`js/main.js`):**
- Mobile menu toggle with ARIA state management
- Event delegation for outside-click detection
- No dependencies on external JavaScript libraries

### SEO Strategy

**On-Page Optimization:**
- Semantic HTML5 structure
- Meta descriptions and keywords on all pages
- Open Graph tags for social media sharing
- Structured data (JSON-LD) for local business information on homepage
- Descriptive page titles following pattern: "[Topic] – [Description] | Latt & Co GmbH Wien"

**Technical SEO:**
- `noindex, nofollow` on legal pages (impressum, datenschutz) to avoid duplicate content issues
- Semantic heading hierarchy (h1 → h2 → h3)
- Alt text for images
- Click-to-call and email links with proper protocols

### Call-to-Action Strategy

**Primary CTAs:**
- Phone: `tel:+4314813099` (appears throughout site)
- Email: `mailto:office@latt.at`
- 24-hour emergency service highlighted on multiple pages

### Brand Identity

**Color Scheme:**
- Primary Red: `#E30613` (latt-red) - Used for CTAs and emphasis
- Primary Blue: `#0066B3` (latt-blue) - Secondary brand color
- Neutral palette from Tailwind defaults for text and backgrounds

**Visual Elements:**
- Logo: `/assets/images/logo.png` (16:9 aspect ratio, h-16 in header)
- Consistent typography using system font stack

### Content Strategy

**Language:** German (Austria)
**Tone:** Professional, trustworthy, service-oriented
**Target Audiences:**
- Homeowners needing electrical/plumbing services
- Property management companies
- Job seekers and apprentices

### Responsive Breakpoints

Following Tailwind's default breakpoints:
- Mobile: < 640px
- Tablet: 640px - 1024px  
- Desktop: > 1024px

Specific behavior:
- Mobile menu visible on `lg:hidden` (< 1024px)
- Desktop navigation visible on `hidden lg:flex` (≥ 1024px)

## External Dependencies

### Third-Party Services

**Tailwind CSS CDN:**
- URL: `https://cdn.tailwindcss.com`
- Purpose: CSS utility framework for styling
- Configuration: Inline via `<script>` tag with custom color theme
- Rationale: Eliminates build process; trade-off is larger initial payload but acceptable for small static sites

### Assets and Media

**Company Logo:**
- Path: `/assets/images/logo.png`
- Usage: Header navigation on all pages
- Requirements: Must exist at this path for site to render correctly

### External Links

**Austrian Business Registry (WKO):**
- Company maintains membership number 0648381
- Expected link to WKO profile from impressum page

**Schema.org Structured Data:**
- LocalBusiness schema on homepage
- Includes geocoordinates (48.2148, 16.3319)
- Contact information and address structured for search engines

### Analytics and Tracking

**Current State:** No analytics, tracking pixels, or third-party scripts implemented
**Privacy Consideration:** Site explicitly states "no personal data processing" and "no personalized cookies"

### Browser Compatibility

**Target Support:**
- Modern browsers with ES6+ support
- CSS Grid and Flexbox support required
- No polyfills included

**Rationale:** Vanilla JavaScript approach assumes modern browser baseline; company's target demographic (Vienna-based property owners/managers) likely uses up-to-date browsers.

### Hosting Requirements

**Server Requirements:**
- Static file hosting capability
- No server-side processing needed
- No database required
- HTTPS recommended for trust signals

**Deployment Platforms:**
- Compatible with: Replit Static, Netlify, Vercel, GitHub Pages, any traditional web host
- No build command needed
- No environment variables required