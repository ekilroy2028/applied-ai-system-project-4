"""
ai_analysis.py
CartoonPal AI Copyright Analysis — RAG (Retrieval-Augmented Generation) feature.

Pattern:
  1. RETRIEVE  — pull structured cartoon data from CartoonPal's database
  2. AUGMENT   — build a detailed prompt using that retrieved data
  3. GENERATE  — send to Claude for plain-English copyright explanation

This follows the RAG pattern required by Project 4:
  - The AI retrieves real structured data before answering
  - The retrieved data meaningfully changes Claude's response
  - Results include a confidence score (HIGH / MEDIUM / LOW)
  - All calls are logged; errors are caught and surfaced in the UI
"""

import logging
from datetime import datetime
from cartoon_system import Cartoon

log = logging.getLogger(__name__)


def analyze_copyright_with_ai(cartoon: Cartoon) -> dict:
    """
    RAG copyright analysis for a cartoon character.

    Step 1 — RETRIEVE: pull structured ownership and copyright data
    Step 2 — AUGMENT:  build a prompt that includes all retrieved facts
    Step 3 — GENERATE: send to Claude, parse response, extract confidence

    Returns:
        dict with keys: success (bool), analysis (str), confidence (str)
    """
    try:
        import anthropic
    except ImportError:
        return {
            "success": False,
            "analysis": "anthropic package not installed. Run: pip install anthropic",
            "confidence": "ERROR"
        }

    # ── STEP 1: RETRIEVE ─────────────────────────────────────────────────
    orig = cartoon.original_owner
    curr = cartoon.current_owner

    ownership_lines = []
    for i, r in enumerate(cartoon.ownership_history):
        end = str(r.year_relinquished) if r.year_relinquished else "present"
        tag = " [CURRENT]" if r.is_current_owner else ""
        line = f"  {i+1}. {r.owner_name} ({r.year_acquired}-{end}) via {r.acquisition_method}{tag}"
        if r.notes:
            line += f" — {r.notes}"
        ownership_lines.append(line)

    ownership_text = "\n".join(ownership_lines) if ownership_lines else "  No ownership records found"
    creators_text = ", ".join(c.full_name for c in cartoon.creators) or "Unknown"
    series_titles = [s.title for s in cartoon.series_list]
    series_text = "; ".join(series_titles[:5])
    if len(series_titles) > 5:
        series_text += f" ... and {len(series_titles) - 5} more"

    current_year = datetime.now().year
    pd_status = "PUBLIC DOMAIN" if cartoon.is_public_domain else "PROTECTED"
    yrs_left = cartoon.years_until_public_domain if not cartoon.is_public_domain else 0

    # ── STEP 2: AUGMENT ──────────────────────────────────────────────────
    prompt = (
        "You are a copyright research assistant specializing in animated cartoon IP.\n\n"
        "CHARACTER DATA RETRIEVED FROM CARTOONPAL DATABASE:\n"
        f"Name: {cartoon.name}\n"
        f"Debut year: {cartoon.debut_year}\n"
        f"Country: {cartoon.country_of_origin}\n"
        f"Character type: {cartoon.character_type}\n"
        f"Creator(s): {creators_text}\n"
        f"Original studio: {cartoon.original_studio}\n"
        f"Productions: {series_text}\n\n"
        "COMPLETE OWNERSHIP CHAIN:\n"
        f"{ownership_text}\n\n"
        f"CARTOONPAL COPYRIGHT DETERMINATION: {pd_status}\n"
        f"Years until US public domain: {yrs_left if yrs_left > 0 else 'Already in public domain'}\n\n"
        f"TASK: Using only the retrieved data above, write a 2-3 sentence plain-English explanation "
        f"of this cartoon's copyright status as of {current_year}. "
        "Include: whether it is public domain or protected, the key legal reason why, "
        "and any important nuances such as the difference between copyright and trademark, "
        "or partial public domain status. "
        "End your response with exactly one line: CONFIDENCE: HIGH, MEDIUM, or LOW\n"
        "Keep the total response under 160 words."
    )

    # ── STEP 3: GENERATE ─────────────────────────────────────────────────
    try:
        client = anthropic.Anthropic()
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=350,
            messages=[{"role": "user", "content": prompt}]
        )
        response_text = message.content[0].text.strip()

        # Parse confidence score
        confidence = "MEDIUM"
        upper = response_text.upper()
        if "CONFIDENCE: HIGH" in upper:
            confidence = "HIGH"
        elif "CONFIDENCE: LOW" in upper:
            confidence = "LOW"

        log.info("AI analysis OK — %s — confidence: %s", cartoon.name, confidence)
        return {"success": True, "analysis": response_text, "confidence": confidence}

    except Exception as e:
        log.error("AI analysis failed for %s: %s", cartoon.name, e)
        return {
            "success": False,
            "analysis": (
                f"Could not reach Claude API: {e}. "
                "Make sure ANTHROPIC_API_KEY is set in your environment."
            ),
            "confidence": "ERROR"
        }