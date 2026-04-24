"""
seed_data.py
Pre-built cartoon records for CartoonPal.
Each Era includes image_url and notes.
Each Cartoon includes wiki_url and origin_location.
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
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Felix_the_cat.svg/240px-Felix_the_cat.svg.png",
        notes="Created by Otto Messmer at Pat Sullivan Studio, New York City. Debuted in Feline Follies (1919)."))
    felix.add_era(Era(1929, 1958,
        "Transitional sound era — design largely unchanged, early color experiments",
        art_style="Black & white / early color",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Felix_the_cat.svg/240px-Felix_the_cat.svg.png",
        notes="Felix struggled to transition to sound cartoons after the Sullivan studio declined."))
    felix.add_era(Era(1958, 1994,
        "TV redesign — rounder, simplified for limited animation; introduced magic bag",
        art_style="Flat color TV cel",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Felix_the_cat.svg/240px-Felix_the_cat.svg.png",
        notes="Joe Oriolo redesigned Felix for TV. The magic bag of tricks became his signature prop."))
    felix.add_era(Era(1995, None,
        "Modern revival — retro-influenced styling, updated palette, more expressive",
        art_style="Mixed digital/traditional",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Felix_the_cat.svg/240px-Felix_the_cat.svg.png",
        notes="Film Roman produced The Twisted Tales of Felix the Cat for CBS Saturday mornings."))

    felix.wiki_url = "https://en.wikipedia.org/wiki/Felix_the_Cat"
    felix.origin_location = "New York City, USA — Pat Sullivan's Manhattan studio"
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
        notes="Steamboat Willie (1928) entered US public domain Jan 1 2024; "
              "Mickey Mouse as a trademark remains fully protected"))

    mickey.add_era(Era(1928, 1935,
        "Steamboat Willie look — black & white, pie-cut eyes, rubber-hose limbs, no pupils",
        art_style="Black & white",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Mickey_Mouse_-_color.svg/240px-Mickey_Mouse_-_color.svg.png",
        notes="Debuted November 18, 1928 at the Colony Theatre, New York City. First cartoon with synchronized sound."))
    mickey.add_era(Era(1935, 1953,
        "Technicolor golden age — oval eyes with pupils, white gloves standardized, color palette locked in",
        art_style="Technicolor cel animation",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Mickey_Mouse_-_color.svg/240px-Mickey_Mouse_-_color.svg.png",
        notes="The Band Concert (1935) was Mickey's first color cartoon, produced at Disney's Hyperion Ave studio, Los Angeles."))
    mickey.add_era(Era(1953, 1999,
        "Classic TV era — slightly simplified lines for cheaper production, same silhouette",
        art_style="Flat cel animation",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Mickey_Mouse_-_color.svg/240px-Mickey_Mouse_-_color.svg.png",
        notes="Mickey transitioned primarily to TV. The Mickey Mouse Club ran 1955–1959 on ABC."))
    mickey.add_era(Era(1999, 2013,
        "Digital cleanup — HD-ready version of classic design, refined linework",
        art_style="Digital cel",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Mickey_Mouse_-_color.svg/240px-Mickey_Mouse_-_color.svg.png",
        notes="Mickey Mouse Works and House of Mouse brought Mickey back to regular animation on Disney Channel."))
    mickey.add_era(Era(2013, None,
        "Short-form redesign — expressive, rubbery, influenced by international animation styles",
        art_style="Stylized digital",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Mickey_Mouse_-_color.svg/240px-Mickey_Mouse_-_color.svg.png",
        notes="New series directed by Paul Rudish. Won 3 Emmy Awards. Episodes set in worldwide locations."))

    mickey.wiki_url = "https://en.wikipedia.org/wiki/Mickey_Mouse"
    mickey.origin_location = "Los Angeles, California, USA — Walt Disney Studios, Hyperion Avenue"
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
        art_style="Early Technicolor",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Bugs_Bunny.svg/240px-Bugs_Bunny.svg.png",
        notes="First appearance in A Wild Hare (1940), directed by Tex Avery at Warner Bros. Termite Terrace, Burbank CA."))
    bugs.add_era(Era(1943, 1969,
        "Golden Age definitive design — grey fur, white gloves, confident posture, expressive face",
        art_style="Technicolor cel",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Bugs_Bunny.svg/240px-Bugs_Bunny.svg.png",
        notes="Chuck Jones and McKimson locked in the final model at Termite Terrace. 'What's Up Doc?' became his catchphrase."))
    bugs.add_era(Era(1970, 1999,
        "Saturday-morning TV era — simplified, softer colors, slightly shorter ears",
        art_style="Limited TV animation",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Bugs_Bunny.svg/240px-Bugs_Bunny.svg.png",
        notes="Production moved to TV after Termite Terrace closed. Bugs remained America's most popular cartoon character."))
    bugs.add_era(Era(2000, 2018,
        "Digital era — cleaned linework, HD-ready version of classic model",
        art_style="Digital cel",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Bugs_Bunny.svg/240px-Bugs_Bunny.svg.png",
        notes="Space Jam (1996) introduced Bugs to a new generation. Looney Tunes: Back in Action followed in 2003."))
    bugs.add_era(Era(2019, None,
        "Looney Tunes Cartoons revival — high-detail return to golden-age style in HD",
        art_style="HD digital classic",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Bugs_Bunny.svg/240px-Bugs_Bunny.svg.png",
        notes="HBO Max series returned to hand-drawn style, praised as most faithful recreation of golden age look."))

    bugs.wiki_url = "https://en.wikipedia.org/wiki/Bugs_Bunny"
    bugs.origin_location = "Burbank, California, USA — Warner Bros. Termite Terrace animation studio"
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
        "MUBI / StudioCanal", "theatrical feature"))

    betty.add_ownership_record(OwnershipRecord(
        "Fleischer Studios / Paramount Pictures", 1930, 1941, "original creation"))
    betty.add_ownership_record(OwnershipRecord(
        "Paramount Pictures", 1941, 1975, "studio takeover of Fleischer",
        notes="Paramount seized Fleischer Studios in 1941"))
    betty.add_ownership_record(OwnershipRecord(
        "King Features Syndicate", 1975, None,
        "license & trademark acquisition", is_current_owner=True))

    betty.add_era(Era(1930, 1932,
        "Original dog-eared design — partly based on a French poodle character",
        art_style="Black & white",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Betty_Boop_1930s.png/200px-Betty_Boop_1930s.png",
        notes="Betty debuted in Dizzy Dishes (1930) from Fleischer Studios at 1600 Broadway, Manhattan."))
    betty.add_era(Era(1932, 1934,
        "Pre-Code peak — short skirt, garter, more overtly suggestive styling",
        art_style="Black & white",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Betty_Boop_1930s.png/200px-Betty_Boop_1930s.png",
        notes="Peak creative period. Snow-White (1933) and Minnie the Moocher (1932) featured Cab Calloway."))
    betty.add_era(Era(1934, 1939,
        "Post-Hays Code redesign — longer dress, more demure, less provocative",
        art_style="Black & white",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Betty_Boop_1930s.png/200px-Betty_Boop_1930s.png",
        notes="The Hays Code enforcement in 1934 forced a redesign. Popularity declined and series ended in 1939."))
    betty.add_era(Era(1985, None,
        "Modern revival — classic 1932 look restored, used in merchandise & media",
        art_style="Retro color recreation",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Betty_Boop_1930s.png/200px-Betty_Boop_1930s.png",
        notes="King Features licensed Betty for a massive merchandise boom in the 1980s–90s."))

    betty.wiki_url = "https://en.wikipedia.org/wiki/Betty_Boop"
    betty.origin_location = "New York City, USA — Fleischer Studios, 1600 Broadway, Manhattan"
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
        notes="King Features has held rights since Segar's original strip"))

    popeye.add_era(Era(1929, 1933,
        "Comic strip origin — rougher, more grotesque design in newspaper print",
        art_style="Newspaper comic strip",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Popeye_-_Thimble_Theatre_strip.png/240px-Popeye_-_Thimble_Theatre_strip.png",
        notes="Debuted January 17, 1929 in E.C. Segar's Thimble Theatre strip, syndicated by King Features, New York."))
    popeye.add_era(Era(1933, 1942,
        "Fleischer animated style — fluid, rubbery, rotoscoped details, expressive",
        art_style="Black & white / early Technicolor",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Popeye_the_Sailor_Man.svg/240px-Popeye_the_Sailor_Man.svg.png",
        notes="Fleischer Studios in Miami, FL produced the most beloved Popeye cartoons. I Yam What I Yam (1933) was first."))
    popeye.add_era(Era(1942, 1957,
        "Famous Studios era — brighter colors, slightly stiffer, more formulaic",
        art_style="Technicolor cel",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Popeye_the_Sailor_Man.svg/240px-Popeye_the_Sailor_Man.svg.png",
        notes="After Paramount seized Fleischer, Famous Studios continued production in New York."))
    popeye.add_era(Era(1960, 1977,
        "TV limited animation — reduced detail, simplified for budget production",
        art_style="Flat TV cel",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Popeye_the_Sailor_Man.svg/240px-Popeye_the_Sailor_Man.svg.png",
        notes="King Features produced new TV cartoons. Hanna-Barbera later revived the series in 1978."))
    popeye.add_era(Era(1978, None,
        "Modern interpretations — various studios, generally referencing classic look",
        art_style="Various",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Popeye_the_Sailor_Man.svg/240px-Popeye_the_Sailor_Man.svg.png",
        notes="Robin Williams played Popeye in the 1980 live-action film directed by Robert Altman."))

    popeye.wiki_url = "https://en.wikipedia.org/wiki/Popeye"
    popeye.origin_location = "New York City, USA — King Features Syndicate, 235 E 45th St, Manhattan"
    lib.add_cartoon(popeye)

    return lib