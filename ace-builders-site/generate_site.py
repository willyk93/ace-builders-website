#!/usr/bin/env python3
"""Generates the static Ace Builders of Canada Ltd. website from shared
header/footer templates + per-page content blocks. Run: python3 generate_site.py
"""
import os

from icons import icon

ROOT = os.path.dirname(os.path.abspath(__file__))
PHONE = "780-667-8436"
PHONE_TEL = "+17806678436"
EMAIL = "info@acebuilderscan.com"
YEAR = "2026"

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("services.html", "Services"),
    ("projects.html", "Projects"),
    ("certifications.html", "Certifications"),
    ("contact.html", "Contact"),
]

def head(title, desc, page):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Ace Builders of Canada Ltd.</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="assets/img/favicon-192.png">
<link rel="apple-touch-icon" href="assets/img/favicon-192.png">
<meta property="og:title" content="Ace Builders of Canada Ltd. | Building Safely, Building Better">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/logo.png">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body data-page="{page}">
"""

def header_html(active):
    parts = []
    for href, label in NAV_ITEMS:
        cls = ' class="active"' if href == active else ''
        parts.append('        <li><a href="{0}"{1}>{2}</a></li>'.format(href, cls, label))
    links = "\n".join(parts)
    return f"""<header class="site-header">
  <div class="topbar">
    <div class="container">
      <div><span class="topbar-tag">{icon('pin')} Edmonton, Alberta &mdash; Serving Alberta-wide</span></div>
      <div class="topbar-links">
        <a href="tel:{PHONE_TEL}">{icon('phone')} {PHONE}</a>
        <a href="mailto:{EMAIL}">{icon('mail')} {EMAIL}</a>
      </div>
    </div>
  </div>
  <nav class="navbar container">
    <a href="index.html" class="brand">
      <img src="assets/img/logo-nav.png" alt="Ace Builders of Canada Ltd. logo">
      <span class="brand-text">
        <span class="name">Ace Builders of Canada</span>
        <span class="tag">Building Safely, Building Better</span>
      </span>
    </a>
    <ul class="nav-links" id="navLinks">
{links}
    </ul>
    <div class="nav-cta">
      <a href="contact.html" class="btn btn-primary"><span class="long">Get a </span>Free Quote</a>
      <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>
</header>
"""

def footer_html():
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a href="index.html" class="footer-brand">
          <img src="assets/img/logo-nav.png" alt="Ace Builders of Canada Ltd. logo">
          <span class="name">Ace Builders of Canada Ltd.</span>
        </a>
        <p>Edmonton-based specialists in hazardous material abatement, HSE consulting &amp; training, asphalt/concrete solutions, and waste management &amp; recycling. Certified crews. Safety-first, every project.</p>
        <div class="footer-socials" style="margin-top:20px;">
          <a href="#" aria-label="LinkedIn">{icon('linkedin')}</a>
          <a href="#" aria-label="Facebook">{icon('facebook')}</a>
          <a href="#" aria-label="Instagram">{icon('instagram')}</a>
        </div>
      </div>
      <div class="footer-col">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="about.html">About Us</a></li>
          <li><a href="services.html">Our Services</a></li>
          <li><a href="projects.html">Projects</a></li>
          <li><a href="certifications.html">Certifications</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Services</h4>
        <ul>
          <li><a href="services.html#hse">HSE Consulting &amp; Training</a></li>
          <li><a href="services.html#abatement">Hazardous Abatement</a></li>
          <li><a href="services.html#asphalt">Asphalt &amp; Concrete</a></li>
          <li><a href="services.html#waste">Waste Management &amp; Recycling</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Contact</h4>
        <ul>
          <li>{icon('pin')} Edmonton, Alberta, Canada</li>
          <li><a href="tel:{PHONE_TEL}">{icon('phone')} {PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{icon('mail')} {EMAIL}</a></li>
          <li>{icon('clock')} Mon &ndash; Fri, 8:00 AM &ndash; 5:00 PM MT</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; {YEAR} Ace Builders of Canada Ltd. All rights reserved.</span>
      <span>COR Certified &middot; WCB Registered &middot; WHMIS Trained Crews</span>
    </div>
  </div>
</footer>
<script src="assets/js/script.js" defer></script>
</body>
</html>
"""

def page(title, desc, active, body):
    return head(title, desc, active) + header_html(active) + body + footer_html()

def write(filename, content):
    path = os.path.join(ROOT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", filename)

# ---- content modules are appended below by build scripts ----
if __name__ == "__main__":
    import pages
    pages.build(page, write)
