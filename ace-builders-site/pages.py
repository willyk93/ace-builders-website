# -*- coding: utf-8 -*-
"""Page body content for the Ace Builders of Canada Ltd. site."""
from icons import icon


def photo_bg(filename, dark=0.92, mid=0.85, light=0.55):
    """Inline background-image style: brand gradient over a photo, for hero/CTA sections."""
    return (
        f"background-image: linear-gradient(120deg, rgba(6,35,26,{dark}) 0%, "
        f"rgba(11,58,39,{mid}) 45%, rgba(20,108,58,{light}) 100%), "
        f"url('assets/img/photos/{filename}');"
    )


def build(page, write):
    write("index.html", page(
        "Home",
        "Ace Builders of Canada Ltd. — Edmonton-based experts in hazardous abatement, HSE consulting, asphalt & concrete, and waste management. Building Safely, Building Better.",
        "index.html",
        HOME_BODY,
    ))
    write("about.html", page(
        "About Us",
        "Learn about Ace Builders of Canada Ltd., our mission, vision, leadership team, and our commitment to safe, sustainable construction and environmental services in Edmonton, Alberta.",
        "about.html",
        ABOUT_BODY,
    ))
    write("services.html", page(
        "Our Services",
        "HSE Consulting & Training, Hazardous Abatement & Surface Preparation, Asphalt & Concrete Solutions, and Waste Management & Recycling — full-service construction & environmental solutions in Edmonton.",
        "services.html",
        SERVICES_BODY,
    ))
    write("projects.html", page(
        "Projects & Capabilities",
        "Explore the types of abatement, construction, paving, and waste-management projects Ace Builders of Canada Ltd. delivers for public, commercial, industrial, and residential clients.",
        "projects.html",
        PROJECTS_BODY,
    ))
    write("certifications.html", page(
        "Certifications & Safety",
        "Ace Builders of Canada Ltd. crews are COR certified, WCB registered, and WHMIS/First Aid trained — safety-first construction and abatement services in Alberta.",
        "certifications.html",
        CERTIFICATIONS_BODY,
    ))
    write("contact.html", page(
        "Contact Us",
        "Get a free consultation and quote from Ace Builders of Canada Ltd. Call 780-667-8436 or send us a message. Edmonton, Alberta.",
        "contact.html",
        CONTACT_BODY,
    ))


# =====================================================================
# HOME
# =====================================================================
HOME_BODY = f"""
<section class="hero has-photo" style="{photo_bg('edmonton-skyline.jpg')}">
  <div class="container hero-inner">
    <div>
      <span class="eyebrow">Edmonton, Alberta &middot; Locally Owned</span>
      <h1>Building Safely, Building Better.</h1>
      <p class="lead">Ace Builders of Canada Ltd. delivers hazardous material abatement, HSE consulting &amp; training, asphalt &amp; concrete solutions, and waste management &amp; recycling &mdash; all under one certified, safety-first team.</p>
      <div class="hero-actions">
        <a href="contact.html" class="btn btn-primary">Get a Free Consultation</a>
        <a href="services.html" class="btn btn-ghost">Explore Our Services</a>
      </div>
      <div class="hero-badges">
        <span class="hero-badge">{icon('shield')} COR Certified</span>
        <span class="hero-badge">{icon('heart-pulse')} WCB Registered Crews</span>
        <span class="hero-badge">{icon('alert')} WHMIS &amp; First Aid Trained</span>
      </div>
    </div>
    <div class="hero-art">
      <div class="stat"><span class="num">4</span><span class="label">Integrated service lines under one roof</span></div>
      <div class="stat"><span class="num">100%</span><span class="label">Certified, WCB-registered crews</span></div>
      <div class="stat"><span class="num">AB</span><span class="label">Edmonton-based, serving all of Alberta</span></div>
      <div class="stat"><span class="num">1</span><span class="label">Call for compliance, abatement &amp; construction</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-header center">
      <span class="eyebrow">What We Do</span>
      <h2>An integrated approach to safety &amp; construction</h2>
      <p>From compliance training to hazardous abatement, paving, and eco-responsible waste disposal &mdash; we combine industry expertise, certified crews, and a strong safety-first culture to deliver reliable, cost-effective results.</p>
    </div>
    <div class="grid grid-4">
      <div class="card service-card">
        <div class="icon-badge">{icon('clipboard-check')}</div>
        <h3>HSE Consulting &amp; Training</h3>
        <p>On-site safety audits, WHMIS training, COR program development, and compliance support.</p>
        <a href="services.html#hse" class="card-link">Learn more {icon('arrow-right')}</a>
      </div>
      <div class="card service-card">
        <div class="icon-badge">{icon('hazmat')}</div>
        <h3>Hazardous Abatement</h3>
        <p>Safe removal of asbestos, lead paint, mould &amp; silica; concrete profiling; water blasting.</p>
        <a href="services.html#abatement" class="card-link">Learn more {icon('arrow-right')}</a>
      </div>
      <div class="card service-card">
        <div class="icon-badge">{icon('road')}</div>
        <h3>Asphalt &amp; Concrete</h3>
        <p>Milling, paving, saw-cutting, compaction, and durable surface finishing.</p>
        <a href="services.html#asphalt" class="card-link">Learn more {icon('arrow-right')}</a>
      </div>
      <div class="card service-card">
        <div class="icon-badge">{icon('recycle')}</div>
        <h3>Waste &amp; Recycling</h3>
        <p>Sorting, roll-off bins, landfill diversion, and eco-responsible disposal.</p>
        <a href="services.html#waste" class="card-link">Learn more {icon('arrow-right')}</a>
      </div>
    </div>
  </div>
</section>

<section class="stats-strip">
  <div class="container">
    <div class="grid">
      <div><div class="stat-num">4</div><div class="stat-label">Core Service Lines</div></div>
      <div><div class="stat-num">COR</div><div class="stat-label">Certificate of Recognition</div></div>
      <div><div class="stat-num">WCB</div><div class="stat-label">Registered Crews</div></div>
      <div><div class="stat-num">15&ndash;20%</div><div class="stat-label">Margin for Quality, Not Corners Cut</div></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-header center">
      <span class="eyebrow">Why Ace Builders</span>
      <h2>Your safety-first construction &amp; environmental partner</h2>
      <p>A unique blend of compliance consulting and hands-on construction services, built by founders who understand both sides of the job.</p>
    </div>
    <div class="grid grid-4">
      <div class="card">
        <div class="icon-badge">{icon('handshake')}</div>
        <h3>One Partner, Full Scope</h3>
        <p>Safety consulting and construction services under one company &mdash; no juggling multiple contractors.</p>
      </div>
      <div class="card">
        <div class="icon-badge">{icon('shield')}</div>
        <h3>Certified Crews</h3>
        <p>COR, WCB, and WHMIS-trained teams that minimize client liability and risk on every site.</p>
      </div>
      <div class="card">
        <div class="icon-badge">{icon('leaf')}</div>
        <h3>Environmentally Responsible</h3>
        <p>Sustainable waste practices and landfill diversion built into how we work, not an afterthought.</p>
      </div>
      <div class="card">
        <div class="icon-badge">{icon('target')}</div>
        <h3>Hazmat Specialists</h3>
        <p>Specialized expertise in projects involving hazardous materials &mdash; a niche with limited local competition.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-header center">
      <span class="eyebrow">How It Works</span>
      <h2>From first call to final inspection</h2>
      <p>A clear, transparent process so you always know what happens next.</p>
    </div>
    <div class="process-steps">
      <div class="process-step"><div class="step-num">1</div><h4>Consultation</h4><p>Client consultation &amp; site assessment</p></div>
      <div class="process-step"><div class="step-num">2</div><h4>Proposal</h4><p>Proposal &amp; transparent cost estimate</p></div>
      <div class="process-step"><div class="step-num">3</div><h4>Safety Planning</h4><p>Compliance checks &amp; safety planning</p></div>
      <div class="process-step"><div class="step-num">4</div><h4>Execution</h4><p>Abatement, paving &amp; construction management</p></div>
      <div class="process-step"><div class="step-num">5</div><h4>Disposal</h4><p>Waste disposal &amp; responsible recycling</p></div>
      <div class="process-step"><div class="step-num">6</div><h4>Final Report</h4><p>Final inspection &amp; project reporting</p></div>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div class="section-header center">
      <span class="eyebrow">Who We Serve</span>
      <h2>Built for public, commercial, industrial &amp; residential clients</h2>
    </div>
    <div class="grid grid-4">
      <div class="card" style="background:rgba(255,255,255,0.06); border-color:rgba(255,255,255,0.15);">
        <div class="icon-badge" style="background:rgba(255,255,255,0.12); color:#fff;">{icon('building')}</div>
        <h3 style="color:#fff;">Public Sector</h3>
        <p style="color:rgba(255,255,255,0.8);">Schools, hospitals &amp; municipal facilities needing safe abatement and compliance.</p>
      </div>
      <div class="card" style="background:rgba(255,255,255,0.06); border-color:rgba(255,255,255,0.15);">
        <div class="icon-badge" style="background:rgba(255,255,255,0.12); color:#fff;">{icon('crane')}</div>
        <h3 style="color:#fff;">Commercial Developers</h3>
        <p style="color:rgba(255,255,255,0.8);">Businesses &amp; landlords requiring asphalt, paving, or abatement during renovations.</p>
      </div>
      <div class="card" style="background:rgba(255,255,255,0.06); border-color:rgba(255,255,255,0.15);">
        <div class="icon-badge" style="background:rgba(255,255,255,0.12); color:#fff;">{icon('factory')}</div>
        <h3 style="color:#fff;">Industrial Clients</h3>
        <p style="color:rgba(255,255,255,0.8);">Plants &amp; warehouses managing hazardous material exposure.</p>
      </div>
      <div class="card" style="background:rgba(255,255,255,0.06); border-color:rgba(255,255,255,0.15);">
        <div class="icon-badge" style="background:rgba(255,255,255,0.12); color:#fff;">{icon('home')}</div>
        <h3 style="color:#fff;">Residential Owners</h3>
        <p style="color:rgba(255,255,255,0.8);">Renovations involving mould, asbestos, or lead paint.</p>
      </div>
    </div>
  </div>
</section>

<section class="cta-band has-photo" style="{photo_bg('parking-lot-asphalt.jpg', dark=0.90, mid=0.88, light=0.78)}">
  <div class="container">
    <h2>Ready to start your project the safe way?</h2>
    <p>Free consultations and compliance risk assessments &mdash; transparent quotes, no surprises.</p>
    <a href="contact.html" class="btn btn-cream">Request Your Free Quote</a>
  </div>
</section>
"""


# =====================================================================
# ABOUT
# =====================================================================
ABOUT_BODY = f"""
<section class="page-hero">
  <img class="page-hero-watermark" src="assets/img/logo-full.png" alt="">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a> / About</div>
    <span class="eyebrow">About Ace Builders</span>
    <h1>Safer, stronger, more sustainable communities.</h1>
    <p>An Edmonton-based construction and environmental services company specializing in hazardous material abatement, HSE consulting &amp; training, asphalt/concrete solutions, and waste management &amp; recycling.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-2" style="align-items:center;">
      <div>
        <span class="eyebrow">Our Story</span>
        <h2>Two founders. One safety-first standard.</h2>
        <p style="margin-top:16px;">Ace Builders of Canada Ltd. was founded in Edmonton, Alberta by two local co-founders to close a gap in the market: general contractors who handle construction but lack niche HSE and abatement expertise, and small abatement firms that don't offer end-to-end services like paving and waste recycling.</p>
        <p style="margin-top:12px;">We combine industry expertise, certified crews, and a strong safety-first culture to deliver reliable, eco-conscious, and cost-effective construction management solutions &mdash; from the first compliance audit to the final load hauled away for recycling.</p>
      </div>
      <div class="photo-block" style="min-height:340px;">
        <img src="assets/img/photos/construction-team-meeting.jpg" alt="Ace Builders crew members reviewing site plans on a job site">
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="grid grid-2">
      <div class="card">
        <div class="icon-badge">{icon('compass')}</div>
        <h3>Our Mission</h3>
        <p>To create safer, stronger, and more sustainable communities through innovation in construction and environmental services.</p>
      </div>
      <div class="card">
        <div class="icon-badge">{icon('award')}</div>
        <h3>Our Vision</h3>
        <p>To be Alberta&rsquo;s go-to partner for hazardous abatement, safety compliance, and quality construction management &mdash; recognized for integrity, safety, and environmental responsibility.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-header center">
      <span class="eyebrow">Leadership Team</span>
      <h2>Meet the founders</h2>
      <p>Complementary backgrounds in strategy and hands-on project delivery.</p>
    </div>
    <div class="grid grid-2">
      <div class="team-card">
        <div class="team-photo">{icon('users', 'icon-svg')}</div>
        <div class="team-body">
          <h3>Co-Founder &amp; VP</h3>
          <div class="team-role">Finance &amp; Strategy</div>
          <p>Background in economics and strategy. Oversees finance, business development, and strategic growth for Ace Builders of Canada Ltd.</p>
        </div>
      </div>
      <div class="team-card">
        <div class="team-photo">{icon('users', 'icon-svg')}</div>
        <div class="team-body">
          <h3>Co-Founder &amp; Project Manager</h3>
          <div class="team-role">Operations &amp; Field Delivery</div>
          <p>Experienced in construction and project coordination. Responsible for daily operations, crew oversight, and quality control on every job.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="grid grid-2" style="align-items:center;">
      <div>
        <span class="eyebrow">Advisors &amp; Partnerships</span>
        <h2>Backed by mentorship and industry expertise</h2>
        <ul style="margin-top:18px; list-style:none;">
          <li style="padding:12px 0; border-bottom:1px solid var(--grey-light);"><strong>Futurpreneur Business Mentorship Program</strong> &mdash; strategic and financial guidance as we grow.</li>
          <li style="padding:12px 0; border-bottom:1px solid var(--grey-light);"><strong>Industry Consultants</strong> &mdash; construction compliance and hazardous waste management expertise.</li>
          <li style="padding:12px 0;"><strong>Certified Disposal &amp; Recycling Facilities</strong> &mdash; partnerships that keep our waste practices eco-responsible.</li>
        </ul>
      </div>
      <div class="card">
        <div class="icon-badge">{icon('quote')}</div>
        <h3>Our Brand Promise</h3>
        <p style="font-size:1.3rem; font-family:var(--font-head); font-weight:700; color:var(--forest-900); margin:10px 0;">&ldquo;Building Safely, Building Better.&rdquo;</p>
        <p>Every audit, every abatement job, every ton of asphalt laid down &mdash; done with certified crews and a safety-first culture, so you can trust the outcome.</p>
      </div>
    </div>
  </div>
</section>

<section class="cta-band has-photo" style="{photo_bg('parking-lot-asphalt.jpg', dark=0.90, mid=0.88, light=0.78)}">
  <div class="container">
    <h2>Want to work with a certified, safety-first team?</h2>
    <p>Let&rsquo;s talk about your next project in Edmonton or anywhere in Alberta.</p>
    <a href="contact.html" class="btn btn-cream">Contact Us</a>
  </div>
</section>
"""


# =====================================================================
# SERVICES
# =====================================================================
SERVICES_BODY = f"""
<section class="page-hero">
  <img class="page-hero-watermark" src="assets/img/logo-full.png" alt="">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a> / Services</div>
    <span class="eyebrow">Our Services</span>
    <h1>Four service lines. One accountable team.</h1>
    <p>HSE consulting, hazardous abatement, asphalt &amp; concrete, and waste management &mdash; each delivered by certified crews under a single safety-first standard.</p>
  </div>
</section>

<section class="section" id="hse">
  <div class="container">
    <div class="grid grid-2" style="align-items:center;">
      <div>
        <div class="icon-badge">{icon('clipboard-check')}</div>
        <span class="tag-pill">Service 01</span>
        <h2>HSE Consulting &amp; Training</h2>
        <p style="margin-top:14px;">We help organizations meet and exceed Alberta&rsquo;s safety and compliance standards, reducing risk before it becomes a liability.</p>
        <ul>
          <li>On-site safety audits</li>
          <li>WHMIS training</li>
          <li>COR program development</li>
          <li>Ongoing compliance support</li>
        </ul>
      </div>
      <div class="photo-block" style="min-height:300px;">
        <img src="assets/img/photos/safety-training-construction.jpg" alt="Safety line marking on a job site, representing HSE compliance standards">
      </div>
    </div>
  </div>
</section>

<section class="section section-alt" id="abatement">
  <div class="container">
    <div class="grid grid-2" style="align-items:center;">
      <div class="photo-block" style="min-height:300px; order:1;">
        <img src="assets/img/photos/hazmat-worker.jpg" alt="Ace Builders crew member in full PPE and respirator performing hazardous material abatement">
      </div>
      <div style="order:2;">
        <div class="icon-badge">{icon('hazmat')}</div>
        <span class="tag-pill">Service 02</span>
        <h2>Hazardous Abatement &amp; Surface Preparation</h2>
        <p style="margin-top:14px;">Safe, compliant removal of hazardous materials plus surface preparation for renovation and rebuild.</p>
        <ul>
          <li>Asbestos removal</li>
          <li>Lead paint abatement</li>
          <li>Mould &amp; silica remediation</li>
          <li>Concrete profiling &amp; water blasting</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section" id="asphalt">
  <div class="container">
    <div class="grid grid-2" style="align-items:center;">
      <div>
        <div class="icon-badge">{icon('road')}</div>
        <span class="tag-pill">Service 03</span>
        <h2>Asphalt &amp; Concrete Solutions</h2>
        <p style="margin-top:14px;">Durable, professionally finished surfaces for parking lots, driveways, and municipal infrastructure.</p>
        <ul>
          <li>Milling &amp; paving</li>
          <li>Saw-cutting</li>
          <li>Compaction</li>
          <li>Durable surface finishing</li>
        </ul>
      </div>
      <div class="photo-block" style="min-height:300px;">
        <img src="assets/img/photos/asphalt-paving.jpg" alt="Asphalt roller compacting a freshly paved road">
      </div>
    </div>
  </div>
</section>

<section class="section section-alt" id="waste">
  <div class="container">
    <div class="grid grid-2" style="align-items:center;">
      <div class="photo-block" style="min-height:300px; order:1;">
        <img src="assets/img/photos/construction-waste-recycling.jpg" alt="Construction and renovation waste ready for sorting and landfill diversion">
      </div>
      <div style="order:2;">
        <div class="icon-badge">{icon('recycle')}</div>
        <span class="tag-pill">Service 04</span>
        <h2>Waste Management &amp; Recycling</h2>
        <p style="margin-top:14px;">Eco-responsible disposal that keeps material out of landfills wherever possible.</p>
        <ul>
          <li>Sorting &amp; material recovery</li>
          <li>Roll-off bin service</li>
          <li>Landfill diversion</li>
          <li>Eco-responsible disposal</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-header center">
      <span class="eyebrow">Who We Serve</span>
      <h2>Target markets</h2>
    </div>
    <div class="grid grid-4">
      <div class="card"><div class="icon-badge">{icon('building')}</div><h3>Public Sector</h3><p>Schools, hospitals &amp; municipal facilities needing safe abatement and compliance.</p></div>
      <div class="card"><div class="icon-badge">{icon('crane')}</div><h3>Commercial Developers</h3><p>Businesses &amp; landlords requiring asphalt, paving, or abatement during renovations.</p></div>
      <div class="card"><div class="icon-badge">{icon('factory')}</div><h3>Industrial Clients</h3><p>Plants &amp; warehouses managing hazardous material exposure.</p></div>
      <div class="card"><div class="icon-badge">{icon('home')}</div><h3>Residential Owners</h3><p>Renovations involving mould, asbestos, or lead paint.</p></div>
    </div>
  </div>
</section>

<section class="cta-band has-photo" style="{photo_bg('parking-lot-asphalt.jpg', dark=0.90, mid=0.88, light=0.78)}">
  <div class="container">
    <h2>Not sure which service you need?</h2>
    <p>Tell us about your project and we&rsquo;ll recommend the right scope &mdash; free of charge.</p>
    <a href="contact.html" class="btn btn-cream">Book a Free Consultation</a>
  </div>
</section>
"""


# =====================================================================
# PROJECTS
# =====================================================================
_PROJECT_CARDS = [
    ("project-public-abatement.jpg", "Demolition and abatement work near a public facility",
     "hazmat", "Hazardous Abatement", "Public Facility Abatement",
     "Safe removal of asbestos, lead paint, or mould in schools, hospitals, and municipal buildings, delivered with full compliance documentation."),
    ("project-concrete-pour.jpg", "Concrete mixer truck being operated on a commercial site",
     "road", "Asphalt &amp; Concrete", "Commercial Parking &amp; Driveways",
     "Milling, paving, and compaction for parking lots and driveways &mdash; built to withstand Alberta&rsquo;s freeze-thaw cycles."),
    ("industrial-warehouse-worker.jpg", "Worker on an industrial site managing equipment",
     "clipboard-check", "HSE Consulting", "Industrial Compliance Programs",
     "COR program development and WHMIS training for plants and warehouses managing hazardous material exposure."),
    ("project-demo-rubble.jpg", "Excavator processing demolition rubble for waste diversion",
     "recycle", "Waste Management", "Renovation Waste Diversion",
     "Sorting and landfill diversion programs for residential and commercial renovation projects."),
    ("home-renovation-interior.jpg", "Residential living space of the type Ace Builders supports",
     "hazmat", "Hazardous Abatement", "Residential Mould &amp; Asbestos",
     "Homeowner renovation support for mould, asbestos, or lead paint discovered mid-project."),
    ("concrete-pressure-washing.jpg", "Worker water-blasting a concrete driveway surface",
     "shield", "Surface Preparation", "Concrete Profiling &amp; Water Blasting",
     "Surface preparation ahead of coatings, resurfacing, or structural repair work."),
]

_project_cards_html = "\n".join(f"""
      <div class="project-card">
        <div class="project-visual">
          <img src="assets/img/photos/{img}" alt="{alt}">
          <span class="pv-badge">{icon(name, 'icon-svg')}</span>
        </div>
        <div class="project-body">
          <span class="tag-pill">{tag}</span>
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>
      </div>""" for img, alt, name, tag, title, desc in _PROJECT_CARDS)

PROJECTS_BODY = f"""
<section class="page-hero has-photo" style="{photo_bg('projects-hero.jpg')}">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a> / Projects</div>
    <span class="eyebrow">Projects &amp; Capabilities</span>
    <h1>What we deliver, by service line.</h1>
    <p>As a growing Edmonton-based team, we&rsquo;re building our project portfolio one job at a time. Here&rsquo;s a look at the type of work we take on across each service line &mdash; real case studies from our own jobs will replace these as projects are completed.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-2">
{_project_cards_html}
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container text-center">
    <span class="eyebrow" style="justify-content:center;">Have a project in mind?</span>
    <h2>Let&rsquo;s add it to the list.</h2>
    <p style="max-width:560px; margin:14px auto 26px; color:var(--grey);">Whether it&rsquo;s a single-site abatement job or an ongoing municipal paving contract, we scope every project with a free consultation and transparent quote.</p>
    <a href="contact.html" class="btn btn-primary">Start a Project</a>
  </div>
</section>
"""


# =====================================================================
# CERTIFICATIONS
# =====================================================================
CERTIFICATIONS_BODY = f"""
<section class="page-hero">
  <img class="page-hero-watermark" src="assets/img/logo-full.png" alt="">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a> / Certifications</div>
    <span class="eyebrow">Certifications &amp; Safety</span>
    <h1>Safety isn&rsquo;t a checkbox. It&rsquo;s our culture.</h1>
    <p>Every crew member is trained, certified, and accountable &mdash; because a safe site is the only kind of site we work on.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-2">
      <div class="cert-badge">
        <div class="icon-badge">{icon('clipboard-check')}</div>
        <div>
          <h3>COR &mdash; Certificate of Recognition</h3>
          <p>A recognized Alberta safety program standard, reflecting a fully implemented health &amp; safety management system.</p>
        </div>
      </div>
      <div class="cert-badge">
        <div class="icon-badge">{icon('heart-pulse')}</div>
        <div>
          <h3>WCB &mdash; Workers&rsquo; Compensation Board</h3>
          <p>All crews are WCB registered, protecting workers and giving clients confidence and reduced liability on every site.</p>
        </div>
      </div>
      <div class="cert-badge">
        <div class="icon-badge">{icon('alert')}</div>
        <div>
          <h3>WHMIS Trained</h3>
          <p>Workplace Hazardous Materials Information System training across the workforce for safe handling of hazardous materials.</p>
        </div>
      </div>
      <div class="cert-badge">
        <div class="icon-badge">{icon('first-aid')}</div>
        <div>
          <h3>First Aid Certified</h3>
          <p>Site-ready first aid training so our crews are prepared to respond, not just comply.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div class="grid grid-2" style="align-items:center;">
      <div>
        <span class="eyebrow">Our Standard</span>
        <h2>Certified crews reduce your risk</h2>
        <p style="margin-top:14px;">Government-mandated safety compliance and environmental standards are driving demand for certified providers across Alberta&rsquo;s aging infrastructure and growing urban development. We built Ace Builders around that standard from day one &mdash; not as an add-on.</p>
        <ul style="margin-top:20px; list-style:none;">
          <li style="padding:10px 0; border-bottom:1px solid rgba(255,255,255,0.15); color:rgba(255,255,255,0.85); display:flex; align-items:center; gap:10px;">{icon('check')} Site safety trained workforce on every project</li>
          <li style="padding:10px 0; border-bottom:1px solid rgba(255,255,255,0.15); color:rgba(255,255,255,0.85); display:flex; align-items:center; gap:10px;">{icon('check')} Ongoing HSE audits &amp; compliance monitoring</li>
          <li style="padding:10px 0; color:rgba(255,255,255,0.85); display:flex; align-items:center; gap:10px;">{icon('check')} Regulatory-change tracking to stay ahead of new standards</li>
        </ul>
      </div>
      <div class="photo-block" style="min-height:300px; background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.2);">
        <img src="assets/img/photos/safety-first-hardhat.jpg" alt="Crew member wearing a Safety First hard hat and hi-vis vest on site">
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-header center">
      <span class="eyebrow">Training Partnerships</span>
      <h2>Investing in our people, continuously</h2>
      <p>We partner with recognized training providers to keep certifications current across WHMIS and First Aid, and we work with industry consultants specializing in construction compliance and hazardous waste management.</p>
    </div>
  </div>
</section>

<section class="cta-band has-photo" style="{photo_bg('parking-lot-asphalt.jpg', dark=0.90, mid=0.88, light=0.78)}">
  <div class="container">
    <h2>Need a compliance risk assessment?</h2>
    <p>We offer free consultations and compliance risk assessments for public, commercial, and industrial clients.</p>
    <a href="contact.html" class="btn btn-cream">Book Your Assessment</a>
  </div>
</section>
"""


# =====================================================================
# CONTACT
# =====================================================================
CONTACT_BODY = f"""
<section class="page-hero">
  <img class="page-hero-watermark" src="assets/img/logo-full.png" alt="">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a> / Contact</div>
    <span class="eyebrow">Get In Touch</span>
    <h1>Let&rsquo;s talk about your project.</h1>
    <p>Free consultations and transparent quotes &mdash; reach out and a member of our team will get back to you.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-2" style="align-items:flex-start;">
      <div class="card">
        <h3 style="margin-bottom:6px;">Send us a message</h3>
        <p style="margin-bottom:24px;">Fill out the form and we&rsquo;ll respond within one business day.</p>
        <form id="contactForm" name="contact" method="POST" data-netlify="true">
          <input type="hidden" name="form-name" value="contact">
          <div class="form-grid">
            <div class="form-field">
              <label for="fullName">Full Name *</label>
              <input type="text" id="fullName" name="fullName" required placeholder="Jane Smith">
            </div>
            <div class="form-field">
              <label for="phone">Phone</label>
              <input type="tel" id="phone" name="phone" placeholder="(780) 000-0000">
            </div>
            <div class="form-field">
              <label for="email">Email *</label>
              <input type="email" id="email" name="email" required placeholder="jane@company.com">
            </div>
            <div class="form-field">
              <label for="service">Service Interested In</label>
              <select id="service" name="service">
                <option value="">Select a service</option>
                <option>HSE Consulting &amp; Training</option>
                <option>Hazardous Abatement &amp; Surface Preparation</option>
                <option>Asphalt &amp; Concrete Solutions</option>
                <option>Waste Management &amp; Recycling</option>
                <option>Not sure / general inquiry</option>
              </select>
            </div>
            <div class="form-field full">
              <label for="message">Project Details *</label>
              <textarea id="message" name="message" rows="5" required placeholder="Tell us about your project, location, and timeline."></textarea>
            </div>
          </div>
          <button type="submit" class="btn btn-primary btn-block">Send Message</button>
          <div id="form-status"></div>
          <p class="form-note">By submitting, you agree to be contacted by Ace Builders of Canada Ltd. regarding your inquiry.</p>
        </form>
      </div>

      <div>
        <div class="contact-info-card">
          <h3>Contact Information</h3>
          <div class="contact-row">
            <div class="icon-badge">{icon('phone')}</div>
            <div><div class="label">Phone</div><a class="value" href="tel:+17806678436">780-667-8436</a></div>
          </div>
          <div class="contact-row">
            <div class="icon-badge">{icon('mail')}</div>
            <div><div class="label">Email</div><a class="value" href="mailto:info@acebuilderscan.com">info@acebuilderscan.com</a></div>
          </div>
          <div class="contact-row">
            <div class="icon-badge">{icon('pin')}</div>
            <div><div class="label">Location</div><span class="value">Edmonton, Alberta, Canada</span></div>
          </div>
          <div class="contact-row">
            <div class="icon-badge">{icon('clock')}</div>
            <div><div class="label">Hours</div><span class="value">Mon &ndash; Fri, 8:00 AM &ndash; 5:00 PM MT</span></div>
          </div>
        </div>
        <div class="map-embed" style="margin-top:24px;">
          <iframe src="https://www.google.com/maps?q=Edmonton,Alberta,Canada&output=embed" loading="lazy" allowfullscreen title="Ace Builders of Canada Ltd. service area map"></iframe>
        </div>
      </div>
    </div>
  </div>
</section>
"""
