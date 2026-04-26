"""
app.py
CartoonPal — Streamlit UI with cartoon theming (light/dark mode).
Run with:  streamlit run app.py
"""

import streamlit as st
from datetime import datetime
from cartoon_system import Cartoon, Creator, ProductionCompany, Series, OwnershipRecord, Era, CartoonAnalyzer
from seed_data import build_library

# ─────────────────────────────────────────────────────────────────────────────
# Page config
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CartoonPal",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded",
)

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# ─────────────────────────────────────────────────────────────────────────────
# SVG LOGO
# ─────────────────────────────────────────────────────────────────────────────
def sidebar_logo(dark: bool) -> str:
    if dark:
        bg      = "#12122a"
        border  = "#f97316"
        star    = "#fbbf24"
        clap_b  = "#f97316"
        clap_t  = "#fb923c"
        text_c  = "#ffffff"
        sub_c   = "#fdba74"
        stripe  = "#12122a"
    else:
        bg      = "#fff7ed"
        border  = "#ea580c"
        star    = "#f59e0b"
        clap_b  = "#ea580c"
        clap_t  = "#fb923c"
        text_c  = "#1c1917"
        sub_c   = "#92400e"
        stripe  = "#fff7ed"

    # Layout rationale:
    # - ViewBox 220×80. Safe inner area starts at x=20 (after left sprockets) and ends x=200 (before right sprockets).
    # - Left zone (x=20–60): clapperboard icon only, no text overlap.
    # - Right text zone (x=66–198): CARTOONPAL title + subtitle, both well clear of icon and sprockets.
    # - Vertical: title baseline at y=40, subtitle at y=58, both inside the 80px box with padding.
    return f"""
<link href="https://fonts.googleapis.com/css2?family=Bangers&display=swap" rel="stylesheet">
<div style="padding:6px 2px 4px 2px; font-family: Bangers, cursive;">
<svg viewBox="0 0 220 80" xmlns="http://www.w3.org/2000/svg"
     style="width:100%;display:block;">

  <!-- Outer pill -->
  <rect x="2" y="2" width="216" height="76" rx="14"
        fill="{bg}" stroke="{border}" stroke-width="2.5"/>

  <!-- Left film-strip column (x=4–16, safe zone ends at 18) -->
  <rect x="4" y="2"  width="14" height="76" rx="8" fill="{border}" opacity="0.15"/>
  <rect x="6"  y="10" width="7" height="9" rx="2" fill="{border}" opacity="0.75"/>
  <rect x="6"  y="27" width="7" height="9" rx="2" fill="{border}" opacity="0.75"/>
  <rect x="6"  y="44" width="7" height="9" rx="2" fill="{border}" opacity="0.75"/>
  <rect x="6"  y="61" width="7" height="9" rx="2" fill="{border}" opacity="0.75"/>

  <!-- Right film-strip column (x=202–216, safe zone starts at 200) -->
  <rect x="202" y="2"  width="14" height="76" rx="8" fill="{border}" opacity="0.15"/>
  <rect x="207" y="10" width="7" height="9" rx="2" fill="{border}" opacity="0.75"/>
  <rect x="207" y="27" width="7" height="9" rx="2" fill="{border}" opacity="0.75"/>
  <rect x="207" y="44" width="7" height="9" rx="2" fill="{border}" opacity="0.75"/>
  <rect x="207" y="61" width="7" height="9" rx="2" fill="{border}" opacity="0.75"/>

  <!-- Clapperboard icon — lives entirely in x=20–58, y=16–54 -->
  <rect x="22" y="20" width="34" height="28" rx="3"
        fill="{clap_b}" stroke="{border}" stroke-width="1.5"/>
  <!-- clapper top bar -->
  <rect x="22" y="20" width="34" height="9" rx="3" fill="{clap_t}"/>
  <!-- diagonal stripes on top bar -->
  <line x1="26" y1="20" x2="23" y2="29" stroke="{stripe}" stroke-width="2.2"/>
  <line x1="32" y1="20" x2="29" y2="29" stroke="{stripe}" stroke-width="2.2"/>
  <line x1="38" y1="20" x2="35" y2="29" stroke="{stripe}" stroke-width="2.2"/>
  <line x1="44" y1="20" x2="41" y2="29" stroke="{stripe}" stroke-width="2.2"/>
  <line x1="50" y1="20" x2="47" y2="29" stroke="{stripe}" stroke-width="2.2"/>
  <!-- play triangle centred in lower body -->
  <polygon points="30,34 30,44 42,39" fill="{star}" opacity="0.95"/>

  <!-- Thin divider line between icon zone and text zone -->
  <line x1="62" y1="14" x2="62" y2="66" stroke="{border}" stroke-width="1" opacity="0.4"/>

  <!-- CARTOONPAL — anchored at x=68, well clear of divider and right sprockets -->
  <text x="68" y="42"
        font-family="Bangers, Impact, cursive"
        font-size="24" letter-spacing="2"
        fill="{text_c}"
        stroke="{border}" stroke-width="1"
        paint-order="stroke fill">CARTOONPAL</text>

  <!-- Subtitle — same left edge, tighter tracking, safely above bottom edge -->
  <text x="68" y="60"
        font-family="Bangers, Impact, cursive"
        font-size="9.5" letter-spacing="1.2"
        fill="{sub_c}" opacity="0.88">COPYRIGHT &amp; VISUAL HISTORY</text>

  <!-- Small star accent — safely inside icon zone, x max = 60 -->
  <polygon points="52,13 54,8 56,13 61,13 57,16 59,21 54,18 49,21 51,16 47,13"
           fill="{star}" stroke="{border}" stroke-width="0.7" opacity="0.9"/>
</svg>
</div>
"""

# ─────────────────────────────────────────────────────────────────────────────
# Hand-drawn 80s cartoon background tile
# Every shape uses wobbly paths + freehand strokes to look like crayon/marker
# ─────────────────────────────────────────────────────────────────────────────
def cartoon_bg_svg(dark: bool) -> str:
    import base64

    if dark:
        sun     = "rgba(251,191,36,0.38)"
        bubble  = "rgba(56,189,248,0.34)"
        star    = "rgba(249,115,22,0.36)"
        heart   = "rgba(244,114,182,0.34)"
        zigzag  = "rgba(52,211,153,0.36)"
        dino    = "rgba(167,139,250,0.34)"
        sk      = "rgba(255,255,255,0.30)"
        sk2     = "rgba(255,255,255,0.18)"
        inner   = "rgba(255,255,255,0.14)"
    else:
        sun     = "rgba(245,158,11,0.42)"
        bubble  = "rgba(14,165,233,0.38)"
        star    = "rgba(234,88,12,0.40)"
        heart   = "rgba(236,72,153,0.36)"
        zigzag  = "rgba(16,185,129,0.40)"
        dino    = "rgba(139,92,246,0.36)"
        sk      = "rgba(0,0,0,0.22)"
        sk2     = "rgba(0,0,0,0.14)"
        inner   = "rgba(0,0,0,0.10)"

    # Each shape is drawn with intentionally wobbly/imperfect paths —
    # simulate the look of a kid drawing with marker or crayon in the 80s.
    # Tile is 240×240 so figures feel generous and slightly overlapping.
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240">
  <defs>
    <!-- Crayon texture filter — roughens edges slightly -->
    <filter id="crayon" x="-5%" y="-5%" width="110%" height="110%">
      <feTurbulence type="fractalNoise" baseFrequency="0.065" numOctaves="3"
                    seed="2" result="noise"/>
      <feDisplacementMap in="SourceGraphic" in2="noise" scale="2.5"
                         xChannelSelector="R" yChannelSelector="G"/>
    </filter>
    <filter id="marker" x="-5%" y="-5%" width="110%" height="110%">
      <feTurbulence type="turbulence" baseFrequency="0.04" numOctaves="2"
                    seed="7" result="noise"/>
      <feDisplacementMap in="SourceGraphic" in2="noise" scale="1.8"
                         xChannelSelector="R" yChannelSelector="G"/>
    </filter>
  </defs>

  <!-- ☀️ Hand-drawn wobbly sun — top-left, tilted 12° -->
  <g transform="translate(38,34) rotate(12,0,0)" filter="url(#crayon)">
    <!-- sun body — slightly lumpy circle drawn as path -->
    <path d="M0,-22 C6,-21 14,-16 16,-9 C19,-1 16,8 10,14
             C4,19 -5,22 -13,19 C-20,16 -24,8 -22,0
             C-20,-8 -14,-18 -6,-21 Z"
          fill="{sun}" stroke="{sk}" stroke-width="2.2" stroke-linejoin="round"/>
    <!-- wonky rays — each a squiggly line -->
    <line x1="0" y1="-26" x2="1" y2="-34" stroke="{sun}" stroke-width="3"
          stroke-linecap="round"/>
    <line x1="18" y1="-18" x2="24" y2="-24" stroke="{sun}" stroke-width="3"
          stroke-linecap="round"/>
    <line x1="25" y1="0"   x2="33" y2="1"  stroke="{sun}" stroke-width="3"
          stroke-linecap="round"/>
    <line x1="17" y1="17"  x2="23" y2="22" stroke="{sun}" stroke-width="3"
          stroke-linecap="round"/>
    <line x1="0"  y1="25"  x2="-1" y2="33" stroke="{sun}" stroke-width="3"
          stroke-linecap="round"/>
    <line x1="-18" y1="17" x2="-24" y2="22" stroke="{sun}" stroke-width="3"
          stroke-linecap="round"/>
    <line x1="-25" y1="0"  x2="-33" y2="-1" stroke="{sun}" stroke-width="3"
          stroke-linecap="round"/>
    <line x1="-17" y1="-18" x2="-23" y2="-23" stroke="{sun}" stroke-width="3"
          stroke-linecap="round"/>
    <!-- simple smiley face inside -->
    <circle cx="-5" cy="-3" r="2.5" fill="{sk}" opacity="0.7"/>
    <circle cx="5"  cy="-3" r="2.5" fill="{sk}" opacity="0.7"/>
    <path d="M-6,5 Q0,11 6,5" fill="none" stroke="{sk}" stroke-width="2"
          stroke-linecap="round" opacity="0.7"/>
  </g>

  <!-- 💬 Hand-drawn speech bubble — top-right, tilted -18° -->
  <g transform="translate(178,42) rotate(-18,0,0)" filter="url(#marker)">
    <path d="M-28,-20 C-26,-26 -18,-30 -8,-30 C4,-30 18,-28 24,-22
             C30,-16 30,-6 24,2 C18,10 6,14 -8,13
             C-16,13 -24,9 -28,3 L-32,18 L-18,5 C-24,3 -28,-2 -28,-8 Z"
          fill="{bubble}" stroke="{sk}" stroke-width="2"
          stroke-linejoin="round" stroke-linecap="round"/>
    <!-- ZZZ inside — classic 80s sleep/cartoon text -->
    <text x="-14" y="2" font-family="Bangers,cursive" font-size="14"
          fill="{sk}" opacity="0.75" letter-spacing="1">ZAP!</text>
  </g>

  <!-- ⭐ Wobbly hand-drawn star — middle-left, tilted -15° -->
  <g transform="translate(32,122) rotate(-15,0,0)" filter="url(#crayon)">
    <path d="M0,-24 C2,-14 4,-12 14,-12 C6,-6 4,-4 8,6
             C2,0 0,2 -8,8 C-6,-2 -8,-4 -18,-10
             C-8,-10 -6,-12 0,-24 Z"
          fill="{star}" stroke="{sk}" stroke-width="2.2"
          stroke-linejoin="round"/>
    <!-- second layer for fat marker look -->
    <path d="M0,-20 C2,-12 3,-10 12,-10 C5,-5 3,-3 7,5
             C1,-1 -1,1 -7,7 C-5,-1 -7,-3 -15,-8
             C-7,-8 -5,-10 0,-20 Z"
          fill="{inner}" stroke="none"/>
  </g>

  <!-- ❤️ Chubby crayon heart — middle-right, tilted 20° -->
  <g transform="translate(192,118) rotate(20,0,0)" filter="url(#crayon)">
    <path d="M0,20 C-2,18 -22,8 -22,-6 C-22,-16 -14,-22 -4,-18
             C-2,-17 0,-14 0,-14 C0,-14 2,-17 4,-18
             C14,-22 22,-16 22,-6 C22,8 2,18 0,20 Z"
          fill="{heart}" stroke="{sk}" stroke-width="2.2"
          stroke-linejoin="round"/>
    <!-- shine mark — 80s cartoon highlight -->
    <path d="M-10,-12 Q-6,-16 -2,-12" fill="none" stroke="{sk}"
          stroke-width="2" stroke-linecap="round" opacity="0.6"/>
  </g>

  <!-- 🦕 Tiny lumpy dinosaur silhouette — bottom-left, tilted 8° -->
  <g transform="translate(44,186) rotate(8,0,0)" filter="url(#marker)">
    <!-- body -->
    <ellipse cx="0" cy="0" rx="22" ry="14" fill="{dino}" stroke="{sk}"
             stroke-width="2"/>
    <!-- neck -->
    <path d="M14,-10 C16,-18 22,-24 24,-30 C20,-28 14,-22 10,-14 Z"
          fill="{dino}" stroke="{sk}" stroke-width="2" stroke-linejoin="round"/>
    <!-- head -->
    <ellipse cx="24" cy="-32" rx="9" ry="7" fill="{dino}" stroke="{sk}"
             stroke-width="2"/>
    <!-- eye -->
    <circle cx="28" cy="-34" r="2" fill="{sk}" opacity="0.7"/>
    <!-- tail -->
    <path d="M-22,4 C-30,2 -36,-2 -38,-8" fill="none" stroke="{dino}"
          stroke-width="5" stroke-linecap="round"/>
    <!-- legs -->
    <line x1="-8"  y1="13" x2="-10" y2="24" stroke="{dino}" stroke-width="5"
          stroke-linecap="round"/>
    <line x1="8"   y1="13" x2="10"  y2="24" stroke="{dino}" stroke-width="5"
          stroke-linecap="round"/>
    <!-- spikes on back -->
    <polygon points="0,-14 -4,-22 4,-22" fill="{dino}" stroke="{sk}" stroke-width="1"/>
    <polygon points="8,-14 4,-20 12,-20" fill="{dino}" stroke="{sk}" stroke-width="1"/>
  </g>

  <!-- ⚡ Fat marker zigzag bolt — bottom-right, tilted -10° -->
  <g transform="translate(188,178) rotate(-10,0,0)" filter="url(#crayon)">
    <path d="M6,-28 C4,-20 2,-14 -4,-8 C2,-8 8,-8 8,-8
             C4,2 0,10 -8,20 C0,14 6,14 6,14
             C2,20 -2,24 -6,28
             L8,10 C2,10 -2,10 -2,10
             C2,0 6,-6 12,-14
             C6,-14 2,-14 2,-14 Z"
          fill="{zigzag}" stroke="{sk}" stroke-width="2"
          stroke-linejoin="round" stroke-linecap="round"/>
  </g>

  <!-- small scattered doodle marks -->
  <!-- wobbly circle — top-center -->
  <circle cx="120" cy="22" r="7" fill="none" stroke="{bubble}"
          stroke-width="2.5" stroke-dasharray="3,2" filter="url(#crayon)"/>
  <!-- x mark -->
  <g transform="translate(164,148) rotate(15,0,0)">
    <line x1="-6" y1="-6" x2="6" y2="6" stroke="{star}" stroke-width="3"
          stroke-linecap="round"/>
    <line x1="6" y1="-6" x2="-6" y2="6" stroke="{star}" stroke-width="3"
          stroke-linecap="round"/>
  </g>
  <!-- tiny star sparkle -->
  <g transform="translate(102,148)">
    <line x1="0" y1="-6" x2="0" y2="6" stroke="{sun}" stroke-width="2.5"
          stroke-linecap="round"/>
    <line x1="-6" y1="0" x2="6" y2="0" stroke="{sun}" stroke-width="2.5"
          stroke-linecap="round"/>
    <line x1="-4" y1="-4" x2="4" y2="4" stroke="{sun}" stroke-width="2"
          stroke-linecap="round"/>
    <line x1="4" y1="-4" x2="-4" y2="4" stroke="{sun}" stroke-width="2"
          stroke-linecap="round"/>
  </g>
</svg>"""

    encoded = base64.b64encode(svg.encode()).decode()
    return f"data:image/svg+xml;base64,{encoded}"


# ─────────────────────────────────────────────────────────────────────────────
# Theme injection
# ─────────────────────────────────────────────────────────────────────────────
def inject_theme():
    dark = st.session_state.dark_mode
    bg_tile = cartoon_bg_svg(dark)

    # Shared Bangers import + sidebar font overrides used in both modes
    bangers_url = "https://fonts.googleapis.com/css2?family=Bangers&family=Nunito:wght@400;600;700;800&display=swap"

    sidebar_font_rules = """
        /* ── Force Bangers on ALL sidebar text ── */
        [data-testid="stSidebar"],
        [data-testid="stSidebar"] *,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] div,
        [data-testid="stSidebar"] a,
        [data-testid="stSidebar"] .stRadio label,
        [data-testid="stSidebar"] .stMarkdown,
        [data-testid="stSidebar"] .stCaption,
        [data-testid="stSidebar"] small {
            font-family: 'Bangers', cursive !important;
            letter-spacing: 1.2px !important;
        }
        /* Byline caption — slightly smaller */
        [data-testid="stSidebar"] .stCaption,
        [data-testid="stSidebar"] small {
            font-size: 0.78rem !important;
            letter-spacing: 0.8px !important;
            opacity: 0.82;
        }
        /* Sidebar metric numbers — 2x larger */
        [data-testid="stSidebar"] [data-testid="stMetricValue"] {
            font-family: 'Bangers', cursive !important;
            font-size: 4.8rem !important;
            letter-spacing: 2px !important;
            line-height: 1.1 !important;
        }
        [data-testid="stSidebar"] [data-testid="metric-container"] {
            padding: 12px 10px 8px 10px !important;
        }
        [data-testid="stSidebar"] [data-testid="metric-container"] label {
            font-size: 1rem !important;
            letter-spacing: 1px !important;
        }
        [data-testid="stSidebar"] .stRadio label {
            font-size: 1.15rem !important;
        }
    """

    if dark:
        css = f"""
        <style>
        @import url('{bangers_url}');

        :root {{
            --bg-main:      #0f0e17;
            --bg-card:      #1e1b2e;
            --bg-sidebar:   #1c1008;
            --accent1:      #f97316;
            --accent2:      #38bdf8;
            --accent3:      #fbbf24;
            --accent5:      #34d399;
            --text-main:    #fef3c7;
            --text-body:    #e8d5b7;
            --text-muted:   #a78bfa;
            --heading-font: 'Bangers', cursive;
            --body-font:    'Nunito', sans-serif;
        }}

        html, body, [data-testid="stAppViewContainer"] {{
            background-color: var(--bg-main) !important;
            font-family: var(--body-font) !important;
            color: var(--text-main) !important;
            font-size: 17px !important;
        }}

        p, li, .stMarkdown p, [data-testid="stMarkdownContainer"] p {{
            color: var(--text-body) !important;
            font-size: 1.05rem !important;
            line-height: 1.7 !important;
        }}

        [data-testid="stAppViewContainer"]::before {{
            content: "";
            position: fixed;
            inset: 0;
            background-image: url('{bg_tile}');
            background-size: 240px 240px;
            background-repeat: repeat;
            pointer-events: none;
            z-index: 0;
            opacity: 0.78;
        }}

        [data-testid="stSidebar"] {{
            background: var(--bg-sidebar) !important;
            border-right: 3px solid var(--accent1) !important;
        }}

        {sidebar_font_rules}

        .main .block-container {{ position: relative; z-index: 1; }}

        h1, [data-testid="stHeading"] h1 {{
            font-family: var(--heading-font) !important;
            letter-spacing: 2px !important;
            font-size: 2.6rem !important;
            color: var(--accent1) !important;
            text-shadow: 3px 3px 0px #1e1b2e, 5px 5px 0px var(--accent2) !important;
        }}
        h2, [data-testid="stHeading"] h2 {{
            font-family: var(--heading-font) !important;
            letter-spacing: 2px !important;
            font-size: 2rem !important;
            color: var(--accent2) !important;
            text-shadow: 2px 2px 0px #1e1b2e !important;
        }}
        h3, h4, h5, [data-testid="stHeading"] h3 {{
            font-family: var(--heading-font) !important;
            letter-spacing: 1.5px !important;
            font-size: 1.5rem !important;
            color: var(--accent3) !important;
        }}

        [data-testid="metric-container"] {{
            background: var(--bg-card) !important;
            border: 2px solid var(--accent2) !important;
            border-radius: 12px !important;
            padding: 10px !important;
            box-shadow: 4px 4px 0px var(--accent1) !important;
        }}
        [data-testid="metric-container"] label {{
            color: var(--accent3) !important;
            font-size: 0.95rem !important;
            font-weight: 800 !important;
        }}
        [data-testid="metric-container"] [data-testid="stMetricValue"] {{
            color: var(--accent2) !important;
            font-family: var(--heading-font) !important;
            font-size: 1.8rem !important;
        }}

        .stButton > button {{
            font-family: var(--heading-font) !important;
            letter-spacing: 2px !important;
            font-size: 1.15rem !important;
            background: var(--accent1) !important;
            color: #0f0e17 !important;
            border: 3px solid var(--accent2) !important;
            border-radius: 8px !important;
            box-shadow: 4px 4px 0px var(--accent2) !important;
            transition: all 0.12s ease !important;
        }}
        .stButton > button:hover {{
            transform: translate(-2px, -2px) !important;
            box-shadow: 6px 6px 0px var(--accent2) !important;
        }}

        .stTextInput input, .stTextArea textarea, .stNumberInput input {{
            background: var(--bg-card) !important;
            border: 1.5px solid rgba(249,115,22,0.5) !important;
            border-radius: 6px !important;
            color: var(--text-main) !important;
            font-family: var(--body-font) !important;
            font-size: 1rem !important;
            box-shadow: 0 1px 4px rgba(0,0,0,0.25) !important;
            transition: border-color 0.15s ease !important;
        }}
        .stTextInput input:focus, .stTextArea textarea:focus, .stNumberInput input:focus {{
            border-color: var(--accent1) !important;
            box-shadow: 0 0 0 2px rgba(249,115,22,0.25) !important;
        }}
        .stTextInput label, .stTextArea label, .stNumberInput label,
        .stSelectbox label, .stCheckbox label {{
            color: var(--text-main) !important;
            font-size: 0.95rem !important;
            font-weight: 700 !important;
            letter-spacing: 0.3px !important;
            text-transform: uppercase !important;
        }}
        .stSelectbox [data-baseweb="select"] {{
            background: var(--bg-card) !important;
            border: 1.5px solid rgba(56,189,248,0.5) !important;
            border-radius: 6px !important;
            color: var(--text-main) !important;
            box-shadow: 0 1px 4px rgba(0,0,0,0.20) !important;
        }}

        details {{
            background: var(--bg-card) !important;
            border: 1.5px solid rgba(249,115,22,0.4) !important;
            border-radius: 8px !important;
            margin-bottom: 6px !important;
            box-shadow: 0 1px 4px rgba(0,0,0,0.18) !important;
        }}
        summary {{
            color: var(--accent3) !important;
            font-weight: 800 !important;
            font-size: 1.05rem !important;
            letter-spacing: 0.3px !important;
        }}

        .stTabs [data-baseweb="tab"] {{
            font-family: var(--heading-font) !important;
            font-size: 1.1rem !important;
            letter-spacing: 1.5px !important;
            color: var(--text-muted) !important;
        }}
        .stTabs [aria-selected="true"] {{
            color: var(--accent1) !important;
            border-bottom: 3px solid var(--accent1) !important;
        }}

        .stAlert {{ border-radius: 10px !important; font-size: 1rem !important; }}
        .stAlert p {{ font-size: 1rem !important; color: inherit !important; }}
        hr {{ border-color: var(--accent1) !important; opacity: 0.35 !important; }}
        .stCaption, small {{ color: var(--text-muted) !important; font-size: 0.95rem !important; }}
        ::-webkit-scrollbar {{ width: 8px; background: var(--bg-main); }}
        ::-webkit-scrollbar-thumb {{ background: var(--accent1); border-radius: 4px; }}
        </style>
        """
    else:
        css = f"""
        <style>
        @import url('{bangers_url}');

        :root {{
            --bg-main:      #fff7ed;
            --bg-card:      #ffffff;
            --accent1:      #ea580c;
            --accent2:      #0891b2;
            --accent3:      #d97706;
            --accent5:      #16a34a;
            --text-main:    #1c1917;
            --text-body:    #292524;
            --text-muted:   #57534e;
            --heading-font: 'Bangers', cursive;
            --body-font:    'Nunito', sans-serif;
        }}

        html, body, [data-testid="stAppViewContainer"] {{
            font-family: var(--body-font) !important;
            color: var(--text-main) !important;
            font-size: 17px !important;
        }}

        p, li, .stMarkdown p, [data-testid="stMarkdownContainer"] p {{
            color: var(--text-body) !important;
            font-size: 1.05rem !important;
            line-height: 1.7 !important;
        }}

        [data-testid="stAppViewContainer"] {{
            background:
                radial-gradient(ellipse at 5%  10%, rgba(234,88,12,0.14)  0%, transparent 40%),
                radial-gradient(ellipse at 90%  8%, rgba(8,145,178,0.13)  0%, transparent 38%),
                radial-gradient(ellipse at 80% 85%, rgba(217,119,6,0.14)  0%, transparent 42%),
                radial-gradient(ellipse at 15% 90%, rgba(22,163,74,0.12)  0%, transparent 38%),
                radial-gradient(ellipse at 50% 50%, rgba(139,92,246,0.08) 0%, transparent 52%),
                #fff7ed !important;
        }}

        [data-testid="stAppViewContainer"]::before {{
            content: "";
            position: fixed;
            inset: 0;
            background-image: url('{bg_tile}');
            background-size: 240px 240px;
            background-repeat: repeat;
            pointer-events: none;
            z-index: 0;
            opacity: 0.88;
        }}

        [data-testid="stSidebar"] {{
            background: linear-gradient(155deg, #fde68a 0%, #fbbf24 40%, #f97316 100%) !important;
            border-right: 4px solid var(--accent1) !important;
        }}
        /* Amber sidebar needs dark text */
        [data-testid="stSidebar"],
        [data-testid="stSidebar"] * {{
            color: #1c1917 !important;
        }}

        {sidebar_font_rules}

        .main .block-container {{ position: relative; z-index: 1; }}

        h1, [data-testid="stHeading"] h1 {{
            font-family: var(--heading-font) !important;
            letter-spacing: 2.5px !important;
            font-size: 2.6rem !important;
            color: var(--accent1) !important;
            text-shadow: 3px 3px 0px #fff, 5px 5px 0px var(--accent2) !important;
        }}
        h2, [data-testid="stHeading"] h2 {{
            font-family: var(--heading-font) !important;
            letter-spacing: 2px !important;
            font-size: 2rem !important;
            color: var(--accent2) !important;
            text-shadow: 2px 2px 0px rgba(0,0,0,0.08) !important;
        }}
        h3, h4, h5, [data-testid="stHeading"] h3 {{
            font-family: var(--heading-font) !important;
            letter-spacing: 1.5px !important;
            font-size: 1.5rem !important;
            color: var(--accent1) !important;
        }}

        [data-testid="metric-container"] {{
            background: var(--bg-card) !important;
            border: 3px solid var(--accent1) !important;
            border-radius: 14px !important;
            padding: 10px !important;
            box-shadow: 5px 5px 0px var(--accent2) !important;
        }}
        [data-testid="metric-container"] label {{
            color: var(--accent3) !important;
            font-size: 0.95rem !important;
            font-weight: 800 !important;
        }}
        [data-testid="metric-container"] [data-testid="stMetricValue"] {{
            color: var(--accent1) !important;
            font-family: var(--heading-font) !important;
            font-size: 1.8rem !important;
        }}

        .stButton > button {{
            font-family: var(--heading-font) !important;
            letter-spacing: 2px !important;
            font-size: 1.15rem !important;
            background: var(--accent1) !important;
            color: #fff !important;
            border: 3px solid var(--accent2) !important;
            border-radius: 8px !important;
            box-shadow: 4px 4px 0px var(--accent2) !important;
            transition: all 0.12s ease !important;
        }}
        .stButton > button:hover {{
            transform: translate(-2px, -2px) !important;
            box-shadow: 6px 6px 0px var(--accent2) !important;
        }}

        .stTextInput input, .stTextArea textarea, .stNumberInput input {{
            background: var(--bg-card) !important;
            border: 1.5px solid rgba(234,88,12,0.45) !important;
            border-radius: 6px !important;
            color: var(--text-main) !important;
            font-family: var(--body-font) !important;
            font-size: 1rem !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.10) !important;
            transition: border-color 0.15s ease !important;
        }}
        .stTextInput input:focus, .stTextArea textarea:focus, .stNumberInput input:focus {{
            border-color: var(--accent1) !important;
            box-shadow: 0 0 0 2px rgba(234,88,12,0.18) !important;
        }}
        .stTextInput label, .stTextArea label, .stNumberInput label,
        .stSelectbox label, .stCheckbox label {{
            color: var(--text-main) !important;
            font-size: 0.95rem !important;
            font-weight: 700 !important;
            letter-spacing: 0.3px !important;
            text-transform: uppercase !important;
        }}
        .stSelectbox [data-baseweb="select"] {{
            background: var(--bg-card) !important;
            border: 1.5px solid rgba(8,145,178,0.45) !important;
            border-radius: 6px !important;
            color: var(--text-main) !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.08) !important;
        }}

        details {{
            background: var(--bg-card) !important;
            border: 1.5px solid rgba(234,88,12,0.35) !important;
            border-radius: 8px !important;
            margin-bottom: 6px !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.07) !important;
        }}
        summary {{
            color: var(--accent1) !important;
            font-weight: 800 !important;
            font-size: 1.05rem !important;
            letter-spacing: 0.3px !important;
        }}

        .stTabs [data-baseweb="tab"] {{
            font-family: var(--heading-font) !important;
            font-size: 1.1rem !important;
            letter-spacing: 1.5px !important;
            color: var(--text-muted) !important;
        }}
        .stTabs [aria-selected="true"] {{
            color: var(--accent1) !important;
            border-bottom: 3px solid var(--accent1) !important;
        }}

        .stAlert {{ border-radius: 10px !important; font-size: 1rem !important; }}
        .stAlert p {{ font-size: 1rem !important; color: var(--text-main) !important; }}
        hr {{ border-color: var(--accent1) !important; opacity: 0.25 !important; }}
        .stCaption, small {{ color: var(--text-muted) !important; font-size: 0.95rem !important; }}
        ::-webkit-scrollbar {{ width: 8px; background: var(--bg-main); }}
        ::-webkit-scrollbar-thumb {{ background: var(--accent1); border-radius: 4px; }}
        </style>
        """

    st.markdown(css, unsafe_allow_html=True)


inject_theme()

# ─────────────────────────────────────────────────────────────────────────────
# Session state
# ─────────────────────────────────────────────────────────────────────────────
if "library" not in st.session_state:
    st.session_state.library = build_library()

lib = st.session_state.library
analyzer = CartoonAnalyzer(lib)

# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────
def copyright_badge(cartoon: Cartoon):
    if cartoon.is_public_domain:
        st.success("✅  Public Domain — free to use")
    else:
        yrs = cartoon.years_until_public_domain
        if yrs <= 10:
            st.warning(f"⚠️  Protected — © {cartoon.current_owner.owner_name if cartoon.current_owner else '?'}  ({yrs} yrs until public domain)")
        else:
            st.error(f"🔒  Protected — © {cartoon.current_owner.owner_name if cartoon.current_owner else '?'}  ({yrs} yrs until public domain)")


def render_ownership_chain(cartoon: Cartoon):
    st.markdown(f"##### 📋 Complete Ownership History — {len(cartoon.ownership_history)} owner(s)")
    total = len(cartoon.ownership_history)
    orig = cartoon.original_owner
    curr = cartoon.current_owner
    c1, c2, c3 = st.columns(3)
    c1.metric("Original Owner", orig.owner_name if orig else "Unknown", help="Who owned it when first created")
    c2.metric("Current Owner", curr.owner_name if curr else "Public Domain", help="Who owns it today")
    c3.metric("Times Changed Hands", total - 1)
    st.divider()
    st.markdown("**Full ownership timeline — every company, every year:**")
    st.caption("Read top to bottom from creation to present day.")
    st.markdown("---")
    for i, record in enumerate(cartoon.ownership_history):
        is_first   = (i == 0)
        is_current = record.is_current_owner
        year_end   = record.year_relinquished or datetime.now().year
        years_held = year_end - record.year_acquired
        year_end_label = str(record.year_relinquished) if record.year_relinquished else "present"
        if is_current and is_first:
            icon = "🟢"; label = "ORIGINAL & CURRENT OWNER"
        elif is_current:
            icon = "🟢"; label = "CURRENT OWNER"
        elif is_first:
            icon = "🔵"; label = "ORIGINAL OWNER (at creation)"
        else:
            icon = "⚪"; label = f"PREVIOUS OWNER #{i}"
        col_icon, col_main, col_stats = st.columns([0.5, 4, 1.5])
        with col_icon:
            st.markdown(f"## {icon}")
        with col_main:
            st.markdown(f"**{label}**")
            st.markdown(f"## {record.owner_name}")
            st.markdown(
                f"📅 &nbsp; Owned from **{record.year_acquired}** to **{year_end_label}** &nbsp;|&nbsp; "
                f"🤝 &nbsp; How acquired: *{record.acquisition_method}*"
            )
            if record.notes:
                st.info(f"📌 {record.notes}")
        with col_stats:
            st.metric("Years held", f"{years_held} yrs")
            if is_current:
                st.success("Active")
            else:
                st.caption(f"Ended {record.year_relinquished}")
        if i < total - 1:
            next_record = cartoon.ownership_history[i + 1]
            st.markdown(
                f"&nbsp; &nbsp; &nbsp; &nbsp; ⬇️ &nbsp; *Transferred to* ***{next_record.owner_name}*** "
                f"*in {next_record.year_acquired} via {next_record.acquisition_method}*"
            )
        st.markdown("---")
    st.markdown("##### ⚖️ Copyright status today")
    if cartoon.is_public_domain:
        st.success(f"✅ **PUBLIC DOMAIN** — This character entered the public domain and is free to use. Original debut: {cartoon.debut_year}.")
    else:
        yrs = cartoon.years_until_public_domain
        st.error(
            f"🔒 **PROTECTED** — Currently owned by **{curr.owner_name if curr else 'Unknown'}**. "
            f"Under US copyright law this character will enter the public domain in approximately **{yrs} year(s)** ({datetime.now().year + yrs})."
        )


def render_era_timeline(cartoon: Cartoon):
    st.markdown("##### Visual timeline")
    for era in cartoon.eras:
        end_label = str(era.year_end) if era.year_end else "present"
        with st.expander(f"**{era.year_start} – {end_label}** · {era.art_style}"):
            col1, col2 = st.columns([2, 1])
            with col1:
                st.write(era.visual_description)
                if era.notes:
                    st.caption(f"📝 {era.notes}")
            with col2:
                if era.image_url:
                    st.image(era.image_url, caption=f"{era.year_start}–{end_label}", width=180)


def render_series_list(cartoon: Cartoon):
    st.markdown(f"##### All series & productions ({len(cartoon.series_list)} total)")
    for s in cartoon.series_list:
        end_label = str(s.year_ended) if s.year_ended else "present"
        years = (s.year_ended or datetime.now().year) - s.year_started
        with st.expander(f"**{s.title}** ({s.year_started}–{end_label})"):
            col1, col2, col3 = st.columns(3)
            col1.metric("Medium", s.medium)
            col2.metric("Years running", years)
            col3.metric("Episodes", s.episode_count if s.episode_count else "N/A")
            st.caption(f"📺 Produced by: {s.produced_by}")
            if s.notes:
                st.info(f"ℹ️ {s.notes}")


def render_creators(cartoon: Cartoon):
    st.markdown("##### Creators")
    for c in cartoon.creators:
        born = str(c.birth_year) if c.birth_year else "?"
        died = str(c.death_year) if c.death_year else "present"
        st.markdown(f"- **{c.full_name}** — {c.role}  ·  *{born}–{died}*")


# ─────────────────────────────────────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────────────────────────────────────
st.sidebar.markdown(sidebar_logo(st.session_state.dark_mode), unsafe_allow_html=True)
st.sidebar.caption("Cartoon copyright & visual history explorer")
st.sidebar.divider()

mode_label = "☀️ Light Mode" if st.session_state.dark_mode else "🌙 Dark Mode"
if st.sidebar.button(mode_label, use_container_width=True):
    st.session_state.dark_mode = not st.session_state.dark_mode
    st.rerun()

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigate",
    ["🔍 Search", "📚 Browse All", "⚖️ Copyright Dashboard", "➕ Add a Cartoon"],
    label_visibility="collapsed",
)

st.sidebar.divider()
summary = analyzer.get_copyright_summary()
st.sidebar.metric("In library", summary["total"])
st.sidebar.metric("Public domain", summary["public_domain"])
st.sidebar.metric("Protected", summary["protected"])

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: Search
# ─────────────────────────────────────────────────────────────────────────────
if page == "🔍 Search":
    st.title("🔍 Search CartoonPal")
    query = st.text_input("Enter a cartoon name", placeholder="e.g. Bugs Bunny, Betty Boop, Felix…")

    if query:
        result = lib.find(query)
        if result:
            # ── Cartoon sound effect (Web Audio API via inline JS) ─────────
            # Plays a classic 2-tone "boing" on each successful search result
            cartoon_sound_js = """
            <script>
            (function() {
                try {
                    var ctx = new (window.AudioContext || window.webkitAudioContext)();
                    function playNote(freq, startTime, duration, type) {
                        var osc = ctx.createOscillator();
                        var gain = ctx.createGain();
                        osc.connect(gain);
                        gain.connect(ctx.destination);
                        osc.type = type || 'sine';
                        osc.frequency.setValueAtTime(freq, startTime);
                        osc.frequency.exponentialRampToValueAtTime(freq * 1.8, startTime + 0.08);
                        osc.frequency.exponentialRampToValueAtTime(freq * 0.5, startTime + duration * 0.6);
                        gain.gain.setValueAtTime(0.28, startTime);
                        gain.gain.exponentialRampToValueAtTime(0.001, startTime + duration);
                        osc.start(startTime);
                        osc.stop(startTime + duration);
                    }
                    var now = ctx.currentTime;
                    playNote(440, now,        0.22, 'square');
                    playNote(660, now + 0.10, 0.18, 'sine');
                    playNote(880, now + 0.20, 0.30, 'sine');
                    playNote(330, now + 0.38, 0.40, 'triangle');
                } catch(e) {}
            })();
            </script>
            """
            st.components.v1.html(cartoon_sound_js, height=0)

            # ── Solid result card background ────────────────────────────────
            dark = st.session_state.dark_mode
            card_bg  = "#1e1b2e" if dark else "#ffffff"
            card_bdr = "#f97316" if dark else "#ea580c"
            st.markdown(f"""
            <style>
            .result-card {{
                background: {card_bg};
                border: 2px solid {card_bdr};
                border-radius: 14px;
                padding: 24px 28px 18px 28px;
                margin-bottom: 16px;
                box-shadow: 5px 5px 0px {card_bdr}44;
            }}
            /* Kill the doodle background in the main block while results show */
            [data-testid="stAppViewContainer"]::before {{
                opacity: 0.18 !important;
            }}
            </style>
            """, unsafe_allow_html=True)

            st.divider()
            col1, col2 = st.columns([2, 1])
            with col1:
                st.header(result.name)
                st.caption(f"Debuted **{result.debut_year}** · {result.character_type} · {result.country_of_origin}")
                st.write(result.description)
                if result.origin_location:
                    st.markdown(f"📍 **Origin:** {result.origin_location}")
                if result.wiki_url:
                    st.markdown(f"[📖 Wikipedia page]({result.wiki_url})")
            with col2:
                copyright_badge(result)
                st.caption(f"Original studio: **{result.original_studio}**")
                orig = result.original_owner
                curr = result.current_owner
                if orig:
                    st.caption(f"Originally owned by: **{orig.owner_name}**")
                if curr:
                    st.caption(f"Currently owned by: **{curr.owner_name}**")
                current_era = result.get_era_at(datetime.now().year)
                if current_era and current_era.image_url:
                    st.image(current_era.image_url, caption=f"Current look ({current_era.art_style})", width=200)

            st.divider()
            tab1, tab2, tab3, tab4 = st.tabs(["👥 Creators", "🏭 Ownership", "📺 Series", "🎨 Visual Eras"])
            with tab1:
                render_creators(result)
            with tab2:
                render_ownership_chain(result)
                overlaps = analyzer.detect_series_overlap(result)
                if overlaps:
                    st.warning(f"⚠️ {len(overlaps)} overlapping series detected")
                    for a, b in overlaps:
                        st.caption(f"'{a.title}' and '{b.title}' ran concurrently")
            with tab3:
                render_series_list(result)
            with tab4:
                render_era_timeline(result)
        else:
            st.warning(f"No cartoon found matching '{query}'. Try Browse All to see what's in the library.")

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: Browse All
# ─────────────────────────────────────────────────────────────────────────────
elif page == "📚 Browse All":
    st.title("📚 Browse All Cartoons")

    col1, col2, col3 = st.columns(3)
    sort_by = col1.selectbox("Sort by", ["Debut year (oldest first)", "Debut year (newest first)", "Name A–Z"])
    filter_status = col2.selectbox("Copyright filter", ["All", "Public domain only", "Protected only"])
    filter_studio = col3.text_input("Filter by studio", placeholder="e.g. Disney, Fleischer…")

    if sort_by == "Debut year (oldest first)":
        cartoons = analyzer.sort_by_debut(ascending=True)
    elif sort_by == "Debut year (newest first)":
        cartoons = analyzer.sort_by_debut(ascending=False)
    else:
        cartoons = analyzer.sort_by_name()

    if filter_status == "Public domain only":
        cartoons = [c for c in cartoons if c.is_public_domain]
    elif filter_status == "Protected only":
        cartoons = [c for c in cartoons if not c.is_public_domain]

    if filter_studio.strip():
        cartoons = [c for c in cartoons
                    if c.original_studio and filter_studio.lower() in c.original_studio.company_name.lower()]

    st.caption(f"Showing {len(cartoons)} cartoon(s)")
    st.divider()

    for cartoon in cartoons:
        with st.container():
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.subheader(cartoon.name)
                st.caption(f"{cartoon.debut_year} · {cartoon.character_type} · {cartoon.original_studio}")
                st.write(cartoon.description[:180] + "…" if len(cartoon.description) > 180 else cartoon.description)
                creator_names = ", ".join(c.full_name for c in cartoon.creators)
                st.caption(f"Created by: {creator_names}")
                if hasattr(cartoon, 'origin_location') and cartoon.origin_location:
                    st.caption(f"📍 {cartoon.origin_location}")
                if hasattr(cartoon, 'wiki_url') and cartoon.wiki_url:
                    st.markdown(f"[📖 Wikipedia]({cartoon.wiki_url})")
            with col2:
                if cartoon.is_public_domain:
                    st.success("✅ Public Domain")
                else:
                    st.error("🔒 Protected")
                    st.caption(f"{cartoon.years_until_public_domain} yrs left")
            with col3:
                curr = cartoon.current_owner
                orig = cartoon.original_owner
                st.caption(f"**Original owner:**\n{orig.owner_name if orig else '?'}")
                st.caption(f"**Current owner:**\n{curr.owner_name if curr else 'Public domain'}")
            st.divider()

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: Copyright Dashboard
# ─────────────────────────────────────────────────────────────────────────────
elif page == "⚖️ Copyright Dashboard":
    st.title("⚖️ Copyright Dashboard")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total cartoons", summary["total"])
    c2.metric("Public domain", summary["public_domain"])
    c3.metric("Protected", summary["protected"])
    c4.metric("% public domain", f"{summary['pd_percent']}%")

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("✅ Public domain")
        for c in lib.all_public_domain():
            st.markdown(f"- **{c.name}** ({c.debut_year})")
    with col2:
        st.subheader("🔒 Protected")
        for c in sorted(lib.all_protected(), key=lambda x: x.years_until_public_domain):
            curr = c.current_owner.owner_name if c.current_owner else "?"
            yrs  = c.years_until_public_domain
            st.markdown(f"- **{c.name}** ({c.debut_year}) — © {curr} — *{yrs} yrs until public domain*")

    st.divider()
    st.subheader("⏳ Approaching public domain (within 20 years)")
    approaching = analyzer.flag_approaching_public_domain(within_years=20)
    if approaching:
        for c in sorted(approaching, key=lambda x: x.years_until_public_domain):
            curr = c.current_owner.owner_name if c.current_owner else "?"
            st.info(f"**{c.name}** — {c.years_until_public_domain} year(s) remaining — currently © {curr}")
    else:
        st.caption("No cartoons in the library are entering public domain within 20 years.")

    st.divider()
    st.subheader("🔄 Ownership changed since creation")
    for c in analyzer.ownership_changed_cartoons():
        orig = c.original_owner.owner_name if c.original_owner else "?"
        curr = c.current_owner.owner_name if c.current_owner else "public domain"
        st.markdown(f"- **{c.name}**: {orig} → **{curr}**")

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: Add a Cartoon
# ─────────────────────────────────────────────────────────────────────────────
elif page == "➕ Add a Cartoon":
    st.title("➕ Add a Cartoon")
    st.caption("Fill in the details below. Fields marked * are required.")

    with st.form("add_cartoon_form"):
        st.subheader("Basic information")
        col1, col2 = st.columns(2)
        name = col1.text_input("Cartoon name *")
        debut_year = col2.number_input("Debut year *", min_value=1880, max_value=datetime.now().year, value=1950)
        description = st.text_area("Description *", height=100)
        character_type = st.text_input("Character type", placeholder="e.g. Anthropomorphic animal — cat")
        country = st.text_input("Country of origin", value="USA")

        st.subheader("Creators")
        creator1_name = st.text_input("Creator 1 — full name")
        creator1_role = st.text_input("Creator 1 — role", placeholder="e.g. Character designer")

        st.subheader("Original studio")
        studio_name    = st.text_input("Studio name")
        studio_founded = st.number_input("Studio founded year", min_value=1880, max_value=datetime.now().year, value=1920)
        studio_active  = st.checkbox("Studio still active", value=True)

        st.subheader("Original ownership")
        orig_owner  = st.text_input("Original owner name *")
        orig_year   = st.number_input("Year acquired", min_value=1880, max_value=datetime.now().year, value=int(debut_year))
        orig_method = st.text_input("Acquisition method", value="original creation")

        st.subheader("Current ownership")
        same_owner      = st.checkbox("Same as original owner", value=True)
        curr_owner_name = st.text_input("Current owner name (if different)")
        curr_year       = st.number_input("Year current owner acquired", min_value=1880, max_value=datetime.now().year, value=int(debut_year))
        curr_method     = st.text_input("Current acquisition method", value="original creation")

        submitted = st.form_submit_button("Add cartoon to library")

    if submitted:
        if not name or not description or not orig_owner:
            st.error("Please fill in all required fields (name, description, original owner).")
        elif lib.find(name):
            st.warning(f"'{name}' already exists in the library.")
        else:
            new_cartoon = Cartoon(
                name=name,
                description=description,
                character_type=character_type or "Unknown",
                country_of_origin=country or "USA",
                debut_year=int(debut_year),
            )
            if studio_name:
                new_cartoon.original_studio = ProductionCompany(studio_name, int(studio_founded), still_active=studio_active)
            if creator1_name:
                new_cartoon.add_creator(Creator(creator1_name, creator1_role or "Creator"))

            if same_owner:
                new_cartoon.add_ownership_record(OwnershipRecord(
                    orig_owner, int(orig_year), None, orig_method, is_current_owner=True))
            else:
                new_cartoon.add_ownership_record(OwnershipRecord(
                    orig_owner, int(orig_year), int(curr_year), orig_method))
                if curr_owner_name:
                    new_cartoon.add_ownership_record(OwnershipRecord(
                        curr_owner_name, int(curr_year), None, curr_method, is_current_owner=True))

            lib.add_cartoon(new_cartoon)
            st.success(f"✅ '{name}' added to the library! Go to Search or Browse All to view it.")