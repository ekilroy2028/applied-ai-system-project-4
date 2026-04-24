"""
seed_data.py
Pre-built cartoon records for CartoonPal.
Import build_library() to get a fully populated Library instance.
"""

from cartoon_system import (
    Cartoon, Creator, ProductionCompany,
    Series, OwnershipRecord, Era, Library
)


def build_library() -> Library:
    lib = Library()

    # ── FELIX THE CAT (1919) ──────────────────────────────────────────────
    felix = Cartoon(
        name="Felix the Cat",
        description=(
            "A clever, mischievous black cat famous for his magic bag of tricks "
            "and surreal silent-era adventures. One of the first animated characters "
            "to become a worldwide pop-culture phenomenon."
        ),
        character_type="Anthropomorphic animal — cat",
        country_of_origin="USA",
        debut_year=1919,
    )
    felix.original_studio = ProductionCompany("Pat Sullivan Cartoon Studio", 1916, still_active=False)
    felix.add_creator(Creator("Otto Messmer", "Character designer & primary animator", 1892, 1983))
    felix.add_creator(Creator("Pat Sullivan", "Producer & copyright holder", 1887, 1933))

    felix.add_series(Series("Feline Follies & silent shorts", 1919, 1930,
        "Pat Sullivan Cartoon Studio", "theatrical short", episode_count=175))
    felix.add_series(Series("Felix the Cat (TV)", 1958, 1961,
        "Trans-Lux", "TV series", episode_count=260))
    felix.add_series(Series("The Twisted Tales of Felix the Cat", 1995, 1997,
        "Film Roman / CBS", "TV series", episode_count=52))

    felix.add_ownership_record(OwnershipRecord(
        "Pat Sullivan", 1919, 1933, "original creation"))
    felix.add_ownership_record(OwnershipRecord(
        "Sullivan Estate / de facto public domain", 1933, 1958,
        "estate dissolution — rights disputed"))
    felix.add_ownership_record(OwnershipRecord(
        "Felix the Cat Productions / Don Oriolo", 1958, None,
        "purchase & trademark revival", is_current_owner=True,
        notes="Oriolo family revived the character via trademark even as early films entered public domain"))

    felix.add_era(Era(1919, 1929,
        "Silent era — simple black silhouette, large expressive white eyes, rubber-hose limbs",
        art_style="Black & white",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/thirty/Felix_the_cat.svg/240px-Felix_the_cat.svg.png"))
    felix.add_era(Era(1929, 1958,
        "Transitional sound era — design largely unchanged, early color experiments",
        art_style="Black & white / early color"))
    felix.add_era(Era(1958, 1994,
        "TV redesign — rounder, simplified for limited animation; introduced magic bag",
        art_style="Flat color TV cel"))
    felix.add_era(Era(1995, None,
        "Modern revival — retro-influenced styling, updated palette, more expressive",
        art_style="Mixed digital/traditional"))
    lib.add_cartoon(felix)

    # ── MICKEY MOUSE (1928) ───────────────────────────────────────────────
    mickey = Cartoon(
        name="Mickey Mouse",
        description=(
            "Disney's iconic mascot — an optimistic anthropomorphic mouse with a "
            "signature falsetto voice. Debuted in Steamboat Willie, the first "
            "synchronized-sound cartoon, and remains one of the most recognizable "
            "fictional characters in the world."
        ),
        character_type="Anthropomorphic animal — mouse",
        country_of_origin="USA",
        debut_year=1928,
    )
    mickey.original_studio = ProductionCompany("Walt Disney Productions", 1923)
    mickey.add_creator(Creator("Walt Disney", "Co-creator, original voice, executive producer", 1901, 1966))
    mickey.add_creator(Creator("Ub Iwerks", "Character designer & chief animator", 1901, 1971))

    mickey.add_series(Series("Mickey Mouse theatrical shorts", 1928, 1953,
        "Walt Disney Productions", "theatrical short", episode_count=130))
    mickey.add_series(Series("The Mickey Mouse Club", 1955, 1959,
        "Walt Disney Productions", "TV series"))
    mickey.add_series(Series("Mickey Mouse Works", 1999, 2000,
        "Walt Disney Television Animation", "TV series", episode_count=66))
    mickey.add_series(Series("Mickey Mouse (short-form series)", 2013, 2019,
        "Walt Disney Animation Studios", "streaming/TV short", episode_count=95))
    mickey.add_series(Series("Mickey Mouse Funhouse", 2021, None,
        "Walt Disney Television Animation", "streaming series"))

    mickey.add_ownership_record(OwnershipRecord(
        "Walt Disney Productions", 1928, 1986, "original creation"))
    mickey.add_ownership_record(OwnershipRecord(
        "The Walt Disney Company", 1986, None,
        "corporate restructuring", is_current_owner=True,
        notes="Note: Steamboat Willie (1928 film) entered US public domain Jan 1 2024; "
              "Mickey Mouse as a trademark remains fully protected"))

    mickey.add_era(Era(1928, 1935,
        "Steamboat Willie look — black & white, pie-cut eyes, rubber-hose limbs, no pupils",
        art_style="Black & white"))
    mickey.add_era(Era(1935, 1953,
        "Technicolor golden age — oval eyes with pupils, white gloves standardized, color palette locked in",
        art_style="Technicolor cel animation"))
    mickey.add_era(Era(1953, 1999,
        "Classic TV era — slightly simplified lines for cheaper production, same silhouette",
        art_style="Flat cel animation"))
    mickey.add_era(Era(1999, 2013,
        "Digital cleanup — HD-ready version of classic design, refined linework",
        art_style="Digital cel"))
    mickey.add_era(Era(2013, None,
        "Short-form redesign — expressive, rubbery, influenced by international animation styles",
        art_style="Stylized digital"))
    lib.add_cartoon(mickey)

    # ── BUGS BUNNY (1940) ─────────────────────────────────────────────────
    bugs = Cartoon(
        name="Bugs Bunny",
        description=(
            "A wisecracking grey rabbit who always outwits hunters, scientists, "
            "and even opera singers with cool confidence and Brooklyn wit. "
            "The quintessential Looney Tunes character and an enduring symbol "
            "of American animated comedy."
        ),
        character_type="Anthropomorphic animal — rabbit",
        country_of_origin="USA",
        debut_year=1940,
    )
    bugs.original_studio = ProductionCompany("Warner Bros. Cartoons", 1933, still_active=False)
    bugs.add_creator(Creator("Tex Avery", "Director of first recognizable appearance (A Wild Hare)", 1908, 1980))
    bugs.add_creator(Creator("Chuck Jones", "Refined the definitive personality and design", 1912, 2002))
    bugs.add_creator(Creator("Robert McKimson", "Co-developed the final on-model design", 1910, 1977))
    bugs.add_creator(Creator("Mel Blanc", "Original voice actor", 1908, 1989))

    bugs.add_series(Series("Looney Tunes / Merrie Melodies theatrical shorts", 1940, 1969,
        "Warner Bros. Cartoons", "theatrical short", episode_count=166))
    bugs.add_series(Series("The Bugs Bunny Show", 1960, 1975,
        "Warner Bros.", "TV series"))
    bugs.add_series(Series("The Bugs Bunny / Road Runner Movie", 1979, 1985,
        "Warner Bros.", "theatrical & TV compilation"))
    bugs.add_series(Series("Tiny Toon Adventures (mentor role)", 1990, 1992,
        "Amblin Entertainment / WB", "TV series", episode_count=98))
    bugs.add_series(Series("Space Jam", 1996, 1996,
        "Warner Bros. Pictures", "theatrical feature"))
    bugs.add_series(Series("Looney Tunes: Back in Action", 2003, 2003,
        "Warner Bros. Pictures", "theatrical feature"))
    bugs.add_series(Series("Looney Tunes Cartoons", 2019, None,
        "Warner Bros. Animation", "streaming short"))

    bugs.add_ownership_record(OwnershipRecord(
        "Warner Bros. Cartoons", 1940, 1969, "original creation"))
    bugs.add_ownership_record(OwnershipRecord(
        "Warner Bros. Inc.", 1969, 1990, "studio consolidation",
        notes="Warner Bros. Cartoons division closed 1969; IP rolled into parent company"))
    bugs.add_ownership_record(OwnershipRecord(
        "Time Warner / Warner Bros.", 1990, 2022, "corporate merger"))
    bugs.add_ownership_record(OwnershipRecord(
        "Warner Bros. Discovery", 2022, None,
        "corporate merger", is_current_owner=True))

    bugs.add_era(Era(1940, 1943,
        "Proto-Bugs — varied look across directors, design still being settled",
        art_style="Early Technicolor"))
    bugs.add_era(Era(1943, 1969,
        "Golden Age definitive design — grey fur, white gloves, confident posture, expressive face",
        art_style="Technicolor cel"))
    bugs.add_era(Era(1970, 1999,
        "Saturday-morning TV era — simplified, softer colors, slightly shorter ears",
        art_style="Limited TV animation"))
    bugs.add_era(Era(2000, 2018,
        "Digital era — cleaned linework, HD-ready version of classic model",
        art_style="Digital cel"))
    bugs.add_era(Era(2019, None,
        "Looney Tunes Cartoons revival — high-detail return to golden-age style in HD",
        art_style="HD digital classic"))
    lib.add_cartoon(bugs)

    # ── BETTY BOOP (1930) ─────────────────────────────────────────────────
    betty = Cartoon(
        name="Betty Boop",
        description=(
            "A saucy, big-eyed flapper who starred in provocative pre-Code cartoons. "
            "Originally based on a caricature of singer Helen Kane, Betty became "
            "one of the first and most iconic female cartoon characters."
        ),
        character_type="Human — stylized flapper",
        country_of_origin="USA",
        debut_year=1930,
    )
    betty.original_studio = ProductionCompany("Fleischer Studios", 1921, still_active=False)
    betty.add_creator(Creator("Max Fleischer", "Studio head & producer", 1883, 1972))
    betty.add_creator(Creator("Grim Natwick", "Character designer", 1890, 1990))

    betty.add_series(Series("Betty Boop theatrical shorts", 1930, 1939,
        "Fleischer Studios / Paramount Pictures", "theatrical short", episode_count=110))
    betty.add_series(Series("Betty Boop (TV reruns & specials)", 1971, 1985,
        "Various TV distributors", "TV broadcast"))
    betty.add_series(Series("Betty Boop's Hollywood Mystery (film)", 2025, None,
        "MUBI / StudioCanal", "theatrical feature",
        notes="Announced feature film revival"))

    betty.add_ownership_record(OwnershipRecord(
        "Fleischer Studios / Paramount Pictures", 1930, 1941, "original creation"))
    betty.add_ownership_record(OwnershipRecord(
        "Paramount Pictures", 1941, 1975,
        "studio takeover of Fleischer",
        notes="Paramount seized Fleischer Studios in 1941"))
    betty.add_ownership_record(OwnershipRecord(
        "King Features Syndicate", 1975, None,
        "license & trademark acquisition", is_current_owner=True))

    betty.add_era(Era(1930, 1932,
        "Original dog-eared design — partly based on a French poodle character",
        art_style="Black & white"))
    betty.add_era(Era(1932, 1934,
        "Pre-Code peak — short skirt, garter, more overtly suggestive styling",
        art_style="Black & white"))
    betty.add_era(Era(1934, 1939,
        "Post-Hays Code redesign — longer dress, more demure, less provocative",
        art_style="Black & white"))
    betty.add_era(Era(1985, None,
        "Modern revival — classic 1932 look restored, used in merchandise & media",
        art_style="Retro color recreation"))
    lib.add_cartoon(betty)

    # ── POPEYE (1929) ─────────────────────────────────────────────────────
    popeye = Cartoon(
        name="Popeye the Sailor",
        description=(
            "A squinting, spinach-powered sailor with a gravelly mumble and a heart "
            "of gold. Originated in the Thimble Theatre comic strip before becoming "
            "one of the most popular animated characters of the 1930s–1950s."
        ),
        character_type="Human — stylized sailor",
        country_of_origin="USA",
        debut_year=1929,
    )
    popeye.original_studio = ProductionCompany("Fleischer Studios", 1921, still_active=False)
    popeye.add_creator(Creator("E.C. Segar", "Comic strip creator", 1894, 1938))
    popeye.add_creator(Creator("Max Fleischer", "Animated adaptation producer", 1883, 1972))

    popeye.add_series(Series("Popeye theatrical shorts (Fleischer)", 1933, 1942,
        "Fleischer Studios / Paramount", "theatrical short", episode_count=109))
    popeye.add_series(Series("Popeye theatrical shorts (Famous Studios)", 1942, 1957,
        "Famous Studios / Paramount", "theatrical short", episode_count=105))
    popeye.add_series(Series("Popeye the Sailor (TV)", 1960, 1963,
        "King Features / various", "TV series", episode_count=220))
    popeye.add_series(Series("The All-New Popeye Hour", 1978, 1983,
        "Hanna-Barbera", "TV series"))
    popeye.add_series(Series("Popeye (feature film)", 1980, 1980,
        "Paramount / Disney co-production", "theatrical feature"))
    popeye.add_series(Series("Popeye's Voyage: The Quest for Pappy", 2004, 2004,
        "Paramount Home Entertainment", "direct-to-video"))

    popeye.add_ownership_record(OwnershipRecord(
        "King Features Syndicate", 1929, None,
        "original creation (comic strip syndication)", is_current_owner=True,
        notes="King Features has held rights since Segar's original strip; "
              "film/TV rights licensed separately"))

    popeye.add_era(Era(1929, 1933,
        "Comic strip origin — rougher, more grotesque design in newspaper print",
        art_style="Newspaper comic strip"))
    popeye.add_era(Era(1933, 1942,
        "Fleischer animated style — fluid, rubbery, rotoscoped details, expressive",
        art_style="Black & white / early Technicolor"))
    popeye.add_era(Era(1942, 1957,
        "Famous Studios era — brighter colors, slightly stiffer, more formulaic",
        art_style="Technicolor cel"))
    popeye.add_era(Era(1960, 1977,
        "TV limited animation — reduced detail, simplified for budget production",
        art_style="Flat TV cel"))
    popeye.add_era(Era(1978, None,
        "Modern interpretations — various studios, generally referencing classic look",
        art_style="Various"))
    lib.add_cartoon(popeye)

    return lib