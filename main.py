"""
main.py
CartoonPal — CLI demo script.
Run this first to verify all backend logic works before opening the Streamlit UI.
    python main.py
"""

from cartoon_system import CartoonAnalyzer
from seed_data import build_library


def divider(char="─", width=60):
    print(char * width)


def run_demo():
    lib = build_library()
    analyzer = CartoonAnalyzer(lib)

    print("\n")
    divider("═")
    print("  CartoonPal — CLI Demo")
    divider("═")

    # ── Full record for each cartoon ───────────────────────────────────────
    for cartoon in analyzer.sort_by_debut():
        print(cartoon.summary())

        print("\n  Creators:")
        for c in cartoon.creators:
            print(f"    · {c}")

        print("\n  Original studio:")
        print(f"    · {cartoon.original_studio}")

        print("\n  Ownership chain (original → current):")
        for record in cartoon.ownership_history:
            print(f"    · {record}")

        print("\n  Series timeline:")
        for s in cartoon.series_list:
            print(f"    · {s}")

        print("\n  Visual eras:")
        for era in cartoon.eras:
            print(f"    · {era}")

        overlaps = analyzer.detect_series_overlap(cartoon)
        if overlaps:
            print("\n  ⚠  Overlapping series detected:")
            for a, b in overlaps:
                print(f"    · '{a.title}' overlaps with '{b.title}'")

    # ── Copyright summary ──────────────────────────────────────────────────
    print("\n")
    divider("═")
    print("  Copyright Summary")
    divider("═")
    summary = analyzer.get_copyright_summary()
    print(f"  Total in library   : {summary['total']}")
    print(f"  Public domain      : {summary['public_domain']}")
    print(f"  Protected          : {summary['protected']}")
    print(f"  % public domain    : {summary['pd_percent']}%")

    # ── Ownership changes ──────────────────────────────────────────────────
    print("\n  Cartoons whose ownership changed since creation:")
    for c in analyzer.ownership_changed_cartoons():
        orig = c.original_owner.owner_name if c.original_owner else "?"
        curr = c.current_owner.owner_name if c.current_owner else "Public domain"
        print(f"    · {c.name}: [{orig}] → [{curr}]")

    # ── Approaching public domain ──────────────────────────────────────────
    print("\n  Protected cartoons approaching public domain (within 20 yrs):")
    approaching = analyzer.flag_approaching_public_domain(within_years=20)
    if approaching:
        for c in approaching:
            print(f"    · {c.name} — {c.years_until_public_domain} year(s) remaining")
    else:
        print("    None in this dataset within 20 years")

    # ── Find by search ─────────────────────────────────────────────────────
    print("\n  Search demo — searching 'bugs':")
    result = lib.find("bugs")
    if result:
        print(f"    Found: {result.name} | {result.copyright_status}")

    print("\n  Filter by studio — 'Fleischer':")
    for c in lib.filter_by_studio("Fleischer"):
        print(f"    · {c.name} ({c.debut_year})")

    print("\n  Filter by decade — 1930s:")
    for c in lib.filter_by_decade(1930):
        print(f"    · {c.name} ({c.debut_year})")

    divider("═")
    print("  Demo complete. Run 'streamlit run app.py' to open the UI.\n")


if __name__ == "__main__":
    run_demo()