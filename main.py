"""
ToonVault — CLI Demo Script
Demonstrates core system functionality with real 20th century cartoons.
Run: python main.py
"""

from toonvault_system import (
    Researcher, Cartoon, CartoonVersion, Credit, Vault,
    COPYRIGHT_PUBLIC_DOMAIN, COPYRIGHT_MIXED, COPYRIGHT_PROTECTED
)


def print_header(title: str):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def print_section(title: str):
    print(f"\n--- {title} ---")


def main():
    print_header("🎬 ToonVault — 20th Century Cartoon Intelligence System")

    # -----------------------------------------------------------------------
    # Setup: Create Researcher
    # -----------------------------------------------------------------------
    researcher = Researcher(name="Demo Researcher")
    vault = Vault(researcher)

    # -----------------------------------------------------------------------
    # Cartoon 1: Felix the Cat (Silent Era → Modern)
    # -----------------------------------------------------------------------
    felix = Cartoon(
        name="Felix the Cat",
        studio="Pat Sullivan Studio / Otto Messmer",
        origin_year=1919,
        country="USA",
        genre="Slapstick / Comedy"
    )

    v1 = CartoonVersion(
        year=1919,
        title="Feline Follies (Original)",
        description="First appearance — simple black and white design, expressive eyes.",
        production_method="Hand-drawn cel animation",
        notes="Created by Otto Messmer, produced under Pat Sullivan's name."
    )
    v1.add_credit("Otto Messmer", "Creator / Animator", "Primary creative force behind Felix")
    v1.add_credit("Pat Sullivan", "Producer", "Studio owner who held the trademark")

    v2 = CartoonVersion(
        year=1928,
        title="Felix the Cat Woos Whoopee",
        description="Sound era transition — Felix redesigned slightly for sound shorts.",
        production_method="Hand-drawn cel animation",
        notes="One of the first Felix cartoons with synchronized sound attempted."
    )
    v2.add_credit("Otto Messmer", "Animator")
    v2.add_credit("Pat Sullivan", "Producer")

    v3 = CartoonVersion(
        year=1958,
        title="Felix the Cat TV Series",
        description="Major redesign for television — simplified, rounder design with magic bag.",
        production_method="Limited animation (TV style)",
        notes="Joe Oriolo redesigned Felix for the TV era. Introduced the Magic Bag of Tricks."
    )
    v3.add_credit("Joe Oriolo", "Director / Redesign Artist", "Introduced the Magic Bag")
    v3.add_credit("Jack Mercer", "Voice Actor", "Voiced Felix in TV series")

    felix.add_version(v1)
    felix.add_version(v2)
    felix.add_version(v3)
    researcher.add_cartoon(felix)

    # -----------------------------------------------------------------------
    # Cartoon 2: Betty Boop (Golden Age)
    # -----------------------------------------------------------------------
    betty = Cartoon(
        name="Betty Boop",
        studio="Fleischer Studios",
        origin_year=1930,
        country="USA",
        genre="Musical / Comedy"
    )

    bv1 = CartoonVersion(
        year=1930,
        title="Dizzy Dishes (First Appearance)",
        description="Original design — exaggerated features, dog-like ears, very flirtatious.",
        production_method="Hand-drawn cel animation",
        notes="Betty initially appeared as a dog-human hybrid character."
    )
    bv1.add_credit("Max Fleischer", "Producer", "Founded Fleischer Studios")
    bv1.add_credit("Grim Natwick", "Animator / Creator", "Designed Betty Boop's original look")
    bv1.add_credit("Mae Questel", "Voice Actress", "Primary voice of Betty Boop")

    bv2 = CartoonVersion(
        year=1932,
        title="Betty Boop M.D.",
        description="Fully human design established — short skirt, garter, more risqué.",
        production_method="Hand-drawn cel animation",
        notes="Pre-Hays Code era — Betty at her most provocative."
    )
    bv2.add_credit("Dave Fleischer", "Director")
    bv2.add_credit("Mae Questel", "Voice Actress")

    bv3 = CartoonVersion(
        year=1934,
        title="Betty Boop's Rise to Fame (Post-Hays Code)",
        description="Toned down significantly — longer skirt, less provocative, more wholesome.",
        production_method="Hand-drawn cel animation",
        notes="Hays Code enforcement in 1934 forced major character redesign."
    )
    bv3.add_credit("Mae Questel", "Voice Actress")
    bv3.add_credit("Dave Fleischer", "Director")

    betty.add_version(bv1)
    betty.add_version(bv2)
    betty.add_version(bv3)
    researcher.add_cartoon(betty)

    # -----------------------------------------------------------------------
    # Cartoon 3: Bugs Bunny (Golden Age → TV)
    # -----------------------------------------------------------------------
    bugs = Cartoon(
        name="Bugs Bunny",
        studio="Warner Bros. / Looney Tunes",
        origin_year=1940,
        country="USA",
        genre="Slapstick / Comedy"
    )

    bbv1 = CartoonVersion(
        year=1940,
        title="A Wild Hare (Official Debut)",
        description="First fully developed Bugs — confident, wisecracking personality established.",
        production_method="Hand-drawn cel animation",
        notes="Generally considered Bugs Bunny's official debut in his modern form."
    )
    bbv1.add_credit("Tex Avery", "Director", "Directed the official debut short")
    bbv1.add_credit("Mel Blanc", "Voice Actor", "Voiced Bugs Bunny throughout his career")
    bbv1.add_credit("Chuck Jones", "Animator")

    bbv2 = CartoonVersion(
        year=1955,
        title="Bugs Bunny (CinemaScope Era)",
        description="Wider format shorts — character art refined for widescreen theatrical presentation.",
        production_method="Hand-drawn cel animation",
        notes="Warner Bros. adopted CinemaScope for theatrical shorts in mid-1950s."
    )
    bbv2.add_credit("Chuck Jones", "Director")
    bbv2.add_credit("Mel Blanc", "Voice Actor")

    bugs.add_version(bbv1)
    bugs.add_version(bbv2)
    researcher.add_cartoon(bugs)

    # -----------------------------------------------------------------------
    # Demo: CLI Output
    # -----------------------------------------------------------------------

    print_section("📚 Collection Summary")
    summary = vault.collection_summary()
    for key, val in summary.items():
        print(f"  {key.replace('_', ' ').title()}: {val}")

    print_section("🗂️ All Cartoons (Sorted by Name)")
    for cartoon in vault.sort_by_name():
        print(f"  {cartoon}")

    print_section("📅 All Versions (Chronological)")
    for cartoon, version in vault.sort_by_year():
        print(f"  [{version.year}] {cartoon.name} — {version.title} | {version.copyright_status}")

    print_section("✅ Public Domain Cartoons")
    for cartoon in vault.filter_by_copyright(COPYRIGHT_PUBLIC_DOMAIN):
        print(f"  {cartoon.name} ({cartoon.origin_year}) — {cartoon.studio}")

    print_section("🎬 Felix the Cat — Evolution Timeline")
    timeline = vault.get_evolution_timeline(felix)
    for entry in timeline:
        print(f"\n  [{entry['year']}] {entry['title']}")
        print(f"    Description : {entry['description']}")
        print(f"    Method      : {entry['production_method']}")
        print(f"    Copyright   : {entry['copyright_status']}")
        print(f"    Change      : {entry['change_from_previous']}")
        if entry['credits']:
            print(f"    Credits     : {', '.join(entry['credits'])}")

    print_section("⚠️ Duplicate Version Detection")
    dupes = vault.detect_all_duplicates()
    if dupes:
        for name, years in dupes.items():
            print(f"  ⚠️  {name}: duplicate years {years}")
    else:
        print("  ✅ No duplicate versions detected.")

    print_section("⚖️ Copyright Breakdown")
    for status in [COPYRIGHT_PUBLIC_DOMAIN, COPYRIGHT_MIXED, COPYRIGHT_PROTECTED]:
        cartoons = vault.filter_by_copyright(status)
        names = [c.name for c in cartoons]
        print(f"  {status}: {names if names else 'None'}")

    print_header("✅ ToonVault Demo Complete")


if __name__ == "__main__":
    main()
