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
        st.success("✅  Public Domain — free to use")
    else:
        yrs = cartoon.years_until_public_domain
        if yrs <= 10:
            st.warning(f"⚠️  Protected — © {cartoon.current_owner.owner_name if cartoon.current_owner else '?'}  ({yrs} yrs until public domain)")
        else:
            st.error(f"🔒  Protected — © {cartoon.current_owner.owner_name if cartoon.current_owner else '?'}  ({yrs} yrs until public domain)")


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
st.sidebar.title("🎨 CartoonPal")
st.sidebar.caption("Cartoon copyright & visual history explorer")
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