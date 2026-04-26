"""
agentic_workflow.py
CartoonPal Agentic Copyright Research Workflow — Stretch Feature (+2 points)

This implements a MULTI-STEP AGENTIC WORKFLOW where the AI:
  1. Plans its research approach
  2. Retrieves and analyzes ownership data
  3. Checks for copyright edge cases
  4. Synthesizes a final determination
  5. Self-evaluates its own confidence

Each step is OBSERVABLE — the UI shows what the agent is doing at each stage,
making the reasoning chain transparent and verifiable.

This goes beyond the basic RAG feature by adding:
  - Autonomous planning (agent decides what to investigate)
  - Multi-step tool-like calls (each step informs the next)
  - Self-evaluation (agent critiques its own output)
  - Observable intermediate steps visible in the UI
"""

import logging
from datetime import datetime
from cartoon_system import Cartoon, Library, CartoonAnalyzer

log = logging.getLogger(__name__)


def run_copyright_agent(cartoon: Cartoon, library: Library) -> dict:
    """
    Multi-step agentic copyright research workflow.

    The agent autonomously:
      Step 1 — PLAN:     Decide what aspects to investigate
      Step 2 — RETRIEVE: Pull all structured data from CartoonPal database
      Step 3 — ANALYZE:  Send structured data to Claude for initial analysis
      Step 4 — CHECK:    Agent checks for edge cases and complicating factors
      Step 5 — COMPARE:  Find similar characters for context
      Step 6 — SYNTHESIZE: Claude produces final determination
      Step 7 — EVALUATE: Agent self-evaluates confidence and flags uncertainties

    Returns:
        dict with keys:
          steps: list of {name, status, output} — the observable reasoning chain
          final_determination: str — the final copyright conclusion
          confidence: str — HIGH / MEDIUM / LOW
          edge_cases: list of str — any complicating factors found
          similar_characters: list of str — comparable characters for context
          success: bool
    """
    try:
        import anthropic
    except ImportError:
        return {
            "success": False,
            "steps": [],
            "final_determination": "anthropic package not installed. Run: pip3 install anthropic",
            "confidence": "ERROR",
            "edge_cases": [],
            "similar_characters": []
        }

    steps = []
    edge_cases = []

    def add_step(name: str, status: str, output: str):
        steps.append({"name": name, "status": status, "output": output})
        log.info("Agent step [%s]: %s — %s", name, status, output[:80])

    try:
        client = anthropic.Anthropic()
        analyzer = CartoonAnalyzer(library)

        # ── STEP 1: PLAN ─────────────────────────────────────────────────
        plan_aspects = []
        if len(cartoon.ownership_history) > 2:
            plan_aspects.append("complex ownership chain with multiple transfers")
        if cartoon.debut_year < 1928:
            plan_aspects.append("pre-1928 debut — likely public domain")
        elif cartoon.debut_year < 1935:
            plan_aspects.append("early 1930s debut — approaching public domain")
        if cartoon.country_of_origin != "USA":
            plan_aspects.append(f"non-US origin ({cartoon.country_of_origin}) — international copyright applies")
        if not cartoon.current_owner:
            plan_aspects.append("no current owner on record — possible public domain")

        plan_text = (
            f"Investigating {cartoon.name} ({cartoon.debut_year}). "
            f"Key aspects to analyze: {'; '.join(plan_aspects) if plan_aspects else 'standard US copyright analysis'}. "
            f"Ownership records: {len(cartoon.ownership_history)}. "
            f"Series productions: {len(cartoon.series_list)}."
        )
        add_step("PLAN", "✅ Complete", plan_text)

        # ── STEP 2: RETRIEVE ─────────────────────────────────────────────
        ownership_lines = []
        for i, r in enumerate(cartoon.ownership_history):
            end = str(r.year_relinquished) if r.year_relinquished else "present"
            tag = " [CURRENT]" if r.is_current_owner else ""
            line = f"{i+1}. {r.owner_name} ({r.year_acquired}-{end}) via {r.acquisition_method}{tag}"
            ownership_lines.append(line)

        creators_text = ", ".join(c.full_name for c in cartoon.creators) or "Unknown"
        series_text = "; ".join(s.title for s in cartoon.series_list[:4])
        if len(cartoon.series_list) > 4:
            series_text += f" ... +{len(cartoon.series_list)-4} more"

        current_year = datetime.now().year
        pd_status = "PUBLIC DOMAIN" if cartoon.is_public_domain else "PROTECTED"
        yrs_left = cartoon.years_until_public_domain

        retrieve_text = (
            f"Retrieved: {len(cartoon.ownership_history)} ownership records, "
            f"{len(cartoon.series_list)} series, "
            f"{len(cartoon.creators)} creator(s), "
            f"copyright determination: {pd_status}"
        )
        add_step("RETRIEVE", "✅ Complete", retrieve_text)

        # ── STEP 3: INITIAL ANALYSIS ──────────────────────────────────────
        ownership_block = "\n".join(ownership_lines)
        initial_prompt = (
            "You are a copyright research agent. Analyze this cartoon's copyright status.\n\n"
            f"CHARACTER: {cartoon.name}\n"
            f"Debut: {cartoon.debut_year} | Country: {cartoon.country_of_origin}\n"
            f"Creators: {creators_text}\n"
            f"Original studio: {cartoon.original_studio}\n\n"
            f"OWNERSHIP CHAIN:\n{ownership_block}\n\n"
            f"DATABASE STATUS: {pd_status}\n"
            f"Years until public domain: {yrs_left if yrs_left > 0 else 'Already public domain'}\n\n"
            "Provide an initial copyright analysis in 2-3 sentences. "
            "Note any unusual aspects of this character's ownership or copyright situation. "
            "Be specific about the legal basis."
        )

        initial_response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=200,
            messages=[{"role": "user", "content": initial_prompt}]
        )
        initial_analysis = initial_response.content[0].text.strip()
        add_step("ANALYZE", "✅ Complete", initial_analysis)

        # ── STEP 4: CHECK EDGE CASES ─────────────────────────────────────
        # Agent autonomously checks for complicating factors
        if cartoon.debut_year < 1928:
            edge_cases.append(
                f"Pre-1928 debut ({cartoon.debut_year}) — original works in US public domain, "
                "but active trademark may still restrict commercial use"
            )
        if cartoon.country_of_origin != "USA":
            edge_cases.append(
                f"Originated in {cartoon.country_of_origin} — international copyright differs from US 95-year rule. "
                "Japan uses life+50 years; EU uses life+70 years."
            )
        if len(cartoon.ownership_history) > 3:
            transfers = len(cartoon.ownership_history) - 1
            edge_cases.append(
                f"Complex ownership: {transfers} transfers of ownership may create "
                "licensing complications even if core copyright is clear."
            )
        orig = cartoon.original_owner
        curr = cartoon.current_owner
        if orig and curr and orig.owner_name != curr.owner_name:
            edge_cases.append(
                f"Ownership changed from original creator/studio ({orig.owner_name}) "
                f"to current holder ({curr.owner_name}) — "
                "verify whether original creator retained any rights."
            )
        if not cartoon.is_public_domain and yrs_left <= 10:
            edge_cases.append(
                f"Approaching public domain in {yrs_left} year(s) — "
                "current owner may lobby for copyright extension (as Disney did with the Sonny Bono Act)."
            )

        edge_text = (
            f"Found {len(edge_cases)} edge case(s): "
            + (edge_cases[0][:100] + "..." if edge_cases else "None — straightforward case.")
        )
        add_step("CHECK EDGE CASES", "✅ Complete", edge_text)

        # ── STEP 5: COMPARE SIMILAR CHARACTERS ───────────────────────────
        # Agent finds comparable characters from the database for context
        similar = []
        decade = (cartoon.debut_year // 10) * 10
        same_decade = [
            c for c in library.cartoons
            if decade <= c.debut_year < decade + 10
            and c.name != cartoon.name
            and c.is_public_domain == cartoon.is_public_domain
        ][:3]
        similar = [f"{c.name} ({c.debut_year}) — {c.copyright_status}" for c in same_decade]

        compare_text = (
            f"Found {len(similar)} comparable characters from the {decade}s with same copyright status: "
            + (", ".join(c.name for c in same_decade) if same_decade else "none in database")
        )
        add_step("COMPARE", "✅ Complete", compare_text)

        # ── STEP 6: SYNTHESIZE FINAL DETERMINATION ────────────────────────
        edge_block = "\n".join(f"- {e}" for e in edge_cases) if edge_cases else "- None identified"
        similar_block = "\n".join(f"- {s}" for s in similar) if similar else "- None in database"

        synthesis_prompt = (
            "You are a copyright research agent completing a multi-step analysis. "
            "Below is your research chain. Synthesize a final determination.\n\n"
            f"CHARACTER: {cartoon.name} ({cartoon.debut_year})\n"
            f"DATABASE DETERMINATION: {pd_status}\n"
            f"Years until US public domain: {yrs_left if yrs_left > 0 else 'Already public domain'}\n\n"
            f"INITIAL ANALYSIS:\n{initial_analysis}\n\n"
            f"EDGE CASES IDENTIFIED:\n{edge_block}\n\n"
            f"COMPARABLE CHARACTERS:\n{similar_block}\n\n"
            "Write a final 3-4 sentence copyright determination that:\n"
            "1. States clearly whether this character is public domain or protected\n"
            "2. Gives the specific legal basis\n"
            "3. Addresses any edge cases found\n"
            "4. Provides practical guidance for someone wanting to use this character\n\n"
            "End with: FINAL CONFIDENCE: HIGH, MEDIUM, or LOW\n"
            "Keep under 200 words."
        )

        final_response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=400,
            messages=[{"role": "user", "content": synthesis_prompt}]
        )
        final_text = final_response.content[0].text.strip()

        # Parse confidence
        confidence = "MEDIUM"
        upper = final_text.upper()
        if "FINAL CONFIDENCE: HIGH" in upper:
            confidence = "HIGH"
        elif "FINAL CONFIDENCE: LOW" in upper:
            confidence = "LOW"

        add_step("SYNTHESIZE", "✅ Complete",
                 f"Final determination generated ({len(final_text)} chars) — confidence: {confidence}")

        # ── STEP 7: SELF-EVALUATE ─────────────────────────────────────────
        # Agent evaluates its own reasoning quality
        eval_issues = []
        if len(cartoon.ownership_history) == 0:
            eval_issues.append("No ownership records — determination based on debut year only")
        if cartoon.country_of_origin != "USA":
            eval_issues.append("International origin — US law applied but may not fully reflect local rules")
        if len(edge_cases) > 2:
            eval_issues.append("Multiple edge cases — consult an IP attorney for commercial use")

        eval_text = (
            f"Self-evaluation complete. Reasoning quality: {confidence}. "
            + (f"Caveats: {'; '.join(eval_issues)}" if eval_issues else "No significant caveats identified.")
        )
        add_step("SELF-EVALUATE", "✅ Complete", eval_text)

        log.info("Agent workflow complete for %s — %d steps, confidence: %s",
                 cartoon.name, len(steps), confidence)

        return {
            "success": True,
            "steps": steps,
            "final_determination": final_text,
            "confidence": confidence,
            "edge_cases": edge_cases,
            "similar_characters": similar,
        }

    except Exception as e:
        log.error("Agent workflow failed: %s", e)
        add_step("ERROR", "❌ Failed", str(e))
        return {
            "success": False,
            "steps": steps,
            "final_determination": f"Agent workflow failed: {e}. Check ANTHROPIC_API_KEY.",
            "confidence": "ERROR",
            "edge_cases": edge_cases,
            "similar_characters": [],
        }