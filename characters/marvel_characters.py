"""
marvel_characters.py
Marvel Comics animated characters for CartoonPal.

Important distinction for all Marvel characters:
- Marvel Comics / Marvel Entertainment ALWAYS owns the characters
- Different studios PRODUCED animated series under LICENSE at different times
- Grantray-Lawrence Animation produced early Marvel cartoons (1966)
- DePatie-Freleng Enterprises produced Fantastic Four (1978)
- Marvel Productions Ltd. produced in-house (1981-1988)
- Saban Entertainment produced X-Men and Spider-Man (1990s)
- Marvel Animation produces current content (2008-present)

Ownership chain for all Marvel characters:
- Timely Comics / Marvel Comics (1939) — original creation
- Marvel Entertainment Group (1986) — corporate restructuring
- Marvel Enterprises (1998) — emerged from bankruptcy
- Marvel Entertainment / Disney (2009) — Disney acquired Marvel for $4 billion
- Marvel Entertainment / The Walt Disney Company (2009-present)

Usage:
    from characters.marvel_characters import add_marvel_characters
    add_marvel_characters(lib)
"""

from cartoon_system import (
    Cartoon, Creator, ProductionCompany,
    Series, OwnershipRecord, Era, Library
)

MARVEL_STUDIO = ProductionCompany("Marvel Animation / Marvel Entertainment", 1939, country="USA")

STAN_LEE     = Creator("Stan Lee", "Marvel co-creator — Spider-Man, X-Men, Avengers, Iron Man, Thor, Hulk, Fantastic Four", 1922, 2018)
JACK_KIRBY   = Creator("Jack Kirby", "Marvel co-creator — Fantastic Four, X-Men, Captain America, Thor, Hulk", 1917, 1994)
STEVE_DITKO  = Creator("Steve Ditko", "Spider-Man and Doctor Strange co-creator", 1927, 2018)
JOE_SIMON    = Creator("Joe Simon", "Captain America co-creator", 1913, 2011)
LARRY_LIEBER = Creator("Larry Lieber", "Thor, Iron Man, Ant-Man co-creator", 1931)
DON_HECK     = Creator("Don Heck", "Iron Man visual designer", 1929, 1995)
LEN_WEIN     = Creator("Len Wein", "Wolverine creator, X-Men revamp co-writer", 1948, 2017)
CHRIS_CLAREMONT = Creator("Chris Claremont", "Definitive X-Men writer 1975-1991", 1950)

MARVEL_OWNERSHIP = [
    ("Timely Comics / Atlas Comics / Marvel Comics", 1939, 1986,
     "original creation — various characters created 1939-1970s"),
    ("Marvel Entertainment Group", 1986, 1998,
     "corporate restructuring"),
    ("Marvel Enterprises (post-bankruptcy)", 1998, 2009,
     "emerged from 1996 bankruptcy reorganization"),
    ("Marvel Entertainment / The Walt Disney Company", 2009, None,
     "Disney acquired Marvel Entertainment for $4.24 billion",
     ),
]

IMG = {
    "spiderman": "https://upload.wikimedia.org/wikipedia/en/thumb/2/21/Spider-Man_TAS_Logo.png/240px-Spider-Man_TAS_Logo.png",
    "xmen":      "https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/X-Men_the_Animated_Series_logo.png/240px-X-Men_the_Animated_Series_logo.png",
    "avengers":  "https://upload.wikimedia.org/wikipedia/en/thumb/f/f8/Avengers_Earth%27s_Mightiest_Heroes_logo.png/240px-Avengers_Earth%27s_Mightiest_Heroes_logo.png",
    "ironman":   "https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/Iron_Man_animated_logo.png/240px-Iron_Man_animated_logo.png",
    "fantastic": "https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/Fantastic_Four_animated_logo.png/240px-Fantastic_Four_animated_logo.png",
    "hulk":      "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/The_Incredible_Hulk_animated_logo.png/240px-The_Incredible_Hulk_animated_logo.png",
    "captain":   "https://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Captain_America_animated.png/200px-Captain_America_animated.png",
    "thor":      "https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/Thor_animated.png/200px-Thor_animated.png",
    "marvel":    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Marvel_Logo.svg/240px-Marvel_Logo.svg.png",
    "spectacular": "https://upload.wikimedia.org/wikipedia/en/thumb/3/3a/Spectacular_Spider-Man_logo.png/240px-Spectacular_Spider-Man_logo.png",
    "wolverine": "https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/Wolverine_and_the_X-Men_logo.png/240px-Wolverine_and_the_X-Men_logo.png",
    "guardians": "https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/Guardians_of_the_Galaxy_animated_logo.png/200px-Guardians_of_the_Galaxy_animated_logo.png",
}


def _marvel(name, description, character_type, debut_year,
            creators, series_list, eras, wiki_slug,
            origin="New York City, USA — Marvel Comics"):
    c = Cartoon(name=name, description=description,
                character_type=character_type,
                country_of_origin="USA", debut_year=debut_year)
    c.original_studio = MARVEL_STUDIO
    for cr in creators:
        c.add_creator(cr)
    for s in series_list:
        c.add_series(s)
    for i, rec in enumerate(MARVEL_OWNERSHIP):
        is_cur = (i == len(MARVEL_OWNERSHIP) - 1)
        c.add_ownership_record(OwnershipRecord(
            rec[0], rec[1], rec[2], rec[3], is_current_owner=is_cur,
        ))
    for era in eras:
        c.add_era(era)
    c.wiki_url = f"https://en.wikipedia.org/wiki/{wiki_slug}"
    c.origin_location = origin
    return c


def add_marvel_characters(lib: Library):

    # ══════════════════════════════════════════════════════════════════════
    # SPIDER-MAN (1962)
    # ══════════════════════════════════════════════════════════════════════
    spiderman = _marvel(
        name="Spider-Man (animated history)",
        description=(
            "Peter Parker — a shy, nerdy high school student bitten by a radioactive "
            "spider who gains proportional strength and agility, wall-crawling ability, "
            "and a spider-sense. His uncle Ben's murder teaches him that with great "
            "power comes great responsibility. Spider-Man is Marvel's most iconic "
            "character and has appeared in more animated series than any other Marvel hero — "
            "every decade from the 1960s to the 2020s has featured at least one "
            "Spider-Man animated series. Each generation has its own defining version. "
            "NOTE: Marvel / Disney has always owned Spider-Man — different studios "
            "produced animated versions under license at different times."
        ),
        character_type="Human — Marvel Comics superhero / Friendly Neighborhood Spider-Man",
        debut_year=1962,
        creators=[STAN_LEE, STEVE_DITKO],
        series_list=[
            Series("Spider-Man (Grantray-Lawrence / Krantz Films)", 1967, 1970,
                   "Grantray-Lawrence Animation / Krantz Films / ABC", "TV series", episode_count=52,
                   notes="PRODUCER: Grantray-Lawrence Animation under Marvel license. "
                         "The original Spider-Man cartoon. Theme song by Bob Harris became "
                         "one of the most recognizable in animation history. "
                         "Heavily recycled animation — infamous for reusing footage constantly."),
            Series("Spider-Man (DePatie-Freleng)", 1970, 1970,
                   "DePatie-Freleng Enterprises", "TV series", episode_count=17,
                   notes="PRODUCER: DePatie-Freleng under Marvel license. "
                         "Final season of the original show, produced by a different studio."),
            Series("Spider-Man and His Amazing Friends", 1981, 1983,
                   "Marvel Productions Ltd. / NBC", "TV series", episode_count=24,
                   notes="PRODUCER: Marvel Productions (in-house). Spider-Man teams with Iceman "
                         "and Firestar (a new character created for the show). "
                         "One of the most beloved Spider-Man animated series."),
            Series("Spider-Man (1981 solo series)", 1981, 1982,
                   "Marvel Productions Ltd. / NBC", "TV series", episode_count=26,
                   notes="PRODUCER: Marvel Productions. Aired simultaneously with Amazing Friends. "
                         "More faithful solo adventures."),
            Series("Spider-Man: The Animated Series (Fox Kids)", 1994, 1998,
                   "Marvel Films Animation / Saban Entertainment / Fox Kids", "TV series", episode_count=65,
                   notes="PRODUCER: Saban Entertainment / Marvel Films Animation under Fox license. "
                         "Christopher Daniel Barnes voiced Spider-Man. "
                         "Rich multi-season mythology. Widely considered the definitive Spider-Man cartoon. "
                         "Introduced the Secret Wars and Spider-Man clone sagas to animation."),
            Series("Spider-Man Unlimited", 1999, 2001,
                   "Marvel Films Animation / Fox Kids", "TV series", episode_count=13,
                   notes="PRODUCER: Marvel Films Animation. Set on Counter-Earth — Spider-Man in a "
                         "new world with a new suit. Cancelled before conclusion."),
            Series("The Spectacular Spider-Man", 2008, 2009,
                   "Sony Pictures Television / Marvel Animation", "TV series", episode_count=26,
                   notes="PRODUCER: Sony Pictures Television under Marvel license. "
                         "Greg Weisman (Gargoyles) created and produced. "
                         "Josh Keaton voiced Spider-Man. Widely praised as the best Spider-Man series. "
                         "Cancelled when Disney acquired Marvel and Sony lost the license."),
            Series("Ultimate Spider-Man", 2012, 2017,
                   "Marvel Animation / Disney XD", "TV series", episode_count=104,
                   notes="PRODUCER: Marvel Animation (in-house post-Disney acquisition). "
                         "Comedic fourth-wall-breaking format. Drake Bell voiced Spider-Man."),
            Series("Spider-Man (2017 series)", 2017, 2020,
                   "Marvel Animation / Disney XD", "TV series", episode_count=78,
                   notes="PRODUCER: Marvel Animation. More faithful to classic comics. "
                         "Robbie Daymond voiced Spider-Man."),
            Series("Marvel's Spider-Man: Maximum Venom", 2019, 2021,
                   "Marvel Animation / Disney XD", "streaming series",
                   notes="PRODUCER: Marvel Animation. Continuation with Venom storyline."),
            Series("Your Friendly Neighborhood Spider-Man", 2025, None,
                   "Marvel Animation / Disney+", "streaming series",
                   notes="PRODUCER: Marvel Animation. Newest Spider-Man animated series for Disney+."),
        ],
        eras=[
            Era(1967, 1970,
                "Original 1967 series — classic blue and red costume, "
                "iconic theme song, heavy animation recycling. "
                "PRODUCED BY: Grantray-Lawrence / Krantz Films / DePatie-Freleng.",
                art_style="Limited TV cel animation",
                image_url=IMG["spiderman"],
                notes="The 1967 theme song — Spider-Man Spider-Man does whatever a spider can — "
                      "is one of the most recognizable pieces of music in pop culture history. "
                      "The series is known for its extraordinarily heavy animation recycling."),
            Era(1981, 1983,
                "Spider-Man and His Amazing Friends era — team dynamic with Iceman and Firestar, "
                "brighter colors, more heroic tone. PRODUCED BY: Marvel Productions (in-house).",
                art_style="Improved TV cel animation",
                image_url=IMG["spiderman"],
                notes="Amazing Friends is particularly beloved for the team dynamic. "
                      "Firestar was created specifically for this show "
                      "and was later introduced into the Marvel Comics universe."),
            Era(1994, 1998,
                "Fox Kids Animated Series era — the definitive Spider-Man cartoon for most fans, "
                "Christopher Daniel Barnes, multi-season mythology. "
                "PRODUCED BY: Saban / Marvel Films Animation.",
                art_style="Detailed TV cel animation",
                image_url=IMG["spiderman"],
                notes="The 1994 series is the definitive Spider-Man cartoon for the generation "
                      "that grew up with it. Its complex multi-season storylines set a new "
                      "standard for superhero animated storytelling."),
            Era(2008, 2009,
                "Spectacular Spider-Man era — Greg Weisman's acclaimed series, "
                "best characterization of Peter Parker, cancelled too soon. "
                "PRODUCED BY: Sony Pictures Television.",
                art_style="Clean modern TV animation",
                image_url=IMG["spectacular"],
                notes="The Spectacular Spider-Man is frequently cited by critics as the "
                      "greatest Spider-Man animated series ever made. "
                      "Its cancellation when Disney acquired Marvel is widely mourned."),
            Era(2012, None,
                "Disney/Marvel Animation era — multiple series under Disney ownership, "
                "various tones from comedic to more faithful. "
                "PRODUCED BY: Marvel Animation (Disney-owned).",
                art_style="Modern digital animation",
                image_url=IMG["spiderman"],
                notes="Post-Disney acquisition Spider-Man animation has varied in quality. "
                      "Your Friendly Neighborhood Spider-Man (2025) is the current iteration."),
        ],
        wiki_slug="Spider-Man_in_other_media",
    )
    lib.add_cartoon(spiderman)

    # ══════════════════════════════════════════════════════════════════════
    # X-MEN (1963)
    # ══════════════════════════════════════════════════════════════════════
    xmen = _marvel(
        name="X-Men (animated history)",
        description=(
            "A team of mutant superheroes led by Professor Charles Xavier — "
            "born with genetic powers in a world that fears and hates them. "
            "The X-Men are Marvel's most beloved team and their animated history "
            "is dominated by the legendary 1992 Fox Kids series that remains "
            "one of the greatest superhero animated series ever made. "
            "The core team includes Cyclops, Jean Grey, Wolverine, Storm, Rogue, "
            "Gambit, Beast, Jubilee, and Professor X. Their stories deal with "
            "civil rights allegory, discrimination, and the meaning of acceptance — "
            "themes that gave the series unusual depth for Saturday morning TV. "
            "NOTE: Marvel / Disney has always owned the X-Men."
        ),
        character_type="Mutant superhero ensemble — Marvel Comics",
        debut_year=1963,
        creators=[STAN_LEE, JACK_KIRBY, LEN_WEIN, CHRIS_CLAREMONT],
        series_list=[
            Series("The Marvel Super Heroes (X-Men segment)", 1966, 1966,
                   "Grantray-Lawrence Animation / Krantz Films", "TV series segment",
                   notes="PRODUCER: Grantray-Lawrence. Very limited animation — "
                         "essentially animated comic book panels. First animated X-Men appearance."),
            Series("Pryde of the X-Men (pilot)", 1989, 1989,
                   "Marvel Productions / Akom", "TV pilot", episode_count=1,
                   notes="PRODUCER: Marvel Productions. Unaired pilot featuring Kitty Pryde. "
                         "Australian accents for Wolverine confused fans. Not picked up."),
            Series("X-Men: The Animated Series (Fox Kids)", 1992, 1997,
                   "Saban Entertainment / Marvel Films Animation / Fox Kids", "TV series", episode_count=76,
                   notes="PRODUCER: Saban / Marvel Films Animation under Fox license. "
                         "THE definitive X-Men adaptation. Directly adapted major comic storylines "
                         "including Dark Phoenix Saga, Days of Future Past, Age of Apocalypse. "
                         "Norm Spencer (Cyclops), Cathal J. Dodd (Wolverine), Iona Morris then "
                         "Alison Sealy-Smith (Storm). The theme song by Ron Wasserman is iconic."),
            Series("X-Men: Evolution", 2000, 2003,
                   "Marvel Films Animation / Kids WB", "TV series", episode_count=52,
                   notes="PRODUCER: Marvel Films Animation / Warner Bros. Animation under Marvel license. "
                         "Reimagined the X-Men as teenagers attending high school. "
                         "Mixed reception but praised for character development."),
            Series("Wolverine and the X-Men", 2008, 2009,
                   "Marvel Animation / Nicktoons", "TV series", episode_count=26,
                   notes="PRODUCER: Marvel Animation. Wolverine-led X-Men in dystopian future storyline. "
                         "Cancelled after one season despite critical praise — "
                         "Disney acquisition disrupted production plans."),
            Series("X-Men '97", 2024, None,
                   "Marvel Animation / Disney+", "streaming series",
                   notes="PRODUCER: Marvel Animation (Disney-owned). Direct continuation of the 1992 series "
                         "with original voice cast returning. Critically acclaimed as one of the "
                         "best animated series of 2024. Picks up immediately where the 1992 series ended."),
        ],
        eras=[
            Era(1966, 1988,
                "Pre-series era — very limited animated appearances, essentially animated comics. "
                "PRODUCED BY: Grantray-Lawrence then Marvel Productions.",
                art_style="Limited / motion comic style",
                image_url=IMG["xmen"],
                notes="Early Marvel animation was produced on minimal budgets. "
                      "The 1966 Marvel Super Heroes segments were literally animated comic panels."),
            Era(1992, 1997,
                "Fox Kids Animated Series — THE definitive X-Men, "
                "direct adaptation of major comic storylines, iconic theme song. "
                "PRODUCED BY: Saban Entertainment / Marvel Films Animation.",
                art_style="Detailed TV cel animation — rich color palette",
                image_url=IMG["xmen"],
                notes="The 1992 X-Men series is one of the greatest superhero animated series ever made. "
                      "It adapted the Dark Phoenix Saga, Days of Future Past, the Phalanx Covenant, "
                      "and many other landmark comic storylines faithfully. "
                      "Ron Wasserman's theme is one of the most beloved in animation history."),
            Era(2000, 2009,
                "Post-Fox era — X-Men Evolution teen reimagining then Wolverine and the X-Men. "
                "PRODUCED BY: Marvel Films Animation then Marvel Animation.",
                art_style="Modern TV animation — cleaner lines",
                image_url=IMG["wolverine"],
                notes="X-Men Evolution was divisive but found an audience. "
                      "Wolverine and the X-Men was cancelled due to the Disney acquisition disruption."),
            Era(2024, None,
                "X-Men '97 revival — direct continuation of 1992 series, "
                "original cast returns, Disney+ streaming. "
                "PRODUCED BY: Marvel Animation (Disney-owned).",
                art_style="Updated version of 1992 cel animation style",
                image_url=IMG["xmen"],
                notes="X-Men '97 is one of the most anticipated and celebrated animated revivals. "
                      "Showrunner Beau DeMayo created a continuation that honored the original "
                      "while telling new stories. Original voice cast returned."),
        ],
        wiki_slug="X-Men_in_other_media",
    )
    lib.add_cartoon(xmen)

    # ══════════════════════════════════════════════════════════════════════
    # WOLVERINE (1974)
    # ══════════════════════════════════════════════════════════════════════
    wolverine = _marvel(
        name="Wolverine (animated history)",
        description=(
            "Logan — a mutant with retractable adamantium claws, superhuman "
            "healing factor, and over a century of violent history. Wolverine "
            "is Marvel's most popular individual character and became the breakout "
            "star of the 1992 X-Men animated series. His gruff Canadian anti-hero "
            "personality, his rivalry with Cyclops over Jean Grey, and his mysterious "
            "past made him the most compelling X-Man in animation. "
            "NOTE: Marvel / Disney has always owned Wolverine."
        ),
        character_type="Mutant — Marvel Comics superhero / anti-hero",
        debut_year=1974,
        creators=[LEN_WEIN, JACK_KIRBY,
                  Creator("Roy Thomas", "Wolverine concept originator", 1940)],
        series_list=[
            Series("X-Men: The Animated Series (Wolverine as breakout star)", 1992, 1997,
                   "Saban / Fox Kids", "TV series",
                   notes="PRODUCER: Saban under Marvel/Fox license. Cathal J. Dodd voiced Wolverine. "
                         "His rivalry with Cyclops and mysterious past made him the series' breakout character."),
            Series("Wolverine and the X-Men (lead role)", 2008, 2009,
                   "Marvel Animation / Nicktoons", "TV series", episode_count=26,
                   notes="PRODUCER: Marvel Animation. First series with Wolverine as the lead. "
                         "Steve Blum voiced Wolverine — his definitive animated voice."),
            Series("X-Men '97 (Wolverine returning)", 2024, None,
                   "Marvel Animation / Disney+", "streaming series",
                   notes="PRODUCER: Marvel Animation. Cal Dodd reprised Wolverine for the revival."),
        ],
        eras=[
            Era(1992, 2007,
                "X-Men animated era — gruff Canadian with adamantium claws, "
                "blue and yellow costume, cigar, intense rivalry with Cyclops. "
                "PRODUCED BY: Saban / Marvel Films Animation.",
                art_style="Detailed TV cel animation",
                image_url=IMG["xmen"],
                notes="Cathal J. Dodd's voice performance defined animated Wolverine for a generation. "
                      "The character's popularity in the 1992 series directly led to his "
                      "prominence in the live-action X-Men films."),
            Era(2008, None,
                "Modern era — Steve Blum as the definitive Wolverine voice, "
                "lead role in own series, X-Men '97 revival. "
                "PRODUCED BY: Marvel Animation.",
                art_style="Modern digital animation",
                image_url=IMG["wolverine"],
                notes="Steve Blum has voiced Wolverine in most post-2008 animated appearances. "
                      "His deep growl became as definitive as Hugh Jackman's live-action performance."),
        ],
        wiki_slug="Wolverine_in_other_media",
    )
    lib.add_cartoon(wolverine)

    # ══════════════════════════════════════════════════════════════════════
    # IRON MAN (1963)
    # ══════════════════════════════════════════════════════════════════════
    iron_man = _marvel(
        name="Iron Man (animated history)",
        description=(
            "Tony Stark — genius billionaire inventor who builds a powered armor suit "
            "to escape captivity and becomes Iron Man, Avenger, and Earth's most "
            "technologically advanced defender. Iron Man's animated history stretches "
            "from the 1966 Marvel Super Heroes segments through his own 1990s series "
            "to his central role in Avengers: Earth's Mightiest Heroes — widely "
            "considered the greatest Avengers animated series. "
            "NOTE: Marvel / Disney has always owned Iron Man."
        ),
        character_type="Human — Marvel Comics superhero / genius inventor",
        debut_year=1963,
        creators=[STAN_LEE, LARRY_LIEBER, DON_HECK, JACK_KIRBY],
        series_list=[
            Series("The Marvel Super Heroes (Iron Man segment)", 1966, 1966,
                   "Grantray-Lawrence Animation / Krantz Films", "TV series segment",
                   notes="PRODUCER: Grantray-Lawrence. Motion comic format. "
                         "First Iron Man animated appearance. Golden Avenger suit design."),
            Series("Iron Man (animated series)", 1994, 1996,
                   "Marvel Films Animation / Saban / Fox Kids", "TV series", episode_count=26,
                   notes="PRODUCER: Marvel Films Animation / Saban under Fox license. "
                         "Two seasons with very different tones — Season 1 campy, Season 2 more serious. "
                         "Robert Hays voiced Tony Stark. Introduced the Mandarin as primary villain."),
            Series("The Invincible Iron Man (animated film)", 2007, 2007,
                   "Marvel Animation", "direct-to-video feature",
                   notes="PRODUCER: Marvel Animation. Origin story film predating the MCU. "
                         "Marc Worden voiced Iron Man."),
            Series("Avengers: Earth's Mightiest Heroes", 2010, 2013,
                   "Marvel Animation / Disney XD", "TV series", episode_count=52,
                   notes="PRODUCER: Marvel Animation (Disney-owned). Eric Loomis voiced Iron Man. "
                         "Widely considered the greatest Avengers animated series. "
                         "Cancelled to make way for Avengers Assemble which tied into MCU."),
            Series("Avengers Assemble", 2013, 2019,
                   "Marvel Animation / Disney XD", "TV series", episode_count=126,
                   notes="PRODUCER: Marvel Animation. MCU-aligned character designs. "
                         "Adrian Pasdar voiced Iron Man."),
            Series("Iron Man and Hulk Heroes United", 2013, 2013,
                   "Marvel Animation", "direct-to-video feature",
                   notes="PRODUCER: Marvel Animation. CGI crossover film."),
        ],
        eras=[
            Era(1966, 1993,
                "Pre-series era — motion comic then absent from animation for decades. "
                "PRODUCED BY: Grantray-Lawrence.",
                art_style="Motion comic / absent",
                image_url=IMG["ironman"],
                notes="Iron Man had minimal animated presence after the 1966 segments "
                      "until his 1994 Fox Kids series."),
            Era(1994, 1996,
                "Fox Kids series — two very different seasons, "
                "Robert Hays as Tony Stark, the Mandarin as villain. "
                "PRODUCED BY: Marvel Films Animation / Saban.",
                art_style="1990s TV cel animation",
                image_url=IMG["ironman"],
                notes="The 1994 series had a notable tonal shift between Season 1 (campy) "
                      "and Season 2 (darker, more serious). Season 2 is much preferred by fans."),
            Era(2010, 2013,
                "Avengers: Earth's Mightiest Heroes era — best animated Iron Man, "
                "sophisticated team dynamics, faithful comic adaptation. "
                "PRODUCED BY: Marvel Animation (Disney-owned).",
                art_style="Modern digital animation — classic comic colors",
                image_url=IMG["avengers"],
                notes="Earth's Mightiest Heroes gave Iron Man his finest animated characterization. "
                      "Its cancellation in favor of MCU-aligned Avengers Assemble "
                      "remains controversial among Marvel animation fans."),
            Era(2013, None,
                "MCU-aligned era — designs match movies, Disney XD and Disney+ productions. "
                "PRODUCED BY: Marvel Animation (Disney-owned).",
                art_style="MCU-influenced digital animation",
                image_url=IMG["avengers"],
                notes="Post-2013 Marvel animation was closely aligned with MCU aesthetics. "
                      "The trade-off of storytelling depth for MCU synergy divided fans."),
        ],
        wiki_slug="Iron_Man_in_other_media",
    )
    lib.add_cartoon(iron_man)

    # ══════════════════════════════════════════════════════════════════════
    # CAPTAIN AMERICA (1941)
    # ══════════════════════════════════════════════════════════════════════
    cap_america = _marvel(
        name="Captain America (animated history)",
        description=(
            "Steve Rogers — a frail young man from Brooklyn who is transformed "
            "into a super-soldier by the Super-Soldier Serum and becomes America's "
            "greatest hero during World War II. Frozen in ice and revived in the "
            "modern era, Captain America struggles to find his place in a changed world "
            "while never compromising his moral core. Cap's animated history spans "
            "from the 1966 Marvel Super Heroes to his central role in "
            "Avengers: Earth's Mightiest Heroes. "
            "NOTE: Marvel / Disney has always owned Captain America."
        ),
        character_type="Human — Marvel Comics superhero / Super-Soldier",
        debut_year=1941,
        creators=[JOE_SIMON, JACK_KIRBY],
        series_list=[
            Series("The Marvel Super Heroes (Captain America segment)", 1966, 1966,
                   "Grantray-Lawrence Animation / Krantz Films", "TV series segment",
                   notes="PRODUCER: Grantray-Lawrence. Motion comic format. "
                         "First Captain America animated appearance. WWII-era storylines adapted."),
            Series("Captain America (1966 segment)", 1966, 1966,
                   "Grantray-Lawrence Animation", "TV series segment", episode_count=13,
                   notes="PRODUCER: Grantray-Lawrence. Part of The Marvel Super Heroes package. "
                         "Thirteen Captain America segments based directly on Stan Lee and Jack Kirby comics."),
            Series("Spider-Man and His Amazing Friends (Cap guest)", 1981, 1983,
                   "Marvel Productions / NBC", "TV series",
                   notes="PRODUCER: Marvel Productions. Captain America appeared as a guest hero "
                         "alongside Spider-Man's team."),
            Series("The Incredible Hulk (Cap guest appearances)", 1996, 1997,
                   "Marvel Films Animation / UPN", "TV series",
                   notes="PRODUCER: Marvel Films Animation. Captain America appeared in several "
                         "Hulk episodes — their shared WWII history was explored."),
            Series("Avengers: Earth's Mightiest Heroes", 2010, 2013,
                   "Marvel Animation / Disney XD", "TV series", episode_count=52,
                   notes="PRODUCER: Marvel Animation. Brian Bloom voiced Captain America. "
                         "The series adapted the WWII origin and modern revival faithfully. "
                         "Widely considered the definitive animated Cap characterization."),
            Series("Avengers Assemble", 2013, 2019,
                   "Marvel Animation / Disney XD", "TV series",
                   notes="PRODUCER: Marvel Animation. Roger Craig Smith voiced Captain America. "
                         "MCU-aligned visual design."),
        ],
        eras=[
            Era(1966, 1980,
                "Original motion comic era — WWII hero, shield-throwing action, "
                "faithful Silver Age comic adaptation. PRODUCED BY: Grantray-Lawrence.",
                art_style="Motion comic / limited animation",
                image_url=IMG["captain"],
                notes="The 1966 Captain America segments are notable for faithfully adapting "
                      "the Stan Lee / Jack Kirby comics including stories featuring "
                      "Bucky Barnes and the Red Skull."),
            Era(1981, 2009,
                "Guest appearance era — Cap appears in other heroes' series "
                "without his own animated vehicle. PRODUCED BY: Various.",
                art_style="Various TV animation styles",
                image_url=IMG["captain"],
                notes="Captain America lacked his own animated series for nearly three decades. "
                      "He appeared as a guest in various Marvel animated productions "
                      "during this period."),
            Era(2010, None,
                "Avengers era — EMH gave Cap his finest animated portrayal, "
                "MCU-aligned designs followed. PRODUCED BY: Marvel Animation.",
                art_style="Modern digital animation",
                image_url=IMG["avengers"],
                notes="Earth's Mightiest Heroes remains the gold standard for animated Captain America. "
                      "Brian Bloom's voice performance captured both the WWII soldier "
                      "and the man out of time aspects of the character."),
        ],
        wiki_slug="Captain_America_in_other_media",
    )
    lib.add_cartoon(cap_america)

    # ══════════════════════════════════════════════════════════════════════
    # THE INCREDIBLE HULK (1962)
    # ══════════════════════════════════════════════════════════════════════
    hulk = _marvel(
        name="The Incredible Hulk (animated history)",
        description=(
            "Dr. Bruce Banner — a brilliant physicist exposed to gamma radiation "
            "who transforms into the Hulk — an enormous green creature of "
            "limitless strength — when he becomes angry. The angrier the Hulk gets, "
            "the stronger he gets. His animated history spans from the 1966 Marvel "
            "Super Heroes through multiple solo series to his central role in "
            "Avengers: Earth's Mightiest Heroes. "
            "NOTE: Marvel / Disney has always owned the Hulk."
        ),
        character_type="Human / creature — Marvel Comics superhero / gamma monster",
        debut_year=1962,
        creators=[STAN_LEE, JACK_KIRBY],
        series_list=[
            Series("The Marvel Super Heroes (Hulk segment)", 1966, 1966,
                   "Grantray-Lawrence Animation", "TV series segment", episode_count=13,
                   notes="PRODUCER: Grantray-Lawrence. Motion comic format. "
                         "First Hulk animated appearance. Rick Jones as sidekick."),
            Series("The Incredible Hulk (1982)", 1982, 1983,
                   "Marvel Productions / NBC", "TV series", episode_count=13,
                   notes="PRODUCER: Marvel Productions (in-house). "
                         "She-Hulk appeared as a supporting character. "
                         "Featured the Leader and Thunderbolt Ross as antagonists."),
            Series("The Incredible Hulk (1996)", 1996, 1997,
                   "Marvel Films Animation / UPN", "TV series", episode_count=21,
                   notes="PRODUCER: Marvel Films Animation under UPN license. "
                         "Two seasons with very different tones. Lou Ferrigno (TV Hulk) voiced the Hulk. "
                         "Season 2 added She-Hulk and other characters."),
            Series("Avengers: Earth's Mightiest Heroes", 2010, 2013,
                   "Marvel Animation / Disney XD", "TV series",
                   notes="PRODUCER: Marvel Animation. Fred Tatasciore voiced the Hulk "
                         "— his definitive animated voice. The Hulk's arc in EMH was "
                         "one of the series' most compelling character journeys."),
            Series("Hulk and the Agents of SMASH", 2013, 2015,
                   "Marvel Animation / Disney XD", "TV series", episode_count=52,
                   notes="PRODUCER: Marvel Animation (Disney-owned). Hulk leads a team "
                         "of gamma-powered heroes. Fred Tatasciore continued as the Hulk."),
        ],
        eras=[
            Era(1966, 1981,
                "Original motion comic era — grey Hulk in first appearance then green, "
                "Hulk SMASH vocabulary established. PRODUCED BY: Grantray-Lawrence.",
                art_style="Motion comic / limited animation",
                image_url=IMG["hulk"],
                notes="The 1966 segments were among the most memorable for Hulk's "
                      "distinctive speech pattern: Hulk smash puny humans. "
                      "The motion comic format actually worked well for action sequences."),
            Era(1982, 1995,
                "Marvel Productions era — improved animation, She-Hulk introduced. "
                "PRODUCED BY: Marvel Productions in-house.",
                art_style="1980s TV cel animation",
                image_url=IMG["hulk"],
                notes="The 1982 series improved significantly on the 1966 segments. "
                      "She-Hulk's inclusion reflected the character's comic book prominence at the time."),
            Era(1996, 2012,
                "UPN series era — Lou Ferrigno's voice, "
                "two-season tonal shift. PRODUCED BY: Marvel Films Animation.",
                art_style="1990s TV cel animation",
                image_url=IMG["hulk"],
                notes="Casting Lou Ferrigno (the live-action Hulk from the 1977 TV series) "
                      "as the voice was a beloved touch of continuity."),
            Era(2013, None,
                "Disney/Marvel era — Fred Tatasciore's definitive voice, "
                "team-based format, MCU-aligned designs. PRODUCED BY: Marvel Animation.",
                art_style="Modern digital animation",
                image_url=IMG["avengers"],
                notes="Fred Tatasciore has become the definitive animated Hulk voice. "
                      "His ability to convey both the Hulk's rage and his surprising "
                      "emotional depth is remarkable."),
        ],
        wiki_slug="Hulk_in_other_media",
    )
    lib.add_cartoon(hulk)

    # ══════════════════════════════════════════════════════════════════════
    # FANTASTIC FOUR (1961)
    # ══════════════════════════════════════════════════════════════════════
    fantastic_four = _marvel(
        name="Fantastic Four (animated history)",
        description=(
            "Marvel's First Family — Mr. Fantastic (Reed Richards), the Invisible Woman "
            "(Sue Storm), the Human Torch (Johnny Storm), and the Thing (Ben Grimm) — "
            "scientists who gained powers from cosmic ray exposure during a space mission. "
            "The Fantastic Four have had more animated series than any Marvel team "
            "except the X-Men, stretching from 1967 to 2006. Each era reflected "
            "its time: the campy 1967 Hanna-Barbera version where the Human Torch "
            "was replaced by a robot named H.E.R.B.I.E., through the acclaimed "
            "1994 Fox Kids series that faithfully adapted Galactus and Doctor Doom. "
            "NOTE: Marvel / Disney has always owned the Fantastic Four."
        ),
        character_type="Superhero ensemble — Marvel Comics / Marvel's First Family",
        debut_year=1961,
        creators=[STAN_LEE, JACK_KIRBY],
        series_list=[
            Series("Fantastic Four (Hanna-Barbera)", 1967, 1970,
                   "Hanna-Barbera / ABC", "TV series", episode_count=20,
                   notes="PRODUCER: Hanna-Barbera under Marvel license. "
                         "The Human Torch was REPLACED by a robot named H.E.R.B.I.E. "
                         "because Marvel had licensed the Human Torch separately for a live-action project. "
                         "H.E.R.B.I.E. became infamous as a deeply unpopular substitute."),
            Series("Fantastic Four (DePatie-Freleng)", 1978, 1979,
                   "DePatie-Freleng Enterprises / NBC", "TV series", episode_count=13,
                   notes="PRODUCER: DePatie-Freleng under Marvel license. "
                         "Human Torch restored. More faithful to comics."),
            Series("Fantastic Four (1994 Fox Kids)", 1994, 1996,
                   "Marvel Films Animation / Saban / Fox Kids", "TV series", episode_count=26,
                   notes="PRODUCER: Marvel Films Animation / Saban under Fox license. "
                         "Faithfully adapted Galactus, the Silver Surfer, and Doctor Doom. "
                         "Season 2 had notably improved animation quality. "
                         "Widely considered the best Fantastic Four animated series."),
            Series("Fantastic Four: World's Greatest Heroes", 2006, 2007,
                   "Marvel Animation / Moonscoop / Cartoon Network", "TV series", episode_count=26,
                   notes="PRODUCER: Moonscoop under Marvel license. Anime-influenced style. "
                         "Mixed critical reception."),
        ],
        eras=[
            Era(1967, 1977,
                "Hanna-Barbera era — H.E.R.B.I.E. replaces Human Torch, "
                "campy adventure format. PRODUCED BY: Hanna-Barbera.",
                art_style="Hanna-Barbera limited TV animation",
                image_url=IMG["fantastic"],
                notes="H.E.R.B.I.E. (Humanoid Experimental Robot B-type Integrated Electronics) "
                      "became one of animation's most infamous character substitutions. "
                      "The Human Torch was excluded due to a separate live-action licensing deal."),
            Era(1978, 1993,
                "Human Torch restored era — DePatie-Freleng more faithful version. "
                "PRODUCED BY: DePatie-Freleng.",
                art_style="1970s TV cel animation",
                image_url=IMG["fantastic"],
                notes="The 1978 series corrected the H.E.R.B.I.E. mistake and restored "
                      "the Human Torch to his proper place on the team."),
            Era(1994, 1996,
                "Fox Kids era — best FF animated series, Galactus adaptation, "
                "Doctor Doom as primary villain. PRODUCED BY: Marvel Films Animation / Saban.",
                art_style="1990s TV cel animation — improved second season",
                image_url=IMG["fantastic"],
                notes="The 1994 series is the definitive Fantastic Four cartoon. "
                      "The two-part Galactus story The Silver Surfer and the Coming of Galactus "
                      "is considered the finest moment in FF animation history."),
            Era(2006, None,
                "Modern era — anime-influenced designs, various digital productions. "
                "PRODUCED BY: Moonscoop / Marvel Animation.",
                art_style="Anime-influenced digital animation",
                image_url=IMG["fantastic"],
                notes="The 2006 series was a significant departure from the classic look. "
                      "A new Fantastic Four animated series has been in development under Disney."),
        ],
        wiki_slug="Fantastic_Four_in_other_media",
    )
    lib.add_cartoon(fantastic_four)

    # ══════════════════════════════════════════════════════════════════════
    # THOR (1962)
    # ══════════════════════════════════════════════════════════════════════
    thor = _marvel(
        name="Thor (animated history)",
        description=(
            "The Asgardian God of Thunder — Thor Odinson wields Mjolnir, "
            "the enchanted hammer only the worthy can lift. Son of Odin, "
            "brother of Loki, and one of the founding Avengers. Thor's animated "
            "history stretches from the 1966 Marvel Super Heroes motion comics "
            "through Avengers: Earth's Mightiest Heroes where his Asgardian mythology "
            "was depicted with impressive faithfulness. "
            "NOTE: Marvel / Disney has always owned Thor."
        ),
        character_type="Deity — Marvel Comics superhero / Asgardian God of Thunder",
        debut_year=1962,
        creators=[STAN_LEE, LARRY_LIEBER, JACK_KIRBY],
        series_list=[
            Series("The Marvel Super Heroes (Thor segment)", 1966, 1966,
                   "Grantray-Lawrence Animation", "TV series segment", episode_count=13,
                   notes="PRODUCER: Grantray-Lawrence. Motion comic format. "
                         "First Thor animated appearance. Norse mythology introduced to animation."),
            Series("Avengers: Earth's Mightiest Heroes", 2010, 2013,
                   "Marvel Animation / Disney XD", "TV series",
                   notes="PRODUCER: Marvel Animation. Travis Willingham voiced Thor. "
                         "The Asgard storylines in EMH are considered the finest animated "
                         "Thor stories ever produced."),
            Series("Avengers Assemble", 2013, 2019,
                   "Marvel Animation / Disney XD", "TV series",
                   notes="PRODUCER: Marvel Animation. Travis Willingham continued as Thor. "
                         "MCU-aligned visual design."),
        ],
        eras=[
            Era(1966, 2009,
                "Early and guest era — motion comics then guest appearances. "
                "PRODUCED BY: Grantray-Lawrence then various.",
                art_style="Motion comic / various",
                image_url=IMG["thor"],
                notes="Thor had no dedicated animated series of his own "
                      "outside the 1966 motion comic segments until the modern era."),
            Era(2010, None,
                "Avengers animated era — EMH gave Thor finest animated treatment, "
                "Asgard mythology depicted faithfully. PRODUCED BY: Marvel Animation.",
                art_style="Modern digital animation",
                image_url=IMG["avengers"],
                notes="Earth's Mightiest Heroes gave Thor the greatest animated treatment "
                      "of his mythology. The Asgard two-parter is particularly praised."),
        ],
        wiki_slug="Thor_in_other_media",
    )
    lib.add_cartoon(thor)

    # ══════════════════════════════════════════════════════════════════════
    # AVENGERS (1963 — team)
    # ══════════════════════════════════════════════════════════════════════
    avengers = _marvel(
        name="The Avengers (animated history)",
        description=(
            "Earth's Mightiest Heroes — Marvel's premier superhero team featuring "
            "Iron Man, Captain America, Thor, Hulk, Ant-Man, Wasp, and many others. "
            "The Avengers have had multiple animated series with wildly varying quality. "
            "Avengers: Earth's Mightiest Heroes (2010-2012) is universally regarded "
            "as the greatest Avengers animated series — faithfully adapting decades "
            "of comic storylines with sophisticated character work. Its cancellation "
            "to make way for the MCU-tied Avengers Assemble remains one of Marvel "
            "animation's most controversial decisions. "
            "NOTE: Marvel / Disney has always owned the Avengers."
        ),
        character_type="Superhero ensemble — Marvel Comics / Earth's Mightiest Heroes",
        debut_year=1963,
        creators=[STAN_LEE, JACK_KIRBY],
        series_list=[
            Series("The Avengers: United They Stand", 1999, 2000,
                   "Marvel Films Animation / Fox Kids", "TV series", episode_count=13,
                   notes="PRODUCER: Marvel Films Animation under Fox license. "
                         "Iron Man and Captain America were absent due to their own concurrent series. "
                         "Poorly received and cancelled after one season."),
            Series("Avengers: Earth's Mightiest Heroes", 2010, 2013,
                   "Marvel Animation / Disney XD", "TV series", episode_count=52,
                   notes="PRODUCER: Marvel Animation (Disney-owned). "
                         "THE definitive Avengers animated series. Adapted Secret Invasion, "
                         "Kree-Skrull War, Masters of Evil, and many classic storylines. "
                         "Cancelled after two seasons to align with MCU aesthetics — "
                         "a widely criticized decision."),
            Series("Avengers Assemble", 2013, 2019,
                   "Marvel Animation / Disney XD", "TV series", episode_count=126,
                   notes="PRODUCER: Marvel Animation. MCU character designs. "
                         "Less critically praised than EMH. "
                         "Later seasons improved with more original storylines."),
            Series("Marvel's Avengers: Ultron Revolution", 2016, 2017,
                   "Marvel Animation / Disney XD", "TV series",
                   notes="PRODUCER: Marvel Animation. Season 3 of Avengers Assemble "
                         "retitled to tie into Age of Ultron film."),
        ],
        eras=[
            Era(1999, 2009,
                "Pre-EMH era — United They Stand failed attempt, "
                "Avengers absent from quality animation for a decade. "
                "PRODUCED BY: Marvel Films Animation.",
                art_style="Late 1990s TV animation",
                image_url=IMG["avengers"],
                notes="The 1999 series United They Stand is considered a significant failure. "
                      "Excluding Iron Man and Captain America — the team's biggest names — "
                      "was a critical handicap the show never overcame."),
            Era(2010, 2012,
                "Earth's Mightiest Heroes — the greatest Avengers animated series, "
                "faithful comic adaptation, complex multi-season storytelling. "
                "PRODUCED BY: Marvel Animation (Disney-owned).",
                art_style="Classic Marvel comic-inspired digital animation",
                image_url=IMG["avengers"],
                notes="EMH is the gold standard for Marvel team animation. "
                      "Its cancellation after two seasons — replaced by a show widely "
                      "considered inferior — remains a sore point for Marvel animation fans."),
            Era(2013, None,
                "MCU-aligned era — Avengers Assemble and sequels tied to film aesthetics. "
                "PRODUCED BY: Marvel Animation.",
                art_style="MCU-influenced digital animation",
                image_url=IMG["avengers"],
                notes="The post-EMH Marvel animation era prioritized MCU synergy "
                      "over storytelling independence. Reception has been mixed."),
        ],
        wiki_slug="Avengers_in_other_media",
    )
    lib.add_cartoon(avengers)

    # ══════════════════════════════════════════════════════════════════════
    # GUARDIANS OF THE GALAXY (1969/2008 modern team)
    # ══════════════════════════════════════════════════════════════════════
    guardians = _marvel(
        name="Guardians of the Galaxy (animated)",
        description=(
            "A ragtag team of cosmic heroes — Star-Lord (Peter Quill), Gamora, "
            "Drax the Destroyer, Rocket Raccoon, and Groot — who protect the galaxy "
            "from various threats. The modern Guardians were largely unknown before "
            "the 2014 MCU film made them household names. The animated series "
            "followed the film's success and used the movie character designs. "
            "NOTE: Marvel / Disney has always owned the Guardians."
        ),
        character_type="Superhero ensemble — Marvel Comics / cosmic heroes",
        debut_year=2015,
        creators=[STAN_LEE,
                  Creator("Dan Abnett", "Modern Guardians team co-creator", 1965),
                  Creator("Andy Lanning", "Modern Guardians team co-creator", 1964)],
        series_list=[
            Series("Marvel's Guardians of the Galaxy", 2015, 2019,
                   "Marvel Animation / Disney XD", "TV series", episode_count=75,
                   notes="PRODUCER: Marvel Animation. Will Friedle voiced Star-Lord. "
                         "Directly inspired by the 2014 MCU film's success. "
                         "MCU-aligned character designs."),
        ],
        eras=[
            Era(2015, None,
                "Post-MCU animated series — character designs based on film versions, "
                "comedic adventure tone. PRODUCED BY: Marvel Animation.",
                art_style="MCU-influenced digital animation",
                image_url=IMG["guardians"],
                notes="The animated Guardians were entirely a product of the MCU film's success. "
                      "No significant animated history predates the 2014 film."),
        ],
        wiki_slug="Guardians_of_the_Galaxy_in_other_media",
    )
    lib.add_cartoon(guardians)

    print(f"Marvel characters added. Library now has {len(lib.cartoons)} cartoons total.")
