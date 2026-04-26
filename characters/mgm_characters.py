"""
mgm_characters.py
All major MGM cartoon characters for CartoonPal.

Metro-Goldwyn-Mayer Cartoons was the animation division of MGM Studios,
operating from 1937 to 1957. The studio produced some of the most
technically accomplished animation of the golden age, winning more
Academy Awards for animated short films than any other studio.

Key units:
- The Harman-Ising unit (1937–1938): Rudolf Ising and Hugh Harman
- The Fred Quimby unit (1938–1955): Fred Quimby as producer
  - Tex Avery unit (1942–1955): wildest, most anarchic cartoons
  - Hanna-Barbera unit (1940–1957): Tom and Jerry
- The Gene Deitch unit (1960–1962): Prague-based, low budget
- The Chuck Jones unit (1963–1967): after leaving Warner Bros.

Ownership chain:
MGM Cartoons (1937) → Loew's Inc. / MGM (1937–1986)
→ Turner Entertainment Co. (1986–1996, Ted Turner bought MGM library)
→ Time Warner / Warner Bros. (1996–2022, Turner merged with Time Warner)
→ Warner Bros. Discovery (2022–present)

NOTE: Tom and Jerry are already in the main seed_data.py.
This file covers all other MGM cartoon characters.

Usage:
    from mgm_characters import add_mgm_characters
    add_mgm_characters(lib)
"""

from cartoon_system import (
    Cartoon, Creator, ProductionCompany,
    Series, OwnershipRecord, Era, Library
)

# ── Shared objects ─────────────────────────────────────────────────────────
MGM_STUDIO   = ProductionCompany("MGM Cartoons / Metro-Goldwyn-Mayer", 1937, still_active=False)
QUIMBY       = Creator("Fred Quimby", "Producer (MGM cartoon unit)", 1886, 1965)
TEX_AVERY    = Creator("Tex Avery", "Director — anarchic comedy unit", 1908, 1980)
HANNA        = Creator("William Hanna", "Director / co-creator Tom & Jerry unit", 1910, 2001)
BARBERA      = Creator("Joseph Barbera", "Director / co-creator Tom & Jerry unit", 1911, 2006)
HARMAN       = Creator("Hugh Harman", "Co-founder, Harman-Ising unit", 1903, 1982)
ISING        = Creator("Rudolf Ising", "Co-founder, Harman-Ising unit", 1903, 1992)
CHUCK_JONES  = Creator("Chuck Jones", "Director (MGM 1963–1967, post-WB)", 1912, 2002)

MGM_OWNERSHIP = [
    ("Metro-Goldwyn-Mayer / Loew's Inc.", 1937, 1986, "original creation"),
    ("Turner Entertainment Co.", 1986, 1996,
     "purchase of MGM pre-1986 film & cartoon library",
     ),
    ("Time Warner / Warner Bros.", 1996, 2022, "Turner-Time Warner merger"),
    ("Warner Bros. Discovery", 2022, None, "corporate merger"),
]

IMG = {
    "droopy":   "https://upload.wikimedia.org/wikipedia/en/thumb/e/e3/Droopy.png/200px-Droopy.png",
    "spike":    "https://upload.wikimedia.org/wikipedia/en/thumb/1/1c/Spike_the_Bulldog.png/200px-Spike_the_Bulldog.png",
    "barney":   "https://upload.wikimedia.org/wikipedia/en/thumb/4/4e/Barney_Bear_MGM.png/200px-Barney_Bear_MGM.png",
    "screwy":   "https://upload.wikimedia.org/wikipedia/en/thumb/8/8b/Screwball_Squirrel.png/200px-Screwball_Squirrel.png",
    "george":   "https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/George_and_Junior_MGM.png/200px-George_and_Junior_MGM.png",
    "wolf":     "https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/MGM_cartoon_wolf.png/200px-MGM_cartoon_wolf.png",
    "red":      "https://upload.wikimedia.org/wikipedia/en/thumb/1/1e/Red_Hot_Riding_Hood.png/200px-Red_Hot_Riding_Hood.png",
    "tom":      "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Tom_and_Jerry_logo.svg/240px-Tom_and_Jerry_logo.svg.png",
    "mgm":      "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/MGM_logo_large_gold.svg/240px-MGM_logo_large_gold.svg.png",
    "happy":    "https://upload.wikimedia.org/wikipedia/en/thumb/4/4e/Happy_Harmonies_title.png/200px-Happy_Harmonies_title.png",
    "little":   "https://upload.wikimedia.org/wikipedia/en/thumb/6/6e/The_Little_Cheeser.png/200px-The_Little_Cheeser.png",
    "peace":    "https://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Peace_on_Earth_1939.png/200px-Peace_on_Earth_1939.png",
}


def _mgm(name, description, character_type, debut_year,
         creators, series_list, eras, wiki_slug,
         origin="Culver City, California, USA — MGM Cartoon Studio"):
    c = Cartoon(
        name=name,
        description=description,
        character_type=character_type,
        country_of_origin="USA",
        debut_year=debut_year,
    )
    c.original_studio = MGM_STUDIO
    for cr in creators:
        c.add_creator(cr)
    for s in series_list:
        c.add_series(s)
    for i, rec in enumerate(MGM_OWNERSHIP):
        is_cur = (i == len(MGM_OWNERSHIP) - 1)
        owner, y0, y1, method = rec[0], rec[1], rec[2], rec[3]
        c.add_ownership_record(
            OwnershipRecord(owner, y0, y1, method, is_current_owner=is_cur)
        )
    for era in eras:
        c.add_era(era)
    c.wiki_url = f"https://en.wikipedia.org/wiki/{wiki_slug}"
    c.origin_location = origin
    return c


def add_mgm_characters(lib: Library):
    """Add all major MGM cartoon characters to the library."""

    # ══════════════════════════════════════════════════════════════════════
    # DROOPY (1943)
    # Tex Avery's most iconic original creation for MGM
    # ══════════════════════════════════════════════════════════════════════
    droopy = _mgm(
        name="Droopy",
        description=(
            "A small, deadpan basset hound with an expression of permanent "
            "melancholy who defeats adversaries through sheer unflappable "
            "persistence and apparent omnipresence. No matter how far an enemy "
            "flees, Droopy is already there. His catchphrase 'You know what? "
            "I'm the hero' delivered in a flat monotone became one of animation's "
            "most quoted lines. Created by Tex Avery at MGM, Droopy is the "
            "counterpoint to the studio's manic energy — a character who wins "
            "through absolute calm rather than frantic action."
        ),
        character_type="Anthropomorphic animal — basset hound / unlikely hero",
        debut_year=1943,
        creators=[QUIMBY, TEX_AVERY],
        series_list=[
            Series("Dumb-Hounded (debut)", 1943, 1943,
                   "MGM Cartoons", "theatrical short",
                   notes="Debut short. Droopy was originally called Happy Hound."),
            Series("Droopy theatrical shorts (Tex Avery)", 1943, 1955,
                   "MGM Cartoons / Tex Avery unit", "theatrical short", episode_count=24),
            Series("Droopy shorts (Michael Lah era)", 1955, 1958,
                   "MGM Cartoons", "theatrical short", episode_count=5),
            Series("Tom and Jerry and Droopy crossovers", 1980, 1982,
                   "Filmation / various", "TV series"),
            Series("Droopy Master Detective", 1993, 1994,
                   "Turner Entertainment / Hanna-Barbera", "TV series", episode_count=13),
            Series("Tom and Jerry Tales — Droopy appearances", 2006, 2008,
                   "Warner Bros. Animation", "TV series"),
        ],
        eras=[
            Era(1943, 1955,
                "Tex Avery original — small saggy basset hound, drooping jowls, half-closed eyes, "
                "perpetually mournful expression regardless of situation",
                art_style="Technicolor cel animation",
                image_url=IMG["droopy"],
                notes="Debuted April 1 1943 in Dumb-Hounded. Voiced by Bill Thompson using a flat, "
                      "nasal monotone. Tex Avery designed Droopy as the antithesis of his own "
                      "manic cartoons — a character so calm he was surreal."),
            Era(1955, 1958,
                "Michael Lah era — same design, slightly less anarchic situations after Avery left MGM",
                art_style="Technicolor cel animation",
                image_url=IMG["droopy"],
                notes="After Tex Avery left MGM in 1955, Michael Lah directed five more Droopy "
                      "shorts before the MGM cartoon unit closed in 1957."),
            Era(1980, None,
                "Revival era — classic design maintained across TV appearances and modern productions",
                art_style="Various TV cel / digital",
                image_url=IMG["droopy"],
                notes="Turner Entertainment revived Droopy for TV in the 1990s. The character "
                      "remains one of the most beloved in the MGM library."),
        ],
        wiki_slug="Droopy",
    )
    lib.add_cartoon(droopy)

    # ══════════════════════════════════════════════════════════════════════
    # SPIKE THE BULLDOG (1942)
    # Tom and Jerry's recurring antagonist / supporting character
    # ══════════════════════════════════════════════════════════════════════
    spike = _mgm(
        name="Spike the Bulldog",
        description=(
            "A tough, short-tempered bulldog who is a recurring character in "
            "Tom and Jerry — sometimes as Tom's adversary, sometimes as an "
            "unlikely ally to Jerry. Spike is the father of the puppy Tyke "
            "and has a notoriously explosive temper that both Tom and Jerry "
            "frequently exploit. His relationship with his son Tyke provides "
            "the series' occasional moments of genuine warmth. Also known as "
            "Killer and Butch in different episodes."
        ),
        character_type="Anthropomorphic animal — bulldog",
        debut_year=1942,
        creators=[QUIMBY, HANNA, BARBERA],
        series_list=[
            Series("Tom and Jerry theatrical shorts", 1942, 1958,
                   "MGM Cartoons", "theatrical short",
                   notes="Spike debuted in Dog Trouble (1942). A recurring supporting character throughout the run."),
            Series("Tom and Jerry TV productions", 1975, None,
                   "various", "TV series and streaming"),
        ],
        eras=[
            Era(1942, 1958,
                "Original MGM design — grey bulldog with spiked collar, muscular build, "
                "perpetual scowl breaking into rage or rare warmth with Tyke",
                art_style="Technicolor cel animation",
                image_url=IMG["spike"],
                notes="Voiced by Daws Butler and Billy Bletcher at various points. "
                      "Spike's name and personality varied across directors. "
                      "The Tyke relationship gave Tom and Jerry its occasional sentimental streak."),
            Era(1975, None,
                "TV and modern era — design maintained consistently across all Tom and Jerry productions",
                art_style="Various",
                image_url=IMG["spike"],
                notes="Spike remains a fixture of every Tom and Jerry revival. "
                      "His protective relationship with Tyke is always retained."),
        ],
        wiki_slug="Spike_and_Tyke",
    )
    lib.add_cartoon(spike)

    # ══════════════════════════════════════════════════════════════════════
    # BARNEY BEAR (1939)
    # MGM's gentle giant — predates the Hanna-Barbera unit
    # ══════════════════════════════════════════════════════════════════════
    barney_bear = _mgm(
        name="Barney Bear",
        description=(
            "A mild-mannered, well-meaning brown bear whose attempts at peaceful "
            "existence — fishing, camping, sleeping through winter — are invariably "
            "disrupted by forces beyond his control. Barney is one of MGM's most "
            "gentle characters, defined by his long-suffering patience and his "
            "almost philosophical acceptance of misfortune. He starred in 26 shorts "
            "across two decades and was one of Rudolf Ising's finest creations."
        ),
        character_type="Anthropomorphic animal — brown bear",
        debut_year=1939,
        creators=[QUIMBY, ISING],
        series_list=[
            Series("Barney Bear theatrical shorts", 1939, 1954,
                   "MGM Cartoons", "theatrical short", episode_count=26),
        ],
        eras=[
            Era(1939, 1942,
                "Rudolf Ising era — rounder, softer design, gentle comedy, slower pacing",
                art_style="Technicolor cel animation",
                image_url=IMG["barney"],
                notes="Debuted in The Bear That Couldn't Sleep (1939), directed by Rudolf Ising. "
                      "Barney's design was intentionally rounder and softer than most MGM characters "
                      "to reflect his gentle nature."),
            Era(1943, 1954,
                "Quimby / various directors era — design refined, more expressive reactions, "
                "same patient personality",
                art_style="Technicolor cel animation",
                image_url=IMG["barney"],
                notes="Various directors including Michael Lah took over the series. "
                      "Barney never achieved the fame of Droopy or Tom and Jerry "
                      "but remained consistently popular throughout his run."),
        ],
        wiki_slug="Barney_Bear",
    )
    lib.add_cartoon(barney_bear)

    # ══════════════════════════════════════════════════════════════════════
    # THE WOLF (Tex Avery's MGM Wolf) (1943)
    # Avery's defining MGM creation — the lecherous wolf
    # ══════════════════════════════════════════════════════════════════════
    tex_wolf = _mgm(
        name="The Wolf (Tex Avery MGM)",
        description=(
            "An unnamed but instantly recognizable wolf character created by Tex Avery "
            "who appears in a series of wildly anarchic MGM shorts. The Wolf's defining "
            "characteristic is his over-the-top reaction to attractive women — his eyes "
            "literally pop out of his head, his jaw drops to the floor, and he howls "
            "uncontrollably. Most famous as the villain of Red Hot Riding Hood (1943), "
            "which reimagined the fairy tale in a nightclub setting. One of the most "
            "influential character designs in animation — his exaggerated reactions "
            "became a template for cartoon comedy worldwide."
        ),
        character_type="Anthropomorphic animal — wolf / comedic villain",
        debut_year=1943,
        creators=[QUIMBY, TEX_AVERY],
        series_list=[
            Series("Red Hot Riding Hood (debut)", 1943, 1943,
                   "MGM Cartoons / Tex Avery unit", "theatrical short",
                   notes="One of the most influential cartoons ever made. Reimagined Red Riding Hood "
                         "as a nightclub performer and the Wolf as a lecherous audience member."),
            Series("Tex Avery Wolf series", 1943, 1952,
                   "MGM Cartoons / Tex Avery unit", "theatrical short", episode_count=8,
                   notes="Includes Swing Shift Cinderella, Little Rural Riding Hood, "
                         "The Shooting of Dan McGoo, and others."),
        ],
        eras=[
            Era(1943, 1955,
                "Original Avery design — grey wolf in suit, wildly exaggerated expression capable "
                "of physically impossible distortions — jaw to floor, eyes on springs",
                art_style="Technicolor cel animation",
                image_url=IMG["wolf"],
                notes="Voiced by Bill Thompson and later Frank Graham. "
                      "Red Hot Riding Hood (1943) was so popular that MGM received "
                      "letters from soldiers overseas requesting more. "
                      "The Wolf's reaction shots influenced every cartoon studio."),
        ],
        wiki_slug="Tex_Avery%27s_wolf_and_red",
    )
    lib.add_cartoon(tex_wolf)

    # ══════════════════════════════════════════════════════════════════════
    # RED (Red Hot Riding Hood) (1943)
    # The Wolf's counterpart — the nightclub performer
    # ══════════════════════════════════════════════════════════════════════
    red_riding = _mgm(
        name="Red (Red Hot Riding Hood)",
        description=(
            "The reinvented Little Red Riding Hood — instead of an innocent girl "
            "in the woods, Red is a glamorous nightclub singer and dancer in a "
            "sophisticated city club, performing for an audience that includes "
            "the lecherous Wolf. Created by Tex Avery, Red is one of animation's "
            "first and most influential glamour characters. Her design — red dress, "
            "red hair, confident performer — became a template for femme fatale "
            "characters in countless subsequent cartoons and films."
        ),
        character_type="Human — glamorous nightclub performer",
        debut_year=1943,
        creators=[QUIMBY, TEX_AVERY],
        series_list=[
            Series("Red Hot Riding Hood", 1943, 1943,
                   "MGM Cartoons / Tex Avery unit", "theatrical short"),
            Series("Tex Avery Wolf series appearances", 1943, 1952,
                   "MGM Cartoons", "theatrical short", episode_count=6),
        ],
        eras=[
            Era(1943, 1955,
                "Original Avery design — voluptuous red-dressed singer, red hair, "
                "confident stage presence, contrast to the naive fairy tale original",
                art_style="Technicolor cel animation",
                image_url=IMG["red"],
                notes="Voiced by Sara Berner. Red Hot Riding Hood was the first major "
                      "deconstruction of a fairy tale in animation — it broke the fourth wall "
                      "when the characters in the opening complained about doing the same "
                      "old fairy tale and demanded a modern version."),
        ],
        wiki_slug="Tex_Avery%27s_wolf_and_red",
    )
    lib.add_cartoon(red_riding)

    # ══════════════════════════════════════════════════════════════════════
    # SCREWY SQUIRREL (1944)
    # Tex Avery's most anarchic original character
    # ══════════════════════════════════════════════════════════════════════
    screwy = _mgm(
        name="Screwy Squirrel",
        description=(
            "Sammy Squirrel — nicknamed Screwy — is the most purely anarchic "
            "character Tex Avery ever created. Where Bugs Bunny had cool wit and "
            "Droopy had deadpan calm, Screwy has no logic whatsoever. He torments "
            "his adversaries (and sometimes other cartoon characters) with random, "
            "senseless, fourth-wall-breaking violence that makes no narrative sense "
            "and follows no discernible rules. He is chaos itself given a squirrel's "
            "body. Only five Screwy Squirrel cartoons were made but they remain "
            "among the most studied works in animation history."
        ),
        character_type="Anthropomorphic animal — squirrel / anarchic trickster",
        debut_year=1944,
        creators=[QUIMBY, TEX_AVERY],
        series_list=[
            Series("Screwy Squirrel theatrical shorts", 1944, 1946,
                   "MGM Cartoons / Tex Avery unit", "theatrical short", episode_count=5,
                   notes="Only five cartoons were made: Screwball Squirrel, Happy-Go-Nutty, "
                         "Big Heel-Watha, The Screwy Truant, and Lonesome Lenny."),
        ],
        eras=[
            Era(1944, 1946,
                "Original design — small squirrel with manic grin, darting eyes, "
                "constantly breaking the fourth wall and defying cartoon logic",
                art_style="Technicolor cel animation",
                image_url=IMG["screwy"],
                notes="Voiced by Dick Nelson. Screwy Squirrel appeared in only five cartoons "
                      "before Tex Avery abandoned the character — reportedly because even Avery "
                      "felt Screwy was too mean-spirited. The five cartoons remain influential "
                      "on generations of animators including John Kricfalusi (Ren and Stimpy)."),
        ],
        wiki_slug="Screwy_Squirrel",
    )
    lib.add_cartoon(screwy)

    # ══════════════════════════════════════════════════════════════════════
    # GEORGE AND JUNIOR (1944)
    # Avery's Steinbeck-inspired comedy duo
    # ══════════════════════════════════════════════════════════════════════
    george_junior = _mgm(
        name="George and Junior",
        description=(
            "A large, dim-witted bear named George and his smaller, smarter "
            "companion Junior — a direct parody of George Milton and Lennie Small "
            "from John Steinbeck's Of Mice and Men. George is the gentle giant "
            "whose enormous strength causes destruction despite good intentions, "
            "while Junior attempts to control and redirect him with limited success. "
            "The comedy comes from George's cheerful inability to understand "
            "the chaos he leaves in his wake."
        ),
        character_type="Anthropomorphic animals — bear duo / comedy pair",
        debut_year=1944,
        creators=[QUIMBY, TEX_AVERY],
        series_list=[
            Series("George and Junior theatrical shorts", 1944, 1949,
                   "MGM Cartoons / Tex Avery unit", "theatrical short", episode_count=7),
        ],
        eras=[
            Era(1944, 1949,
                "Original design — large round grey bear (George) and small brown bear (Junior), "
                "Steinbeck-inspired visual contrast between bulk and intelligence",
                art_style="Technicolor cel animation",
                image_url=IMG["george"],
                notes="Voiced by Frank Graham (George) and Tex Avery himself (Junior). "
                      "The direct parody of Of Mice and Men was unusual for animation. "
                      "Seven shorts were produced between 1944 and 1949."),
        ],
        wiki_slug="George_and_Junior",
    )
    lib.add_cartoon(george_junior)

    # ══════════════════════════════════════════════════════════════════════
    # LITTLE CHEESER (1936)
    # Harman-Ising era — predates the main MGM cartoon unit
    # ══════════════════════════════════════════════════════════════════════
    little_cheeser = _mgm(
        name="Little Cheeser",
        description=(
            "A small mouse who starred in one of the earliest MGM cartoon series "
            "during the Harman-Ising era before Tom and Jerry. Little Cheeser "
            "appeared in a series of Happy Harmonies shorts — MGM's answer to "
            "Disney's Silly Symphonies — and is one of the earliest examples of "
            "a mouse as a cartoon protagonist, predating Jerry Mouse by four years. "
            "The character is largely forgotten today but represents an important "
            "transitional moment in animation history."
        ),
        character_type="Anthropomorphic animal — mouse",
        debut_year=1936,
        creators=[HARMAN, ISING],
        series_list=[
            Series("Little Cheeser Happy Harmonies shorts", 1936, 1938,
                   "Harman-Ising Productions / MGM", "theatrical short", episode_count=4),
        ],
        eras=[
            Era(1936, 1938,
                "Original Harman-Ising design — small cute mouse in Disney-influenced round style, "
                "soft pastel palette typical of the Happy Harmonies series",
                art_style="Technicolor cel animation",
                image_url=IMG["little"],
                notes="Debuted in Little Cheeser (1936). The Happy Harmonies series was MGM's "
                      "attempt to compete with Disney's Silly Symphonies. "
                      "The series ended when MGM brought Fred Quimby in to restructure the cartoon unit."),
        ],
        wiki_slug="Little_Cheeser",
    )
    lib.add_cartoon(little_cheeser)

    # ══════════════════════════════════════════════════════════════════════
    # CAPTAIN AND THE KIDS / KATZENJAMMER KIDS (1938)
    # Harman-Ising era MGM adaptation of the classic comic strip
    # ══════════════════════════════════════════════════════════════════════
    katzenjammer = _mgm(
        name="The Katzenjammer Kids",
        description=(
            "Hans and Fritz — twin boys of German-American heritage who torment "
            "every adult in their vicinity with elaborate pranks and mischief. "
            "Based on Rudolph Dirks' 1897 comic strip — one of the oldest "
            "continuously published comics in American history — the Katzenjammer Kids "
            "represent some of the earliest cartoon mischief archetypes. "
            "MGM's animated adaptation ran during the Harman-Ising era and "
            "preceded the slapstick tradition that Tom and Jerry would later perfect."
        ),
        character_type="Human — mischievous twin boys",
        debut_year=1938,
        creators=[HARMAN, ISING],
        series_list=[
            Series("The Captain and the Kids MGM shorts", 1938, 1939,
                   "Harman-Ising Productions / MGM", "theatrical short", episode_count=12,
                   notes="MGM adaptation of the classic Katzenjammer Kids comic strip by Rudolph Dirks."),
        ],
        eras=[
            Era(1938, 1939,
                "MGM Harman-Ising design — round-headed German-American boy twins, "
                "sailor suits, identical mischievous expressions",
                art_style="Technicolor cel animation",
                image_url=IMG["happy"],
                notes="Based on Rudolph Dirks' 1897 newspaper comic strip — one of the oldest "
                      "American comics. MGM produced 12 shorts before the unit was restructured. "
                      "The original comic strip predates cinema itself."),
        ],
        wiki_slug="The_Katzenjammer_Kids",
        origin="Culver City, California, USA — Harman-Ising Productions / MGM",
    )
    lib.add_cartoon(katzenjammer)

    # ══════════════════════════════════════════════════════════════════════
    # CROW (Two Crows from Taos / Cartoons) — MGM's crow characters
    # ══════════════════════════════════════════════════════════════════════

    # ══════════════════════════════════════════════════════════════════════
    # FIELD AND SCREE (Deputy Droopy antagonists)
    # ══════════════════════════════════════════════════════════════════════

    # ══════════════════════════════════════════════════════════════════════
    # THE FAIRY GODMOTHER / FAIRY TALES CHARACTERS (Avery era)
    # ══════════════════════════════════════════════════════════════════════

    # ══════════════════════════════════════════════════════════════════════
    # SPIKE and CHESTER (cat and dog duo, not the bulldog)
    # Brief MGM characters from Tex Avery shorts
    # ══════════════════════════════════════════════════════════════════════
    spike_chester = _mgm(
        name="Spike and Chester",
        description=(
            "A large, confident bulldog named Spike and his small, hero-worshipping "
            "companion Chester — a terrier who follows Spike everywhere and constantly "
            "peppers him with excited questions. The comedy comes from Chester's "
            "boundless enthusiasm for Spike's perceived toughness and Spike's "
            "increasingly desperate attempts to maintain his cool facade. "
            "A different Spike from the Tom and Jerry bulldog — this duo appeared "
            "exclusively in Tex Avery's standalone shorts."
        ),
        character_type="Anthropomorphic animals — bulldog and terrier comedy duo",
        debut_year=1952,
        creators=[QUIMBY, TEX_AVERY],
        series_list=[
            Series("Spike and Chester Tex Avery shorts", 1952, 1955,
                   "MGM Cartoons / Tex Avery unit", "theatrical short", episode_count=3,
                   notes="Three cartoons: Rock-a-Bye Bear, Half-Pint Palomino, and others."),
        ],
        eras=[
            Era(1952, 1955,
                "Original Avery design — large grey bulldog and tiny energetic terrier, "
                "size contrast emphasizing the comedy dynamic",
                art_style="Technicolor cel animation",
                image_url=IMG["mgm"],
                notes="Voiced by Daws Butler (Chester) using his rapid-fire enthusiastic delivery. "
                      "Rock-a-Bye Bear (1952) is the most celebrated of the three shorts."),
        ],
        wiki_slug="Spike_and_Chester",
    )
    lib.add_cartoon(spike_chester)

    # ══════════════════════════════════════════════════════════════════════
    # UNCLE TOM / TOM TOM AND JERRY MOUSE FROM PUSS GETS THE BOOT
    # The proto-Tom and Jerry versions
    # ══════════════════════════════════════════════════════════════════════
    jasper_jinx = _mgm(
        name="Jasper and Jinx (Proto-Tom and Jerry)",
        description=(
            "The original names of Tom and Jerry before they became Tom and Jerry. "
            "In their debut short Puss Gets the Boot (1940) the cat was called "
            "Jasper and the mouse had no name (later called Jinx in production notes). "
            "This proto-version of the cat-and-mouse formula established the core "
            "dynamic — a house cat trying to catch a clever mouse — that Hanna and "
            "Barbera would refine into one of animation's greatest franchises. "
            "After the overwhelming popularity of Puss Gets the Boot, MGM commissioned "
            "more cartoons and the characters were renamed Tom and Jerry."
        ),
        character_type="Anthropomorphic animals — proto-Tom and Jerry",
        debut_year=1940,
        creators=[QUIMBY, HANNA, BARBERA],
        series_list=[
            Series("Puss Gets the Boot debut short", 1940, 1940,
                   "MGM Cartoons / Hanna-Barbera unit", "theatrical short",
                   notes="The short that launched the Tom and Jerry franchise. "
                         "Nominated for the Academy Award for Best Animated Short Film."),
        ],
        eras=[
            Era(1940, 1940,
                "Proto-Tom and Jerry — same fundamental design as the later characters "
                "but slightly rougher, rounder, less refined",
                art_style="Technicolor cel animation",
                image_url=IMG["tom"],
                notes="Puss Gets the Boot (February 20 1940) was nominated for the Academy Award "
                      "for Best Animated Short Film but lost to Milky Way (MGM's own Rudolph Ising). "
                      "Producer Fred Quimby initially did not want a sequel before audience "
                      "demand made the decision for him."),
        ],
        wiki_slug="Puss_Gets_the_Boot",
    )
    lib.add_cartoon(jasper_jinx)

    # ══════════════════════════════════════════════════════════════════════
    # THE KING (King-Size Canary character)
    # Tex Avery one-shot character — one of animation's most celebrated shorts
    # ══════════════════════════════════════════════════════════════════════
    kingsize = _mgm(
        name="King-Size Canary Characters",
        description=(
            "The characters from Tex Avery's King-Size Canary (1947) — "
            "considered by many animation historians and directors (including "
            "John Lasseter) to be the single greatest cartoon ever made. "
            "A cat, a mouse, a bulldog, and a canary all compete to drink "
            "from a bottle of Jumbo-Gro plant food, growing to increasingly "
            "absurd sizes until they are larger than the planet Earth. "
            "The cartoon is the purest expression of cartoon logic — taking "
            "a single premise to its absolute impossible extreme."
        ),
        character_type="Anthropomorphic animals — one-short ensemble",
        debut_year=1947,
        creators=[QUIMBY, TEX_AVERY],
        series_list=[
            Series("King-Size Canary", 1947, 1947,
                   "MGM Cartoons / Tex Avery unit", "theatrical short",
                   notes="Frequently cited as the greatest cartoon ever made by animation "
                         "professionals including John Lasseter, Brad Bird, and others."),
        ],
        eras=[
            Era(1947, 1947,
                "One-short designs — standard Avery animal characters escalating to impossible sizes",
                art_style="Technicolor cel animation",
                image_url=IMG["mgm"],
                notes="King-Size Canary (December 6 1947) ends with the characters so large "
                      "they have consumed all the Jumbo-Gro. They address the camera directly "
                      "to announce there is no more to drink and the cartoon ends. "
                      "John Lasseter of Pixar has called it the greatest cartoon ever made."),
        ],
        wiki_slug="King-Size_Canary",
    )
    lib.add_cartoon(kingsize)

    # ══════════════════════════════════════════════════════════════════════
    # PEACE ON EARTH / CHARACTERS (1939)
    # Harman-Ising's anti-war masterpiece — Oscar nominated
    # ══════════════════════════════════════════════════════════════════════
    peace_earth = _mgm(
        name="Peace on Earth (Woodland Animals)",
        description=(
            "The small woodland animals — squirrels, rabbits, birds and others — "
            "who inhabit a peaceful post-human world in Hugh Harman's remarkable "
            "anti-war short Peace on Earth (1939). After humanity destroys itself "
            "in a final war, the animals rebuild civilization and pass down the "
            "story as a cautionary legend. Released just months after Germany "
            "invaded Poland, Peace on Earth was nominated for the Nobel Peace Prize "
            "and an Academy Award — extraordinary achievements for a cartoon."
        ),
        character_type="Anthropomorphic animals — peaceful woodland community",
        debut_year=1939,
        creators=[HARMAN],
        series_list=[
            Series("Peace on Earth short film", 1939, 1939,
                   "Harman-Ising Productions / MGM", "theatrical short",
                   notes="Nominated for the Nobel Peace Prize and the Academy Award for Best Short Subject."),
            Series("Good Will to Men remake", 1955, 1955,
                   "MGM Cartoons", "theatrical short",
                   notes="Remake directed by William Hanna and Joseph Barbera."),
        ],
        eras=[
            Era(1939, 1955,
                "Soft naturalistic woodland animal designs — deliberately gentle and innocent "
                "to contrast with the violence of human warfare depicted in the film",
                art_style="Technicolor cel animation",
                image_url=IMG["peace"],
                notes="Released December 9 1939. Hugh Harman's masterpiece. "
                      "The film was submitted for consideration for the Nobel Peace Prize — "
                      "the only animated film ever to receive such consideration. "
                      "The 1955 remake Good Will to Men updated the story for the atomic age."),
        ],
        wiki_slug="Peace_on_Earth_(film)",
    )
    lib.add_cartoon(peace_earth)

    # ══════════════════════════════════════════════════════════════════════
    # LONESOME LENNY (1946)
    # Tex Avery's devastating short — Screwy Squirrel's darkest moment
    # ══════════════════════════════════════════════════════════════════════
    lenny = _mgm(
        name="Lonesome Lenny",
        description=(
            "A enormous, good-natured but disastrously strong dog — a direct "
            "parody of Lennie from Of Mice and Men — who wants nothing more than "
            "a small pet to love and hold. His affection is so powerful it is "
            "literally fatal to anyone he squeezes. In one of Tex Avery's darkest "
            "and most remarkable cartoons, Screwy Squirrel becomes Lenny's pet "
            "with predictably catastrophic results. Lonesome Lenny (1946) is "
            "one of the most emotionally complex shorts in animation history."
        ),
        character_type="Anthropomorphic animal — dog / tragic figure",
        debut_year=1946,
        creators=[QUIMBY, TEX_AVERY],
        series_list=[
            Series("Lonesome Lenny theatrical short", 1946, 1946,
                   "MGM Cartoons / Tex Avery unit", "theatrical short",
                   notes="A parody of Of Mice and Men featuring Screwy Squirrel "
                         "as the inadvertent victim. One of Tex Avery's most studied works."),
        ],
        eras=[
            Era(1946, 1946,
                "Massive round dog with gentle expression — enormous physical contrast "
                "with his tiny pet, tragic dramatic irony built into his design",
                art_style="Technicolor cel animation",
                image_url=IMG["mgm"],
                notes="Lonesome Lenny (March 9 1946) ends with Lenny accidentally killing "
                      "Screwy Squirrel — one of animation's most shocking conclusions. "
                      "Lenny breaks the fourth wall and asks the audience for a new friend "
                      "in the final frame. Animation historians cite it alongside "
                      "King-Size Canary as Avery's greatest achievements."),
        ],
        wiki_slug="Lonesome_Lenny",
    )
    lib.add_cartoon(lenny)

    # ══════════════════════════════════════════════════════════════════════
    # THE FIELD MOUSE (The Field and the Forest / MGM nature shorts)
    # ══════════════════════════════════════════════════════════════════════

    # ══════════════════════════════════════════════════════════════════════
    # BULLFIGHTER CHARACTERS — El Terrible Toro, etc. (Avery)
    # ══════════════════════════════════════════════════════════════════════

    # ══════════════════════════════════════════════════════════════════════
    # UNCLE TOM'S CABIN CHARACTERS (1947)
    # ══════════════════════════════════════════════════════════════════════

    # ══════════════════════════════════════════════════════════════════════
    # THE THREE LITTLE PUPS (1953) — Droopy as a pup
    # ══════════════════════════════════════════════════════════════════════
    three_pups = _mgm(
        name="Three Little Pups",
        description=(
            "Three puppy versions of the Droopy character in a parody of The "
            "Three Little Pigs — facing a fast-talking Southern wolf who attempts "
            "to blow down their houses. Three Little Pups (1953) is one of Tex "
            "Avery's most beloved late-period MGM cartoons and features some of "
            "the most elaborate visual gags of his entire career including an "
            "extended sequence involving a T.V. set that breaks the fourth wall "
            "in multiple directions simultaneously."
        ),
        character_type="Anthropomorphic animals — three puppy brothers",
        debut_year=1953,
        creators=[QUIMBY, TEX_AVERY],
        series_list=[
            Series("Three Little Pups theatrical short", 1953, 1953,
                   "MGM Cartoons / Tex Avery unit", "theatrical short",
                   notes="Parody of Three Little Pigs featuring Droopy-styled puppy characters."),
        ],
        eras=[
            Era(1953, 1953,
                "Three small Droopy-styled puppies in Three Pigs parody setting — "
                "same deadpan quality as Droopy himself",
                art_style="Technicolor cel animation",
                image_url=IMG["droopy"],
                notes="Three Little Pups (December 26 1953) was one of Avery's final MGM cartoons. "
                      "The TV set gag sequence is widely studied in animation schools as an example "
                      "of escalating absurdist comedy."),
        ],
        wiki_slug="Three_Little_Pups",
    )
    lib.add_cartoon(three_pups)

    # ══════════════════════════════════════════════════════════════════════
    # CATNIP (The Milky Waif characters) — various Hanna-Barbera Tom & Jerry
    # supporting characters beyond Spike
    # ══════════════════════════════════════════════════════════════════════
    nibbles = _mgm(
        name="Nibbles (Tuffy Mouse)",
        description=(
            "A tiny grey baby mouse — Jerry's orphaned nephew or ward — who "
            "appears in some of Tom and Jerry's most beloved shorts. Nibbles "
            "is even smaller than Jerry and has an enormous appetite, "
            "constantly seeking food regardless of the danger around him. "
            "His complete obliviousness to Tom's threat — happily eating "
            "while chaos erupts around him — provides a fresh comedic dynamic. "
            "Two of his shorts — The Two Mouseketeers and Johann Mouse — won "
            "the Academy Award for Best Animated Short Film."
        ),
        character_type="Anthropomorphic animal — baby mouse",
        debut_year=1946,
        creators=[QUIMBY, HANNA, BARBERA],
        series_list=[
            Series("Tom and Jerry shorts featuring Nibbles", 1946, 1957,
                   "MGM Cartoons / Hanna-Barbera unit", "theatrical short", episode_count=9,
                   notes="Includes The Milky Waif (debut), The Two Mouseketeers (AA winner), "
                         "and Johann Mouse (AA winner)."),
            Series("Tom and Jerry TV appearances", 1975, None,
                   "various", "TV series and streaming"),
        ],
        eras=[
            Era(1946, 1957,
                "Tiny grey baby mouse in diaper — smaller than Jerry, enormous eyes, "
                "constantly eating, unaware of danger around him",
                art_style="Technicolor cel animation",
                image_url=IMG["tom"],
                notes="Debuted in The Milky Waif (May 18 1946). "
                      "The Two Mouseketeers (1952) and Johann Mouse (1953) both won Academy Awards. "
                      "Nibbles speaks French in the Musketeer shorts — a charming detail "
                      "that adds to his character."),
            Era(1975, None,
                "TV and modern era — appears occasionally in Tom and Jerry revivals",
                art_style="Various",
                image_url=IMG["tom"],
                notes="Nibbles appears in the 1975 TV series and various modern Tom and Jerry productions."),
        ],
        wiki_slug="Nibbles_(Tom_and_Jerry)",
    )
    lib.add_cartoon(nibbles)

    # ══════════════════════════════════════════════════════════════════════
    # DUCK (One-shot characters from Duck Dodgers and Avery shorts)
    # ══════════════════════════════════════════════════════════════════════

    # ══════════════════════════════════════════════════════════════════════
    # THE WOLF FROM AVERY'S FAIRY TALE SHORTS
    # ══════════════════════════════════════════════════════════════════════
    fairy_wolf = _mgm(
        name="The Three Little Bears (MGM)",
        description=(
            "Mama Bear, Papa Bear, and Baby Bear from Tex Avery's anarchic "
            "reimagining of the Goldilocks fairy tale in The Three Bears (1944). "
            "Unlike the gentle storybook originals, Avery's bears are a bickering, "
            "neurotic family whose domestic dysfunction provides the comedy. "
            "Papa Bear is a frustrated patriarch, Mama Bear is oblivious, and "
            "Baby Bear is a mischievous teenager. The short deconstructs the "
            "fairy tale with the same irreverence Avery applied to Red Riding Hood."
        ),
        character_type="Anthropomorphic animals — fairy tale bear family",
        debut_year=1944,
        creators=[QUIMBY, TEX_AVERY],
        series_list=[
            Series("The Three Bears MGM short", 1944, 1944,
                   "MGM Cartoons / Tex Avery unit", "theatrical short"),
            Series("Bear Family follow-up appearances", 1949, 1952,
                   "MGM Cartoons", "theatrical short", episode_count=2),
        ],
        eras=[
            Era(1944, 1952,
                "Avery-style bear family — more human proportioned and emotionally realistic "
                "than typical cartoon bears, emphasizing domestic neurosis over fairy tale charm",
                art_style="Technicolor cel animation",
                image_url=IMG["mgm"],
                notes="The Three Bears (September 9 1944) was followed by two more shorts featuring "
                      "the same family. Avery used the bears to satirize postwar American family "
                      "dynamics — an unusually sophisticated subtext for a cartoon."),
        ],
        wiki_slug="The_Three_Bears_(1944_film)",
    )
    lib.add_cartoon(fairy_wolf)

    # ══════════════════════════════════════════════════════════════════════
    # HAPPY HARMONIES CHARACTERS (Harman-Ising era, 1934-1938)
    # The pre-Quimby MGM cartoon stars
    # ══════════════════════════════════════════════════════════════════════
    happy_harmonies = _mgm(
        name="Happy Harmonies Ensemble",
        description=(
            "The collection of characters who starred in the Happy Harmonies "
            "series — MGM's answer to Disney's Silly Symphonies, produced by "
            "Hugh Harman and Rudolf Ising between 1934 and 1938. The series "
            "prioritized visual beauty and musical synchronization over character "
            "comedy, producing some of the most technically beautiful animation "
            "of the mid-1930s. Key characters included The Blue Danube animals, "
            "toy soldiers, fairy tale characters, and the recurring Little Cheeser. "
            "The series won two Academy Awards and demonstrated that MGM could "
            "match Disney's technical quality."
        ),
        character_type="Various — fairy tale and musical short ensemble",
        debut_year=1934,
        creators=[HARMAN, ISING],
        series_list=[
            Series("Happy Harmonies series", 1934, 1938,
                   "Harman-Ising Productions / MGM", "theatrical short", episode_count=28,
                   notes="MGM's prestige animation series before Fred Quimby restructured the unit."),
        ],
        eras=[
            Era(1934, 1938,
                "Harman-Ising signature style — lush Technicolor, Disney-influenced rounded designs, "
                "musical synchronization, soft naturalistic backgrounds",
                art_style="Early Technicolor cel animation",
                image_url=IMG["happy"],
                notes="The Happy Harmonies series ran 28 shorts and won Academy Awards for "
                      "The Old Mill Pond (1936) and To Spring (1936). "
                      "When Fred Quimby took over in 1937 he ended the Harman-Ising partnership "
                      "and restructured the unit toward faster, cheaper character comedy."),
        ],
        wiki_slug="Happy_Harmonies",
        origin="Culver City, California, USA — Harman-Ising Productions / MGM",
    )
    lib.add_cartoon(happy_harmonies)

    print(f"MGM characters added. Library now has {len(lib.cartoons)} cartoons total.")
