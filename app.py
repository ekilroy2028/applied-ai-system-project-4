"""
app.py
CartoonPal — Streamlit UI.
Run with:  streamlit run app.py
"""

import streamlit as st
from datetime import datetime
import anthropic
import logging
from ai_analysis import analyze_copyright_with_ai
from agentic_workflow import run_copyright_agent
from few_shot_analysis import run_few_shot_analysis
import anthropic
import logging
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


# ─────────────────────────────────────────────────────────────────────────────
# THEME — applied via session_state toggle BEFORE rendering anything else
# ─────────────────────────────────────────────────────────────────────────────
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# CSS variables swap based on mode
if st.session_state.dark_mode:
    BG        = "#050014"
    CARD      = "#12003A"
    BORDER    = "#FF6B00"
    TEXT      = "#FFFFFF"
    SUBTEXT   = "#CC99FF"
    SIDEBAR_BG = "#02000A"
    INPUT_BG  = "#1A0050"
else:
    BG        = "#FFF700"
    CARD      = "#FFFFFF"
    BORDER    = "#FF0080"
    TEXT      = "#1B0060"
    SUBTEXT   = "#5500AA"
    SIDEBAR_BG = "#FF0080"
    INPUT_BG  = "#FFFFFF"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bangers&family=Fredoka+One&family=Nunito:wght@400;600;700;800;900&display=swap');

html, body, [class*="css"] {{
    font-family: 'Fredoka One', 'Nunito', sans-serif !important;
    background-color: {BG} !important;
    color: {TEXT} !important;
}}

/* ── APP BACKGROUND ── */
.stApp, [data-testid="stAppViewContainer"] {{
    background-color: {BG} !important;
}}
[data-testid="stMain"] {{
    background-color: {BG} !important;
}}

/* ── SIDEBAR ── */
section[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, {SIDEBAR_BG} 0%, #AA0060 100%) !important;
    border-right: 4px solid #F4A261;
}}
section[data-testid="stSidebar"] * {{
    color: #FFFDF7 !important;
}}

/* ── ANIMATED RAINBOW HEADER BANNER ── */
.cp-header {{
    background: linear-gradient(135deg, #FF0000 0%, #FF6B00 20%, #FFD700 40%, #00FF88 60%, #0099FF 80%, #CC00FF 100%);
    background-size: 300% 300%;
    animation: gradientShift 6s ease infinite;
    border-radius: 22px;
    padding: 30px 40px;
    margin-bottom: 28px;
    box-shadow: 0 8px 32px rgba(230,57,70,0.3), 6px 6px 0px rgba(0,0,0,0.15);
    border: 4px solid rgba(255,255,255,0.3);
    position: relative;
    overflow: hidden;
}}
@keyframes gradientShift {{
    0%   {{ background-position: 0% 50%; }}
    50%  {{ background-position: 100% 50%; }}
    100% {{ background-position: 0% 50%; }}
}}
/* watermarks handled per-page with SVG */
.cp-header h1 {{
    color: #ffffff !important;
    font-family: 'Bangers', cursive !important;
    font-size: 3rem !important;
    font-weight: 400 !important;
    text-shadow: 4px 4px 0px rgba(0,0,0,0.25), -1px -1px 0px rgba(0,0,0,0.1);
    margin: 0 !important;
    letter-spacing: 2px;
}}
.cp-header p {{
    color: rgba(255,255,255,0.95) !important;
    font-size: 1.05rem !important;
    margin: 8px 0 0 0 !important;
    font-weight: 700;
    text-shadow: 1px 1px 0px rgba(0,0,0,0.2);
}}

/* ── PER-PAGE HEADER VARIANTS ── */

/* Browse All — pencil ruled lines pattern */
.cp-header-browse {{
    background: linear-gradient(135deg, #FF0000 0%, #FF6B00 20%, #FFD700 40%, #00FF88 60%, #0099FF 80%, #CC00FF 100%) !important;
    background-size: 300% 300% !important;
}}
.cp-header-browse::after {{
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image:
        repeating-linear-gradient(
            0deg,
            transparent,
            transparent 28px,
            rgba(255,255,255,0.12) 28px,
            rgba(255,255,255,0.12) 30px
        ),
        linear-gradient(90deg, rgba(255,255,255,0.15) 2px, transparent 2px);
    background-size: 100% 30px, 60px 100%;
    border-radius: 22px;
    pointer-events: none;
}}

/* Copyright Dashboard — halftone dot grid pattern */
.cp-header-dash {{
    background: linear-gradient(135deg, #7B2D8B 0%, #E63946 40%, #FF6B00 100%) !important;
    background-size: 300% 300% !important;
}}
.cp-header-dash::after {{
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: radial-gradient(circle, rgba(255,255,255,0.18) 2px, transparent 2px);
    background-size: 20px 20px;
    border-radius: 22px;
    pointer-events: none;
}}

/* Add a Cartoon — diagonal stripe pattern like comic book coloring */
.cp-header-add {{
    background: linear-gradient(135deg, #06D6A0 0%, #118AB2 40%, #073B4C 100%) !important;
    background-size: 300% 300% !important;
}}
.cp-header-add::after {{
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: repeating-linear-gradient(
        45deg,
        transparent,
        transparent 12px,
        rgba(255,255,255,0.1) 12px,
        rgba(255,255,255,0.1) 14px
    );
    border-radius: 22px;
    pointer-events: none;
}}

/* ── CARTOONPAL SIDEBAR LOGO ── */
.cp-logo-wrap {{
    text-align: center;
    padding: 20px 12px 10px 12px;
}}
/* Cartoon badge — speech bubble shape */
.cp-logo-badge {{
    display: inline-block;
    background: linear-gradient(135deg, #FFD700, #FF6B00);
    border: 4px solid #7B00FF;
    border-radius: 50%;
    width: 72px;
    height: 72px;
    line-height: 72px;
    text-align: center;
    box-shadow: 4px 4px 0px #7B00FF, 0 0 20px rgba(123,0,255,0.4);
    position: relative;
    margin-bottom: 8px;
    animation: logoPulse 3s ease-in-out infinite;
}}
@keyframes logoPulse {{
    0%, 100% {{ box-shadow: 4px 4px 0px #7B00FF, 0 0 20px rgba(123,0,255,0.4); }}
    50% {{ box-shadow: 4px 4px 0px #7B00FF, 0 0 35px rgba(123,0,255,0.7); }}
}}
/* Tail of speech bubble */
.cp-logo-badge::after {{
    content: "";
    position: absolute;
    bottom: -14px;
    left: 50%;
    transform: translateX(-50%);
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
    border-top: 14px solid #7B00FF;
}}
.cp-logo-pencil {{
    font-size: 1.6rem;
    display: inline-block;
    transform: rotate(-20deg);
    position: relative;
    top: -4px;
}}
.cp-logo-brush {{
    font-size: 1.6rem;
    display: inline-block;
    transform: rotate(20deg);
    position: relative;
    top: -4px;
}}
.cp-logo-star-icon {{
    font-size: 1rem;
    position: absolute;
    top: 4px;
    right: 4px;
}}
.cp-logo-text {{
    font-family: 'Bangers', cursive !important;
    font-size: 2.2rem;
    color: #FFD700;
    letter-spacing: 3px;
    text-shadow: 3px 3px 0px #7B00FF, -1px -1px 0px rgba(0,0,0,0.4);
    display: block;
    line-height: 1;
    margin-top: 14px;
}}
.cp-logo-sub {{
    font-size: 0.68rem;
    color: #AAAACC;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 5px;
    display: block;
}}
.cp-logo-stars {{
    font-size: 0.9rem;
    color: #FFD700;
    display: block;
    margin-top: 4px;
    letter-spacing: 6px;
}}

/* ── CARTOON CARDS ── */
.stExpander, [data-testid="stExpander"] {{
    background: {CARD} !important;
    border: 3px solid {BORDER} !important;
    border-radius: 18px !important;
    box-shadow: 5px 5px 0px {BORDER} !important;
}}

/* ── METRICS ── */
[data-testid="metric-container"] {{
    background: {CARD} !important;
    border: 3px solid {BORDER} !important;
    border-radius: 16px !important;
    padding: 16px !important;
    box-shadow: 4px 4px 0px {BORDER} !important;
}}
[data-testid="stMetricValue"] {{
    color: #E63946 !important;
    font-family: 'Bangers', cursive !important;
    font-size: 2rem !important;
    letter-spacing: 1px;
}}
[data-testid="stMetricLabel"] {{
    color: {SUBTEXT} !important;
    font-weight: 700 !important;
}}

/* ── BUTTONS ── */
.stButton > button {{
    background: linear-gradient(135deg, #FF0080, #FF6B00, #FFD700) !important;
    color: white !important;
    border: 3px solid rgba(0,0,0,0.15) !important;
    border-radius: 6px !important;
    min-width: 180px !important;
    min-height: 44px !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 900 !important;
    font-size: 1rem !important;
    padding: 10px 24px !important;
    box-shadow: 4px 4px 0px rgba(0,0,0,0.25) !important;
    transition: all 0.15s !important;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}
.stButton > button:hover {{
    transform: translate(-3px, -3px) !important;
    box-shadow: 7px 7px 0px rgba(0,0,0,0.25) !important;
    background: linear-gradient(135deg, #CC0066, #FF3300, #FFA500) !important;
}}
.stButton > button:active {{
    transform: translate(1px, 1px) !important;
    box-shadow: 2px 2px 0px rgba(0,0,0,0.25) !important;
}}

/* ── TEXT INPUT ── */
.stTextInput input {{
    border: 3px solid #F4A261 !important;
    border-radius: 16px !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    padding: 14px 20px !important;
    background: {INPUT_BG} !important;
    color: {TEXT} !important;
    box-shadow: 3px 3px 0px {BORDER} !important;
}}
.stTextInput input:focus {{
    border-color: #E63946 !important;
    box-shadow: 0 0 0 3px rgba(230,57,70,0.25), 3px 3px 0px {BORDER} !important;
}}
.stTextInput input::placeholder {{
    color: {SUBTEXT} !important;
    font-style: italic;
}}

/* ── DASHBOARD LIST TEXT — purplish navy ── */
.element-container p,
.stMarkdown p,
.stMarkdown li,
.stMarkdown strong {{
    color: {TEXT} !important;
}}
/* Dashboard specific — all list and caption text */
.stMarkdown {{
    color: {TEXT} !important;
}}

/* ── COPYRIGHT DASHBOARD OVERRIDES ── */
/* Large readable yellow text for dashboard stats */
[data-testid="metric-container"] [data-testid="stMetricValue"] {{
    color: #FFD700 !important;
    font-family: 'Bangers', cursive !important;
    font-size: 2.6rem !important;
    letter-spacing: 2px !important;
    text-shadow: 2px 2px 0px rgba(0,0,0,0.3) !important;
}}
[data-testid="metric-container"] [data-testid="stMetricLabel"] {{
    color: #FF6B00 !important;
    font-size: 1rem !important;
    font-weight: 800 !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}}
/* Headings on dashboard */
h2, h3, h4, h5 {{
    color: #7B00FF !important;
    font-family: 'Bangers', cursive !important;
    letter-spacing: 1px !important;
}}

/* ── SELECTBOX ── */
.stSelectbox > div > div {{
    border: 3px solid {BORDER} !important;
    border-radius: 12px !important;
    background: {INPUT_BG} !important;
    color: {TEXT} !important;
    font-weight: 700 !important;
}}

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {{
    gap: 8px !important;
    background: {CARD} !important;
    padding: 8px !important;
    border-radius: 16px !important;
    border: 3px solid {BORDER} !important;
    box-shadow: 3px 3px 0px {BORDER};
}}
.stTabs [data-baseweb="tab"] {{
    border-radius: 10px !important;
    font-weight: 800 !important;
    font-size: 0.95rem !important;
    padding: 8px 20px !important;
    color: {TEXT} !important;
}}
.stTabs [aria-selected="true"] {{
    background: linear-gradient(135deg, #FF0080, #FF6B00) !important;
    color: white !important;
    box-shadow: 2px 2px 0px rgba(0,0,0,0.2);
}}

/* ── DIVIDERS — wavy SVG line ── */
hr {{
    border: none !important;
    height: 12px !important;
    margin: 20px 0 !important;
    background:
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='12'%3E%3Cpath d='M0 6 Q5 0 10 6 Q15 12 20 6 Q25 0 30 6 Q35 12 40 6' stroke='%23F4A261' stroke-width='2.5' fill='none'/%3E%3C/svg%3E")
        repeat-x center !important;
    opacity: 0.9;
}}

/* ── SUCCESS / WARNING / ERROR ── */
[data-testid="stNotification"], .stAlert {{
    border-radius: 14px !important;
    border-width: 3px !important;
    font-weight: 700 !important;
}}
/* ── STATUS BOX BORDERS — darker version of each box color ── */

/* Public Domain — green box: dark green border + shadow */
div[data-testid="stAlert"][data-baseweb="notification"][kind="success"],
[data-testid="stAlert"].st-success,
div[class*="stSuccess"] {{
    border: 3px solid #006400 !important;
    border-radius: 12px !important;
    box-shadow: 3px 3px 0px #004d00 !important;
    font-weight: 700 !important;
}}

/* Protected (warning) — yellow box: dark amber border */
div[data-testid="stAlert"][kind="warning"],
[data-testid="stAlert"].st-warning,
div[class*="stWarning"] {{
    border: 3px solid #B8860B !important;
    border-radius: 12px !important;
    box-shadow: 3px 3px 0px #8B6508 !important;
    font-weight: 700 !important;
}}

/* Protected (error) — red box: dark red border */
div[data-testid="stAlert"][kind="error"],
[data-testid="stAlert"].st-error,
div[class*="stError"] {{
    border: 3px solid #8B0000 !important;
    border-radius: 12px !important;
    box-shadow: 3px 3px 0px #660000 !important;
    font-weight: 700 !important;
}}

/* Catch-all for Streamlit alert containers */
div[role="alert"] {{
    border-radius: 12px !important;
    border-width: 3px !important;
    font-weight: 700 !important;
}}

/* ── MARKDOWN TEXT ── */
p, .stMarkdown p {{
    color: {TEXT} !important;
}}
h1, h2, h3, h4, h5, h6 {{
    color: {TEXT} !important;
}}

/* ── ALERT BOX BORDERS — guaranteed catch-all ── */
/* Streamlit renders alerts inside these selectors */
.stAlert {{
    border-radius: 12px !important;
    font-weight: 700 !important;
}}
/* Green / Public Domain */
.stAlert[data-baseweb="notification"] svg + div,
[data-testid="stNotification"] {{
    border-radius: 12px !important;
}}
/* Force borders on ALL alert types via attribute */
[data-testid="stAlert"] {{
    border-radius: 12px !important;
    border-width: 3px !important;
    border-style: solid !important;
    box-shadow: 3px 3px 0px currentColor !important;
}}
/* Green success */
[data-testid="stAlert"][style*="rgb(33, 195, 84)"],
[data-testid="stAlert"][style*="green"],
.st-emotion-cache-j7qwjs,
[data-testid="stAlert"] p {{
    font-weight: 800 !important;
}}
/* Inline style override — hardcode strokes on each color */
.element-container div[style*="background-color: rgb(230, 244, 234)"] {{
    border: 3px solid #006400 !important;
    box-shadow: 3px 3px 0px #004d00 !important;
    border-radius: 12px !important;
}}
.element-container div[style*="background-color: rgb(255, 237, 171)"] {{
    border: 3px solid #B8860B !important;
    box-shadow: 3px 3px 0px #8B6508 !important;
    border-radius: 12px !important;
}}
.element-container div[style*="background-color: rgb(255, 220, 220)"] {{
    border: 3px solid #8B0000 !important;
    box-shadow: 3px 3px 0px #660000 !important;
    border-radius: 12px !important;
}}

/* ── SIDEBAR NAV RADIO — larger text ── */
section[data-testid="stSidebar"] [data-testid="stRadio"] label {{
    font-size: 1.15rem !important;
    font-weight: 800 !important;
    color: #FFFDF7 !important;
    padding: 6px 4px !important;
    letter-spacing: 0.5px !important;
    font-family: 'Fredoka One', sans-serif !important;
}}
section[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {{
    color: #FFD700 !important;
}}
/* Selected nav item */
section[data-testid="stSidebar"] [data-testid="stRadio"] [aria-checked="true"] + label,
section[data-testid="stSidebar"] [data-testid="stRadio"] label[data-checked="true"] {{
    color: #FFD700 !important;
}}

/* ── SIDEBAR METRICS — larger label and value ── */
section[data-testid="stSidebar"] [data-testid="metric-container"] {{
    padding: 10px 14px !important;
}}
section[data-testid="stSidebar"] [data-testid="stMetricValue"] {{
    font-size: 2.2rem !important;
    font-family: 'Bangers', cursive !important;
    color: #FFD700 !important;
    letter-spacing: 2px !important;
}}
section[data-testid="stSidebar"] [data-testid="stMetricLabel"] {{
    font-size: 1.3rem !important;
    font-weight: 800 !important;
    color: #FF6B00 !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    font-family: 'Fredoka One', sans-serif !important;
}}

/* ── SCROLLBAR ── */
::-webkit-scrollbar {{ width: 8px; }}
::-webkit-scrollbar-track {{ background: {BG}; }}
::-webkit-scrollbar-thumb {{ background: #F4A261; border-radius: 4px; }}
::-webkit-scrollbar-thumb:hover {{ background: #E63946; }}

/* ── CAPTION / SMALL TEXT ── */
.stCaption, small, caption {{
    color: {SUBTEXT} !important;
}}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# Session state — persist library across reruns
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
        st.markdown("""
        <div style="
            background: #CCFFD6;
            border: 4px solid #006400;
            border-radius: 12px;
            box-shadow: 4px 4px 0px #004d00;
            padding: 12px 18px;
            font-weight: 800;
            font-size: 1rem;
            color: #004d00;
            font-family: 'Fredoka One', sans-serif;
        ">✅ Public Domain — free to use</div>
        """, unsafe_allow_html=True)
    else:
        yrs = cartoon.years_until_public_domain
        owner = cartoon.current_owner.owner_name if cartoon.current_owner else "?"
        if yrs <= 10:
            st.markdown(f"""
            <div style="
                background: #FFF3CD;
                border: 4px solid #B8860B;
                border-radius: 12px;
                box-shadow: 4px 4px 0px #8B6508;
                padding: 12px 18px;
                font-weight: 800;
                font-size: 1rem;
                color: #7A5000;
                font-family: 'Fredoka One', sans-serif;
            ">⚠️ Protected — © {owner} ({yrs} yrs until public domain)</div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="
                background: #FFDCDC;
                border: 4px solid #8B0000;
                border-radius: 12px;
                box-shadow: 4px 4px 0px #660000;
                padding: 12px 18px;
                font-weight: 800;
                font-size: 1rem;
                color: #660000;
                font-family: 'Fredoka One', sans-serif;
            ">🔒 Protected — © {owner} ({yrs} yrs until public domain)</div>
            """, unsafe_allow_html=True)


def render_ownership_chain(cartoon: Cartoon):
    total = len(cartoon.ownership_history)
    st.markdown(f"##### 📋 Complete Ownership History — {total} owner(s)")

    # Summary bar
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
        is_first = (i == 0)
        is_current = record.is_current_owner
        year_end = record.year_relinquished or datetime.now().year
        years_held = year_end - record.year_acquired
        year_end_label = str(record.year_relinquished) if record.year_relinquished else "present"

        # Choose icon and color label
        if is_current and is_first:
            icon = "🟢"
            label = "ORIGINAL & CURRENT OWNER"
        elif is_current:
            icon = "🟢"
            label = "CURRENT OWNER"
        elif is_first:
            icon = "🔵"
            label = "ORIGINAL OWNER (at creation)"
        else:
            icon = "⚪"
            label = f"PREVIOUS OWNER #{i}"

        # Main record block
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

        # Arrow to next owner
        if i < total - 1:
            next_record = cartoon.ownership_history[i + 1]
            st.markdown(
                f"&nbsp; &nbsp; &nbsp; &nbsp; ⬇️ &nbsp; *Transferred to* ***{next_record.owner_name}*** *in {next_record.year_acquired} via {next_record.acquisition_method}*"
            )
        st.markdown("---")

    # Copyright status conclusion
    st.markdown("##### ⚖️ Copyright status today")
    if cartoon.is_public_domain:
        st.success(f"✅ **PUBLIC DOMAIN** — This character entered the public domain and is free to use. Original debut: {cartoon.debut_year}.")
    else:
        yrs = cartoon.years_until_public_domain
        st.error(
            f"🔒 **PROTECTED** — Currently owned by **{curr.owner_name if curr else 'Unknown'}**. "
            f"Under US copyright law this character will enter the public domain in approximately **{yrs} year(s)** ({datetime.now().year + yrs})."        )


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
# STRETCH FEATURE 1: AGENTIC WORKFLOW (+2)
# ─────────────────────────────────────────────────────────────────────────────
def render_agentic_workflow(cartoon: Cartoon):
    """Multi-step agentic copyright research with observable reasoning chain."""
    st.markdown("##### 🤖 Agentic Copyright Research")
    st.caption(
        "**Stretch Feature:** Multi-step AI agent that plans, retrieves, analyzes, "
        "checks edge cases, compares similar characters, synthesizes, and self-evaluates. "
        "Each step is observable in real time."
    )
    btn_key = f"agent_btn_{cartoon.name.replace(' ', '_')}"
    if st.button(f"Run Agent Research: {cartoon.name}", key=btn_key):
        progress = st.progress(0)
        status_text = st.empty()
        step_names = ["Planning", "Retrieving", "Analyzing", "Checking edge cases",
                      "Comparing", "Synthesizing", "Self-evaluating"]
        for i, step in enumerate(step_names):
            status_text.text(f"Agent step {i+1}/7: {step}...")
            progress.progress((i + 1) / 7)

        with st.spinner("Agent completing final synthesis..."):
            result = run_copyright_agent(cartoon, lib)
        progress.progress(1.0)
        status_text.empty()

        if result["success"]:
            conf = result["confidence"]
            if conf == "HIGH":
                st.success(f"Research complete — Confidence: {conf}")
            elif conf == "MEDIUM":
                st.warning(f"Research complete — Confidence: {conf}")
            else:
                st.error(f"Research complete — Confidence: {conf}")

            st.markdown("**Observable reasoning chain:**")
            for i, step in enumerate(result["steps"]):
                with st.expander(f"Step {i+1}: {step['name']} {step['status']}"):
                    st.write(step["output"])

            if result["edge_cases"]:
                st.markdown("**Edge cases identified:**")
                for ec in result["edge_cases"]:
                    st.warning(f"⚠️ {ec}")

            if result["similar_characters"]:
                st.markdown("**Comparable characters from database:**")
                for sc in result["similar_characters"]:
                    st.caption(f"• {sc}")

            st.markdown("**Final determination:**")
            st.write(result["final_determination"])
            st.caption("Educational purposes only — not legal advice.")
        else:
            st.error(f"Agent failed: {result['final_determination']}")


# ─────────────────────────────────────────────────────────────────────────────
# STRETCH FEATURE 2: FEW-SHOT FINE-TUNING (+2)
# ─────────────────────────────────────────────────────────────────────────────
def render_few_shot_analysis(cartoon: Cartoon):
    """Few-shot specialized analysis using CartoonPal curated examples."""
    st.markdown("##### 📚 Specialized Analysis (Few-Shot)")
    st.caption(
        "**Stretch Feature:** Uses few-shot prompting with curated CartoonPal examples "
        "to produce structured, consistent, domain-specific copyright analysis. "
        "Output format and tone are calibrated using 2-3 scenario-matched examples."
    )
    btn_key = f"fewshot_btn_{cartoon.name.replace(' ', '_')}"
    if st.button(f"Specialized Analysis: {cartoon.name}", key=btn_key):
        with st.spinner("Selecting calibration examples → running specialized analysis..."):
            result = run_few_shot_analysis(cartoon)

        if result["success"]:
            conf = result["confidence"]
            st.info(f"📖 Calibrated with {result['examples_used']} scenario-matched example(s)")
            if conf == "HIGH":
                st.success(f"Confidence: {conf}")
            elif conf == "MEDIUM":
                st.warning(f"Confidence: {conf}")
            else:
                st.error(f"Confidence: {conf}")

            sections = result["format_sections"]
            if sections:
                if "STATUS" in sections:
                    st.markdown(f"**Status:** {sections['STATUS']}")
                if "BASIS" in sections:
                    st.markdown(f"**Legal basis:** {sections['BASIS']}")
                if "NUANCE" in sections:
                    st.markdown(f"**Nuance:** {sections['NUANCE']}")
                if "PRACTICAL GUIDANCE" in sections:
                    st.success(f"**Practical guidance:** {sections['PRACTICAL GUIDANCE']}")
            else:
                st.write(result["analysis"])
            st.caption("Educational purposes only — not legal advice.")
        else:
            st.error(f"Analysis failed: {result['analysis']}")


# ─────────────────────────────────────────────────────────────────────────────
# AI ANALYSIS UI  (RAG feature — Project 4 requirement)
# ─────────────────────────────────────────────────────────────────────────────
def render_ai_analysis(cartoon: Cartoon):
    """Streamlit panel for AI-powered copyright analysis using RAG pattern."""
    st.markdown("##### AI Copyright Analysis")
    st.caption(
        "Uses Claude (Anthropic) via RAG: retrieves structured data from CartoonPal "
        "then sends it to Claude for a plain-English copyright explanation with confidence score."
    )
    btn_key = f"ai_btn_{cartoon.name.replace(' ', '_')}"
    if st.button(f"Analyze: {cartoon.name}", key=btn_key):
        with st.spinner("Step 1: Retrieving data... Step 2: Sending to Claude... Step 3: Generating analysis..."):
            result = analyze_copyright_with_ai(cartoon)
        if result["success"]:
            conf = result["confidence"]
            if conf == "HIGH":
                st.success(f"Confidence: {conf}")
            elif conf == "MEDIUM":
                st.warning(f"Confidence: {conf}")
            else:
                st.error(f"Confidence: {conf}")
            st.markdown("**Claude AI Analysis:**")
            st.write(result["analysis"])
            st.caption(
                "Educational use only — not legal advice. "
                "Claude analyzed structured ownership data retrieved from CartoonPal database (RAG pattern)."
            )
        else:
            st.error(f"Analysis unavailable: {result['analysis']}")


# ─────────────────────────────────────────────────────────────────────────────
# Sidebar navigation
# ─────────────────────────────────────────────────────────────────────────────
# ── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="cp-logo-wrap">
        <div class="cp-logo-badge">
            <span class="cp-logo-pencil">✏️</span>
            <span class="cp-logo-brush">🖌️</span>
            <span class="cp-logo-star-icon">⭐</span>
        </div>
        <span class="cp-logo-text">CartoonPal</span>
        <span class="cp-logo-sub">Copyright Explorer</span>
        <span class="cp-logo-stars">✦ ✦ ✦</span>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # ── DARK / LIGHT MODE TOGGLE ─────────────────────────────
    label = "🌙 Switch to Dark Mode" if not st.session_state.dark_mode else "☀️ Switch to Light Mode"
    if st.button(label, key="mode_toggle", use_container_width=True):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

    current_mode = "🌙 Dark Mode" if st.session_state.dark_mode else "☀️ Light Mode"
    st.markdown(
        f"<div style='text-align:center;font-size:0.75rem;color:#AAAACC;margin-top:2px;'>"
        f"Active: <b style='color:#FFD166;'>{current_mode}</b></div>",
        unsafe_allow_html=True)

    st.divider()

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
    st.markdown("""
    <div class="cp-header cp-header-search">
        <h1 style="font-family: 'Bangers', cursive !important;
                   font-size: 3.2rem !important;
                   letter-spacing: 4px !important;
                   text-shadow: 4px 4px 0px rgba(0,0,0,0.25), -2px -2px 0px rgba(255,255,255,0.15) !important;
                   color: white !important;">
            🔍 Search CartoonPal!
        </h1>
        <p>Find any animated character — copyright status, ownership history, and AI analysis</p>
    </div>
    """, unsafe_allow_html=True)
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

                # Show current era image in sidebar panel
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


            st.divider()
            render_ai_analysis(result)

            with st.expander("🤖 Agentic Workflow Research"):
                render_agentic_workflow(result)

            with st.expander("📚 Few-Shot Specialized Analysis"):
                render_few_shot_analysis(result)

        else:
            st.warning(f"No cartoon found matching '{query}'. Try Browse All to see what's in the library.")

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: Browse All
# ─────────────────────────────────────────────────────────────────────────────
elif page == "📚 Browse All":
    st.markdown("""
    <div class="cp-header cp-header-browse">
        <h1>📚 Browse All Cartoons</h1>
        <p>255 characters across 10 studios — sort, filter, and explore</p>
    </div>
    """, unsafe_allow_html=True)

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
                    st.error(f"🔒 Protected")
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
    <div class="cp-header cp-header-dash">
        <h1>⚖️ Copyright Dashboard</h1>
        <p>Who owns what — and when does it expire?</p>
    </div>
    """, unsafe_allow_html=True)

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
            yrs = c.years_until_public_domain
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
    <div class="cp-header cp-header-add">
        <h1>➕ Add a Cartoon</h1>
        <p>Contribute a new character to the CartoonPal database</p>
    </div>
    """, unsafe_allow_html=True)
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
        studio_name = st.text_input("Studio name")
        studio_founded = st.number_input("Studio founded year", min_value=1880, max_value=datetime.now().year, value=1920)
        studio_active = st.checkbox("Studio still active", value=True)

        st.subheader("Original ownership")
        orig_owner = st.text_input("Original owner name *")
        orig_year = st.number_input("Year acquired", min_value=1880, max_value=datetime.now().year, value=int(debut_year))
        orig_method = st.text_input("Acquisition method", value="original creation")

        st.subheader("Current ownership")
        same_owner = st.checkbox("Same as original owner", value=True)
        curr_owner_name = st.text_input("Current owner name (if different)")
        curr_year = st.number_input("Year current owner acquired", min_value=1880, max_value=datetime.now().year, value=int(debut_year))
        curr_method = st.text_input("Current acquisition method", value="original creation")

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