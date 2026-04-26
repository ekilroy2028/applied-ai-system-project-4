"""
wb_characters.py
Warner Bros. Looney Tunes, Merrie Melodies, and WB Animation characters.

Warner Bros. Cartoons operated from 1930 to 1969, producing the Looney Tunes
and Merrie Melodies theatrical short series. The studio was home to the
greatest concentration of animation talent in history — Chuck Jones, Tex Avery,
Bob Clampett, Friz Freleng, Robert McKimson, Frank Tashlin — and produced
what many consider the finest body of work in animated short film history.

Key directors:
- Tex Avery (1935–1942): anarchic, speed-driven comedy
- Bob Clampett (1937–1946): wildest, most surreal cartoons
- Chuck Jones (1938–1962): masterful timing, character depth
- Friz Freleng (1930–1963): musical comedy, Sylvester & Tweety
- Robert McKimson (1946–1969): Foghorn Leghorn, Tasmanian Devil
- Frank Tashlin (1933–1946): cinematic, self-aware comedy

Ownership chain (all Looney Tunes / WB Animation characters):
- Warner Bros. Cartoons (1930–1969): original theatrical production
- Warner Bros. Inc. (1969–1990): after closing the cartoon unit
- Time Warner / Warner Bros. (1990–2022)
- Warner Bros. Discovery (2022–present)

NOTE: Bugs Bunny is already in seed_data.py.
      Tom & Jerry, Droopy, and MGM characters are in mgm_characters.py.
      HB characters (Scooby, Yogi, Flintstones, etc.) are in hanna_barbera_characters.py.
      This file covers the remaining Looney Tunes cast and WB Animation originals.

Usage:
    from wb_characters import add_wb_characters
    add_wb_characters(lib)
"""

from cartoon_system import (
    Cartoon, Creator, ProductionCompany,
    Series, OwnershipRecord, Era, Library
)

# ── Shared objects ─────────────────────────────────────────────────────────
WBC  = ProductionCompany("Warner Bros. Cartoons", 1930, still_active=False)
WBAS = ProductionCompany("Warner Bros. Animation", 1980)

CHUCK_JONES   = Creator("Chuck Jones", "Director — timing, character depth", 1912, 2002)
FRIZ_FRELENG  = Creator("Friz Freleng", "Director — musical comedy, Sylvester & Tweety", 1905, 1995)
BOB_CLAMPETT  = Creator("Bob Clampett", "Director — wildest, most surreal WB cartoons", 1913, 1984)
TEX_AVERY_WB  = Creator("Tex Avery", "Director — anarchic speed-driven comedy (WB era 1935-1942)", 1908, 1980)
MCKIMSON      = Creator("Robert McKimson", "Director — Foghorn Leghorn, Tasmanian Devil", 1910, 1977)
MEL_BLANC     = Creator("Mel Blanc", "Voice of virtually every major Looney Tunes character", 1908, 1989)

WB_OWNERSHIP = [
    ("Warner Bros. Cartoons", 1930, 1969, "original creation"),
    ("Warner Bros. Inc.", 1969, 1990, "studio consolidation after cartoon unit closed"),
    ("Time Warner / Warner Bros.", 1990, 2022, "corporate merger"),
    ("Warner Bros. Discovery", 2022, None, "corporate merger"),
]

IMG = {
    "daffy":    "https://upload.wikimedia.org/wikipedia/en/thumb/a/aa/Daffy_Duck.svg/200px-Daffy_Duck.svg.png",
    "porky":    "https://upload.wikimedia.org/wikipedia/en/thumb/e/e2/Porky_Pig.svg/200px-Porky_Pig.svg.png",
    "tweety":   "https://upload.wikimedia.org/wikipedia/en/thumb/0/00/Tweety.svg/200px-Tweety.svg.png",
    "sylvester":"https://upload.wikimedia.org/wikipedia/en/thumb/7/71/Sylvester_Cat.svg/200px-Sylvester_Cat.svg.png",
    "elmer":    "https://upload.wikimedia.org/wikipedia/en/thumb/4/4a/Elmer_Fudd.png/200px-Elmer_Fudd.png",
    "foghorn":  "https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/Foghorn_Leghorn.png/200px-Foghorn_Leghorn.png",
    "taz":      "https://upload.wikimedia.org/wikipedia/en/thumb/4/4e/Tasmanian_Devil_-_Looney_Tunes.png/200px-Tasmanian_Devil_-_Looney_Tunes.png",
    "roadrunner":"https://upload.wikimedia.org/wikipedia/en/thumb/3/thirty/Road_Runner_and_Wile_E._Coyote.png/240px-Road_Runner_and_Wile_E._Coyote.png",
    "pepe":     "https://upload.wikimedia.org/wikipedia/en/thumb/6/6d/Pepe_Le_Pew.png/200px-Pepe_Le_Pew.png",
    "speedy":   "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Speedy_Gonzales.png/200px-Speedy_Gonzales.png",
    "marvin":   "https://upload.wikimedia.org/wikipedia/en/thumb/e/e8/Marvin_the_Martian.png/200px-Marvin_the_Martian.png",
    "granny":   "https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Granny_%28Looney_Tunes%29.png/200px-Granny_%28Looney_Tunes%29.png",
    "lola":     "https://upload.wikimedia.org/wikipedia/en/thumb/5/5d/Lola_Bunny.png/200px-Lola_Bunny.png",
    "tiny":     "https://upload.wikimedia.org/wikipedia/en/thumb/e/e3/Tiny_Toon_Adventures_logo.png/240px-Tiny_Toon_Adventures_logo.png",
    "animaniacs":"https://upload.wikimedia.org/wikipedia/en/thumb/4/4b/Animaniacs_logo.png/240px-Animaniacs_logo.png",
    "pinky":    "https://upload.wikimedia.org/wikipedia/en/thumb/2/2b/Pinky_and_the_Brain_logo.png/240px-Pinky_and_the_Brain_logo.png",
    "freakazoid":"https://upload.wikimedia.org/wikipedia/en/thumb/6/6e/Freakazoid%21_logo.png/240px-Freakazoid%21_logo.png",
    "batman":   "https://upload.wikimedia.org/wikipedia/en/thumb/1/10/Batman_The_Animated_Series_logo.png/240px-Batman_The_Animated_Series_logo.png",
    "superman": "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Superman_The_Animated_Series_logo.png/240px-Superman_The_Animated_Series_logo.png",
    "looney":   "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Looney_Tunes_logo.svg/240px-Looney_Tunes_logo.svg.png",
    "wb":       "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Warner_Bros_logo.svg/240px-Warner_Bros_logo.svg.png",
    "justice":  "https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Justice_League_animated_logo.png/240px-Justice_League_animated_logo.png",
    "batman_beyond":"https://upload.wikimedia.org/wikipedia/en/thumb/2/2b/Batman_Beyond_logo.png/240px-Batman_Beyond_logo.png",
    "static":   "https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/Static_Shock_logo.png/240px-Static_Shock_logo.png",
    "teen":     "https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Teen_Titans_logo.png/240px-Teen_Titans_logo.png",
}


def _wb(name, description, character_type, debut_year,
        directors, series_list, eras, wiki_slug,
        studio=None, origin="Burbank, California, USA — Warner Bros. Cartoons, Termite Terrace"):
    c = Cartoon(name=name, description=description,
                character_type=character_type,
                country_of_origin="USA", debut_year=debut_year)
    c.original_studio = studio or WBC
    c.add_creator(MEL_BLANC)
    for d in directors:
        c.add_creator(d)
    for s in series_list:
        c.add_series(s)
    for i, rec in enumerate(WB_OWNERSHIP):
        is_cur = (i == len(WB_OWNERSHIP) - 1)
        c.add_ownership_record(
            OwnershipRecord(rec[0], rec[1], rec[2], rec[3], is_current_owner=is_cur)
        )
    for era in eras:
        c.add_era(era)
    c.wiki_url = f"https://en.wikipedia.org/wiki/{wiki_slug}"
    c.origin_location = origin
    return c


LOONEY_SERIES = [
    Series("Looney Tunes / Merrie Melodies theatrical shorts", 1930, 1969,
           "Warner Bros. Cartoons", "theatrical short"),
    Series("The Bugs Bunny Show / various TV compilations", 1960, 1985,
           "Warner Bros.", "TV series"),
    Series("Looney Tunes Cartoons (HBO Max)", 2019, None,
           "Warner Bros. Animation", "streaming short"),
]


def add_wb_characters(lib: Library):

    # ══════════════════════════════════════════════════════════════════════
    # CORE LOONEY TUNES CAST
    # ══════════════════════════════════════════════════════════════════════

    # DAFFY DUCK (1937)
    daffy = _wb(
        name="Daffy Duck",
        description=(
            "Warner Bros.' second-most famous character and one of animation's "
            "most complex — starting as a completely screwball anarchist in 1937 "
            "and gradually transforming into a jealous, scheming egotist by the "
            "1950s. Both versions are brilliant. Daffy's relationship with Bugs "
            "Bunny — where Daffy is always outwitted, always furious, always "
            "certain the world is conspiring against him — is one of comedy's "
            "greatest double acts. His distinctive lisp, created by Mel Blanc, "
            "is one of the most recognizable sounds in animation."
        ),
        character_type="Anthropomorphic animal — duck",
        debut_year=1937,
        directors=[BOB_CLAMPETT, CHUCK_JONES, FRIZ_FRELENG],
        series_list=LOONEY_SERIES + [
            Series("Duck Dodgers in the 24th and a Half Century", 1953, 1953,
                   "Warner Bros. Cartoons", "theatrical short",
                   notes="Chuck Jones' masterpiece. Daffy as a pompous space hero."),
            Series("Duck Dodgers animated series", 2003, 2005,
                   "Warner Bros. Animation / Cartoon Network", "TV series", episode_count=39),
            Series("Space Jam A New Legacy", 2021, 2021,
                   "Warner Bros. Pictures", "theatrical feature"),
        ],
        eras=[
            Era(1937, 1943,
                "Screwball era — whoo-hoo anarchist duck, completely unpredictable, "
                "rubber-limbed slapstick energy",
                art_style="Technicolor cel animation",
                image_url=IMG["daffy"],
                notes="Debuted in Porky's Duck Hunt (1937) directed by Tex Avery. "
                      "Early Daffy was pure id — bouncing off walls howling whoo-hoo. "
                      "Voiced by Mel Blanc who gave him his famous lisp."),
            Era(1943, 1969,
                "Jealous schemer era — competitive with Bugs, self-promoting, "
                "convinced the universe owes him stardom",
                art_style="Technicolor cel animation",
                image_url=IMG["daffy"],
                notes="Chuck Jones transformed Daffy into Bugs' foil — jealous, "
                      "scheming, self-defeating. Rabbit Fire (1951) and Duck Amuck "
                      "(1953) are masterpieces of the jealous Daffy era."),
            Era(1970, None,
                "Modern era — blends both personalities depending on the production",
                art_style="Various digital / cel",
                image_url=IMG["daffy"],
                notes="Modern Daffy draws on both the screwball and jealous personas. "
                      "The 2003 Duck Dodgers series is widely praised as the best modern Daffy production."),
        ],
        wiki_slug="Daffy_Duck",
    )
    lib.add_cartoon(daffy)

    # PORKY PIG (1935)
    porky = _wb(
        name="Porky Pig",
        description=(
            "The first major Looney Tunes star — a mild-mannered, stuttering pig "
            "who predates Bugs Bunny and Daffy Duck and served as the studio's "
            "primary protagonist through the late 1930s. Porky's famous sign-off — "
            "Th-th-th-that's all folks! — has closed Looney Tunes productions "
            "for 90 years. Initially the star, Porky gradually became a straight-man "
            "foil for more anarchic characters but remained a beloved constant "
            "throughout the series. Mel Blanc used his own stutter for Porky."
        ),
        character_type="Anthropomorphic animal — pig",
        debut_year=1935,
        directors=[BOB_CLAMPETT, CHUCK_JONES, FRIZ_FRELENG, TEX_AVERY_WB],
        series_list=LOONEY_SERIES,
        eras=[
            Era(1935, 1942,
                "Star era — round plump pig, primary protagonist of the Looney Tunes shorts",
                art_style="Black & white / early Technicolor",
                image_url=IMG["porky"],
                notes="Debuted in I Haven't Got a Hat (1935). "
                      "Porky was the studio's first real star, predating Bugs and Daffy. "
                      "Bob Clampett's early Porky cartoons established the character's gentle nature."),
            Era(1943, None,
                "Supporting era — straight man and reliable sidekick to more chaotic characters",
                art_style="Technicolor cel / digital",
                image_url=IMG["porky"],
                notes="As Bugs and Daffy rose to prominence Porky became the reliable foil. "
                      "His partnership with Daffy produced some of Jones' best work. "
                      "That's All Folks! remains the most recognizable sign-off in animation."),
        ],
        wiki_slug="Porky_Pig",
    )
    lib.add_cartoon(porky)

    # TWEETY (1942)
    tweety = _wb(
        name="Tweety",
        description=(
            "A small yellow canary bird of apparently innocent appearance who is "
            "actually thoroughly capable of outwitting his pursuer Sylvester the "
            "Cat. Tweety's distinctive baby-talk voice and his famous line "
            "I tawt I taw a puddy tat! became one of the most recognizable phrases "
            "in American culture. Created by Bob Clampett as a wild pink naked bird, "
            "Tweety was softened and paired with Sylvester by Friz Freleng "
            "into the definitive innocent-victim-who-always-wins formula."
        ),
        character_type="Anthropomorphic animal — canary bird",
        debut_year=1942,
        directors=[BOB_CLAMPETT, FRIZ_FRELENG],
        series_list=LOONEY_SERIES + [
            Series("The Sylvester and Tweety Mysteries", 1995, 2001,
                   "Warner Bros. Animation", "TV series", episode_count=55),
        ],
        eras=[
            Era(1942, 1946,
                "Original Clampett era — pink naked bird, wilder more anarchic personality",
                art_style="Technicolor cel animation",
                image_url=IMG["tweety"],
                notes="Debuted in A Tale of Two Kitties (1942). "
                      "Bob Clampett's original Tweety was a naked pink bird — censors demanded feathers. "
                      "Voiced by Mel Blanc. The name Tweety was inspired by the Tweety Bird toy."),
            Era(1947, None,
                "Freleng era — yellow feathers, permanently paired with Sylvester, "
                "innocent-seeming but ruthlessly clever",
                art_style="Technicolor cel / digital",
                image_url=IMG["tweety"],
                notes="Tweetie Pie (1947) won the Academy Award and established the "
                      "Tweety/Sylvester formula. Freleng's Tweety is more calculated — "
                      "he weaponizes his innocent appearance against Sylvester."),
        ],
        wiki_slug="Tweety",
    )
    lib.add_cartoon(tweety)

    # SYLVESTER THE CAT (1945)
    sylvester = _wb(
        name="Sylvester the Cat",
        description=(
            "A tuxedo cat with a lisp who spends his existence in futile pursuit "
            "of Tweety Bird, thwarted by Granny, Hector the Bulldog, and Tweety's "
            "own deceptive cleverness. Sylvester is one of animation's great "
            "losers — perpetually optimistic, perpetually defeated, perpetually "
            "returning for more. His suffix — Sufferin' Succotash! — became "
            "a national catchphrase. He also starred opposite Porky Pig in "
            "a separate horror-comedy series."
        ),
        character_type="Anthropomorphic animal — cat",
        debut_year=1945,
        directors=[FRIZ_FRELENG, CHUCK_JONES],
        series_list=LOONEY_SERIES + [
            Series("The Sylvester and Tweety Mysteries", 1995, 2001,
                   "Warner Bros. Animation", "TV series", episode_count=55),
        ],
        eras=[
            Era(1945, 1969,
                "Original theatrical era — black and white tuxedo cat, "
                "red nose, large round eyes, perpetual drool",
                art_style="Technicolor cel animation",
                image_url=IMG["sylvester"],
                notes="Debuted in Life with Feathers (1945). "
                      "Friz Freleng created Sylvester. "
                      "Mel Blanc gave him a lisp similar to Daffy but heavier and wetter. "
                      "Puss n Booty (1943) featuring a Sylvester prototype won an Oscar."),
            Era(1970, None,
                "Modern era — same classic design in TV series and modern productions",
                art_style="Various cel / digital",
                image_url=IMG["sylvester"],
                notes="The Sylvester and Tweety Mysteries (1995) gave both characters "
                      "a full adventure series. Sylvester also raised a son Junior "
                      "who was ashamed of his father's failures."),
        ],
        wiki_slug="Sylvester_the_Cat",
    )
    lib.add_cartoon(sylvester)

    # ELMER FUDD (1940)
    elmer = _wb(
        name="Elmer Fudd",
        description=(
            "Bugs Bunny's primary hunting nemesis — a bald, round hunter who "
            "pursues wabbits with his hunting rifle while speaking in a distinctive "
            "rhotacism that replaces R and L sounds with W. Elmer Fudd is the "
            "everyman fall guy of Looney Tunes — pompous enough to be satisfying "
            "when he fails, sympathetic enough to not be purely villainous. "
            "His opera-singing in What's Opera Doc? is one of animation's most "
            "celebrated moments."
        ),
        character_type="Human — bumbling hunter",
        debut_year=1940,
        directors=[CHUCK_JONES, FRIZ_FRELENG, TEX_AVERY_WB],
        series_list=LOONEY_SERIES,
        eras=[
            Era(1940, 1942,
                "Early Egghead/Elmer — slightly different design, transitioning "
                "from the Egghead prototype character",
                art_style="Technicolor cel animation",
                image_url=IMG["elmer"],
                notes="Elmer evolved from Egghead — a recurring character in Tex Avery's WB shorts. "
                      "Elmer's Candid Camera (1940) was the first proper Elmer Fudd cartoon. "
                      "Arthur Q. Bryan voiced Elmer until his death in 1959."),
            Era(1943, None,
                "Definitive Elmer — round bald hunter in tan outfit and hunting cap, "
                "full rhotacism established",
                art_style="Technicolor cel / digital",
                image_url=IMG["elmer"],
                notes="What's Opera Doc? (1957) is the greatest Elmer cartoon. "
                      "Chuck Jones spent the entire unit's budget for six weeks on it. "
                      "Elmer sings Kill the Wabbit to the tune of Wagner's Ride of the Valkyries."),
        ],
        wiki_slug="Elmer_Fudd",
    )
    lib.add_cartoon(elmer)

    # ROAD RUNNER AND WILE E. COYOTE (1949)
    roadrunner = _wb(
        name="Road Runner and Wile E. Coyote",
        description=(
            "The Road Runner — a fast bird who says Beep Beep — and Wile E. Coyote "
            "— a genius-level predator who purchases elaborate ACME products "
            "that invariably backfire catastrophically — in an infinite chase "
            "across the American Southwest desert. Created entirely by Chuck Jones "
            "as a parody of cartoon chase formulas, the series has no dialogue "
            "beyond beeping and the ACME product labels. Wile E. Coyote's "
            "frustrated intellect applied to hopeless situations is one of "
            "comedy's purest archetypes."
        ),
        character_type="Anthropomorphic animals — bird and coyote / eternal chase",
        debut_year=1949,
        directors=[CHUCK_JONES],
        series_list=LOONEY_SERIES + [
            Series("Fast and Furry-ous debut short", 1949, 1949,
                   "Warner Bros. Cartoons", "theatrical short",
                   notes="The very first Road Runner cartoon. Chuck Jones' pure comedic formula established immediately."),
            Series("Wile E. Coyote and Road Runner shorts", 1949, 1966,
                   "Warner Bros. Cartoons", "theatrical short", episode_count=48),
            Series("Looney Tunes Cartoons Road Runner segments", 2019, None,
                   "Warner Bros. Animation / HBO Max", "streaming short"),
        ],
        eras=[
            Era(1949, 1966,
                "Original theatrical shorts — pure formula, no dialogue, "
                "elaborate ACME devices, desert Southwest setting",
                art_style="Technicolor cel animation",
                image_url=IMG["roadrunner"],
                notes="Debuted September 17 1949 in Fast and Furry-ous. "
                      "Chuck Jones and writer Michael Maltese created the series as a parody. "
                      "The Road Runner never loses, the Coyote never wins — "
                      "a perfect closed comedic loop. ACME became a pop culture institution."),
            Era(1967, None,
                "Post-theatrical era — same formula adapted for TV and streaming",
                art_style="Various cel / digital",
                image_url=IMG["roadrunner"],
                notes="The Road Runner formula proved infinitely adaptable. "
                      "Chuck Jones continued making Road Runner cartoons independently. "
                      "The 2019 HBO Max series returned to classic theatrical short format."),
        ],
        wiki_slug="Wile_E._Coyote_and_the_Road_Runner",
    )
    lib.add_cartoon(roadrunner)

    # FOGHORN LEGHORN (1946)
    foghorn = _wb(
        name="Foghorn Leghorn",
        description=(
            "A massive, boisterous Southern rooster with an unstoppable need "
            "to lecture everyone around him — particularly a small, bespectacled "
            "chicken hawk named Henery who wants to eat him and a quiet dog "
            "he torments endlessly. Foghorn's rapid-fire self-important monologues — "
            "I say, I say, son! — are delivered with magnificent pomposity. "
            "Created by Robert McKimson, Foghorn is loosely based on Senator "
            "Claghorn from The Fred Allen Show."
        ),
        character_type="Anthropomorphic animal — rooster",
        debut_year=1946,
        directors=[MCKIMSON],
        series_list=LOONEY_SERIES + [
            Series("Foghorn Leghorn theatrical shorts", 1946, 1963,
                   "Warner Bros. Cartoons / McKimson unit", "theatrical short", episode_count=28),
        ],
        eras=[
            Era(1946, 1969,
                "Original theatrical design — enormous white rooster, "
                "red comb and wattle, booming voice, inexhaustible monologues",
                art_style="Technicolor cel animation",
                image_url=IMG["foghorn"],
                notes="Debuted August 31 1946 in Walky Talky Hawky. "
                      "Voiced by Mel Blanc doing an exaggerated Southern colonel voice. "
                      "Based on Senator Beauregard Claghorn from The Fred Allen Show. "
                      "Walky Talky Hawky was nominated for the Academy Award."),
            Era(1970, None,
                "TV and modern era — same magnificent design and personality intact",
                art_style="Various",
                image_url=IMG["foghorn"],
                notes="Foghorn Leghorn became a beloved TV presence. "
                      "His catchphrase I say I say son became a permanent part of American vernacular."),
        ],
        wiki_slug="Foghorn_Leghorn",
    )
    lib.add_cartoon(foghorn)

    # TASMANIAN DEVIL / TAZ (1954)
    taz = _wb(
        name="Tasmanian Devil (Taz)",
        description=(
            "A ferocious, spinning, constantly hungry predator from Tasmania "
            "who communicates primarily in growls and destroys everything in "
            "his path — except when Bugs Bunny distracts him. Taz appeared "
            "in only five theatrical shorts but became one of the most "
            "popular Looney Tunes characters through merchandise. "
            "His spinning tornado attack, his insatiable appetite, and his "
            "dim-but-dangerous personality made him a perfect foil for Bugs."
        ),
        character_type="Anthropomorphic animal — Tasmanian devil",
        debut_year=1954,
        directors=[MCKIMSON],
        series_list=LOONEY_SERIES + [
            Series("Taz theatrical shorts", 1954, 1964,
                   "Warner Bros. Cartoons / McKimson unit", "theatrical short", episode_count=5),
            Series("Taz-Mania animated series", 1991, 1995,
                   "Warner Bros. Animation / Fox Kids", "TV series", episode_count=65),
        ],
        eras=[
            Era(1954, 1964,
                "Original theatrical — squat furry creature, spinning tornado attack, "
                "voracious appetite, only five appearances",
                art_style="Technicolor cel animation",
                image_url=IMG["taz"],
                notes="Debuted May 22 1954 in Devil May Hare. "
                      "Robert McKimson created Taz. "
                      "Jack Warner initially wanted to retire the character after two cartoons — "
                      "massive merchandise demand forced more productions."),
            Era(1991, None,
                "Taz-Mania era — expanded into lead character with full personality "
                "and supporting cast including his family",
                art_style="Flat color TV cel / digital",
                image_url=IMG["taz"],
                notes="The 1991 Fox Kids series made Taz a proper lead character for the first time. "
                      "His popularity in merchandise has consistently exceeded his screen time."),
        ],
        wiki_slug="Tasmanian_Devil_(Looney_Tunes)",
    )
    lib.add_cartoon(taz)

    # PEPE LE PEW (1945)
    pepe = _wb(
        name="Pepe Le Pew",
        description=(
            "A French skunk of irrepressible romantic confidence who mistakes "
            "a black cat with a white stripe for a female skunk and pursues "
            "her relentlessly with passionate declarations of love — oblivious "
            "to the fact that his overwhelming odor drives everyone away. "
            "Chuck Jones created Pepe as a parody of French romantic heroes — "
            "specifically Charles Boyer. Won the Academy Award for Best Animated "
            "Short Film in 1949 for For Scent-imental Reasons."
        ),
        character_type="Anthropomorphic animal — skunk / romantic",
        debut_year=1945,
        directors=[CHUCK_JONES],
        series_list=LOONEY_SERIES + [
            Series("Pepe Le Pew theatrical shorts", 1945, 1962,
                   "Warner Bros. Cartoons / Jones unit", "theatrical short", episode_count=16),
        ],
        eras=[
            Era(1945, 1969,
                "Original theatrical — elegant black and white skunk, "
                "bounding half-skip walk, oblivious romantic confidence",
                art_style="Technicolor cel animation",
                image_url=IMG["pepe"],
                notes="Debuted in Odor-able Kitty (1945). "
                      "For Scent-imental Reasons (1949) won the Academy Award for Best Animated Short. "
                      "Mel Blanc based Pepe's French accent on Charles Boyer. "
                      "Chuck Jones said Pepe was based on his own tendency to be too forward."),
            Era(1970, None,
                "TV and modern era — same romantic formula with occasional contemporary updates",
                art_style="Various",
                image_url=IMG["pepe"],
                notes="Pepe remains a beloved character. A planned Space Jam 2 scene featuring "
                      "Pepe was cut from the film following social media discussion about his character."),
        ],
        wiki_slug="Pepe_Le_Pew",
    )
    lib.add_cartoon(pepe)

    # SPEEDY GONZALES (1953)
    speedy = _wb(
        name="Speedy Gonzales",
        description=(
            "The fastest mouse in all Mexico — a tiny mouse in an oversized "
            "sombrero who races to the rescue of fellow mice oppressed by "
            "Sylvester the Cat, Daffy Duck, and various other villains. "
            "His catchphrase Andale! Andale! Arriba! Arriba! delivered at "
            "full sprint became one of the most recognizable in animation. "
            "Speedy was briefly removed from Cartoon Network in the late 1990s "
            "over concerns about ethnic stereotyping, but was reinstated after "
            "Mexican and Mexican-American fans protested strongly in his defense."
        ),
        character_type="Anthropomorphic animal — mouse / hero",
        debut_year=1953,
        directors=[FRIZ_FRELENG, MCKIMSON],
        series_list=LOONEY_SERIES + [
            Series("Speedy Gonzales theatrical shorts", 1953, 1968,
                   "Warner Bros. Cartoons", "theatrical short", episode_count=46),
        ],
        eras=[
            Era(1953, 1955,
                "Prototype Speedy — slightly different design in first appearance, "
                "rougher and more broadly comic",
                art_style="Technicolor cel animation",
                image_url=IMG["speedy"],
                notes="First appeared in Cat-Tails for Two (1953) directed by Robert McKimson "
                      "with a slightly different look before Friz Freleng refined the character."),
            Era(1955, None,
                "Definitive Speedy — white outfit, large sombrero, "
                "red kerchief, enormous speed blur, Andale catchphrase locked in",
                art_style="Technicolor cel / digital",
                image_url=IMG["speedy"],
                notes="Speedy Gonzales (1955) by Friz Freleng won the Academy Award. "
                      "This version established all his key traits. "
                      "Speedy is enormously popular in Mexico and Latin America. "
                      "Mexican audiences successfully campaigned for his return to Cartoon Network."),
        ],
        wiki_slug="Speedy_Gonzales",
    )
    lib.add_cartoon(speedy)

    # MARVIN THE MARTIAN (1948)
    marvin = _wb(
        name="Marvin the Martian",
        description=(
            "A soft-spoken, polite Martian conqueror who wishes to destroy "
            "Earth because it obstructs his view of Venus — and is perpetually "
            "thwarted by Bugs Bunny. Marvin's calm, measured announcements of "
            "planetary destruction and his subsequent quiet frustration created "
            "one of comedy's most effective contrasts. His Roman centurion helmet "
            "and sneakers design is immediately iconic. Created entirely by "
            "Chuck Jones, Marvin appeared in only a handful of theatrical shorts "
            "but became one of WB's most recognizable characters through merchandise."
        ),
        character_type="Alien — Martian conqueror with good manners",
        debut_year=1948,
        directors=[CHUCK_JONES],
        series_list=LOONEY_SERIES + [
            Series("Haredevil Hare debut", 1948, 1948,
                   "Warner Bros. Cartoons", "theatrical short",
                   notes="First appearance — Marvin had no name on screen initially."),
            Series("Marvin the Martian theatrical shorts", 1948, 1963,
                   "Warner Bros. Cartoons / Jones unit", "theatrical short", episode_count=5),
        ],
        eras=[
            Era(1948, None,
                "Consistent design across all eras — Roman centurion helmet, "
                "no visible face except eyes, sneakers, green uniform",
                art_style="Technicolor cel / digital",
                image_url=IMG["marvin"],
                notes="Debuted in Haredevil Hare (1948). "
                      "Marvin was unnamed in all original theatrical shorts — "
                      "the name was created for merchandise in the 1990s. "
                      "Mel Blanc voiced him in a soft polite tone to contrast his destructive goals."),
        ],
        wiki_slug="Marvin_the_Martian",
    )
    lib.add_cartoon(marvin)

    # GRANNY (1950)
    granny = _wb(
        name="Granny",
        description=(
            "Tweety's guardian — a tiny elderly woman of deceptively frail "
            "appearance who is actually formidably strong and an expert fighter "
            "when motivated to protect her bird. Granny's transformation from "
            "helpless little old lady to Sylvester-thrashing powerhouse is one "
            "of Looney Tunes' most reliable comedy reversals. She also appeared "
            "as Sam's mother in some shorts. Voiced by June Foray — one of "
            "the greatest voice actresses in animation history."
        ),
        character_type="Human — elderly woman / Tweety's guardian",
        debut_year=1950,
        directors=[FRIZ_FRELENG],
        series_list=LOONEY_SERIES + [
            Series("The Sylvester and Tweety Mysteries", 1995, 2001,
                   "Warner Bros. Animation", "TV series"),
        ],
        eras=[
            Era(1950, None,
                "Small white-haired old woman in grey dress and glasses — "
                "deceptively frail appearance hiding surprising strength",
                art_style="Technicolor cel / digital",
                image_url=IMG["granny"],
                notes="Voiced by June Foray throughout virtually her entire run. "
                      "Foray also voiced Rocky the Flying Squirrel and Witch Hazel. "
                      "Granny's violence toward Sylvester — always justified by his attacks on Tweety — "
                      "is one of WB's most reliable comedy reversals."),
        ],
        wiki_slug="Granny_(Looney_Tunes)",
    )
    lib.add_cartoon(granny)

    # YOSEMITE SAM (1945)
    yosemite_sam = _wb(
        name="Yosemite Sam",
        description=(
            "The angriest, loudest, most aggressively mustachioed gunslinger in "
            "the West — and Bugs Bunny's most temperamentally explosive adversary. "
            "Yosemite Sam was created by Friz Freleng specifically because Freleng "
            "felt Elmer Fudd was too passive — he wanted a villain who could "
            "plausibly threaten Bugs. Sam's enormous red mustache, his constant "
            "explosive rage, and his Southern drawl made him instantly iconic. "
            "He appears as a pirate, a knight, a space villain, and in countless "
            "other roles across the WB shorts."
        ),
        character_type="Human — explosive-tempered gunslinger / villain",
        debut_year=1945,
        directors=[FRIZ_FRELENG],
        series_list=LOONEY_SERIES + [
            Series("Hare Trigger debut", 1945, 1945,
                   "Warner Bros. Cartoons", "theatrical short",
                   notes="First appearance. Freleng created Sam as a more aggressive Bugs adversary."),
        ],
        eras=[
            Era(1945, None,
                "Tiny but volcanic gunslinger — enormous red mustache larger than his body, "
                "cowboy hat, pistols always drawn, perpetual fury",
                art_style="Technicolor cel / digital",
                image_url=IMG["looney"],
                notes="Debuted in Hare Trigger (1945). "
                      "Voiced by Mel Blanc. "
                      "Freleng based Sam partly on himself — particularly his explosive temper. "
                      "Sam is one of the most versatile Looney Tunes characters, "
                      "appearing in Western, pirate, medieval, and science fiction settings."),
        ],
        wiki_slug="Yosemite_Sam",
    )
    lib.add_cartoon(yosemite_sam)

    # TWEETY'S CAT NEMESIS — ALSO Lola Bunny
    lola = _wb(
        name="Lola Bunny",
        description=(
            "Bugs Bunny's girlfriend — a confident, athletic female rabbit "
            "introduced in Space Jam (1996) who is as skilled a basketball "
            "player as any of her teammates and bristles at being called doll. "
            "Lola was reinvented as a more comedic, quirky character in "
            "The Looney Tunes Show (2011) where her confident exterior conceals "
            "genuine eccentricity. She is the most prominent female character "
            "in the Looney Tunes franchise."
        ),
        character_type="Anthropomorphic animal — rabbit / athlete",
        debut_year=1996,
        directors=[],
        series_list=[
            Series("Space Jam theatrical feature", 1996, 1996,
                   "Warner Bros. Pictures", "theatrical feature"),
            Series("Baby Looney Tunes", 2002, 2005,
                   "Warner Bros. Animation", "TV series"),
            Series("The Looney Tunes Show", 2011, 2014,
                   "Warner Bros. Animation / Cartoon Network", "TV series", episode_count=52),
            Series("Space Jam A New Legacy", 2021, 2021,
                   "Warner Bros. Pictures", "theatrical feature"),
        ],
        eras=[
            Era(1996, 2010,
                "Space Jam era — athletic confident rabbit in purple basketball uniform, "
                "distinctive don't call me doll attitude",
                art_style="Flat color animation / CGI",
                image_url=IMG["lola"],
                notes="Created for Space Jam (1996) as a love interest for Bugs. "
                      "Voiced by Kath Soucie. Lola was designed to be a capable athlete "
                      "not a traditional passive love interest."),
            Era(2011, None,
                "The Looney Tunes Show era — same design but personality reimagined "
                "as comedically overconfident and delightfully odd",
                art_style="Digital animation",
                image_url=IMG["lola"],
                notes="The 2011 series reinvented Lola as a comedy character rather than "
                      "a straight action hero. Kristen Wiig voiced her to great acclaim. "
                      "The reimagining divided fans but is often cited as the best modern WB character work."),
        ],
        wiki_slug="Lola_Bunny",
        origin="Burbank, California, USA — Warner Bros. Pictures / Warner Bros. Animation",
    )
    lib.add_cartoon(lola)

    # HENERY HAWK (1942)
    henery = _wb(
        name="Henery Hawk",
        description=(
            "A tiny but magnificently confident chicken hawk who is absolutely "
            "certain he can catch and eat a chicken regardless of size disparities. "
            "Henery's total conviction in his own predatory abilities despite "
            "being roughly the size of a tennis ball makes him one of Looney "
            "Tunes' most purely comedic creations. He serves as Foghorn Leghorn's "
            "primary nemesis and is delightfully oblivious to the absurdity "
            "of his position."
        ),
        character_type="Anthropomorphic animal — chicken hawk / tiny predator",
        debut_year=1942,
        directors=[CHUCK_JONES, MCKIMSON],
        series_list=LOONEY_SERIES + [
            Series("Henery Hawk theatrical shorts", 1942, 1955,
                   "Warner Bros. Cartoons", "theatrical short", episode_count=8),
        ],
        eras=[
            Era(1942, None,
                "Tiny fierce hawk — minute body, enormous attitude, "
                "complete confidence in his hunting ability",
                art_style="Technicolor cel / digital",
                image_url=IMG["foghorn"],
                notes="Debuted in The Squawkin Hawk (1942) by Chuck Jones. "
                      "Became primarily a Foghorn Leghorn foil under McKimson's direction. "
                      "Mel Blanc gave him a small high voice that perfectly contrasted his big attitude."),
        ],
        wiki_slug="Henery_Hawk",
    )
    lib.add_cartoon(henery)

    # SAM THE SHEEPDOG AND RALPH WOLF (1952)
    sam_ralph = _wb(
        name="Sam Sheepdog and Ralph Wolf",
        description=(
            "A sheepdog named Sam and a wolf named Ralph who are sworn enemies "
            "during working hours — Ralph endlessly attempts to steal sheep while "
            "Sam foils him with casual efficiency — but clock in and out together "
            "as polite coworkers, sharing lunches and friendly conversation. "
            "Chuck Jones created this series as a meditation on the absurdity "
            "of professional enmity and the separation of work from personal "
            "relationships. One of Looney Tunes' most philosophically interesting premises."
        ),
        character_type="Anthropomorphic animals — sheepdog and wolf / professional rivals",
        debut_year=1952,
        directors=[CHUCK_JONES],
        series_list=LOONEY_SERIES + [
            Series("Don't Give Up the Sheep debut", 1952, 1952,
                   "Warner Bros. Cartoons", "theatrical short"),
            Series("Sam and Ralph theatrical shorts", 1952, 1963,
                   "Warner Bros. Cartoons / Jones unit", "theatrical short", episode_count=7),
        ],
        eras=[
            Era(1952, None,
                "Sam — shaggy sheepdog barely visible under fur; Ralph — Wile E. Coyote-like wolf "
                "in professional attire for clocking in",
                art_style="Technicolor cel animation",
                image_url=IMG["looney"],
                notes="Debuted in Don't Give Up the Sheep (1952). "
                      "Chuck Jones and Michael Maltese created the series. "
                      "The punch-clock premise made the series unique in the WB catalog — "
                      "enmity as a job rather than a personal matter."),
        ],
        wiki_slug="Ralph_Wolf_and_Sam_Sheepdog",
    )
    lib.add_cartoon(sam_ralph)

    # MICHIGAN J. FROG (1955)
    michigan_frog = _wb(
        name="Michigan J. Frog",
        description=(
            "A frog discovered in a cornerstone of a demolished building who "
            "performs elaborate vaudeville song-and-dance routines — including "
            "Hello! Ma Baby — but only when alone with the construction worker "
            "who found him, reverting to a silent ordinary frog whenever anyone "
            "else is present. One-Froggy-Evening (1955) is frequently cited by "
            "animation professionals as the single greatest cartoon ever made. "
            "Michigan J. Frog later became the mascot of the WB Television Network."
        ),
        character_type="Anthropomorphic animal — singing frog",
        debut_year=1955,
        directors=[CHUCK_JONES],
        series_list=[
            Series("One-Froggy-Evening theatrical short", 1955, 1955,
                   "Warner Bros. Cartoons", "theatrical short",
                   notes="Frequently cited by animation professionals as the greatest cartoon ever made."),
            Series("WB Network mascot appearances", 1995, 2006,
                   "The WB Television Network", "TV network mascot"),
        ],
        eras=[
            Era(1955, None,
                "Simple green frog — top hat and cane only during performances, "
                "ordinary frog in all other circumstances",
                art_style="Technicolor cel animation",
                image_url=IMG["looney"],
                notes="One-Froggy-Evening (December 31 1955) by Chuck Jones. "
                      "No dialogue except the frog's songs. "
                      "The horror of the construction worker's situation — "
                      "a frog that only performs for him — is treated with genuine pathos. "
                      "Jerry Beck and other animation historians consistently rank it "
                      "the greatest single cartoon ever produced."),
        ],
        wiki_slug="Michigan_J._Frog",
    )
    lib.add_cartoon(michigan_frog)

    # PEPÉ'S CAT — Penelope Pussycat (1945)
    penelope = _wb(
        name="Penelope Pussycat",
        description=(
            "The black cat with a white stripe who is perpetually mistaken "
            "for a female skunk by Pepe Le Pew and endlessly pursued by his "
            "overwhelming romantic attention. Penelope is the straight character "
            "in the Pepe series — her genuine terror and revulsion at Pepe's "
            "odor and persistence provides the grounding reality against which "
            "Pepe's oblivious confidence plays. She often finds clever ways to "
            "escape but Pepe always catches her."
        ),
        character_type="Anthropomorphic animal — cat",
        debut_year=1945,
        directors=[CHUCK_JONES],
        series_list=LOONEY_SERIES + [
            Series("Pepe Le Pew theatrical shorts (as Penelope)", 1945, 1962,
                   "Warner Bros. Cartoons", "theatrical short"),
        ],
        eras=[
            Era(1945, None,
                "Black cat with white stripe painted on her back — "
                "her horror at Pepe's pursuit is the core comedy engine",
                art_style="Technicolor cel / various",
                image_url=IMG["pepe"],
                notes="The white stripe is always accidental — paint, chalk, a skunk's spray — "
                      "making Penelope an unwilling participant in Pepe's romantic fantasies. "
                      "Voiced by various actresses over the years. "
                      "The character's name Penelope Pussycat was not established until merchandise."),
        ],
        wiki_slug="Penelope_Pussycat",
    )
    lib.add_cartoon(penelope)

    # ══════════════════════════════════════════════════════════════════════
    # EARLY LOONEY TUNES (Pre-1940)
    # ══════════════════════════════════════════════════════════════════════

    bosko = _wb(
        name="Bosko",
        description=(
            "The very first recurring Looney Tunes character — a black cartoon "
            "boy of ambiguous species (described as a human ink-blot) who starred "
            "in the earliest Warner Bros. cartoons from 1930 to 1933. Created by "
            "Hugh Harman and Rudolf Ising before they left Warner Bros. for MGM, "
            "Bosko starred in the first sound Looney Tune Sinkin' in the Bathtub. "
            "He is an important but complicated figure in animation history "
            "as his design reflected the racial caricatures common in 1930s media."
        ),
        character_type="Cartoon character — early animated protagonist",
        debut_year=1930,
        directors=[Creator("Hugh Harman", "Co-creator & director", 1903, 1982),
                   Creator("Rudolf Ising", "Co-creator & director", 1903, 1992)],
        series_list=[
            Series("Bosko Looney Tunes shorts", 1930, 1933,
                   "Harman-Ising Productions / Warner Bros.", "theatrical short", episode_count=39),
        ],
        eras=[
            Era(1930, 1933,
                "Original Harman-Ising design — simple cartoon figure, rubber-hose animation, "
                "earliest Warner Bros. character",
                art_style="Black & white then early color",
                image_url=IMG["looney"],
                notes="Sinkin' in the Bathtub (April 19 1930) was the first Looney Tune ever released. "
                      "Bosko left WB when Harman and Ising departed for MGM in 1933. "
                      "The character is now primarily discussed in historical animation contexts."),
        ],
        wiki_slug="Bosko",
        origin="Los Angeles, California, USA — Harman-Ising Productions / Warner Bros.",
    )
    lib.add_cartoon(bosko)

    # BUDDY (1933)
    buddy = _wb(
        name="Buddy",
        description=(
            "Bosko's replacement after Harman and Ising left for MGM — "
            "a generic, personality-free cartoon boy who starred in 23 "
            "Looney Tunes shorts from 1933 to 1935 before being replaced "
            "by Porky Pig. Buddy is notable primarily for being one of "
            "animation history's most spectacularly unsuccessful characters — "
            "audiences found him completely unengaging, which directly "
            "motivated the studio to develop Porky Pig and eventually "
            "the entire Looney Tunes golden age cast."
        ),
        character_type="Cartoon character — generic boy protagonist",
        debut_year=1933,
        directors=[Creator("Tom Palmer", "Director", 1906, 1984),
                   Creator("Earl Duvall", "Director", 1897, 1940)],
        series_list=[
            Series("Buddy Looney Tunes shorts", 1933, 1935,
                   "Warner Bros. Cartoons", "theatrical short", episode_count=23),
        ],
        eras=[
            Era(1933, 1935,
                "Generic cartoon boy — deliberately designed to be Bosko's replacement "
                "but without Bosko's anarchic energy",
                art_style="Black & white / early color",
                image_url=IMG["looney"],
                notes="Buddy was so personality-free that animators nicknamed him the nothing character. "
                      "His spectacular failure directly motivated Warner Bros. "
                      "to develop Porky Pig and the golden age approach. "
                      "Buddy is remembered as one of animation's most famous failures."),
        ],
        wiki_slug="Buddy_(Looney_Tunes)",
    )
    lib.add_cartoon(buddy)

    # ══════════════════════════════════════════════════════════════════════
    # WB ANIMATION ERA (1980s–2000s)
    # ══════════════════════════════════════════════════════════════════════

    # TINY TOON ADVENTURES (1990)
    buster_babs = _wb(
        name="Buster and Babs Bunny (Tiny Toons)",
        description=(
            "No relation! Buster Bunny and Babs Bunny are the male and female "
            "leads of Tiny Toon Adventures — students at Acme Looniversity where "
            "they study under the Looney Tunes legends. Buster is cool and "
            "resourceful like Bugs while Babs is energetic and impressionistic. "
            "Tiny Toon Adventures was the show that relaunched Warner Bros. "
            "Animation and began the golden age of WB animated TV including "
            "Animaniacs, Pinky and the Brain, and Batman: The Animated Series."
        ),
        character_type="Anthropomorphic animals — rabbit duo / animation students",
        debut_year=1990,
        directors=[],
        series_list=[
            Series("Tiny Toon Adventures", 1990, 1992,
                   "Warner Bros. Animation / Amblin Entertainment / Fox Kids", "TV series", episode_count=98),
            Series("Tiny Toons Looniversity HBO Max reboot", 2023, None,
                   "Warner Bros. Animation / HBO Max", "streaming series"),
        ],
        eras=[
            Era(1990, 1992,
                "Original series — Buster in blue, Babs in pink, "
                "student versions of classic WB energy",
                art_style="Flat color TV cel",
                image_url=IMG["tiny"],
                notes="Debuted September 14 1990. Executive produced by Steven Spielberg with Warner Bros. "
                      "The show relaunched WB Animation and set the template for the 1990s golden age. "
                      "John Byrne and Tom Ruegger created the series."),
            Era(2023, None,
                "Looniversity reboot — updated design for HBO Max streaming audience",
                art_style="Modern digital animation",
                image_url=IMG["tiny"],
                notes="The 2023 HBO Max reboot updated the premise for a new generation."),
        ],
        wiki_slug="Tiny_Toon_Adventures",
        origin="Burbank, California, USA — Warner Bros. Animation / Amblin Entertainment",
    )
    lib.add_cartoon(buster_babs)

    # ANIMANIACS — YAKKO, WAKKO, DOT (1993)
    animaniacs = _wb(
        name="Yakko, Wakko and Dot (Animaniacs)",
        description=(
            "The Warner siblings — Yakko (the fast-talking eldest), Wakko "
            "(the food-obsessed middle child), and Dot (the cute but dangerous "
            "youngest) — escaped from the Warner Bros. water tower where they "
            "were locked during the 1930s and now run amok through the studio "
            "and across history. Animaniacs was the most culturally sophisticated "
            "American animated series of the 1990s — layering adult satire, "
            "genuine slapstick, musical parody, and educational content simultaneously."
        ),
        character_type="Cartoon animals — anarchic sibling trio",
        debut_year=1993,
        directors=[],
        series_list=[
            Series("Animaniacs original run", 1993, 1998,
                   "Warner Bros. Animation / Amblin Entertainment / Fox Kids / WB", "TV series", episode_count=99),
            Series("Animaniacs reboot", 2020, 2023,
                   "Warner Bros. Animation / Amblin Entertainment / Hulu", "streaming series", episode_count=39),
        ],
        eras=[
            Era(1993, 1998,
                "Original — black and white cartoon characters with gloves and ears, "
                "timeless design that belongs to no specific era",
                art_style="Flat color TV cel",
                image_url=IMG["animaniacs"],
                notes="Debuted September 13 1993. Created by Tom Ruegger. "
                      "Steven Spielberg executive produced. "
                      "The show's educational segments — Wakko's America, Nations of the World — "
                      "became genuine teaching tools. The 1990s run is considered a creative peak."),
            Era(2020, 2023,
                "Hulu reboot — same characters updated for contemporary streaming audience "
                "with more topical satire",
                art_style="Modern digital animation",
                image_url=IMG["animaniacs"],
                notes="The Hulu reboot ran for three seasons. "
                      "Original voice cast Rob Paulsen, Jess Harnell, and Tress MacNeille returned."),
        ],
        wiki_slug="Animaniacs",
        origin="Burbank, California, USA — Warner Bros. Animation / Amblin Entertainment",
    )
    lib.add_cartoon(animaniacs)

    # PINKY AND THE BRAIN (1995)
    pinky_brain = _wb(
        name="Pinky and the Brain",
        description=(
            "Two genetically enhanced laboratory mice from Acme Labs — "
            "Brain, a genius mouse with plans for global domination, "
            "and Pinky, his good-natured but spectacularly dim companion "
            "whose accidental brilliance consistently ruins Brain's schemes. "
            "Their nightly ritual: Pinky asks what they're going to do tonight "
            "and Brain replies they're going to try to take over the world. "
            "Originated in Animaniacs before spinning off into their own series."
        ),
        character_type="Anthropomorphic animals — laboratory mice duo",
        debut_year=1995,
        directors=[],
        series_list=[
            Series("Animaniacs (Pinky and the Brain segments)", 1993, 1998,
                   "Warner Bros. Animation", "TV series segments"),
            Series("Pinky and the Brain", 1995, 1998,
                   "Warner Bros. Animation / The WB", "TV series", episode_count=65),
            Series("Pinky Elmyra and the Brain", 1998, 1999,
                   "Warner Bros. Animation / The WB", "TV series", episode_count=13,
                   notes="Widely considered a disappointing spinoff by both fans and its creators."),
            Series("Animaniacs reboot featuring Pinky and the Brain", 2020, 2023,
                   "Warner Bros. Animation / Hulu", "streaming series"),
        ],
        eras=[
            Era(1993, 1998,
                "Original — Brain modeled on Orson Welles, Pinky on Rob Paulsen's own physicality, "
                "Acme Labs setting",
                art_style="Flat color TV cel",
                image_url=IMG["pinky"],
                notes="Created by Tom Ruegger. Voice cast: Rob Paulsen (Pinky) and Maurice LaMarche (Brain). "
                      "LaMarche's Brain voice was inspired by Orson Welles — "
                      "a choice that paid off spectacularly in the Orson Welles parody episodes. "
                      "Won four Emmy Awards."),
            Era(2020, None,
                "Hulu reboot — same chemistry updated for contemporary satire",
                art_style="Modern digital animation",
                image_url=IMG["pinky"],
                notes="The Hulu Animaniacs reboot brought back Pinky and Brain with the original cast. "
                      "Their segments were widely praised as the highlight of the reboot series."),
        ],
        wiki_slug="Pinky_and_the_Brain",
        origin="Burbank, California, USA — Warner Bros. Animation",
    )
    lib.add_cartoon(pinky_brain)

    # FREAKAZOID! (1995)
    freakazoid = _wb(
        name="Freakazoid!",
        description=(
            "Dexter Douglas, a nerdy teenager who is accidentally sucked into "
            "the internet and emerges with superpowers and a completely unhinged "
            "personality as Freakazoid — a superhero who routinely breaks the "
            "fourth wall, goes on irrelevant tangents, and generally ignores "
            "the plot in favor of whatever he finds more interesting. "
            "Created by Bruce Timm and Paul Dini but taken in a more comedic "
            "direction by Tom Ruegger and John McCann, Freakazoid! is one of "
            "the most purely funny WB animated series ever made."
        ),
        character_type="Human / superhero — internet-powered goofball",
        debut_year=1995,
        directors=[],
        series_list=[
            Series("Freakazoid!", 1995, 1997,
                   "Warner Bros. Animation / Amblin Entertainment / The WB", "TV series", episode_count=24),
        ],
        eras=[
            Era(1995, 1997,
                "Original series — blue-skinned superhero with white streaked hair, "
                "manic fourth-wall-breaking energy",
                art_style="Flat color TV cel",
                image_url=IMG["freakazoid"],
                notes="Created by Bruce Timm and Paul Dini, reimagined by Tom Ruegger and John McCann. "
                      "Won two Daytime Emmy Awards. Voiced by Paul Rugg. "
                      "The show abandoned its original serious superhero concept for pure comedy — "
                      "a decision that produced one of WB Animation's most beloved series."),
        ],
        wiki_slug="Freakazoid!",
        origin="Burbank, California, USA — Warner Bros. Animation / Amblin Entertainment",
    )
    lib.add_cartoon(freakazoid)

    # ══════════════════════════════════════════════════════════════════════
    # DC ANIMATED UNIVERSE (WB Animation / Bruce Timm era)
    # ══════════════════════════════════════════════════════════════════════

    batman_tas = _wb(
        name="Batman (The Animated Series)",
        description=(
            "The definitive animated Batman — a brooding, brilliant Dark Knight "
            "in an art deco Gotham City rendered in a revolutionary retro-futurist "
            "visual style. Batman: The Animated Series (1992) redefined superhero "
            "animation, gave the Joker his greatest performance (Mark Hamill), "
            "created Harley Quinn, and is widely considered the greatest superhero "
            "animated series ever made. Its influence on all subsequent DC media — "
            "animated and live-action — cannot be overstated."
        ),
        character_type="Human — superhero / DC Comics character",
        debut_year=1992,
        directors=[],
        series_list=[
            Series("Batman The Animated Series", 1992, 1995,
                   "Warner Bros. Animation / Fox Kids", "TV series", episode_count=85),
            Series("Batman Mask of the Phantasm theatrical film", 1993, 1993,
                   "Warner Bros. Animation / Warner Bros. Pictures", "theatrical feature"),
            Series("The New Batman Adventures", 1997, 1999,
                   "Warner Bros. Animation / Kids WB", "TV series", episode_count=24),
            Series("Justice League animated series", 2001, 2004,
                   "Warner Bros. Animation / Cartoon Network", "TV series"),
            Series("Justice League Unlimited", 2004, 2006,
                   "Warner Bros. Animation / Cartoon Network", "TV series"),
        ],
        eras=[
            Era(1992, 1998,
                "DCAU Bruce Timm design — art deco Gotham, dark retro-futurist aesthetic, "
                "Kevin Conroy as the definitive Batman voice",
                art_style="Noir-influenced flat color animation",
                image_url=IMG["batman"],
                notes="Debuted September 5 1992. Created by Bruce Timm and Paul Dini. "
                      "Kevin Conroy voiced Batman — a role he held until his death in 2022. "
                      "Mark Hamill voiced the Joker. The show created Harley Quinn "
                      "who became a major DC character across all media."),
            Era(1999, None,
                "Evolved DCAU and beyond — redesigned for New Batman Adventures, "
                "then referenced across all subsequent DC animation",
                art_style="Simplified DCAU style / various modern",
                image_url=IMG["batman"],
                notes="The New Batman Adventures (1997) updated the designs. "
                      "Kevin Conroy continued voicing Batman in Justice League, "
                      "Batman Beyond, and multiple animated films until 2022."),
        ],
        wiki_slug="Batman:_The_Animated_Series",
        origin="Burbank, California, USA — Warner Bros. Animation",
    )
    batman_tas.ownership_history.clear()
    batman_tas.add_ownership_record(OwnershipRecord(
        "DC Comics / Warner Bros. Discovery", 1939, None,
        "Batman created by Bob Kane and Bill Finger for DC Comics in 1939 — "
        "Warner Bros. Animation produced under license",
        is_current_owner=True))
    lib.add_cartoon(batman_tas)

    # HARLEY QUINN (created in BTAS)
    harley = _wb(
        name="Harley Quinn",
        description=(
            "Dr. Harleen Quinzel — the Joker's psychiatrist at Arkham Asylum "
            "who fell in love with her patient and became his devoted henchwoman. "
            "Created by Paul Dini and Bruce Timm exclusively for Batman: The "
            "Animated Series, Harley Quinn became so popular that DC Comics "
            "retroactively introduced her into the comics continuity. "
            "She later became one of DC's most prominent standalone characters, "
            "appearing in films and her own Harley Quinn animated series on HBO Max."
        ),
        character_type="Human — villain / antihero / DC Comics character",
        debut_year=1992,
        directors=[],
        series_list=[
            Series("Batman The Animated Series", 1992, 1995,
                   "Warner Bros. Animation / Fox Kids", "TV series"),
            Series("Harley Quinn animated series", 2019, None,
                   "Warner Bros. Animation / DC Universe / HBO Max", "streaming series"),
            Series("Birds of Prey film", 2020, 2020,
                   "Warner Bros. Pictures", "theatrical feature"),
            Series("The Suicide Squad", 2021, 2021,
                   "Warner Bros. Pictures", "theatrical feature"),
        ],
        eras=[
            Era(1992, 2011,
                "BTAS original design — red and black harlequin costume, blonde pigtails underneath, "
                "devotedly loyal to the Joker",
                art_style="DCAU flat color animation / comics",
                image_url=IMG["batman"],
                notes="Created by Paul Dini and Bruce Timm. Voiced by Arleen Sorkin. "
                      "First appeared in Joker's Favor (September 11 1992). "
                      "Introduced into DC Comics canon in Batman Adventures #12 (1993). "
                      "One of the most successful new characters created for animation."),
            Era(2012, None,
                "New 52 and beyond — redesigned with blonde and pink hair, "
                "more independent identity separate from the Joker",
                art_style="Various modern — comics, animation, live-action",
                image_url=IMG["batman"],
                notes="Margot Robbie played Harley in Suicide Squad (2016) and Birds of Prey (2020). "
                      "The HBO Max Harley Quinn animated series (2019) gave her a full standalone story. "
                      "Kaley Cuoco voices Harley in the streaming series."),
        ],
        wiki_slug="Harley_Quinn",
        origin="Burbank, California, USA — Warner Bros. Animation (created for animated series)",
    )
    harley.ownership_history.clear()
    harley.add_ownership_record(OwnershipRecord(
        "DC Comics / Warner Bros. Discovery", 1992, None,
        "Created for Batman: The Animated Series — now a major DC Comics character",
        is_current_owner=True))
    lib.add_cartoon(harley)

    # SUPERMAN: THE ANIMATED SERIES (1996)
    superman_tas = _wb(
        name="Superman (The Animated Series)",
        description=(
            "The Man of Steel in the DCAU — Clark Kent, last son of Krypton, "
            "raised in Smallville and working at the Daily Planet in Metropolis. "
            "Superman: The Animated Series was the direct follow-up to BTAS "
            "using the same visual language but a brighter palette appropriate "
            "to the optimistic hero. Tim Daly's vocal performance defined "
            "animated Superman for a generation. Brainiac, Livewire, and "
            "other original villains were introduced."
        ),
        character_type="Human / alien — superhero / DC Comics character",
        debut_year=1996,
        directors=[],
        series_list=[
            Series("Superman The Animated Series", 1996, 2000,
                   "Warner Bros. Animation / Kids WB", "TV series", episode_count=54),
            Series("Justice League animated series", 2001, 2004,
                   "Warner Bros. Animation / Cartoon Network", "TV series"),
            Series("Justice League Unlimited", 2004, 2006,
                   "Warner Bros. Animation / Cartoon Network", "TV series"),
        ],
        eras=[
            Era(1996, None,
                "DCAU Superman — bright primary colors, art deco Metropolis, "
                "Tim Daly as Clark / Dana Delany as Lois Lane",
                art_style="DCAU flat color animation",
                image_url=IMG["superman"],
                notes="Debuted September 6 1996. Created by Bruce Timm, Paul Dini, and Alan Burnett. "
                      "Tim Daly voiced Superman. The show introduced Livewire — "
                      "an original villain who later appeared in the comics."),
        ],
        wiki_slug="Superman:_The_Animated_Series",
        origin="Burbank, California, USA — Warner Bros. Animation",
    )
    superman_tas.ownership_history.clear()
    superman_tas.add_ownership_record(OwnershipRecord(
        "DC Comics / Warner Bros. Discovery", 1938, None,
        "Superman created by Jerry Siegel and Joe Shuster for Action Comics #1 in 1938",
        is_current_owner=True))
    lib.add_cartoon(superman_tas)

    # BATMAN BEYOND (1999)
    batman_beyond = _wb(
        name="Batman Beyond (Terry McGinnis)",
        description=(
            "Set in futuristic Gotham City in 2039 — a teenage boy named Terry "
            "McGinnis becomes the new Batman under the mentorship of an elderly "
            "Bruce Wayne, using a high-tech Batsuit to battle villains of the "
            "future. Batman Beyond was created at network request for a teenage "
            "Batman but exceeded all expectations becoming a critically acclaimed "
            "series with genuine emotional depth. The show explored what Batman "
            "means as a legacy rather than an individual."
        ),
        character_type="Human — teenage Batman / DC Comics character",
        debut_year=1999,
        directors=[],
        series_list=[
            Series("Batman Beyond", 1999, 2001,
                   "Warner Bros. Animation / Kids WB", "TV series", episode_count=52),
            Series("Batman Beyond Return of the Joker film", 2000, 2000,
                   "Warner Bros. Animation", "direct-to-video feature"),
        ],
        eras=[
            Era(1999, 2001,
                "Futuristic all-black Batsuit with red bat symbol — "
                "sleek aerodynamic design appropriate to 2039 Gotham",
                art_style="DCAU flat color animation with sleeker future aesthetic",
                image_url=IMG["batman_beyond"],
                notes="Debuted January 10 1999. Created by Bruce Timm, Paul Dini, and Alan Burnett. "
                      "Will Friedle voiced Terry. Kevin Conroy continued as Bruce Wayne. "
                      "Return of the Joker (2000) is considered one of the best DC animated films. "
                      "The uncut version was initially withheld due to violent content."),
        ],
        wiki_slug="Batman_Beyond",
        origin="Burbank, California, USA — Warner Bros. Animation",
    )
    batman_beyond.ownership_history.clear()
    batman_beyond.add_ownership_record(OwnershipRecord(
        "DC Comics / Warner Bros. Discovery", 1999, None,
        "Created for animation — later introduced into DC Comics continuity",
        is_current_owner=True))
    lib.add_cartoon(batman_beyond)

    # JUSTICE LEAGUE (2001)
    justice_league = _wb(
        name="Justice League (animated)",
        description=(
            "The founding seven members of the Justice League — Superman, Batman, "
            "Wonder Woman, The Flash, Green Lantern (John Stewart), Hawkgirl, "
            "and Martian Manhunter — team up to face threats too large for any "
            "individual hero. Justice League and its sequel Justice League Unlimited "
            "represent the culmination of the Bruce Timm DCAU — a grand unified "
            "DC universe that remains the gold standard for superhero ensemble "
            "animation."
        ),
        character_type="Superhero ensemble — DC Comics characters",
        debut_year=2001,
        directors=[],
        series_list=[
            Series("Justice League", 2001, 2004,
                   "Warner Bros. Animation / Cartoon Network", "TV series", episode_count=52),
            Series("Justice League Unlimited", 2004, 2006,
                   "Warner Bros. Animation / Cartoon Network", "TV series", episode_count=39),
        ],
        eras=[
            Era(2001, 2006,
                "DCAU Justice League — consistent Bruce Timm art style across all seven members, "
                "John Stewart as Green Lantern (first major Black superhero lead in DC animation)",
                art_style="DCAU flat color animation",
                image_url=IMG["justice"],
                notes="Debuted November 17 2001. Created by Bruce Timm. "
                      "The choice of John Stewart as Green Lantern introduced millions of children "
                      "to a Black superhero lead — a significant representation milestone. "
                      "Justice League Unlimited expanded the roster to nearly every DC hero."),
        ],
        wiki_slug="Justice_League_(TV_series)",
        origin="Burbank, California, USA — Warner Bros. Animation",
    )
    justice_league.ownership_history.clear()
    justice_league.add_ownership_record(OwnershipRecord(
        "DC Comics / Warner Bros. Discovery", 1960, None,
        "Justice League created 1960 — animated series produced by Warner Bros. Animation",
        is_current_owner=True))
    lib.add_cartoon(justice_league)

    # STATIC SHOCK (2000)
    static = _wb(
        name="Static Shock (Virgil Hawkins)",
        description=(
            "Virgil Hawkins is a Black teenage superhero from Dakota City who "
            "gains electromagnetic superpowers after a gang war chemical explosion "
            "and becomes Static — a wisecracking electricity-based hero. "
            "Created by Milestone Media and Dwayne McDuffie, Static Shock was "
            "one of the first animated superhero series to center a Black "
            "protagonist and to address issues like gang violence, racism, "
            "and gun control directly."
        ),
        character_type="Human — teenage superhero / DC / Milestone Comics character",
        debut_year=2000,
        directors=[],
        series_list=[
            Series("Static Shock", 2000, 2004,
                   "Warner Bros. Animation / Kids WB", "TV series", episode_count=52),
        ],
        eras=[
            Era(2000, 2004,
                "Original animated design — teenage Black hero in blue and white costume "
                "with electromagnetic disc and lightning powers",
                art_style="DCAU-influenced flat color animation",
                image_url=IMG["static"],
                notes="Debuted September 23 2000. Created by Dwayne McDuffie based on his Milestone Comics character. "
                      "Phil LaMarr voiced Virgil. "
                      "The show addressed gun violence directly — unusual for superhero animation. "
                      "Guest starred many DCAU characters including Batman."),
        ],
        wiki_slug="Static_Shock",
        origin="Burbank, California, USA — Warner Bros. Animation",
    )
    static.ownership_history.clear()
    static.add_ownership_record(OwnershipRecord(
        "DC Comics / Warner Bros. Discovery (via Milestone Media acquisition)", 1993, None,
        "Static created by Dwayne McDuffie for Milestone Media in 1993 — "
        "DC acquired Milestone; now Warner Bros. Discovery",
        is_current_owner=True))
    lib.add_cartoon(static)

    # TEEN TITANS (2003)
    teen_titans = _wb(
        name="Teen Titans",
        description=(
            "Robin, Starfire, Raven, Beast Boy, and Cyborg — five teenage "
            "superheroes who live together in Titans Tower and battle villains "
            "while navigating the complexities of adolescence. Teen Titans "
            "blended American superhero action with anime visual influences — "
            "big eyes, speed lines, super-deformed comedy sequences — "
            "creating a distinctive hybrid style that became enormously popular. "
            "The series' emotional depth, particularly Raven's arc, elevated it "
            "beyond typical superhero fare."
        ),
        character_type="Superhero ensemble — teenage DC Comics characters",
        debut_year=2003,
        directors=[],
        series_list=[
            Series("Teen Titans", 2003, 2006,
                   "Warner Bros. Animation / Cartoon Network", "TV series", episode_count=65),
            Series("Teen Titans Go!", 2013, None,
                   "Warner Bros. Animation / Cartoon Network", "TV series",
                   notes="Comedy reimagining of the same characters in a more irreverent format."),
            Series("Teen Titans The Judas Contract film", 2017, 2017,
                   "Warner Bros. Animation", "direct-to-video feature"),
        ],
        eras=[
            Era(2003, 2006,
                "Original series — anime-influenced designs with Western superhero action, "
                "emotional storytelling, distinctive mixed visual style",
                art_style="Anime-influenced American digital animation",
                image_url=IMG["teen"],
                notes="Debuted July 19 2003. Created by Glen Murakami and Sam Register. "
                      "The show's willingness to handle dark emotional content — "
                      "particularly Raven's storylines — distinguished it from typical superhero shows. "
                      "The finale was deeply unsatisfying to fans who wanted more."),
            Era(2013, None,
                "Teen Titans Go! era — same characters in comedic self-aware format, "
                "extremely popular with younger audiences, divisive with older fans",
                art_style="Simple digital animation — comedic exaggeration",
                image_url=IMG["teen"],
                notes="Teen Titans Go! became Cartoon Network's most-aired series. "
                      "Its meta-humor and self-awareness about being a cartoon is sophisticated "
                      "even if its presentation targets younger viewers."),
        ],
        wiki_slug="Teen_Titans_(TV_series)",
        origin="Burbank, California, USA — Warner Bros. Animation",
    )
    teen_titans.ownership_history.clear()
    teen_titans.add_ownership_record(OwnershipRecord(
        "DC Comics / Warner Bros. Discovery", 1964, None,
        "Teen Titans created 1964 — animated series produced by Warner Bros. Animation",
        is_current_owner=True))
    lib.add_cartoon(teen_titans)

    print(f"Warner Bros. characters added. Library now has {len(lib.cartoons)} cartoons total.")
