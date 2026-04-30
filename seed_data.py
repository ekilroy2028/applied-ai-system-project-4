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
from characters.anime_characters import add_anime_characters
from characters.hanna_barbera_characters import add_hanna_barbera_characters
from characters.disney_characters import add_disney_characters
from characters.mgm_characters import add_mgm_characters
from characters.schoolhouse_rock import add_schoolhouse_rock
from characters.dic_characters import add_dic_characters
from characters.filmation_characters import add_filmation_characters
from characters.wb_characters import add_wb_characters
from characters.dc_characters import add_dc_characters
from characters.marvel_characters import add_marvel_characters
from characters.sanrio_characters import add_sanrio_characters
from characters.nickelodeon_characters import add_nickelodeon_characters
from characters.hasbro_characters import add_hasbro_characters
from characters.cartoon_network_characters import add_cartoon_network_characters


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


    # TOM AND JERRY (1940)
    tomjerry = Cartoon(
        name="Tom and Jerry",
        description=(
            "A cat-and-mouse duo locked in an eternal slapstick rivalry. Tom, a "
            "house cat, perpetually chases Jerry, a clever mouse, in increasingly "
            "elaborate gags. Won seven Academy Awards and remains one of the most "
            "recognized cartoons worldwide."
        ),
        character_type="Anthropomorphic animals — cat and mouse",
        country_of_origin="USA",
        debut_year=1940,
    )
    tomjerry.original_studio = ProductionCompany("MGM Cartoons", 1937, still_active=False)
    tomjerry.add_creator(Creator("William Hanna", "Co-creator, director & producer", 1910, 2001))
    tomjerry.add_creator(Creator("Joseph Barbera", "Co-creator, animator & story artist", 1911, 2006))
    tomjerry.add_series(Series("Tom and Jerry theatrical shorts (MGM)", 1940, 1958, "MGM Cartoons", "theatrical short", episode_count=114))
    tomjerry.add_series(Series("Tom and Jerry Gene Deitch era", 1961, 1962, "Rembrandt Films", "theatrical short", episode_count=13))
    tomjerry.add_series(Series("Tom and Jerry Chuck Jones era", 1963, 1967, "Sib Tower 12 / MGM", "theatrical short", episode_count=34))
    tomjerry.add_series(Series("The Tom and Jerry Show CBS", 1975, 1977, "Hanna-Barbera", "TV series"))
    tomjerry.add_series(Series("Tom and Jerry Kids", 1990, 1994, "Turner / Hanna-Barbera", "TV series", episode_count=65))
    tomjerry.add_series(Series("The Tom and Jerry Show Cartoon Network", 2014, 2021, "Warner Bros. Animation", "TV series", episode_count=201))
    tomjerry.add_series(Series("Tom and Jerry feature film", 2021, 2021, "Warner Bros. Pictures", "theatrical feature"))
    tomjerry.add_ownership_record(OwnershipRecord("Metro-Goldwyn-Mayer (MGM)", 1940, 1986, "original creation"))
    tomjerry.add_ownership_record(OwnershipRecord("Turner Entertainment Co.", 1986, 1996, "purchase of MGM library"))
    tomjerry.add_ownership_record(OwnershipRecord("Warner Bros. / Time Warner", 1996, 2022, "Turner-Time Warner merger"))
    tomjerry.add_ownership_record(OwnershipRecord("Warner Bros. Discovery", 2022, None, "corporate merger", is_current_owner=True))
    tomjerry.add_era(Era(1940, 1942, "Early MGM style — rounder less refined designs; Tom more feral-looking", art_style="Technicolor cel", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Tom_and_Jerry_logo.svg/240px-Tom_and_Jerry_logo.svg.png", notes="Debuted in Puss Gets the Boot (1940) at MGM Studios, Culver City, CA."))
    tomjerry.add_era(Era(1943, 1958, "Golden Age — sleeker Tom, rounder Jerry, lush MGM backgrounds", art_style="Technicolor cel", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Tom_and_Jerry_logo.svg/240px-Tom_and_Jerry_logo.svg.png", notes="Peak era. Won 7 Academy Awards. Produced at MGM Culver City."))
    tomjerry.add_era(Era(1961, 1962, "Gene Deitch era — angular limited animation, stark Eastern European look", art_style="Limited animation", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Tom_and_Jerry_logo.svg/240px-Tom_and_Jerry_logo.svg.png", notes="Filmed in Prague by Gene Deitch for Rembrandt Films. Very low budget."))
    tomjerry.add_era(Era(1963, 1967, "Chuck Jones era — sharper expressions, different proportions", art_style="Technicolor cel", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Tom_and_Jerry_logo.svg/240px-Tom_and_Jerry_logo.svg.png", notes="Jones imposed Looney Tunes sensibility on the characters."))
    tomjerry.add_era(Era(1975, 2013, "TV era — simplified less violent softer colors", art_style="Limited TV animation", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Tom_and_Jerry_logo.svg/240px-Tom_and_Jerry_logo.svg.png", notes="CBS required reduced violence. Tom and Jerry briefly depicted as friends."))
    tomjerry.add_era(Era(2014, None, "Modern HD revival — classic designs restored smooth digital animation", art_style="HD digital", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Tom_and_Jerry_logo.svg/240px-Tom_and_Jerry_logo.svg.png", notes="Cartoon Network series and 2021 hybrid feature returned to classic slapstick."))
    tomjerry.wiki_url = "https://en.wikipedia.org/wiki/Tom_and_Jerry"
    tomjerry.origin_location = "Culver City, California, USA — MGM Cartoon Studio"
    lib.add_cartoon(tomjerry)

    # WOODY WOODPECKER (1940)
    woody = Cartoon(
        name="Woody Woodpecker",
        description=(
            "A hyperactive, mischievous red-crested woodpecker famous for his "
            "distinctive machine-gun laugh and anarchic personality. Created at "
            "Walter Lantz Productions, Woody became Universal's most successful "
            "animated character and one of the most recognized cartoon birds in history."
        ),
        character_type="Anthropomorphic animal — woodpecker",
        country_of_origin="USA",
        debut_year=1940,
    )
    woody.original_studio = ProductionCompany("Walter Lantz Productions", 1929, still_active=False)
    woody.add_creator(Creator("Walter Lantz", "Creator & producer", 1899, 1994))
    woody.add_creator(Creator("Ben Hardaway", "Original story concept", 1895, 1957))
    woody.add_creator(Creator("Mel Blanc", "Original voice actor 1940-1941", 1908, 1989))
    woody.add_creator(Creator("Grace Stafford", "Voice actress 1950-1972", 1900, 1992))
    woody.add_series(Series("Woody Woodpecker theatrical shorts", 1940, 1972, "Walter Lantz Productions / Universal", "theatrical short", episode_count=195))
    woody.add_series(Series("The Woody Woodpecker Show ABC", 1957, 1966, "Walter Lantz Productions", "TV series"))
    woody.add_series(Series("The New Woody Woodpecker Show", 1999, 2002, "Universal Cartoon Studios", "TV series", episode_count=52))
    woody.add_series(Series("Woody Woodpecker Brazilian film", 2017, 2017, "Universal 1440 Entertainment", "theatrical feature"))
    woody.add_series(Series("Woody Woodpecker Goes to Camp", 2024, None, "Universal Pictures / Netflix", "streaming feature"))
    woody.add_ownership_record(OwnershipRecord("Walter Lantz Productions / Universal Pictures", 1940, 1990, "original creation"))
    woody.add_ownership_record(OwnershipRecord("Universal Pictures MCA", 1990, 2004, "acquisition of Walter Lantz Productions"))
    woody.add_ownership_record(OwnershipRecord("NBCUniversal", 2004, 2022, "corporate restructuring"))
    woody.add_ownership_record(OwnershipRecord("Universal Pictures / Comcast NBCUniversal", 2022, None, "current holding", is_current_owner=True))
    woody.add_era(Era(1940, 1942, "Original design — wilder more grotesque; tall angular beak manic eyes", art_style="Technicolor cel", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Woody_Woodpecker.svg/240px-Woody_Woodpecker.svg.png", notes="Debuted in Knock Knock (1940) at Walter Lantz studio, Burbank, CA."))
    woody.add_era(Era(1942, 1950, "Transitional — slightly rounder more expressive red crest more pronounced", art_style="Technicolor cel", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Woody_Woodpecker.svg/240px-Woody_Woodpecker.svg.png", notes="Mel Blanc left for Warner Bros. Grace Stafford eventually took over the voice."))
    woody.add_era(Era(1950, 1972, "Classic definitive design — rounder head blue body red crest friendlier face", art_style="Technicolor cel", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Woody_Woodpecker.svg/240px-Woody_Woodpecker.svg.png", notes="Most recognized design era. Grace Stafford became the permanent voice."))
    woody.add_era(Era(1972, 1999, "TV and licensing era — classic design maintained primarily merchandising", art_style="Flat color / limited animation", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Woody_Woodpecker.svg/240px-Woody_Woodpecker.svg.png", notes="Walter Lantz retired 1972. Woody remained active in licensing and TV reruns."))
    woody.add_era(Era(1999, 2016, "Modernized design — smoother lines brighter colors updated for digital", art_style="Digital cel", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Woody_Woodpecker.svg/240px-Woody_Woodpecker.svg.png", notes="The New Woody Woodpecker Show (1999) updated the character for Fox Kids."))
    woody.add_era(Era(2017, None, "CGI and hybrid era — fully rendered 3D model based on classic design", art_style="CGI / hybrid live-action", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Woody_Woodpecker.svg/240px-Woody_Woodpecker.svg.png", notes="2017 Brazilian feature and 2024 Netflix film used CGI Woody with live-action."))
    woody.wiki_url = "https://en.wikipedia.org/wiki/Woody_Woodpecker"
    woody.origin_location = "Burbank, California, USA — Walter Lantz Productions studio"
    lib.add_cartoon(woody)


    # CASPER THE FRIENDLY GHOST (1945)
    casper = Cartoon(
        name="Casper the Friendly Ghost",
        description=(
            "A kind-hearted young ghost who only wants to make friends, despite "
            "frightening everyone he meets. One of the most beloved animated "
            "characters of the 1940s-1950s, known for his gentle nature in stark "
            "contrast to the typical scary ghost archetype."
        ),
        character_type="Supernatural — friendly ghost",
        country_of_origin="USA",
        debut_year=1945,
    )
    casper.original_studio = ProductionCompany("Famous Studios / Paramount Pictures", 1942, still_active=False)
    casper.add_creator(Creator("Seymour Reit", "Original children's book author", 1918, 2001))
    casper.add_creator(Creator("Joe Oriolo", "Adapted for animation", 1913, 1985))
    casper.add_series(Series("Casper theatrical shorts", 1945, 1959, "Famous Studios / Paramount", "theatrical short", episode_count=62))
    casper.add_series(Series("The New Casper Cartoon Show", 1963, 1969, "Harvey Films / ABC", "TV series", episode_count=260))
    casper.add_series(Series("Casper and the Angels", 1979, 1980, "Hanna-Barbera", "TV series", episode_count=26))
    casper.add_series(Series("Casper live-action feature film", 1995, 1995, "Universal Pictures / Amblin", "theatrical feature"))
    casper.add_series(Series("Caspers Scare School", 2006, 2009, "Classic Media", "TV series"))
    casper.add_ownership_record(OwnershipRecord("Paramount Pictures / Famous Studios", 1945, 1960, "original creation"))
    casper.add_ownership_record(OwnershipRecord("Harvey Comics / Harvey Entertainment", 1960, 1993, "purchase from Paramount"))
    casper.add_ownership_record(OwnershipRecord("Classic Media", 1993, 2012, "corporate restructuring"))
    casper.add_ownership_record(OwnershipRecord("DreamWorks Classics / NBCUniversal", 2012, None, "acquisition", is_current_owner=True, notes="NBCUniversal acquired DreamWorks Animation in 2016"))
    casper.add_era(Era(1945, 1959, "Original theatrical — round white ghost, simple black eyes, gentle expression", art_style="Black & white / early color", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Casper_the_Friendly_Ghost.png/200px-Casper_the_Friendly_Ghost.png", notes="Debuted in The Friendly Ghost (1945), Famous Studios, 1600 Broadway, New York City."))
    casper.add_era(Era(1963, 1994, "Harvey Comics TV era — rounder, brighter whites, more expressive face", art_style="Flat color TV cel", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Casper_the_Friendly_Ghost.png/200px-Casper_the_Friendly_Ghost.png", notes="Harvey Entertainment built a massive licensing empire around Casper during this period."))
    casper.add_era(Era(1995, 2005, "CGI movie era — translucent 3D ghost, more detailed rendering", art_style="CGI", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Casper_the_Friendly_Ghost.png/200px-Casper_the_Friendly_Ghost.png", notes="1995 Universal/Amblin film was among the first major CGI characters in a live-action feature."))
    casper.add_era(Era(2006, None, "Modern era — classic 2D look restored for most media", art_style="Mixed", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Casper_the_Friendly_Ghost.png/200px-Casper_the_Friendly_Ghost.png", notes="NBCUniversal maintains the property through DreamWorks Classics."))
    casper.wiki_url = "https://en.wikipedia.org/wiki/Casper_the_Friendly_Ghost"
    casper.origin_location = "New York City, USA — Famous Studios, 1600 Broadway, Manhattan"
    lib.add_cartoon(casper)

    # SCOOBY-DOO (Friday March 20 interpreted as the show that debuted that era — adding Scooby-Doo)
    scooby = Cartoon(
        name="Scooby-Doo",
        description=(
            "A cowardly but lovable Great Dane who solves mysteries alongside "
            "Fred, Daphne, Velma, and Shaggy. Known for unmasking fake monsters "
            "and the catchphrase Scooby-Dooby-Doo. One of the longest-running "
            "animated franchises in television history, spanning over five decades."
        ),
        character_type="Anthropomorphic animal — Great Dane dog",
        country_of_origin="USA",
        debut_year=1969,
    )
    scooby.original_studio = ProductionCompany("Hanna-Barbera Productions", 1957, still_active=False)
    scooby.add_creator(Creator("William Hanna", "Co-creator & executive producer", 1910, 2001))
    scooby.add_creator(Creator("Joseph Barbera", "Co-creator & executive producer", 1911, 2006))
    scooby.add_creator(Creator("Ken Spears", "Series developer & writer", 1938, 2020))
    scooby.add_creator(Creator("Joe Ruby", "Series developer & writer", 1933, 2020))
    scooby.add_series(Series("Scooby-Doo Where Are You!", 1969, 1970, "Hanna-Barbera / CBS", "TV series", episode_count=25))
    scooby.add_series(Series("The New Scooby-Doo Movies", 1972, 1973, "Hanna-Barbera / CBS", "TV series", episode_count=24))
    scooby.add_series(Series("Scooby-Doo and Scrappy-Doo", 1979, 1983, "Hanna-Barbera / ABC", "TV series", episode_count=62))
    scooby.add_series(Series("A Pup Named Scooby-Doo", 1988, 1991, "Hanna-Barbera / ABC", "TV series", episode_count=30))
    scooby.add_series(Series("Scooby-Doo Mystery Incorporated", 2010, 2013, "Warner Bros. Animation", "TV series", episode_count=52))
    scooby.add_series(Series("Scoob! feature film", 2020, 2020, "Warner Bros. Pictures", "theatrical feature"))
    scooby.add_ownership_record(OwnershipRecord("Hanna-Barbera Productions", 1969, 1989, "original creation"))
    scooby.add_ownership_record(OwnershipRecord("Turner Broadcasting", 1989, 1996, "acquisition of Hanna-Barbera"))
    scooby.add_ownership_record(OwnershipRecord("Warner Bros. / Time Warner", 1996, 2022, "Turner-Time Warner merger"))
    scooby.add_ownership_record(OwnershipRecord("Warner Bros. Discovery", 2022, None, "corporate merger", is_current_owner=True))
    scooby.add_era(Era(1969, 1978, "Original — classic lanky Great Dane, brown with black spots, green collar", art_style="Flat color TV cel", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Scooby-doo.png/200px-Scooby-doo.png", notes="Debuted September 13 1969 on CBS. Created at Hanna-Barbera Studios, Hollywood, CA."))
    scooby.add_era(Era(1979, 1987, "Scrappy-Doo era — Scooby unchanged; tiny nephew Scrappy-Doo added to boost ratings", art_style="Flat color TV cel", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Scooby-doo.png/200px-Scooby-doo.png", notes="Scrappy dramatically boosted ratings but is now widely considered the low point of the franchise."))
    scooby.add_era(Era(1988, 2001, "Refined TV era — cleaner lines, updated palette, more consistent model", art_style="Improved TV cel", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Scooby-doo.png/200px-Scooby-doo.png", notes="Warner Bros. took over production. Pup Named Scooby-Doo reimagined the gang as children."))
    scooby.add_era(Era(2002, 2018, "Modern Warner era — HD-ready designs, various art styles per series", art_style="Digital cel", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Scooby-doo.png/200px-Scooby-doo.png", notes="Mystery Incorporated (2010) is critically acclaimed as the most sophisticated Scooby series."))
    scooby.add_era(Era(2019, None, "Streaming era — CGI for Scoob! film; 2D retained for TV productions", art_style="Mixed CGI and digital", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Scooby-doo.png/200px-Scooby-doo.png", notes="Scoob! (2020) used full CGI. HBO Max and Cartoon Network continue 2D productions."))
    scooby.wiki_url = "https://en.wikipedia.org/wiki/Scooby-Doo"
    scooby.origin_location = "Hollywood, California, USA — Hanna-Barbera Productions studio"
    lib.add_cartoon(scooby)

    # SPEED BUGGY (1973)
    speedbuggy = Cartoon(
        name="Speed Buggy",
        description=(
            "A lovable anthropomorphic dune buggy named Speedy who goes on "
            "adventures and solves mysteries with teenage companions Tinker, Mark, "
            "and Debbie. A Hanna-Barbera spin on the Scooby-Doo formula, replacing "
            "the dog with a talking car known for his sputtering speech and "
            "good-natured personality."
        ),
        character_type="Anthropomorphic vehicle — dune buggy",
        country_of_origin="USA",
        debut_year=1973,
    )
    speedbuggy.original_studio = ProductionCompany("Hanna-Barbera Productions", 1957, still_active=False)
    speedbuggy.add_creator(Creator("William Hanna", "Executive producer", 1910, 2001))
    speedbuggy.add_creator(Creator("Joseph Barbera", "Executive producer", 1911, 2006))
    speedbuggy.add_series(Series("Speed Buggy CBS", 1973, 1974, "Hanna-Barbera / CBS", "TV series", episode_count=16))
    speedbuggy.add_series(Series("Speed Buggy reruns", 1975, 1984, "Hanna-Barbera / various", "TV reruns"))
    speedbuggy.add_series(Series("Speed Buggy crossover appearances", 2015, None, "Warner Bros. Animation", "cameo appearances"))
    speedbuggy.add_ownership_record(OwnershipRecord("Hanna-Barbera Productions", 1973, 1989, "original creation"))
    speedbuggy.add_ownership_record(OwnershipRecord("Turner Broadcasting", 1989, 1996, "acquisition of Hanna-Barbera"))
    speedbuggy.add_ownership_record(OwnershipRecord("Warner Bros. / Time Warner", 1996, 2022, "Turner-Time Warner merger"))
    speedbuggy.add_ownership_record(OwnershipRecord("Warner Bros. Discovery", 2022, None, "corporate merger", is_current_owner=True))
    speedbuggy.add_era(Era(1973, 1984, "Original — orange dune buggy with large eyes in windshield and buck-teeth grille", art_style="Flat color TV cel", image_url="https://upload.wikimedia.org/wikipedia/en/thumb/2/2f/SpeedBuggy.jpg/200px-SpeedBuggy.jpg", notes="Debuted September 8 1973 on CBS. Produced at Hanna-Barbera Studios, Hollywood, CA."))
    speedbuggy.add_era(Era(2015, None, "Modern cameo era — classic design retained in HD for crossover appearances", art_style="Digital cel", image_url="https://upload.wikimedia.org/wikipedia/en/thumb/2/2f/SpeedBuggy.jpg/200px-SpeedBuggy.jpg", notes="Appeared in Scooby-Doo and Guess Who and other Warner Bros. crossover specials."))
    speedbuggy.wiki_url = "https://en.wikipedia.org/wiki/Speed_Buggy"
    speedbuggy.origin_location = "Hollywood, California, USA — Hanna-Barbera Productions studio"
    lib.add_cartoon(speedbuggy)

    # SPEED RACER (1966)
    speedracer = Cartoon(
        name="Speed Racer",
        description=(
            "A young race car driver who competes internationally in his "
            "technologically advanced Mach 5 alongside his family. Originally "
            "a Japanese manga and anime that became a cultural phenomenon in "
            "the United States, introducing millions of Western viewers to "
            "Japanese animation for the first time."
        ),
        character_type="Human — race car driver",
        country_of_origin="Japan",
        debut_year=1966,
    )
    speedracer.original_studio = ProductionCompany("Tatsunoko Production", 1962)
    speedracer.add_creator(Creator("Tatsuo Yoshida", "Manga creator & anime producer", 1935, 1977))
    speedracer.add_series(Series("Mach GoGoGo Japan original", 1966, 1968, "Tatsunoko Production / Fuji TV", "TV series", episode_count=52, notes="Original Japanese title. Speed Racer is Go Mifune in Japan."))
    speedracer.add_series(Series("Speed Racer US broadcast", 1967, 1968, "Trans-Lux / Tatsunoko", "TV series", episode_count=52, notes="English dubbed version distributed by Trans-Lux for American audiences."))
    speedracer.add_series(Series("Speed Racer New Adventures", 1993, 1993, "Speed Racer Enterprises", "TV series", episode_count=13))
    speedracer.add_series(Series("Speed Racer The Next Generation", 2008, 2009, "Lionsgate / Nicktoons", "TV series", episode_count=26))
    speedracer.add_series(Series("Speed Racer live-action film", 2008, 2008, "Warner Bros. Pictures / Village Roadshow", "theatrical feature", notes="Directed by the Wachowskis. Visually ambitious but underperformed at box office."))
    speedracer.add_ownership_record(OwnershipRecord("Tatsunoko Production / Tatsuo Yoshida estate", 1966, 1993, "original creation", notes="Tatsunoko holds original Japanese rights permanently"))
    speedracer.add_ownership_record(OwnershipRecord("Speed Racer Enterprises (Peter Fernandez estate)", 1993, 2011, "US licensing rights", notes="Peter Fernandez who dubbed the US version acquired US rights"))
    speedracer.add_ownership_record(OwnershipRecord("Tatsunoko Production (Japan) / Various licensees (US)", 2011, None, "reversion of rights", is_current_owner=True, notes="Rights situation is complex — Tatsunoko holds master rights; US licensees vary by media"))
    speedracer.add_era(Era(1966, 1968, "Original anime design — clean lined Japanese animation style, distinctive helmet and scarf", art_style="Japanese cel animation", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Speed_racer_GoGoGo.png/200px-Speed_racer_GoGoGo.png", notes="Produced by Tatsunoko Production, Tokyo. US version dubbed by Peter Fernandez who voiced both Speed and Racer X."))
    speedracer.add_era(Era(1993, 2007, "Revival era — updated line art closer to original but cleaned up for modern TV", art_style="Updated cel animation", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Speed_racer_GoGoGo.png/200px-Speed_racer_GoGoGo.png", notes="New series attempted to modernize the franchise with limited success."))
    speedracer.add_era(Era(2008, None, "Modern era — CGI film and animated series used 3D and updated 2D styles", art_style="CGI / digital", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Speed_racer_GoGoGo.png/200px-Speed_racer_GoGoGo.png", notes="Wachowski film used hyper-stylized CGI racing sequences. Next Generation used flash-style animation."))
    speedracer.wiki_url = "https://en.wikipedia.org/wiki/Speed_Racer"
    speedracer.origin_location = "Tokyo, Japan — Tatsunoko Production studio"
    lib.add_cartoon(speedracer)

    # VOLTRON (1984)
    voltron = Cartoon(
        name="Voltron",
        description=(
            "Five heroic space explorers pilot giant robot lions that combine "
            "to form Voltron, Defender of the Universe — a massive robot warrior "
            "who battles the evil King Zarkon. Adapted from the Japanese anime "
            "Beast King GoLion, Voltron became one of the defining American "
            "cartoons of the 1980s and pioneered the combining-robot genre "
            "for Western audiences."
        ),
        character_type="Science fiction — combining robot / mecha",
        country_of_origin="Japan / USA",
        debut_year=1984,
    )
    voltron.original_studio = ProductionCompany("Toei Animation", 1948)
    voltron.add_creator(Creator("Tadao Nagahama", "Original GoLion director", 1932, 1980))
    voltron.add_creator(Creator("Peter Keefe", "US adaptation producer", 0, 0))
    voltron.add_creator(Creator("World Events Productions", "US adaptation company", 0, 0))
    voltron.add_series(Series("Voltron Defender of the Universe", 1984, 1985, "World Events Productions / Toei", "TV series", episode_count=52, notes="Adapted and edited from Japanese anime Beast King GoLion (1981)."))
    voltron.add_series(Series("Voltron The Third Dimension", 1998, 2000, "World Events Productions", "TV series", episode_count=26))
    voltron.add_series(Series("Voltron Force", 2011, 2012, "World Events Productions / Nickelodeon", "TV series", episode_count=26))
    voltron.add_series(Series("Voltron Legendary Defender", 2016, 2018, "DreamWorks Animation / Netflix", "streaming series", episode_count=78, notes="Critically acclaimed Netflix reboot. Widely considered the best modern Voltron adaptation."))
    voltron.add_ownership_record(OwnershipRecord("Toei Animation / Bandai (Japan)", 1981, None, "original creation of GoLion", notes="Toei holds original Japanese rights to Beast King GoLion permanently"))
    voltron.add_ownership_record(OwnershipRecord("World Events Productions (US rights)", 1984, 2012, "US adaptation license & trademark"))
    voltron.add_ownership_record(OwnershipRecord("Classic Media / DreamWorks Classics", 2012, None, "acquisition of WEP library", is_current_owner=True, notes="NBCUniversal acquired DreamWorks Animation including Classic Media in 2016"))
    voltron.add_era(Era(1984, 1997, "Classic 1980s design — five lion robots in primary colors combining into armored humanoid warrior", art_style="Japanese cel animation adapted for US TV", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Voltron_Legendary_Defender.png/200px-Voltron_Legendary_Defender.png", notes="Aired September 10 1984. World Events Productions edited GoLion footage for American broadcast, removing graphic violence."))
    voltron.add_era(Era(1998, 2015, "CGI transition era — 3D rendered Voltron replacing traditional animation", art_style="Early CGI", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Voltron_Legendary_Defender.png/200px-Voltron_Legendary_Defender.png", notes="Third Dimension (1998) used early CGI. Voltron Force (2011) blended 2D and 3D styles."))
    voltron.add_era(Era(2016, None, "Legendary Defender era — sleek modern redesign with anime-influenced fluid action", art_style="Modern digital animation", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Voltron_Legendary_Defender.png/200px-Voltron_Legendary_Defender.png", notes="DreamWorks / Netflix series praised for storytelling, diverse cast, and updated designs. Won Annie Awards."))
    voltron.wiki_url = "https://en.wikipedia.org/wiki/Voltron"
    voltron.origin_location = "Tokyo, Japan (original) — World Events Productions, St. Louis, Missouri, USA (US adaptation)"
    lib.add_cartoon(voltron)

    # YOGI BEAR (1958)
    yogi = Cartoon(
        name="Yogi Bear",
        description=(
            "A clever, picnic-basket-stealing bear who lives in Jellystone Park "
            "and outwits the long-suffering Ranger Smith with the help of his "
            "smaller sidekick Boo-Boo. Famous for his catchphrase I am smarter "
            "than the average bear and his pork-pie hat and collar. One of the "
            "first breakout stars of the Hanna-Barbera television animation era."
        ),
        character_type="Anthropomorphic animal — bear",
        country_of_origin="USA",
        debut_year=1958,
    )
    yogi.original_studio = ProductionCompany("Hanna-Barbera Productions", 1957, still_active=False)
    yogi.add_creator(Creator("William Hanna", "Co-creator & director", 1910, 2001))
    yogi.add_creator(Creator("Joseph Barbera", "Co-creator & story artist", 1911, 2006))
    yogi.add_series(Series("The Huckleberry Hound Show (Yogi segments)", 1958, 1961, "Hanna-Barbera / Syndicated", "TV series"))
    yogi.add_series(Series("The Yogi Bear Show", 1961, 1962, "Hanna-Barbera / Syndicated", "TV series", episode_count=33))
    yogi.add_series(Series("Yogi Bear feature film", 1964, 1964, "Hanna-Barbera / Columbia", "theatrical feature"))
    yogi.add_series(Series("Laff-a-Lympics", 1977, 1979, "Hanna-Barbera / ABC", "TV series", episode_count=48))
    yogi.add_series(Series("Yogi's Treasure Hunt", 1985, 1988, "Hanna-Barbera / TBS", "TV series", episode_count=33))
    yogi.add_series(Series("Yogi Bear live-action film", 2010, 2010, "Warner Bros. Pictures", "theatrical feature"))
    yogi.add_ownership_record(OwnershipRecord("Hanna-Barbera Productions", 1958, 1989, "original creation"))
    yogi.add_ownership_record(OwnershipRecord("Turner Broadcasting", 1989, 1996, "acquisition of Hanna-Barbera"))
    yogi.add_ownership_record(OwnershipRecord("Warner Bros. / Time Warner", 1996, 2022, "Turner-Time Warner merger"))
    yogi.add_ownership_record(OwnershipRecord("Warner Bros. Discovery", 2022, None, "corporate merger", is_current_owner=True))
    yogi.add_era(Era(1958, 1972, "Original design — green hat and tie collar brown fur confident grin", art_style="Flat color TV cel", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Yogi_Bear.png/200px-Yogi_Bear.png", notes="Debuted October 2 1958 on Huckleberry Hound Show. Hanna-Barbera Studios, Hollywood, CA. Voiced by Daws Butler."))
    yogi.add_era(Era(1973, 2009, "Classic TV era — same design maintained consistently across all productions", art_style="Limited TV animation", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Yogi_Bear.png/200px-Yogi_Bear.png", notes="Design remained remarkably consistent for over four decades of TV productions and specials."))
    yogi.add_era(Era(2010, None, "CGI film and modern era — rendered in 3D for 2010 film; 2D for other media", art_style="CGI / digital", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Yogi_Bear.png/200px-Yogi_Bear.png", notes="2010 Warner Bros. film used CGI Yogi and Boo-Boo in live-action Jellystone Park. Dan Aykroyd voiced Yogi."))
    yogi.wiki_url = "https://en.wikipedia.org/wiki/Yogi_Bear"
    yogi.origin_location = "Hollywood, California, USA — Hanna-Barbera Productions studio"
    lib.add_cartoon(yogi)

    # CAPTAIN CAVEMAN (1977)
    captcaveman = Cartoon(
        name="Captain Caveman",
        description=(
            "A prehistoric caveman superhero thawed from a block of ice by three "
            "teenage crime-solving girls — Dee Dee, Brenda, and Taffy. Known for "
            "his battle cry Captain CAAAAAVE MAAAAN and his magical club that "
            "conceals various tools and gadgets. A comedic take on the superhero "
            "genre set in the modern day."
        ),
        character_type="Human — prehistoric caveman superhero",
        country_of_origin="USA",
        debut_year=1977,
    )
    captcaveman.original_studio = ProductionCompany("Hanna-Barbera Productions", 1957, still_active=False)
    captcaveman.add_creator(Creator("William Hanna", "Executive producer", 1910, 2001))
    captcaveman.add_creator(Creator("Joseph Barbera", "Executive producer", 1911, 2006))
    captcaveman.add_series(Series("Captain Caveman and the Teen Angels ABC", 1977, 1980, "Hanna-Barbera / ABC", "TV series", episode_count=40))
    captcaveman.add_series(Series("Captain Caveman on The Flintstone Comedy Show", 1980, 1982, "Hanna-Barbera / NBC", "TV series segments"))
    captcaveman.add_series(Series("Captain Caveman crossover appearances", 1990, None, "Hanna-Barbera / Warner Bros.", "cameo appearances"))
    captcaveman.add_ownership_record(OwnershipRecord("Hanna-Barbera Productions", 1977, 1989, "original creation"))
    captcaveman.add_ownership_record(OwnershipRecord("Turner Broadcasting", 1989, 1996, "acquisition of Hanna-Barbera"))
    captcaveman.add_ownership_record(OwnershipRecord("Warner Bros. / Time Warner", 1996, 2022, "Turner-Time Warner merger"))
    captcaveman.add_ownership_record(OwnershipRecord("Warner Bros. Discovery", 2022, None, "corporate merger", is_current_owner=True))
    captcaveman.add_era(Era(1977, 1982, "Original design — small hairy caveman almost completely covered in fur with giant club", art_style="Flat color TV cel", image_url="https://upload.wikimedia.org/wikipedia/en/thumb/7/70/Captain_caveman.jpg/200px-Captain_caveman.jpg", notes="Debuted September 10 1977 on ABC. Voiced by Mel Blanc. Produced at Hanna-Barbera, Hollywood, CA."))
    captcaveman.add_era(Era(1983, None, "Modern era — classic design retained for reruns merchandise and crossover cameos", art_style="Various", image_url="https://upload.wikimedia.org/wikipedia/en/thumb/7/70/Captain_caveman.jpg/200px-Captain_caveman.jpg", notes="Character remains in the Warner Bros. Discovery library available for future productions."))
    captcaveman.wiki_url = "https://en.wikipedia.org/wiki/Captain_Caveman_and_the_Teen_Angels"
    captcaveman.origin_location = "Hollywood, California, USA — Hanna-Barbera Productions studio"
    lib.add_cartoon(captcaveman)

    # GOOFY (1932)
    goofy = Cartoon(
        name="Goofy",
        description=(
            "A tall clumsy anthropomorphic dog who is one of Mickey Mouse's "
            "best friends. Known for his distinctive laugh, his signature hat "
            "and vest, and his extraordinary bad luck with everyday tasks. "
            "Starred in a long-running series of instructional parody shorts "
            "in which he demonstrates how NOT to do things. One of the core "
            "Disney Fab Five characters."
        ),
        character_type="Anthropomorphic animal — dog",
        country_of_origin="USA",
        debut_year=1932,
    )
    goofy.original_studio = ProductionCompany("Walt Disney Productions", 1923)
    goofy.add_creator(Creator("Walt Disney", "Executive producer", 1901, 1966))
    goofy.add_creator(Creator("Art Babbitt", "Character animator who defined Goofy's movement", 1907, 1992))
    goofy.add_series(Series("Mickey Mouse theatrical shorts (Goofy supporting)", 1932, 1942, "Walt Disney Productions", "theatrical short"))
    goofy.add_series(Series("Goofy How-To shorts", 1942, 1953, "Walt Disney Productions", "theatrical short", episode_count=27))
    goofy.add_series(Series("Goof Troop", 1992, 1993, "Walt Disney Television Animation", "TV series", episode_count=78))
    goofy.add_series(Series("A Goofy Movie", 1995, 1995, "Walt Disney Pictures", "theatrical feature"))
    goofy.add_series(Series("An Extremely Goofy Movie", 2000, 2000, "Walt Disney Television Animation", "direct-to-video"))
    goofy.add_series(Series("Mickey Mouse shorts and specials", 2013, None, "Walt Disney Animation Studios", "various"))
    goofy.add_ownership_record(OwnershipRecord("Walt Disney Productions", 1932, 1986, "original creation"))
    goofy.add_ownership_record(OwnershipRecord("The Walt Disney Company", 1986, None, "corporate restructuring", is_current_owner=True))
    goofy.add_era(Era(1932, 1938, "Dippy Dawg era — scruffy rough design closer to a generic dog character", art_style="Black & white", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Goofy_Headshot_Transparent.PNG/200px-Goofy_Headshot_Transparent.PNG", notes="First appeared as Dippy Dawg in Mickey's Revue (1932). Disney Studios, Hyperion Ave, Los Angeles."))
    goofy.add_era(Era(1938, 1960, "Classic golden age design — tall lanky build green hat orange turtleneck white gloves", art_style="Technicolor cel", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Goofy_Headshot_Transparent.PNG/200px-Goofy_Headshot_Transparent.PNG", notes="How-To shorts defined Goofy as the comedic everyman. Art Babbitt's animation style locked in his walk."))
    goofy.add_era(Era(1960, 1991, "TV and park era — same design used consistently across Disney parks and TV", art_style="Flat cel animation", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Goofy_Headshot_Transparent.PNG/200px-Goofy_Headshot_Transparent.PNG", notes="Goofy became a Disney Parks staple. Design remained stable for decades."))
    goofy.add_era(Era(1992, None, "Modern era — refined digital design; Goof Troop gave him son Max and suburban setting", art_style="Digital cel", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Goofy_Headshot_Transparent.PNG/200px-Goofy_Headshot_Transparent.PNG", notes="Goof Troop (1992) and A Goofy Movie (1995) reimagined Goofy as a single father. Bill Farmer has voiced him since 1987."))
    goofy.wiki_url = "https://en.wikipedia.org/wiki/Goofy"
    goofy.origin_location = "Los Angeles, California, USA — Walt Disney Productions, Hyperion Avenue studio"
    lib.add_cartoon(goofy)

    # MINNIE MOUSE (1928)
    minnie = Cartoon(
        name="Minnie Mouse",
        description=(
            "Mickey Mouse's sweetheart and one of the most iconic female cartoon "
            "characters ever created. Known for her polka-dot bow, her cheerful "
            "personality, and her high-pitched voice. Debuted alongside Mickey "
            "in Steamboat Willie and has appeared in hundreds of productions "
            "across nearly a century of Disney history."
        ),
        character_type="Anthropomorphic animal — mouse",
        country_of_origin="USA",
        debut_year=1928,
    )
    minnie.original_studio = ProductionCompany("Walt Disney Productions", 1923)
    minnie.add_creator(Creator("Walt Disney", "Co-creator", 1901, 1966))
    minnie.add_creator(Creator("Ub Iwerks", "Character designer", 1901, 1971))
    minnie.add_creator(Creator("Russi Taylor", "Voice actress 1986-2019", 1944, 2019))
    minnie.add_series(Series("Mickey Mouse theatrical shorts (Minnie supporting)", 1928, 1953, "Walt Disney Productions", "theatrical short"))
    minnie.add_series(Series("Mickey Mouse Club", 1955, 1959, "Walt Disney Productions", "TV series"))
    minnie.add_series(Series("Minnie-ella short and specials", 1990, 2010, "Walt Disney Television Animation", "various"))
    minnie.add_series(Series("Mickey Mouse Clubhouse (Minnie lead role)", 2006, 2016, "Walt Disney Television Animation", "TV series", episode_count=182))
    minnie.add_series(Series("Minnie's Bow-Toons", 2011, 2016, "Walt Disney Television Animation", "streaming short series", episode_count=104))
    minnie.add_series(Series("Mickey Mouse Funhouse", 2021, None, "Walt Disney Television Animation", "streaming series"))
    minnie.add_ownership_record(OwnershipRecord("Walt Disney Productions", 1928, 1986, "original creation"))
    minnie.add_ownership_record(OwnershipRecord("The Walt Disney Company", 1986, None, "corporate restructuring", is_current_owner=True))
    minnie.add_era(Era(1928, 1940, "Original design — simple round ears, large skirt, no defined color palette", art_style="Black & white", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Minnie_Mouse.png/200px-Minnie_Mouse.png", notes="Debuted November 18 1928 in Steamboat Willie alongside Mickey. Colony Theatre, New York."))
    minnie.add_era(Era(1940, 1986, "Classic color design — red polka-dot dress and bow established as her signature look", art_style="Technicolor cel animation", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Minnie_Mouse.png/200px-Minnie_Mouse.png", notes="Minnie's iconic red and white polka-dot aesthetic was standardized during the Technicolor era."))
    minnie.add_era(Era(1986, 2005, "Modern classic — refined digital lines same iconic look updated for HD", art_style="Digital cel", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Minnie_Mouse.png/200px-Minnie_Mouse.png", notes="Russi Taylor became the definitive voice of Minnie in 1986 and held the role until her death in 2019."))
    minnie.add_era(Era(2006, None, "Contemporary era — Minnie given more prominent starring roles in her own shows", art_style="Stylized digital", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Minnie_Mouse.png/200px-Minnie_Mouse.png", notes="Mickey Mouse Clubhouse and Minnie's Bow-Toons gave Minnie starring vehicles for the first time."))
    minnie.wiki_url = "https://en.wikipedia.org/wiki/Minnie_Mouse"
    minnie.origin_location = "Los Angeles, California, USA — Walt Disney Productions, Hyperion Avenue studio"
    lib.add_cartoon(minnie)

    # DOPEY (1937)
    dopey = Cartoon(
        name="Dopey",
        description=(
            "The youngest and most childlike of the Seven Dwarfs from Snow White "
            "and the Seven Dwarfs. The only dwarf who cannot grow a beard and the "
            "only one who never speaks. Known for his oversized hat floppy ears "
            "and endearing wide-eyed innocence. Often considered the most popular "
            "of the seven dwarfs by audiences."
        ),
        character_type="Fantasy — dwarf",
        country_of_origin="USA",
        debut_year=1937,
    )
    dopey.original_studio = ProductionCompany("Walt Disney Productions", 1923)
    dopey.add_creator(Creator("Walt Disney", "Producer", 1901, 1966))
    dopey.add_creator(Creator("Ward Kimball", "Lead animator for Dopey", 1914, 2002))
    dopey.add_series(Series("Snow White and the Seven Dwarfs feature film", 1937, 1937, "Walt Disney Productions", "theatrical feature", notes="First feature-length animated film ever made. Released December 21 1937."))
    dopey.add_series(Series("Snow White TV specials and park appearances", 1955, None, "Walt Disney Productions / Disney Parks", "various"))
    dopey.add_series(Series("Once Upon a Time TV series", 2012, 2018, "ABC Studios", "live-action TV", notes="Live-action adaptation featured Dopey as a recurring character."))
    dopey.add_ownership_record(OwnershipRecord("Walt Disney Productions", 1937, 1986, "original creation"))
    dopey.add_ownership_record(OwnershipRecord("The Walt Disney Company", 1986, None, "corporate restructuring", is_current_owner=True))
    dopey.add_era(Era(1937, 1960, "Original film design — oversized purple hat floppy ears huge blue eyes childlike proportions", art_style="Technicolor cel animation", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Dopey_%28Disney%29.png/200px-Dopey_%28Disney%29.png", notes="Designed by Ward Kimball at Disney's Hyperion Ave studio. Dopey was nearly cut from the film before Walt insisted on keeping him."))
    dopey.add_era(Era(1960, None, "Modern era — same classic design maintained across all Disney Parks and media", art_style="Digital recreation of original", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Dopey_%28Disney%29.png/200px-Dopey_%28Disney%29.png", notes="Dopey's design has remained virtually unchanged since 1937 making him one of Disney's most consistent characters."))
    dopey.wiki_url = "https://en.wikipedia.org/wiki/Dopey_(Disney)"
    dopey.origin_location = "Los Angeles, California, USA — Walt Disney Productions, Hyperion Avenue studio"
    lib.add_cartoon(dopey)

    # MIGHTY MOUSE (1942)
    mightymouse = Cartoon(
        name="Mighty Mouse",
        description=(
            "A tiny but incredibly powerful anthropomorphic mouse superhero who "
            "battles villains and rescues the innocent — often in operatic parody "
            "style with characters singing their dialogue. Originally created as "
            "a parody of Superman, Mighty Mouse became a beloved icon of the "
            "Terrytoons era and later experienced a celebrated revival in the 1980s."
        ),
        character_type="Anthropomorphic animal — mouse superhero",
        country_of_origin="USA",
        debut_year=1942,
    )
    mightymouse.original_studio = ProductionCompany("Terrytoons / 20th Century Fox", 1929, still_active=False)
    mightymouse.add_creator(Creator("Paul Terry", "Terrytoons founder & original producer", 1887, 1971))
    mightymouse.add_creator(Creator("I. Klein", "Original character designer", 0, 0))
    mightymouse.add_series(Series("Mighty Mouse theatrical shorts", 1942, 1961, "Terrytoons / 20th Century Fox", "theatrical short", episode_count=80))
    mightymouse.add_series(Series("Mighty Mouse Playhouse CBS", 1955, 1967, "Terrytoons / CBS", "TV series", notes="One of the first superhero Saturday morning cartoons."))
    mightymouse.add_series(Series("The New Adventures of Mighty Mouse and Heckle and Jeckle", 1979, 1982, "Filmation / CBS", "TV series", episode_count=32))
    mightymouse.add_series(Series("Mighty Mouse The New Adventures", 1987, 1988, "Viacom / CBS", "TV series", episode_count=19, notes="Ralph Bakshi revival. Critically acclaimed for pushing boundaries of TV animation."))
    mightymouse.add_series(Series("Mighty Mouse in the Great Space Chase film", 1982, 1982, "Filmation", "theatrical feature"))
    mightymouse.add_ownership_record(OwnershipRecord("Terrytoons / 20th Century Fox", 1942, 1966, "original creation"))
    mightymouse.add_ownership_record(OwnershipRecord("CBS / Viacom", 1966, 1994, "purchase of Terrytoons library"))
    mightymouse.add_ownership_record(OwnershipRecord("Paramount Pictures / Viacom", 1994, 2019, "Viacom corporate restructuring"))
    mightymouse.add_ownership_record(OwnershipRecord("Paramount Pictures / ViacomCBS / Paramount Global", 2019, None, "corporate merger", is_current_owner=True))
    mightymouse.add_era(Era(1942, 1945, "Original Super Mouse design — blue costume yellow cape before name change to Mighty Mouse", art_style="Technicolor cel", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Mighty_Mouse.svg/200px-Mighty_Mouse.svg.png", notes="Debuted as Super Mouse in The Mouse of Tomorrow (1942). Terrytoons studio, New Rochelle, New York."))
    mightymouse.add_era(Era(1945, 1967, "Classic Mighty Mouse — red and yellow costume cape and boots operatic adventure style", art_style="Technicolor cel", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Mighty_Mouse.svg/200px-Mighty_Mouse.svg.png", notes="Renamed Mighty Mouse in 1945. The opera-style singing format became his trademark presentation."))
    mightymouse.add_era(Era(1979, 1986, "Filmation revival era — updated cleaner design same color scheme", art_style="Limited TV animation", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Mighty_Mouse.svg/200px-Mighty_Mouse.svg.png", notes="Filmation produced revival series for CBS. Lower budget than original theatrical shorts."))
    mightymouse.add_era(Era(1987, None, "Bakshi modern era — more expressive deconstructed take on the classic design", art_style="Modern cel / digital", image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Mighty_Mouse.svg/200px-Mighty_Mouse.svg.png", notes="Ralph Bakshi's New Adventures (1987) pushed creative boundaries and launched John Kricfalusi's career."))
    mightymouse.wiki_url = "https://en.wikipedia.org/wiki/Mighty_Mouse"
    mightymouse.origin_location = "New Rochelle, New York, USA — Terrytoons studio"
    lib.add_cartoon(mightymouse)

    add_anime_characters(lib)
    add_hanna_barbera_characters(lib)
    add_disney_characters(lib)
    add_mgm_characters(lib)
    add_schoolhouse_rock(lib)
    add_dic_characters(lib)
    add_filmation_characters(lib)
    add_wb_characters(lib)
    add_dc_characters(lib)
    add_marvel_characters(lib)
    add_sanrio_characters(lib)
    add_nickelodeon_characters(lib)
    add_hasbro_characters(lib)
    add_cartoon_network_characters(lib)
    return lib