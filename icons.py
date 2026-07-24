# -*- coding: utf-8 -*-
"""Inline SVG icon library (stroke-based, currentColor) replacing emoji glyphs."""

_S = 'fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"'

ICONS = {
    "shield": f'<svg viewBox="0 0 24 24" {_S}><path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/></svg>',
    "hazmat": f'<svg viewBox="0 0 24 24" {_S}><circle cx="12" cy="6.6" r="2.1"/><circle cx="7.2" cy="15" r="2.1"/><circle cx="16.8" cy="15" r="2.1"/><circle cx="12" cy="12" r="1.8"/><path d="M12 8.7v2.2M10.3 13.1L9.1 12M13.7 13.1l1.2-1.1"/></svg>',
    "road": f'<svg viewBox="0 0 24 24" {_S}><path d="M4.5 20.5L9 3.5h6l4.5 17"/><path d="M12 7.5v2.2M12 12.3v2.2M12 17v1.3"/></svg>',
    "recycle": f'<svg viewBox="0 0 24 24" {_S}><path d="M4 12a8 8 0 0113.3-6"/><path d="M20 12a8 8 0 01-13.3 6"/><path d="M15.8 3.6l1 3.6-3.6.6"/><path d="M8.2 20.4l-1-3.6 3.6-.6"/></svg>',
    "clipboard-check": f'<svg viewBox="0 0 24 24" {_S}><rect x="5.5" y="4" width="13" height="17" rx="2"/><path d="M9 4V3.2a1 1 0 011-1h4a1 1 0 011 1V4"/><path d="M9 12.3l2 2 4-4.3"/></svg>',
    "first-aid": f'<svg viewBox="0 0 24 24" {_S}><rect x="3" y="3" width="18" height="18" rx="3.5"/><path d="M12 8v8M8 12h8"/></svg>',
    "heart-pulse": f'<svg viewBox="0 0 24 24" {_S}><path d="M20.8 8.6c0 5-8.8 10-8.8 10s-8.8-5-8.8-10a4.8 4.8 0 018.8-2.7A4.8 4.8 0 0120.8 8.6z"/><path d="M5.7 11h2l1.5-3 2 5 1.5-3h2.9"/></svg>',
    "alert": f'<svg viewBox="0 0 24 24" {_S}><path d="M12 3L2 20h20z"/><path d="M12 10v4M12 16.7h.01"/></svg>',
    "compass": f'<svg viewBox="0 0 24 24" {_S}><circle cx="12" cy="12" r="9"/><path d="M15.2 8.8l-2 5-5 2 2-5z"/></svg>',
    "award": f'<svg viewBox="0 0 24 24" {_S}><circle cx="12" cy="8" r="5"/><path d="M8.3 12.6L6.8 21l5.2-2.6L17.2 21l-1.5-8.4"/></svg>',
    "quote": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M9.3 7C6.4 7 4.3 9.4 4.3 12.5S6.4 18 9.3 18v-2.3c-1.4 0-2.4-1.2-2.4-3.2S7.9 9.3 9.3 9.3V7zm9 0c-2.9 0-5 2.4-5 5.5S15.4 18 18.3 18v-2.3c-1.4 0-2.4-1.2-2.4-3.2S16.9 9.3 18.3 9.3V7z"/></svg>',
    "phone": f'<svg viewBox="0 0 24 24" {_S}><path d="M5 4h4l1.4 4.3-2 1.6a12.3 12.3 0 006 6l1.6-2L20 15.4V19a1 1 0 01-1 1C10.7 20 4 13.3 4 5a1 1 0 011-1z"/></svg>',
    "mail": f'<svg viewBox="0 0 24 24" {_S}><rect x="3" y="5" width="18" height="14" rx="2.2"/><path d="M3.4 6.5l8.6 6.2 8.6-6.2"/></svg>',
    "pin": f'<svg viewBox="0 0 24 24" {_S}><path d="M12 21s-7-6.2-7-11.5A7 7 0 0119 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.3"/></svg>',
    "clock": f'<svg viewBox="0 0 24 24" {_S}><circle cx="12" cy="12" r="9"/><path d="M12 7.3v5l3.3 2"/></svg>',
    "users": f'<svg viewBox="0 0 24 24" {_S}><circle cx="9" cy="8" r="3.2"/><path d="M2.6 20c0-3.6 2.8-6 6.4-6s6.4 2.4 6.4 6"/><circle cx="17.3" cy="9" r="2.5"/><path d="M15.4 14.2c2.6.4 4.8 2.5 4.8 5.8"/></svg>',
    "target": f'<svg viewBox="0 0 24 24" {_S}><circle cx="12" cy="12" r="8.3"/><circle cx="12" cy="12" r="4.8"/><circle cx="12" cy="12" r="1.4" fill="currentColor" stroke="none"/></svg>',
    "handshake": f'<svg viewBox="0 0 24 24" {_S}><path d="M2.2 11.7l3.6-3.4 3.7 1.9 2.8-1.9 2.8 1.9 3.6-1.9 1.8 1.8"/><path d="M5.8 11.7l3.7 3.7 1.8-.9 1.8.9 3.7-3.7"/></svg>',
    "leaf": f'<svg viewBox="0 0 24 24" {_S}><path d="M19.8 4.2c-9.2 0-15 5.5-15 13.6 8 0 14-5.5 14.6-13.6z"/><path d="M6 18C10 14 14.3 9.7 19 4.9"/></svg>',
    "building": f'<svg viewBox="0 0 24 24" {_S}><rect x="4" y="3" width="10" height="18"/><rect x="14" y="9" width="6" height="12"/><path d="M7 7h1M11 7h1M7 11h1M11 11h1M7 15h1M11 15h1"/></svg>',
    "crane": f'<svg viewBox="0 0 24 24" {_S}><path d="M4.5 21V9.3l8.5-5.8v17.5"/><path d="M13 6.2h6.5l-2.8 4.6H13"/><path d="M17 10.8V21"/><path d="M2.5 21h19"/></svg>',
    "factory": f'<svg viewBox="0 0 24 24" {_S}><path d="M3 21V11.5l5 2.8v-2.8l5 2.8V7l5.5 4v10z"/><path d="M3 21h18.5"/></svg>',
    "home": f'<svg viewBox="0 0 24 24" {_S}><path d="M3.5 11L12 4.3 20.5 11"/><path d="M5.3 9.8V20h13.4V9.8"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12l5 5L20 6"/></svg>',
    "arrow-right": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 11-.02 5 2.5 2.5 0 01.02-5zM3 9h4v12H3zM9 9h3.6v1.7h.05c.5-.9 1.8-1.9 3.7-1.9 4 0 4.7 2.6 4.7 6V21h-4v-5.3c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9V21H9z"/></svg>',
    "facebook": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 21v-8h2.7l.4-3.2h-3.1V7.7c0-.9.3-1.6 1.7-1.6h1.5V3.2C16.4 3.1 15.3 3 14 3c-2.6 0-4.4 1.6-4.4 4.5v2.3H7v3.2h2.6V21z"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1"/></svg>',
}


def icon(name, css_class="icon-svg"):
    """Return an inline <span> wrapper around the named icon's SVG markup."""
    svg = ICONS.get(name)
    if svg is None:
        raise KeyError(f"Unknown icon: {name}")
    cls = f' class="{css_class}"' if css_class else ""
    return f"<span{cls}>{svg}</span>"
