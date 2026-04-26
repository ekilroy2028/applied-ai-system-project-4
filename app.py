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
# SVG LOGO — compact, text fits inside the box
# ─────────────────────────────────────────────────────────────────────────────
def sidebar_logo(dark: bool) -> str:
    if dark:
        bg      = "#12122a"
        border  = "#f97316"   # orange
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

    # viewBox is 200×72 — generous horizontal room, compact height
    return f"""
<div style="padding:6px 2px 2px 2px;">
<svg viewBox="0 0 200 72" xmlns="http://www.w3.org/2000/svg"
     style="width:100%;display:block;">
  <!-- Rounded pill background -->
  <rect x="2" y="2" width="196" height="68" rx="14"
        fill="{bg}" stroke="{border}" stroke-width="2.5"/>

  <!-- Sprocket holes — left strip -->
  <rect x="7"  y="10" width="6" height="8" rx="1.5" fill="{border}" opacity="0.6"/>
  <rect x="7"  y="26" width="6" height="8" rx="1.5" fill="{border}" opacity="0.6"/>
  <rect x="7"  y="42" width="6" height="8" rx="1.5" fill="{border}" opacity="0.6"/>
  <rect x="7"  y="58" width="6" height="8" rx="1.5" fill="{border}" opacity="0.6"/>

  <!-- Sprocket holes — right strip -->
  <rect x="187" y="10" width="6" height="8" rx="1.5" fill="{border}" opacity="0.6"/>
  <rect x="187" y="26" width="6" height="8" rx="1.5" fill="{border}" opacity="0.6"/>
  <rect x="187" y="42" width="6" height="8" rx="1.5" fill="{border}" opacity="0.6"/>
  <rect x="187" y="58" width="6" height="8" rx="1.5" fill="{border}" opacity="0.6"/>

  <!-- Clapperboard icon (left of text) -->
  <rect x="18" y="18" width="24" height="20" rx="2.5"
        fill="{clap_b}" stroke="{border}" stroke-width="1.2"/>
  <!-- clapper top bar -->
  <rect x="18" y="18" width="24" height="6" rx="2" fill="{clap_t}"/>
  <!-- diagonal stripes on top bar -->
  <line x1="21" y1="18" x2="19" y2="24" stroke="{stripe}" stroke-width="1.8"/>
  <line x1="26" y1="18" x2="24" y2="24" stroke="{stripe}" stroke-width="1.8"/>
  <line x1="31" y1="18" x2="29" y2="24" stroke="{stripe}" stroke-width="1.8"/>
  <line x1="36" y1="18" x2="34" y2="24" stroke="{stripe}" stroke-width="1.8"/>
  <!-- play triangle -->
  <polygon points="24,28 24,34 31,31" fill="{star}"/>

  <!-- Star accent -->
  <polygon points="48,14 50,9 52,14 57,14 53,17 55,22 50,19 45,22 47,17 43,14"
           fill="{star}" stroke="{border}" stroke-width="0.8"/>

  <!-- CARTOONPAL — scaled to fit horizontally -->
  <text x="62" y="36"
        font-family="Bangers, Impact, cursive"
        font-size="22"
        letter-spacing="1.5"
        fill="{text_c}"
        stroke="{border}" stroke-width="0.8"
        paint-order="stroke fill">CARTOONPAL</text>

  <!-- Subtitle line -->
  <text x="62" y="52"
        font-family="Nunito, Arial, sans-serif"
        font-size="8.5"
        font-weight="700"
        letter-spacing="0.3"
        fill="{sub_c}">Copyright &amp; Visual History</text>
</svg>
</div>
"""

# ─────────────────────────────────────────────────────────────────────────────
# Background tile — cartoon doodles each rotated differently
# ─────────────────────────────────────────────────────────────────────────────
def cartoon_bg_svg(dark: bool) -> str:
    import base64

    if dark:
        # semi-transparent on dark bg
        c_star   = "rgba(251,191,36,0.30)"   # amber
        c_bubble = "rgba(56,189,248,0.28)"   # sky blue
        c_bolt   = "rgba(249,115,22,0.30)"   # orange
        c_film   = "rgba(167,139,250,0.28)"  # violet
        c_wave   = "rgba(52,211,153,0.30)"   # emerald
        sk       = "rgba(255,255,255,0.22)"
        pl       = "rgba(255,255,255,0.55)"
    else:
        # more vivid on light/cream bg
        c_star   = "rgba(245,158,11,0.35)"   # amber
        c_bubble = "rgba(14,165,233,0.32)"   # sky blue
        c_bolt   = "rgba(234,88,12,0.32)"    # orange
        c_film   = "rgba(139,92,246,0.30)"   # violet
        c_wave   = "rgba(16,185,129,0.34)"   # emerald
        sk       = "rgba(0,0,0,0.18)"
        pl       = "rgba(0,0,0,0.50)"

    # 200×200 tile; each icon gets a rotate() transform so they scatter naturally
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200">

  <!-- ★ Star — top-left, tilted 15° -->
  <g transform="translate(32,28) rotate(15,0,0)">
    <polygon points="0,-18 4,-7 16,-7 7,0 10,11 0,4 -10,11 -7,0 -16,-7 -4,-7"
             fill="{c_star}" stroke="{sk}" stroke-width="1.4"/>
  </g>

  <!-- 💬 Speech bubble — top-right, tilted -20° -->
  <g transform="translate(148,34) rotate(-20,0,0)">
    <rect x="-22" y="-18" width="44" height="28" rx="8"
          fill="{c_bubble}" stroke="{sk}" stroke-width="1.3"/>
    <polygon points="-10,10 -16,22 2,10" fill="{c_bubble}" stroke="{sk}" stroke-width="1"/>
    <circle cx="-10" cy="-4" r="3.5" fill="{sk}"/>
    <circle cx="0"   cy="-4" r="3.5" fill="{sk}"/>
    <circle cx="10"  cy="-4" r="3.5" fill="{sk}"/>
  </g>

  <!-- ⚡ Lightning bolt — middle-left, tilted 10° -->
  <g transform="translate(28,110) rotate(10,0,0)">
    <polygon points="8,-22 -4,4 4,4 -6,22 14,0 6,0 18,-22"
             fill="{c_bolt}" stroke="{sk}" stroke-width="1.3"/>
  </g>

  <!-- 🎬 Film frame — middle-right, tilted -12° -->
  <g transform="translate(158,105) rotate(-12,0,0)">
    <rect x="-22" y="-18" width="44" height="36" rx="3.5"
          fill="{c_film}" stroke="{sk}" stroke-width="1.3"/>
    <rect x="-22" y="-18" width="44" height="8" rx="2.5" fill="{sk}" opacity="0.35"/>
    <line x1="-17" y1="-18" x2="-19" y2="-10" stroke="white" stroke-width="1.5" opacity="0.5"/>
    <line x1="-10" y1="-18" x2="-12" y2="-10" stroke="white" stroke-width="1.5" opacity="0.5"/>
    <line x1="-3"  y1="-18" x2="-5"  y2="-10" stroke="white" stroke-width="1.5" opacity="0.5"/>
    <line x1="4"   y1="-18" x2="2"   y2="-10" stroke="white" stroke-width="1.5" opacity="0.5"/>
    <line x1="11"  y1="-18" x2="9"   y2="-10" stroke="white" stroke-width="1.5" opacity="0.5"/>
    <line x1="18"  y1="-18" x2="16"  y2="-10" stroke="white" stroke-width="1.5" opacity="0.5"/>
    <polygon points="-10,0 -10,14 6,7" fill="{pl}"/>
  </g>

  <!-- ~ Squiggle wave — bottom, tilted -8° -->
  <g transform="translate(100,168) rotate(-8,0,0)">
    <path d="M-50,-6 Q-38,-18 -26,-6 Q-14,6 -2,-6 Q10,-18 22,-6 Q34,6 46,-6 Q58,-18 70,-6"
          fill="none" stroke="{c_wave}" stroke-width="3.5" stroke-linecap="round"/>
    <path d="M-50,8 Q-38,-4 -26,8 Q-14,20 -2,8 Q10,-4 22,8 Q34,20 46,8 Q58,-4 70,8"
          fill="none" stroke="{c_wave}" stroke-width="3.5" stroke-linecap="round"/>
  </g>

  <!-- ✦ 4-point sparkle — bottom-left, tilted 25° -->
  <g transform="translate(38,164) rotate(25,0,0)">
    <polygon points="0,-14 3,-5 12,-5 5,1 8,10 0,5 -8,10 -5,1 -12,-5 -3,-5"
             fill="{c_star}" stroke="{sk}" stroke-width="1"/>
  </g>

  <!-- small accent dots scattered -->
  <circle cx="88"  cy="52"  r="4" fill="{c_bubble}" opacity="0.6"/>
  <circle cx="168" cy="168" r="3" fill="{c_bolt}"   opacity="0.6"/>
  <circle cx="60"  cy="80"  r="3" fill="{c_film}"   opacity="0.55"/>
  <circle cx="140" cy="148" r="4" fill="{c_star}"   opacity="0.6"/>
</svg>"""

    encoded = base64.b64encode(svg.encode()).decode()
    return f"data:image/svg+xml;base64,{encoded}"


# ─────────────────────────────────────────────────────────────────────────────
# Theme injection
# ─────────────────────────────────────────────────────────────────────────────
def inject_theme():
    dark = st.session_state.dark_mode
    bg_tile = cartoon_bg_svg(dark)

    if dark:
        # Dark mode: warm orange/amber cartoon palette — readable on dark navy
        css = f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Bangers&family=Nunito:wght@400;600;700;800&display=swap');

        :root {{
            --bg-main:      #0f0e17;
            --bg-card:      #1e1b2e;
            --bg-sidebar:   #13121f;
            --accent1:      #f97316;   /* orange — headings */
            --accent2:      #38bdf8;   /* sky blue */
            --accent3:      #fbbf24;   /* amber */
            --accent5:      #34d399;   /* emerald */
            --text-main:    #fef3c7;   /* warm cream — excellent contrast on dark */
            --text-body:    #e8d5b7;   /* slightly warmer for paragraphs */
            --text-muted:   #a78bfa;   /* violet muted */
            --heading-font: 'Bangers', cursive;
            --body-font:    'Nunito', sans-serif;
        }}

        html, body, [data-testid="stAppViewContainer"] {{
            background-color: var(--bg-main) !important;
            font-family: var(--body-font) !important;
            color: var(--text-main) !important;
            font-size: 17px !important;
        }}

        /* General paragraph / markdown text */
        p, li, .stMarkdown p, [data-testid="stMarkdownContainer"] p {{
            color: var(--text-body) !important;
            font-size: 1.05rem !important;
            line-height: 1.7 !important;
        }}

        /* Cartoon doodle background tile */
        [data-testid="stAppViewContainer"]::before {{
            content: "";
            position: fixed;
            inset: 0;
            background-image: url('{bg_tile}');
            background-size: 200px 200px;
            background-repeat: repeat;
            pointer-events: none;
            z-index: 0;
            opacity: 0.80;
        }}

        [data-testid="stSidebar"] {{
            background: var(--bg-sidebar) !important;
            border-right: 3px solid var(--accent1) !important;
        }}
        [data-testid="stSidebar"] * {{
            color: var(--text-main) !important;
            font-family: var(--body-font) !important;
        }}

        .main .block-container {{ position: relative; z-index: 1; }}

        /* Headings — orange with sky-blue shadow */
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

        /* Metric boxes */
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

        /* Buttons */
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

        /* Inputs */
        .stTextInput input, .stTextArea textarea, .stNumberInput input {{
            background: var(--bg-card) !important;
            border: 2px solid var(--accent1) !important;
            border-radius: 8px !important;
            color: var(--text-main) !important;
            font-family: var(--body-font) !important;
            font-size: 1rem !important;
        }}
        .stTextInput label, .stTextArea label, .stNumberInput label,
        .stSelectbox label, .stCheckbox label {{
            color: var(--text-main) !important;
            font-size: 1rem !important;
            font-weight: 700 !important;
        }}

        .stSelectbox [data-baseweb="select"] {{
            background: var(--bg-card) !important;
            border: 2px solid var(--accent2) !important;
            border-radius: 8px !important;
            color: var(--text-main) !important;
        }}

        /* Expanders */
        details {{
            background: var(--bg-card) !important;
            border: 2px solid var(--accent1) !important;
            border-radius: 10px !important;
            margin-bottom: 8px !important;
        }}
        summary {{
            color: var(--accent3) !important;
            font-weight: 800 !important;
            font-size: 1.05rem !important;
        }}

        /* Tabs */
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

        /* Alert boxes */
        .stAlert {{ border-radius: 10px !important; font-size: 1rem !important; }}
        .stAlert p {{ font-size: 1rem !important; color: inherit !important; }}

        hr {{ border-color: var(--accent1) !important; opacity: 0.35 !important; }}

        /* Sidebar nav */
        [data-testid="stSidebar"] .stRadio label {{
            font-size: 1.1rem !important;
            font-weight: 700 !important;
        }}
        [data-testid="stSidebar"] .stCaption,
        [data-testid="stSidebar"] small {{
            color: var(--text-muted) !important;
            font-size: 0.92rem !important;
        }}

        /* Caption / small text */
        .stCaption, small {{
            color: var(--text-muted) !important;
            font-size: 0.95rem !important;
        }}

        ::-webkit-scrollbar {{ width: 8px; background: var(--bg-main); }}
        ::-webkit-scrollbar-thumb {{ background: var(--accent1); border-radius: 4px; }}
        </style>
        """
    else:
        # Light mode: deep navy text on warm cream — cartoon orange/teal palette
        css = f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Bangers&family=Nunito:wght@400;600;700;800&display=swap');

        :root {{
            --bg-main:      #fff7ed;   /* warm cream */
            --bg-card:      #ffffff;
            --accent1:      #ea580c;   /* burnt orange — headings */
            --accent2:      #0891b2;   /* teal */
            --accent3:      #d97706;   /* amber */
            --accent5:      #16a34a;   /* green */
            --text-main:    #1c1917;   /* near-black — maximum readability */
            --text-body:    #292524;   /* dark brown-black for paragraphs */
            --text-muted:   #57534e;   /* warm gray */
            --heading-font: 'Bangers', cursive;
            --body-font:    'Nunito', sans-serif;
        }}

        html, body, [data-testid="stAppViewContainer"] {{
            font-family: var(--body-font) !important;
            color: var(--text-main) !important;
            font-size: 17px !important;
        }}

        /* General paragraph / markdown text */
        p, li, .stMarkdown p, [data-testid="stMarkdownContainer"] p {{
            color: var(--text-body) !important;
            font-size: 1.05rem !important;
            line-height: 1.7 !important;
        }}

        /* Warm cream + colour-burst gradient base */
        [data-testid="stAppViewContainer"] {{
            background:
                radial-gradient(ellipse at 5%  10%, rgba(234,88,12,0.14)  0%, transparent 40%),
                radial-gradient(ellipse at 90%  8%, rgba(8,145,178,0.13)  0%, transparent 38%),
                radial-gradient(ellipse at 80% 85%, rgba(217,119,6,0.14)  0%, transparent 42%),
                radial-gradient(ellipse at 15% 90%, rgba(22,163,74,0.12)  0%, transparent 38%),
                radial-gradient(ellipse at 50% 50%, rgba(139,92,246,0.08) 0%, transparent 52%),
                #fff7ed !important;
        }}

        /* Cartoon doodle background tile */
        [data-testid="stAppViewContainer"]::before {{
            content: "";
            position: fixed;
            inset: 0;
            background-image: url('{bg_tile}');
            background-size: 200px 200px;
            background-repeat: repeat;
            pointer-events: none;
            z-index: 0;
            opacity: 0.88;
        }}

        [data-testid="stSidebar"] {{
            background: linear-gradient(155deg, #fff7ed 0%, #ecfeff 55%, #fefce8 100%) !important;
            border-right: 4px solid var(--accent1) !important;
        }}
        [data-testid="stSidebar"] * {{
            color: var(--text-main) !important;
            font-family: var(--body-font) !important;
        }}

        .main .block-container {{ position: relative; z-index: 1; }}

        /* Headings — orange with teal shadow */
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

        /* Metric boxes */
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

        /* Buttons */
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

        /* Inputs */
        .stTextInput input, .stTextArea textarea, .stNumberInput input {{
            background: var(--bg-card) !important;
            border: 2px solid var(--accent1) !important;
            border-radius: 8px !important;
            color: var(--text-main) !important;
            font-family: var(--body-font) !important;
            font-size: 1rem !important;
        }}
        .stTextInput label, .stTextArea label, .stNumberInput label,
        .stSelectbox label, .stCheckbox label {{
            color: var(--text-main) !important;
            font-size: 1rem !important;
            font-weight: 700 !important;
        }}

        .stSelectbox [data-baseweb="select"] {{
            background: var(--bg-card) !important;
            border: 2px solid var(--accent2) !important;
            border-radius: 8px !important;
            color: var(--text-main) !important;
        }}

        /* Expanders */
        details {{
            background: var(--bg-card) !important;
            border: 2px solid var(--accent1) !important;
            border-radius: 12px !important;
            margin-bottom: 8px !important;
        }}
        summary {{
            color: var(--accent1) !important;
            font-weight: 800 !important;
            font-size: 1.05rem !important;
        }}

        /* Tabs */
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

        /* Alert boxes */
        .stAlert {{ border-radius: 10px !important; font-size: 1rem !important; }}
        .stAlert p {{ font-size: 1rem !important; color: var(--text-main) !important; }}

        hr {{ border-color: var(--accent1) !important; opacity: 0.25 !important; }}

        /* Sidebar nav */
        [data-testid="stSidebar"] .stRadio label {{
            font-size: 1.1rem !important;
            font-weight: 700 !important;
            color: var(--text-main) !important;
        }}
        [data-testid="stSidebar"] .stCaption,
        [data-testid="stSidebar"] small {{
            color: var(--text-muted) !important;
            font-size: 0.92rem !important;
        }}

        /* Caption / small text */
        .stCaption, small {{
            color: var(--text-muted) !important;
            font-size: 0.95rem !important;
        }}

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
        studio_name   = st.text_input("Studio name")
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