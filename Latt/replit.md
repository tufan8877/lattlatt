# Latt & Co GmbH Website

## Overview
A static HTML website for Latt & Co GmbH, a Viennese electrical and plumbing company offering 24-hour emergency services.

## Project Structure
```
latt/
├── server.py          # Python HTTP server (serves static files on port 5000)
├── index.html         # Homepage
├── dienstleistungen.html  # Services page
├── hausverwaltungen.html  # Property management page
├── sanierung.html     # Renovation page
├── notdienst.html     # 24h emergency service page
├── jobs.html          # Jobs page
├── lehrlinge.html     # Apprentice page
├── kontakt.html       # Contact page
├── impressum.html     # Legal notice
├── datenschutz.html   # Privacy policy
├── assets/
│   └── images/
│       └── logo.png   # Company logo
├── attached_assets/   # Additional assets
└── js/
    └── main.js        # JavaScript functionality
```

## Technology Stack
- **Frontend**: Static HTML with Tailwind CSS (via CDN)
- **Server**: Python's built-in HTTP server with no-cache headers
- **Port**: 5000 (0.0.0.0)

## Running the Project
The server runs from the `latt/` directory:
```bash
cd latt && python server.py
```

## Recent Changes
- January 2026: Initial Replit setup
