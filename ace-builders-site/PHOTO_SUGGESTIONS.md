# Photography credits / placement log

All photography has been sourced and placed. This is a record of what's used where, in
case you want to swap anything later.

| File (`assets/img/photos/`) | Placed on | Used as |
|---|---|---|
| `edmonton-skyline.jpg` | Home | Hero background photo |
| `construction-team-meeting.jpg` | About | "Our Story" photo |
| `safety-training-construction.jpg` | Services | HSE Consulting & Training photo |
| `hazmat-worker.jpg` | Services | Hazardous Abatement photo |
| `asphalt-paving.jpg` | Services | Asphalt & Concrete photo |
| `construction-waste-recycling.jpg` | Services | Waste Management & Recycling photo |
| `safety-first-hardhat.jpg` | Certifications | "Our Standard" photo |
| `projects-hero.jpg` | Projects | Page-hero background photo |
| `project-public-abatement.jpg` | Projects | Public Facility Abatement card |
| `project-concrete-pour.jpg` | Projects | Commercial Parking & Driveways card |
| `industrial-warehouse-worker.jpg` | Projects | Industrial Compliance Programs card |
| `project-demo-rubble.jpg` | Projects | Renovation Waste Diversion card |
| `home-renovation-interior.jpg` | Projects | Residential Mould & Asbestos card |
| `concrete-pressure-washing.jpg` | Projects | Concrete Profiling & Water Blasting card |
| `parking-lot-asphalt.jpg` | Site-wide | CTA band background (Home, About, Services, Certifications) |
| `home-renovation-interior2.jpg` | — | Not used (near-duplicate of `home-renovation-interior.jpg`) — available if you want it placed somewhere |

All photos were resized to a 1920px max dimension and compressed for web (originals from
the source folder were 1–8MB each; site copies are 120–700KB).

The original brand-colored SVG illustrations that were used before real photography was
available are still in `assets/img/illustrations/` if you ever want to revert a section to
the illustrated look — see `README.md` for how to swap.

## Adding more photos later

Want to add or replace a photo? Drop the new file into `assets/img/photos/`, then either:

- point an existing `<img src="...">` at it (for a `.photo-block` or `.project-visual`), or
- update the filename inside the matching `photo_bg('filename.jpg')` call in `pages.py`
  for hero/CTA-band backgrounds, then run `python3 generate_site.py`.
