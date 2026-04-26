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
    """
    CartoonPal sidebar logo — 3:1 width:height ratio (~216×72px).
    Left icon cell: hand-drawn SVG cartoon face (spiky hair, big eyes, grin).
    Right text cell: CARTOONPAL title + subtitle in Bangers.
    Built as an HTML table so Streamlit's wildcard sidebar CSS cannot
    override the cell backgrounds or layout.
    """
    if dark:
        bg      = "#1e1b2e"
        border  = "#f97316"
        shadow  = "#f97316"
        title_c = "#fef3c7"
        sub_c   = "#fb923c"
        icon_bg = "#f97316"
        face_c  = "#fbbf24"   # cartoon face fill
        eye_c   = "#1e1b2e"   # eyes
        hair_c  = "#fef3c7"   # spiky hair
        cheek_c = "#fb7185"   # rosy cheeks
    else:
        bg      = "#fff7ed"
        border  = "#ea580c"
        shadow  = "#c2410c"
        title_c = "#1c1917"
        sub_c   = "#9a3412"
        icon_bg = "#ea580c"
        face_c  = "#fde68a"
        eye_c   = "#1c1917"
        hair_c  = "#1c1917"
        cheek_c = "#fca5a5"

    # Hand-drawn cartoon character SVG: round head, spiky hair, big dot eyes,
    # wide grin, rosy cheeks — classic 80s cartoon style at 46×46px viewBox.
    cartoon_svg = f"""<svg viewBox="0 0 46 46" width="46" height="46"
         xmlns="http://www.w3.org/2000/svg">
  <!-- Spiky hair — drawn as jagged polygon behind the head -->
  <polygon points="23,2 18,10 14,4 12,12 8,7 10,15 5,14 10,20 23,18 36,20 41,14 36,7 38,12 34,4 30,10"
           fill="{hair_c}" stroke="{hair_c}" stroke-linejoin="round" stroke-width="1"/>
  <!-- Face circle — slightly wobbly for hand-drawn feel -->
  <ellipse cx="23" cy="28" rx="14" ry="15"
           fill="{face_c}" stroke="{border}" stroke-width="2"/>
  <!-- Rosy cheeks -->
  <ellipse cx="13" cy="31" rx="4" ry="2.5" fill="{cheek_c}" opacity="0.55"/>
  <ellipse cx="33" cy="31" rx="4" ry="2.5" fill="{cheek_c}" opacity="0.55"/>
  <!-- Eyes — big filled circles with white shine -->
  <circle cx="17" cy="26" r="3.5" fill="{eye_c}"/>
  <circle cx="29" cy="26" r="3.5" fill="{eye_c}"/>
  <circle cx="18.2" cy="24.8" r="1.2" fill="white" opacity="0.9"/>
  <circle cx="30.2" cy="24.8" r="1.2" fill="white" opacity="0.9"/>
  <!-- Wide cartoon grin -->
  <path d="M14,34 Q23,42 32,34" fill="none" stroke="{eye_c}"
        stroke-width="2.5" stroke-linecap="round"/>
  <!-- Teeth peek -->
  <path d="M17,35 Q23,40 29,35" fill="white" stroke="none" opacity="0.7"/>
  <!-- Star sparkle accent -->
  <polygon points="39,6 40,3 41,6 44,6 42,8 43,11 40,9 37,11 38,8 36,6"
           fill="{face_c}" stroke="{border}" stroke-width="0.7" opacity="0.9"/>
</svg>"""

    return f"""
<link href="https://fonts.googleapis.com/css2?family=Bangers&display=swap" rel="stylesheet">
<style>
  .cp-logo-wrap  {{ all:unset; display:block; padding:4px 0 10px 0;
                    width:216px; min-width:216px; max-width:216px; }}
  .cp-logo-tbl   {{ border-collapse:separate; border-spacing:0;
                    background:{bg}; border:2.5px solid {border};
                    border-radius:14px; width:216px; min-width:216px; max-width:216px;
                    table-layout:fixed;
                    box-shadow:3px 3px 0px {shadow}55; overflow:hidden; }}
  .cp-logo-icon  {{ width:66px; padding:8px 0 8px 10px; vertical-align:middle;
                    background:{icon_bg}; }}
  .cp-logo-text  {{ padding:10px 10px 10px 10px; vertical-align:middle; }}
  .cp-logo-title {{ font-family:'Bangers',Impact,cursive !important;
                    font-size:1.55rem; letter-spacing:3px;
                    color:{title_c} !important; line-height:1.05;
                    display:block; white-space:nowrap; }}
  .cp-logo-sub   {{ font-family:'Bangers',Impact,cursive !important;
                    font-size:0.58rem; letter-spacing:1.4px;
                    color:{sub_c} !important; opacity:0.88;
                    display:block; white-space:nowrap; margin-top:2px; }}
</style>
<div class="cp-logo-wrap">
  <table class="cp-logo-tbl" cellpadding="0" cellspacing="0">
    <tr>
      <td class="cp-logo-icon">{cartoon_svg}</td>
      <td class="cp-logo-text">
        <span class="cp-logo-title">CARTOONPAL</span>
        <span class="cp-logo-sub">COPYRIGHT &amp; VISUAL HISTORY</span>
      </td>
    </tr>
  </table>
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
# Page header banner — rounded box with icon + title, used on Browse/Copyright/Add
# ─────────────────────────────────────────────────────────────────────────────
_PAGE_HEADER_CSS = """
<style>
.pg-header-wrap { margin: 0 0 18px 0; }
.pg-header-tbl  { border-collapse:separate; border-spacing:0;
                  border-radius:16px; overflow:hidden; }
.pg-header-icon { width:72px; text-align:center; vertical-align:middle;
                  font-size:2.2rem; padding:14px 0; }
.pg-header-text { vertical-align:middle; padding:14px 20px; }
.pg-header-title { font-family:'Bangers',Impact,cursive;
                   font-size:2rem; letter-spacing:3px;
                   line-height:1.05; display:block; white-space:nowrap; }
.pg-header-sub  { font-family:'Bangers',Impact,cursive;
                  font-size:0.72rem; letter-spacing:1.5px;
                  opacity:0.75; display:block; margin-top:3px; }
</style>
"""

def page_header_html(icon, title, subtitle, bg, border, icon_bg, title_c, sub_c, shadow):
    return f"""{_PAGE_HEADER_CSS}
<div class="pg-header-wrap">
  <table class="pg-header-tbl" cellpadding="0" cellspacing="0"
         style="background:{bg}; border:2.5px solid {border}; box-shadow:4px 4px 0px {shadow}44;">
    <tr>
      <td class="pg-header-icon" style="background:{icon_bg};">{icon}</td>
      <td class="pg-header-text">
        <span class="pg-header-title" style="color:{title_c};">{title}</span>
        <span class="pg-header-sub"   style="color:{sub_c};">{subtitle}</span>
      </td>
    </tr>
  </table>
</div>
"""

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
        /* ── Logo fixed size — does not stretch with sidebar ── */
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] div[style*="width: 240px"],
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] div[style*="width:240px"] {{
            width: 240px !important;
            min-width: 240px !important;
            max-width: 240px !important;
            flex-shrink: 0 !important;
        }}

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
            border-right: none !important;
            position: sticky !important;
            top: 0 !important;
            height: 100vh !important;
            overflow-y: auto !important;
            clip-path: polygon(
                0% 0%,
                98% 0%,   99% 2.5%,  97% 5%,
                99% 7.5%, 97% 10%,   99% 12.5%, 97% 15%,
                99% 17.5%,97% 20%,   99% 22.5%, 97% 25%,
                99% 27.5%,97% 30%,   99% 32.5%, 97% 35%,
                99% 37.5%,97% 40%,   99% 42.5%, 97% 45%,
                99% 47.5%,97% 50%,   99% 52.5%, 97% 55%,
                99% 57.5%,97% 60%,   99% 62.5%, 97% 65%,
                99% 67.5%,97% 70%,   99% 72.5%, 97% 75%,
                99% 77.5%,97% 80%,   99% 82.5%, 97% 85%,
                99% 87.5%,97% 90%,   99% 92.5%, 97% 95%,
                99% 97.5%,98% 100%,
                0% 100%
            ) !important;
        }}
        /* SVG wave stroke drawn as ::before — thick orange, sits outside clip-path */
        [data-testid="stSidebar"]::before {{
            content: "" !important;
            position: absolute !important;
            top: 0 !important; right: 0 !important;
            width: 28px !important; height: 100% !important;
            background-image: url("%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2228%22%20height%3D%221000%22%20preserveAspectRatio%3D%22none%22%3E%3Cpolyline%20points%3D%2210%2C0%208%2C0%2010%2C25%206%2C50%2010%2C75%206%2C100%2010%2C125%206%2C150%2010%2C175%206%2C200%2010%2C225%206%2C250%2010%2C275%206%2C300%2010%2C325%206%2C350%2010%2C375%206%2C400%2010%2C425%206%2C450%2010%2C475%206%2C500%2010%2C525%206%2C550%2010%2C575%206%2C600%2010%2C625%206%2C650%2010%2C675%206%2C700%2010%2C725%206%2C750%2010%2C775%206%2C800%2010%2C825%206%2C850%2010%2C875%206%2C900%2010%2C925%206%2C950%2010%2C975%208%2C1000%22%20fill%3D%22none%22%20stroke%3D%22%23f97316%22%20stroke-width%3D%2218%22%20stroke-linejoin%3D%22round%22%20stroke-linecap%3D%22round%22%2F%3E%3C%2Fsvg%3E") !important;
            background-size: 28px 100% !important;
            background-repeat: no-repeat !important;
            pointer-events: none !important;
            z-index: 999 !important;
        }}
        /* Thick orange fill behind the wave stroke */
        [data-testid="stSidebar"]::after {{
            content: "" !important;
            position: absolute !important;
            top: 0 !important; right: 0 !important;
            width: 4px !important; height: 100% !important;
            background: #f97316 !important;
            pointer-events: none !important;
            z-index: 998 !important;
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


        /* ── Hide ALL Streamlit keyboard/accessibility hint text ── */

        /* Radio widget screen-reader hints */
        [data-testid="stSidebar"] .stRadio [data-baseweb="radio"] ~ div > div[aria-hidden="true"],
        [data-testid="stSidebar"] .stRadio > div > div > div:last-child > div:last-child,
        [data-baseweb="radio"] + div[data-testid="stMarkdownContainer"],
        div[class*="st-emotion-cache"] span[aria-hidden="true"]:empty,
        .st-emotion-cache-hidden,
        span[style*="position: absolute"][style*="overflow: hidden"],
        span[style*="clip: rect(0px"][style*="white-space: nowrap"] {{
            display: none !important;
        }}

        /* ── Sidebar & top-bar collapse button tooltip text ── */
        /* Suppress the native browser tooltip by zeroing font on text nodes
           inside the collapse buttons, while keeping the SVG arrow visible */
        [data-testid="stSidebarCollapseButton"] span:not(:has(svg)),
        [data-testid="stSidebarCollapseButton"] > div > span,
        [data-testid="collapsedControl"] span:not(:has(svg)),
        [data-testid="collapsedControl"] > div > span,
        button[kind="header"] span:not(:has(svg)),
        button[data-testid="baseButton-header"] span:not(:has(svg)) {{
            font-size: 0 !important;
            width: 0 !important;
            overflow: hidden !important;
            display: inline-block !important;
        }}

        /* Prevent native browser title= tooltip from ever showing */
        [data-testid="stSidebarCollapseButton"],
        [data-testid="collapsedControl"],
        [data-testid="stSidebarCollapseButton"] *,
        [data-testid="collapsedControl"] * {{
            pointer-events: auto !important;
        }}
        /* Zero out any injected text-based tooltips via attribute */
        [data-testid="stSidebarCollapseButton"]::after,
        [data-testid="collapsedControl"]::after {{
            display: none !important;
            content: "" !important;
        }}

        /* Alert boxes — stronger border strokes */
        .stAlert {{
            border-radius: 10px !important;
            font-size: 1rem !important;
            border-width: 2px !important;
            border-style: solid !important;
            box-shadow: 3px 3px 0px rgba(0,0,0,0.45) !important;
        }}
        div[data-testid="stAlert"][data-baseweb="notification"][kind="error"],
        div.stAlert.st-emotion-cache-1wivap2 {{
            border-color: #c53030 !important;
            box-shadow: 3px 3px 0px #7b1c1c !important;
        }}
        div[data-testid="stAlert"][kind="warning"] {{
            border-color: #b45309 !important;
            box-shadow: 3px 3px 0px #78350f !important;
        }}
        div[data-testid="stAlert"][kind="success"] {{
            border-color: #166534 !important;
            box-shadow: 3px 3px 0px #14532d !important;
        }}
        .stAlert p {{ font-size: 1rem !important; color: inherit !important; }}
        hr {{ border-color: var(--accent1) !important; opacity: 0.35 !important; }}
        .stCaption, small {{ color: var(--text-muted) !important; font-size: 0.95rem !important; }}

        /* ── Hide Streamlit top black bar ── */
        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        header[data-testid="stHeader"] {{
            display: none !important;
            height: 0 !important;
            visibility: hidden !important;
        }}
        /* Reclaim the space the header occupied */
        .main .block-container {{
            padding-top: 1.5rem !important;
        }}
        ::-webkit-scrollbar {{ width: 8px; background: var(--bg-main); 
        /* ── Wave stroke overlay on body — outside sidebar clip-path ── */
        body::after {{
            content: "" !important;
            position: fixed !important;
            top: 0 !important; left: 0 !important;
            width: 21rem !important; height: 100vh !important;
            background-image: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2232%22%20height%3D%221000%22%20preserveAspectRatio%3D%22none%22%3E%3Cpolyline%20points%3D%2210%2C0%208%2C0%2010%2C25%206%2C50%2010%2C75%206%2C100%2010%2C125%206%2C150%2010%2C175%206%2C200%2010%2C225%206%2C250%2010%2C275%206%2C300%2010%2C325%206%2C350%2010%2C375%206%2C400%2010%2C425%206%2C450%2010%2C475%206%2C500%2010%2C525%206%2C550%2010%2C575%206%2C600%2010%2C625%206%2C650%2010%2C675%206%2C700%2010%2C725%206%2C750%2010%2C775%206%2C800%2010%2C825%206%2C850%2010%2C875%206%2C900%2010%2C925%206%2C950%2010%2C975%208%2C1000%22%20fill%3D%22none%22%20stroke%3D%22%23f97316%22%20stroke-width%3D%2220%22%20stroke-linejoin%3D%22round%22%20stroke-linecap%3D%22round%22/%3E%3C/svg%3E") !important;
            background-position: right center !important;
            background-size: 32px 100% !important;
            background-repeat: no-repeat !important;
            pointer-events: none !important;
            z-index: 9999 !important;
        }}
}}
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
            border-right: none !important;
            position: sticky !important;
            top: 0 !important;
            height: 100vh !important;
            overflow-y: auto !important;
            clip-path: polygon(
                0% 0%,
                98% 0%,   99% 2.5%,  97% 5%,
                99% 7.5%, 97% 10%,   99% 12.5%, 97% 15%,
                99% 17.5%,97% 20%,   99% 22.5%, 97% 25%,
                99% 27.5%,97% 30%,   99% 32.5%, 97% 35%,
                99% 37.5%,97% 40%,   99% 42.5%, 97% 45%,
                99% 47.5%,97% 50%,   99% 52.5%, 97% 55%,
                99% 57.5%,97% 60%,   99% 62.5%, 97% 65%,
                99% 67.5%,97% 70%,   99% 72.5%, 97% 75%,
                99% 77.5%,97% 80%,   99% 82.5%, 97% 85%,
                99% 87.5%,97% 90%,   99% 92.5%, 97% 95%,
                99% 97.5%,98% 100%,
                0% 100%
            ) !important;
        }}
        /* SVG wave stroke — thick orange, sits on top of the clipped sidebar */
        [data-testid="stSidebar"]::before {{
            content: "" !important;
            position: absolute !important;
            top: 0 !important; right: 0 !important;
            width: 28px !important; height: 100% !important;
            background-image: url("%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2228%22%20height%3D%221000%22%20preserveAspectRatio%3D%22none%22%3E%3Cpolyline%20points%3D%2210%2C0%208%2C0%2010%2C25%206%2C50%2010%2C75%206%2C100%2010%2C125%206%2C150%2010%2C175%206%2C200%2010%2C225%206%2C250%2010%2C275%206%2C300%2010%2C325%206%2C350%2010%2C375%206%2C400%2010%2C425%206%2C450%2010%2C475%206%2C500%2010%2C525%206%2C550%2010%2C575%206%2C600%2010%2C625%206%2C650%2010%2C675%206%2C700%2010%2C725%206%2C750%2010%2C775%206%2C800%2010%2C825%206%2C850%2010%2C875%206%2C900%2010%2C925%206%2C950%2010%2C975%208%2C1000%22%20fill%3D%22none%22%20stroke%3D%22%23ea580c%22%20stroke-width%3D%2218%22%20stroke-linejoin%3D%22round%22%20stroke-linecap%3D%22round%22%2F%3E%3C%2Fsvg%3E") !important;
            background-size: 28px 100% !important;
            background-repeat: no-repeat !important;
            pointer-events: none !important;
            z-index: 999 !important;
        }}
        /* Thick orange fill behind the wave stroke */
        [data-testid="stSidebar"]::after {{
            content: "" !important;
            position: absolute !important;
            top: 0 !important; right: 0 !important;
            width: 4px !important; height: 100% !important;
            background: #ea580c !important;
            pointer-events: none !important;
            z-index: 998 !important;
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


        /* ── Hide ALL Streamlit keyboard/accessibility hint text ── */

        /* Radio widget screen-reader hints */
        [data-testid="stSidebar"] .stRadio [data-baseweb="radio"] ~ div > div[aria-hidden="true"],
        [data-testid="stSidebar"] .stRadio > div > div > div:last-child > div:last-child,
        [data-baseweb="radio"] + div[data-testid="stMarkdownContainer"],
        div[class*="st-emotion-cache"] span[aria-hidden="true"]:empty,
        .st-emotion-cache-hidden,
        span[style*="position: absolute"][style*="overflow: hidden"],
        span[style*="clip: rect(0px"][style*="white-space: nowrap"] {{
            display: none !important;
        }}

        /* ── Sidebar & top-bar collapse button tooltip text ── */
        /* Suppress the native browser tooltip by zeroing font on text nodes
           inside the collapse buttons, while keeping the SVG arrow visible */
        [data-testid="stSidebarCollapseButton"] span:not(:has(svg)),
        [data-testid="stSidebarCollapseButton"] > div > span,
        [data-testid="collapsedControl"] span:not(:has(svg)),
        [data-testid="collapsedControl"] > div > span,
        button[kind="header"] span:not(:has(svg)),
        button[data-testid="baseButton-header"] span:not(:has(svg)) {{
            font-size: 0 !important;
            width: 0 !important;
            overflow: hidden !important;
            display: inline-block !important;
        }}

        /* Prevent native browser title= tooltip from ever showing */
        [data-testid="stSidebarCollapseButton"],
        [data-testid="collapsedControl"],
        [data-testid="stSidebarCollapseButton"] *,
        [data-testid="collapsedControl"] * {{
            pointer-events: auto !important;
        }}
        /* Zero out any injected text-based tooltips via attribute */
        [data-testid="stSidebarCollapseButton"]::after,
        [data-testid="collapsedControl"]::after {{
            display: none !important;
            content: "" !important;
        }}

        /* Alert boxes — stronger border strokes */
        .stAlert {{
            border-radius: 10px !important;
            font-size: 1rem !important;
            border-width: 2px !important;
            border-style: solid !important;
            box-shadow: 3px 3px 0px rgba(0,0,0,0.22) !important;
        }}
        div[data-testid="stAlert"][kind="error"] {{
            border-color: #b91c1c !important;
            box-shadow: 3px 3px 0px #7f1d1d !important;
        }}
        div[data-testid="stAlert"][kind="warning"] {{
            border-color: #b45309 !important;
            box-shadow: 3px 3px 0px #78350f !important;
        }}
        div[data-testid="stAlert"][kind="success"] {{
            border-color: #15803d !important;
            box-shadow: 3px 3px 0px #14532d !important;
        }}
        .stAlert p {{ font-size: 1rem !important; color: var(--text-main) !important; }}
        hr {{ border-color: var(--accent1) !important; opacity: 0.25 !important; }}
        .stCaption, small {{ color: var(--text-muted) !important; font-size: 0.95rem !important; }}

        /* ── Hide Streamlit top black bar ── */
        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        header[data-testid="stHeader"] {{
            display: none !important;
            height: 0 !important;
            visibility: hidden !important;
        }}
        /* Reclaim the space the header occupied */
        .main .block-container {{
            padding-top: 1.5rem !important;
        }}
        ::-webkit-scrollbar {{ width: 8px; background: var(--bg-main); 
        /* ── Wave stroke overlay on body — outside sidebar clip-path ── */
        body::after {{
            content: "" !important;
            position: fixed !important;
            top: 0 !important; left: 0 !important;
            width: 21rem !important; height: 100vh !important;
            background-image: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2232%22%20height%3D%221000%22%20preserveAspectRatio%3D%22none%22%3E%3Cpolyline%20points%3D%2210%2C0%208%2C0%2010%2C25%206%2C50%2010%2C75%206%2C100%2010%2C125%206%2C150%2010%2C175%206%2C200%2010%2C225%206%2C250%2010%2C275%206%2C300%2010%2C325%206%2C350%2010%2C375%206%2C400%2010%2C425%206%2C450%2010%2C475%206%2C500%2010%2C525%206%2C550%2010%2C575%206%2C600%2010%2C625%206%2C650%2010%2C675%206%2C700%2010%2C725%206%2C750%2010%2C775%206%2C800%2010%2C825%206%2C850%2010%2C875%206%2C900%2010%2C925%206%2C950%2010%2C975%208%2C1000%22%20fill%3D%22none%22%20stroke%3D%22%23ea580c%22%20stroke-width%3D%2220%22%20stroke-linejoin%3D%22round%22%20stroke-linecap%3D%22round%22/%3E%3C/svg%3E") !important;
            background-position: right center !important;
            background-size: 32px 100% !important;
            background-repeat: no-repeat !important;
            pointer-events: none !important;
            z-index: 9999 !important;
        }}
}}
        ::-webkit-scrollbar-thumb {{ background: var(--accent1); border-radius: 4px; }}
        </style>
        """

    st.markdown(css, unsafe_allow_html=True)


inject_theme()

# ── Strip native browser tooltip ("keyboard double arrow left") from
#    Streamlit's collapse buttons using JS + MutationObserver ─────────────────
st.components.v1.html("""
<script>
(function() {
    function stripTitles() {
        var selectors = [
            '[data-testid="stSidebarCollapseButton"]',
            '[data-testid="collapsedControl"]',
            'button[kind="header"]',
            'button[data-testid="baseButton-header"]',
            '[data-testid="stSidebarCollapseButton"] button',
            '[data-testid="collapsedControl"] button'
        ];
        selectors.forEach(function(sel) {
            document.querySelectorAll(sel).forEach(function(el) {
                el.removeAttribute('title');
                el.removeAttribute('aria-label');
                el.setAttribute('title', '');
                // Walk all descendants too
                el.querySelectorAll('[title], [aria-label]').forEach(function(child) {
                    child.removeAttribute('title');
                    child.setAttribute('title', '');
                });
            });
        });
    }

    // Run immediately and after a short delay (Streamlit renders async)
    stripTitles();
    setTimeout(stripTitles, 500);
    setTimeout(stripTitles, 1500);

    // MutationObserver: re-strip whenever DOM changes (Streamlit re-renders)
    var observer = new MutationObserver(function() { stripTitles(); });
    observer.observe(document.body, { childList: true, subtree: true, attributes: true, attributeFilter: ['title', 'aria-label'] });
})();
</script>
""", height=0)

# ─────────────────────────────────────────────────────────────────────────────
# Audio helpers — load local MP3s from sounds/ folder as base64
# ─────────────────────────────────────────────────────────────────────────────
import base64 as _b64, os as _os, pathlib as _pl

def _audio_b64(filename: str) -> str:
    """Return base64-encoded data URI for a file in the sounds/ folder, or '' if missing."""
    path = _pl.Path(__file__).parent / "sounds" / filename
    if not path.exists():
        return ""
    return _b64.b64encode(path.read_bytes()).decode()

KAZOO_FILE  = "Kazoo_freesound_community-075667_two-kazoo-fanfarewav-83382.mp3"
BOING_FILE  = "u_wb4wgxdwxo-boing2-418548.mp3"

def play_sound(filename: str) -> None:
    """Play a local MP3 via st.audio() with autoplay=True.
    Counter key ensures a new widget on every call so audio always replays."""
    path = _pl.Path(__file__).parent / "sounds" / filename
    if not path.exists():
        return
    counter_key = f"_snd_{filename}"
    count = st.session_state.get(counter_key, 0) + 1
    st.session_state[counter_key] = count
    audio_bytes = path.read_bytes()
    st.audio(audio_bytes, format="audio/mp3", autoplay=True)

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

# ── Boing on every page switch ────────────────────────────────────────────────
if "current_page" not in st.session_state:
    st.session_state.current_page = page
elif st.session_state.current_page != page:
    st.session_state.current_page = page
    play_sound(BOING_FILE)

st.sidebar.divider()
summary = analyzer.get_copyright_summary()
st.sidebar.metric("In library", summary["total"])
st.sidebar.metric("Public domain", summary["public_domain"])
st.sidebar.metric("Protected", summary["protected"])

# ── Play boing once on first app load (after sidebar is fully rendered) ───────
if "boing_played" not in st.session_state:
    st.session_state.boing_played = True
    play_sound(BOING_FILE)

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: Search
# ─────────────────────────────────────────────────────────────────────────────
if page == "🔍 Search":
    dark = st.session_state.dark_mode

    # ── Speech-bubble hero header ──────────────────────────────────────────
    bubble_bg     = "#1e1435"      if dark else "#ffffff"
    bubble_border = "#f97316"      if dark else "#ea580c"
    bubble_title  = "#fef3c7"      if dark else "#1c1917"
    bubble_shadow = "#f97316"      if dark else "#c2410c"
    bubble_tail_l = "#1e1435"      if dark else "#ffffff"  # left tail fill
    input_bg      = "#13121f"      if dark else "#fff7ed"
    input_text    = "#fef3c7"      if dark else "#1c1917"
    input_border  = "#f97316"      if dark else "#ea580c"
    lens_c        = "#f97316"      if dark else "#ea580c"
    page_bg       = "#0f0e17"      if dark else "#fff7ed"

    st.markdown(f"""
    <style>
    /* Fade the doodle background while on search page */
    [data-testid="stAppViewContainer"]::before {{
        opacity: 0.22 !important;
    }}

    /* Speech bubble container */
    .search-bubble-wrap {{
        display: flex;
        justify-content: center;
        margin: 18px 0 32px 0;
    }}
    .search-bubble {{
        position: relative;
        background: {bubble_bg};
        border: 3px solid {bubble_border};
        border-radius: 28px;
        padding: 28px 36px 22px 36px;
        max-width: 360px;
        width: auto;
        box-shadow: 6px 6px 0px {bubble_shadow};
    }}
    /* Tail pointing down-left */
    .search-bubble::after {{
        content: "";
        position: absolute;
        bottom: -28px;
        left: 60px;
        width: 0;
        height: 0;
        border-left: 18px solid transparent;
        border-right: 10px solid transparent;
        border-top: 28px solid {bubble_border};
    }}
    .search-bubble::before {{
        content: "";
        position: absolute;
        bottom: -22px;
        left: 63px;
        width: 0;
        height: 0;
        border-left: 15px solid transparent;
        border-right: 8px solid transparent;
        border-top: 24px solid {bubble_bg};
        z-index: 1;
    }}
    /* Title inside bubble */
    .bubble-title {{
        font-family: 'Bangers', Impact, cursive;
        font-size: 2.2rem;
        letter-spacing: 3px;
        color: {bubble_title};
        text-shadow: 3px 3px 0px {bubble_shadow}55;
        margin: 0 0 16px 0;
        display: flex;
        align-items: center;
        gap: 10px;
    }}
    /* Magnifying glass SVG icon style */
    .bubble-title .lens-wrap {{
        display: inline-flex;
        align-items: center;
    }}
    /* Custom styled search input inside bubble */
    .bubble-input-wrap {{
        display: flex;
        align-items: center;
        gap: 10px;
        background: {input_bg};
        border: 2px solid {input_border};
        border-radius: 50px;
        padding: 8px 16px;
        box-shadow: inset 0 2px 6px rgba(0,0,0,0.2);
    }}
    .bubble-dots {{
        display: flex;
        gap: 5px;
        margin-top: 12px;
        justify-content: flex-end;
    }}
    .bubble-dot {{
        width: 8px; height: 8px;
        border-radius: 50%;
        background: {bubble_border};
        opacity: 0.4;
    }}
    .bubble-dot:last-child {{ opacity: 0.2; width:6px; height:6px; margin-top:1px; }}
    </style>

    <div class="search-bubble-wrap">
      <div class="search-bubble">
        <div class="bubble-title">
          <!-- Cartoony magnifying glass: chunky handle, thick lens ring,
               big shine blob, small stars scattered around it -->
          <svg width="54" height="54" viewBox="0 0 54 54" xmlns="http://www.w3.org/2000/svg"
               style="flex-shrink:0;">
            <!-- Outer glow ring -->
            <circle cx="21" cy="21" r="17" fill="{lens_c}" opacity="0.18"/>
            <!-- Lens fill -->
            <circle cx="21" cy="21" r="14" fill="{bubble_bg}"/>
            <!-- Lens border — thick, slightly wobbly feel via large stroke -->
            <circle cx="21" cy="21" r="14" fill="none" stroke="{lens_c}" stroke-width="4"/>
            <!-- Inner tint so glass looks like glass -->
            <circle cx="21" cy="21" r="12" fill="{lens_c}" opacity="0.08"/>
            <!-- Big cartoon shine blob — top-left -->
            <ellipse cx="15" cy="14" rx="5" ry="3.5"
                     fill="white" opacity="0.55" transform="rotate(-30 15 14)"/>
            <!-- Small secondary shine dot -->
            <circle cx="25" cy="12" r="2" fill="white" opacity="0.35"/>
            <!-- Chunky handle — thick rounded line with end cap -->
            <line x1="31" y1="31" x2="46" y2="46"
                  stroke="{lens_c}" stroke-width="7" stroke-linecap="round"/>
            <!-- Handle inner highlight -->
            <line x1="31" y1="31" x2="44" y2="44"
                  stroke="white" stroke-width="2" stroke-linecap="round" opacity="0.25"/>
            <!-- Tiny star sparkles around the lens -->
            <polygon points="6,8 7,5 8,8 11,8 9,10 10,13 7,11 4,13 5,10 3,8"
                     fill="{lens_c}" opacity="0.7"/>
            <circle cx="36" cy="10" r="2" fill="{lens_c}" opacity="0.5"/>
            <circle cx="40" cy="18" r="1.5" fill="{lens_c}" opacity="0.4"/>
            <!-- Motion lines on handle (cartoon speed lines) -->
            <line x1="38" y1="40" x2="42" y2="36"
                  stroke="{lens_c}" stroke-width="2" stroke-linecap="round" opacity="0.35"/>
            <line x1="41" y1="43" x2="45" y2="39"
                  stroke="{lens_c}" stroke-width="1.5" stroke-linecap="round" opacity="0.25"/>
          </svg>
          SEARCH CARTOONPAL
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Actual Streamlit input (cannot style natively to match bubble,
    # but sits visually below the bubble tail)
    query = st.text_input(
        "",
        placeholder="🔍  Type a cartoon name… e.g. Bugs Bunny, Betty Boop, Felix",
        label_visibility="collapsed"
    )

    if query:
        result = lib.find(query)
        if result:
            # ── Kazoo fanfare from real MP3 file ──────────────────────────
            play_sound(KAZOO_FILE)

            # ── Suppress doodle bg on results ─────────────────────────────
            card_bg  = "#1e1b2e" if dark else "#ffffff"
            card_bdr = "#f97316" if dark else "#ea580c"
            st.markdown(f"""
            <style>
            [data-testid="stAppViewContainer"]::before {{
                opacity: 0.10 !important;
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
    st.markdown("""
    <style id="pg-bg">
    [data-testid="stAppViewContainer"]::before { opacity: 0.12 !important; }
    [data-testid="stAppViewContainer"] { background-attachment: fixed !important; }
    </style>
    """, unsafe_allow_html=True)
    _dark = st.session_state.dark_mode
    st.markdown(page_header_html(
        icon     = "📚",
        title    = "BROWSE ALL CARTOONS",
        subtitle = "EVERY CHARACTER IN THE LIBRARY",
        bg       = "#1e1b2e" if _dark else "#ffffff",
        border   = "#f97316" if _dark else "#ea580c",
        icon_bg  = "#f97316" if _dark else "#ea580c",
        title_c  = "#fef3c7" if _dark else "#1c1917",
        sub_c    = "#fb923c" if _dark else "#9a3412",
        shadow   = "#f97316" if _dark else "#c2410c",
    ), unsafe_allow_html=True)

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
    st.markdown("""
    <style id="pg-bg">
    [data-testid="stAppViewContainer"]::before { opacity: 0.12 !important; }
    [data-testid="stAppViewContainer"] { background-attachment: fixed !important; }
    </style>
    """, unsafe_allow_html=True)
    _dark = st.session_state.dark_mode
    st.markdown(page_header_html(
        icon     = "⚖️",
        title    = "COPYRIGHT DASHBOARD",
        subtitle = "OWNERSHIP STATUS & PUBLIC DOMAIN TRACKER",
        bg       = "#1e1b2e" if _dark else "#ffffff",
        border   = "#f97316" if _dark else "#ea580c",
        icon_bg  = "#fef9c3" if _dark else "#fef9c3",
        title_c  = "#fef3c7" if _dark else "#1c1917",
        sub_c    = "#fb923c" if _dark else "#9a3412",
        shadow   = "#f97316" if _dark else "#c2410c",
    ), unsafe_allow_html=True)

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
    st.markdown("""
    <style id="pg-bg">
    [data-testid="stAppViewContainer"]::before { opacity: 0.12 !important; }
    [data-testid="stAppViewContainer"] { background-attachment: fixed !important; }
    </style>
    """, unsafe_allow_html=True)
    _dark = st.session_state.dark_mode
    st.markdown(page_header_html(
        icon     = "➕",
        title    = "ADD A CARTOON",
        subtitle = "REGISTER A NEW CHARACTER TO THE LIBRARY",
        bg       = "#1e1b2e" if _dark else "#ffffff",
        border   = "#34d399" if _dark else "#16a34a",
        icon_bg  = "#34d399" if _dark else "#16a34a",
        title_c  = "#fef3c7" if _dark else "#1c1917",
        sub_c    = "#6ee7b7" if _dark else "#14532d",
        shadow   = "#34d399" if _dark else "#15803d",
    ), unsafe_allow_html=True)
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