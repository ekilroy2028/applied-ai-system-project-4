"""
nickelodeon_characters.py
Major Nickelodeon animated characters for CartoonPal.

Nickelodeon launched as a cable channel in 1977 and began producing
original animation (Nicktoons) in 1991. It is owned by Paramount Global
(formerly ViacomCBS / Viacom).

Ownership chain for all Nickelodeon originals:
- Nickelodeon / Viacom (original) — various dates
- ViacomCBS (2019) — Viacom and CBS merger
- Paramount Global (2022) — ViacomCBS rebranded

NOTE: Avatar: The Last Airbender and Legend of Korra are Nickelodeon
productions but their IP is controlled separately through Nickelodeon's
Avatar Studios division.

Usage:
    from characters.nickelodeon_characters import add_nickelodeon_characters
    add_nickelodeon_characters(lib)
"""

from cartoon_system import (
    Cartoon, Creator, ProductionCompany,
    Series, OwnershipRecord, Era, Library
)

NICK = ProductionCompany("Nickelodeon Animation Studio", 1977, country="USA", still_active=True)

NICK_OWN = [
    ("Nickelodeon / Viacom", 1977, 2019, "original creation"),
    ("ViacomCBS", 2019, 2022, "Viacom and CBS merger"),
    ("Paramount Global", 2022, None, "ViacomCBS rebranded to Paramount Global"),
]

IMG = {
    "sponge":  "https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/SpongeBob_SquarePants_character.svg/200px-SpongeBob_SquarePants_character.svg.png",
    "rugrats": "https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/Rugrats_logo.png/240px-Rugrats_logo.png",
    "arnold":  "https://upload.wikimedia.org/wikipedia/en/thumb/6/6d/Hey_Arnold_title_card.png/240px-Hey_Arnold_title_card.png",
    "avatar":  "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Avatar_The_Last_Airbender_title_card.png/240px-Avatar_The_Last_Airbender_title_card.png",
    "fairly":  "https://upload.wikimedia.org/wikipedia/en/thumb/4/4e/Fairly_OddParents_logo.png/240px-Fairly_OddParents_logo.png",
    "danny":   "https://upload.wikimedia.org/wikipedia/en/thumb/5/5a/Danny_Phantom_logo.png/240px-Danny_Phantom_logo.png",
    "invader": "https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/Invader_Zim_logo.png/240px-Invader_Zim_logo.png",
    "rocko":   "https://upload.wikimedia.org/wikipedia/en/thumb/6/6e/Rocko%27s_Modern_Life_title_card.png/240px-Rocko%27s_Modern_Life_title_card.png",
    "ren":     "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Ren_%26_Stimpy.png/240px-Ren_%26_Stimpy.png",
    "doug":    "https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/Doug_title_card.png/200px-Doug_title_card.png",
    "catdog":  "https://upload.wikimedia.org/wikipedia/en/thumb/4/4e/CatDog_title_card.png/200px-CatDog_title_card.png",
    "korra":   "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/The_Legend_of_Korra_logo.png/240px-The_Legend_of_Korra_logo.png",
    "loud":    "https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/The_Loud_House_logo.png/240px-The_Loud_House_logo.png",
    "ninja":   "https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/Teenage_Mutant_Ninja_Turtles_2012_logo.png/240px-Teenage_Mutant_Ninja_Turtles_2012_logo.png",
    "nick":    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Nickelodeon_2009_logo.svg/240px-Nickelodeon_2009_logo.svg.png",
}


def _nick(name, description, character_type, debut_year,
          creators, series_list, eras, wiki_slug,
          origin="Burbank, California, USA — Nickelodeon Animation Studio"):
    c = Cartoon(name=name, description=description,
                character_type=character_type,
                country_of_origin="USA", debut_year=debut_year)
    c.original_studio = NICK
    for cr in creators:
        c.add_creator(cr)
    for s in series_list:
        c.add_series(s)
    for i, rec in enumerate(NICK_OWN):
        is_cur = (i == len(NICK_OWN) - 1)
        c.add_ownership_record(OwnershipRecord(
            rec[0], rec[1], rec[2], rec[3], is_current_owner=is_cur))
    for era in eras:
        c.add_era(era)
    c.wiki_url = f"https://en.wikipedia.org/wiki/{wiki_slug}"
    c.origin_location = origin
    return c


def add_nickelodeon_characters(lib: Library):

    # ── SpongeBob SquarePants (1999) ──────────────────────────────────────
    spongebob = _nick(
        name="SpongeBob SquarePants",
        description=(
            "A cheerful, optimistic sea sponge who lives in a pineapple under "
            "the sea in Bikini Bottom and works as a fry cook at the Krusty Krab. "
            "Created by marine science educator Stephen Hillenburg, SpongeBob is "
            "Nickelodeon's most successful franchise — generating billions annually "
            "in merchandise. Beloved for its surreal humor, visual creativity, and "
            "writing that appeals equally to adults and children. "
            "SpongeBob memes became a defining internet cultural phenomenon."
        ),
        character_type="Anthropomorphic animal — sea sponge / fry cook",
        debut_year=1999,
        creators=[Creator("Stephen Hillenburg", "Series creator — marine science educator turned animator", 1961, 2018)],
        series_list=[
            Series("SpongeBob SquarePants", 1999, None,
                   "Nickelodeon Animation Studio", "TV series",
                   notes="Longest-running Nickelodeon series. 14+ seasons, 300+ episodes. "
                         "Debuted May 1 1999."),
            Series("The SpongeBob SquarePants Movie", 2004, 2004,
                   "Paramount Pictures / Nickelodeon Movies", "theatrical feature"),
            Series("The SpongeBob Movie Sponge Out of Water", 2015, 2015,
                   "Paramount Pictures", "theatrical feature"),
            Series("The SpongeBob Movie Sponge on the Run", 2020, 2020,
                   "Paramount Pictures", "theatrical feature"),
            Series("The Patrick Star Show spinoff", 2021, None,
                   "Nickelodeon", "TV series"),
            Series("Kamp Koral prequel series", 2021, None,
                   "Nickelodeon / Paramount+", "streaming series"),
        ],
        eras=[
            Era(1999, 2004,
                "Stephen Hillenburg golden era — hand-drawn surreal humor, "
                "Seasons 1-3 widely considered the creative peak",
                art_style="Traditional cel animation",
                image_url=IMG["sponge"],
                notes="Hillenburg insisted on no merchandise during his original tenure. "
                      "The first three seasons are animation classics. "
                      "Hillenburg left after the 2004 film, returned 2015, died 2018 from ALS."),
            Era(2005, 2018,
                "Post-Hillenburg first era — more slapstick, enormous global expansion, "
                "SpongeBob memes become internet staple",
                art_style="Digital animation",
                image_url=IMG["sponge"],
                notes="Hillenburg returned in 2015 to steer the show back to its roots. "
                      "SpongeBob became one of the most-memed characters in internet history."),
            Era(2019, None,
                "Expanded universe era — spinoffs Hillenburg opposed, "
                "streaming content, CGI productions",
                art_style="Digital animation / CGI",
                image_url=IMG["sponge"],
                notes="Following Hillenburg's death the franchise expanded with spinoffs. "
                      "SpongeBob remains Nickelodeon's most valuable IP."),
        ],
        wiki_slug="SpongeBob_SquarePants",
    )
    lib.add_cartoon(spongebob)

    # ── Patrick Star ────────────────────────────────────────────────────
    patrick = _nick(
        name="Patrick Star",
        description=(
            "SpongeBob's best friend — a dim-witted, cheerful pink starfish who "
            "lives under a rock in Bikini Bottom with no job and no goals beyond "
            "eating and spending time with SpongeBob. Patrick's stupidity produces "
            "moments of accidental wisdom and unshakeable loyalty. "
            "'Surprised Patrick' became one of the most used reaction memes "
            "in internet history. He stars in his own spinoff The Patrick Star Show."
        ),
        character_type="Anthropomorphic animal — starfish / loyal best friend",
        debut_year=1999,
        creators=[Creator("Stephen Hillenburg", "Series creator", 1961, 2018)],
        series_list=[
            Series("SpongeBob SquarePants", 1999, None, "Nickelodeon", "TV series"),
            Series("The Patrick Star Show", 2021, None, "Nickelodeon", "TV series",
                   notes="Patrick's own spinoff series featuring his eccentric family."),
        ],
        eras=[
            Era(1999, None,
                "Pink starfish in green shorts — perpetually confused, "
                "lives under a rock, one of animation's great sidekicks",
                art_style="Traditional cel / digital animation",
                image_url=IMG["sponge"],
                notes="Voiced by Bill Fagerbakke throughout. "
                      "Surprised Patrick meme is one of the most recognizable reaction images online."),
        ],
        wiki_slug="Patrick_Star",
    )
    lib.add_cartoon(patrick)

    # ── Squidward Tentacles ─────────────────────────────────────────────
    squidward = _nick(
        name="Squidward Tentacles",
        description=(
            "SpongeBob's grumpy, self-important neighbor — a squid (actually an "
            "octopus) who considers himself a great artist and clarinet player "
            "despite being terrible at both. Works the cash register at the Krusty "
            "Krab and resents every moment of it. Squidward's thwarted ambitions "
            "and perpetual misery make him one of animation's most relatable "
            "adult characters — the overqualified worker trapped in a job he hates."
        ),
        character_type="Anthropomorphic animal — octopus / reluctant neighbor",
        debut_year=1999,
        creators=[Creator("Stephen Hillenburg", "Series creator", 1961, 2018)],
        series_list=[
            Series("SpongeBob SquarePants", 1999, None, "Nickelodeon", "TV series"),
        ],
        eras=[
            Era(1999, None,
                "Large-nosed teal octopus in brown shirt, Easter Island head home, "
                "perpetual disdain for SpongeBob and existence",
                art_style="Traditional cel / digital animation",
                image_url=IMG["sponge"],
                notes="Voiced by Rodger Bumpass. Despite being called Squidward Tentacles "
                      "he is an octopus — a running in-show joke. "
                      "Adults who grew up watching SpongeBob see themselves in Squidward."),
        ],
        wiki_slug="Squidward_Tentacles",
    )
    lib.add_cartoon(squidward)

    # ── Rugrats (1991) ──────────────────────────────────────────────────
    rugrats = _nick(
        name="Rugrats",
        description=(
            "Tommy Pickles, Chuckie Finster, Phil and Lil DeVille, and the bossy "
            "Angelica Pickles — toddlers who experience the world from a baby's "
            "perspective, embarking on imaginative adventures their parents know "
            "nothing about. Nickelodeon's first original animated series, "
            "Rugrats was groundbreaking for depicting babies as complex characters "
            "with genuine inner lives, fears, and friendships. "
            "The Rugrats Movie (1998) grossed $140 million worldwide."
        ),
        character_type="Human — toddler ensemble / imagination adventures",
        debut_year=1991,
        creators=[
            Creator("Arlene Klasky", "Co-creator", 1949),
            Creator("Gabor Csupo", "Co-creator", 1952),
            Creator("Paul Germain", "Co-creator", 1959),
        ],
        series_list=[
            Series("Rugrats original run", 1991, 2004,
                   "Klasky Csupo / Nickelodeon", "TV series", episode_count=172,
                   notes="Debuted August 11 1991 — one of the original three Nicktoons."),
            Series("The Rugrats Movie", 1998, 1998,
                   "Paramount Pictures / Nickelodeon Movies", "theatrical feature"),
            Series("Rugrats in Paris The Movie", 2000, 2000,
                   "Paramount Pictures", "theatrical feature"),
            Series("Rugrats Go Wild", 2003, 2003,
                   "Paramount Pictures", "theatrical feature"),
            Series("All Grown Up spinoff", 2003, 2008,
                   "Nickelodeon", "TV series", episode_count=54),
            Series("Rugrats CGI reboot", 2021, 2023,
                   "Nickelodeon / Paramount+", "streaming series"),
        ],
        eras=[
            Era(1991, 2004,
                "Klasky Csupo original — scratchy hand-drawn style, baby-eye-view of the world",
                art_style="Klasky Csupo hand-drawn animation",
                image_url=IMG["rugrats"],
                notes="Rugrats ran for 13 years and spawned a successful film trilogy. "
                      "The All Grown Up spinoff showed the babies as teenagers."),
            Era(2021, None,
                "CGI reboot — updated 3D designs on Paramount+",
                art_style="CGI animation",
                image_url=IMG["rugrats"],
                notes="The 2021 reboot updated the visual style to CGI. Mixed fan reception."),
        ],
        wiki_slug="Rugrats",
    )
    lib.add_cartoon(rugrats)

    # ── Hey Arnold! (1996) ──────────────────────────────────────────────
    hey_arnold = _nick(
        name="Hey Arnold!",
        description=(
            "Arnold Shortman — a kind, philosophical fourth-grader with a "
            "football-shaped head — lives with his grandparents in a boarding house "
            "in the urban city of Hillwood. Created by Craig Bartlett, Hey Arnold! "
            "was notable for its urban setting, diverse cast, jazz soundtrack, "
            "and unusual emotional maturity — dealing with poverty, abandonment, "
            "and loneliness in ways rare in children's animation. "
            "The Jungle Movie (2017) finally resolved Arnold's missing parents mystery."
        ),
        character_type="Human — philosophical urban kid / daydreamer",
        debut_year=1996,
        creators=[Creator("Craig Bartlett", "Series creator", 1956)],
        series_list=[
            Series("Hey Arnold!", 1996, 2004,
                   "Nickelodeon Animation Studio", "TV series", episode_count=100,
                   notes="Debuted October 7 1996."),
            Series("Hey Arnold! The Movie", 2002, 2002,
                   "Paramount Pictures", "theatrical feature"),
            Series("Hey Arnold! The Jungle Movie", 2017, 2017,
                   "Nickelodeon", "TV movie",
                   notes="13-year-later conclusion resolving Arnold's missing parents storyline."),
        ],
        eras=[
            Era(1996, 2004,
                "Original series — football-headed kid in urban boarding house, "
                "jazz soundtrack, unusual emotional depth",
                art_style="Flat color TV animation",
                image_url=IMG["arnold"],
                notes="Craig Bartlett based Arnold on characters from his own short films. "
                      "The show's urban diversity and jazz aesthetic set it apart."),
            Era(2017, None,
                "Jungle Movie conclusion — 13 years later, resolved the mystery fans waited for",
                art_style="Updated digital animation",
                image_url=IMG["arnold"],
                notes="The Jungle Movie was widely praised for giving the show a proper ending."),
        ],
        wiki_slug="Hey_Arnold!",
    )
    lib.add_cartoon(hey_arnold)

    # ── Rocko's Modern Life (1993) ──────────────────────────────────────
    rocko = _nick(
        name="Rocko's Modern Life",
        description=(
            "Rocko — a wallaby from Australia living in the American city of O-Town — "
            "navigates modern suburban life with friends Heffer the steer and Filburt "
            "the turtle. Created by Joe Murray, Rocko's Modern Life was Nickelodeon's "
            "most adult-oriented 1990s Nicktoon — packed with disguised adult humor "
            "satirizing consumerism, conformity, and the absurdity of modern life. "
            "The 2019 Netflix special Static Cling dealt boldly with transgender identity."
        ),
        character_type="Anthropomorphic animal — Australian wallaby / suburban everyman",
        debut_year=1993,
        creators=[Creator("Joe Murray", "Series creator", 1961)],
        series_list=[
            Series("Rocko's Modern Life", 1993, 1996,
                   "Nickelodeon Animation Studio", "TV series", episode_count=52,
                   notes="Debuted September 18 1993."),
            Series("Rocko's Modern Life Static Cling Netflix special", 2019, 2019,
                   "Nickelodeon / Netflix", "streaming special",
                   notes="Long-awaited Netflix revival. Praised for its transgender storyline."),
        ],
        eras=[
            Era(1993, 1996,
                "Original series — dense adult jokes in children's format, "
                "O-Town suburban satire, Heffer and Filburt",
                art_style="Flat color TV animation",
                image_url=IMG["rocko"],
                notes="Notoriously filled with adult jokes that Nickelodeon censors missed. "
                      "Hugely influential on the generation of animators that followed."),
            Era(2019, None,
                "Static Cling revival — meta-commentary on nostalgia, "
                "transgender storyline handled with grace",
                art_style="Updated digital animation",
                image_url=IMG["rocko"],
                notes="The 2019 Netflix special featured a beloved character coming out "
                      "as transgender — one of animation's most thoughtful handling of the topic."),
        ],
        wiki_slug="Rocko%27s_Modern_Life",
    )
    lib.add_cartoon(rocko)

    # ── The Ren & Stimpy Show (1991) ────────────────────────────────────
    ren_stimpy = _nick(
        name="The Ren and Stimpy Show",
        description=(
            "Ren Hoek — a neurotic, violent Chihuahua — and Stimpy — a cheerful, "
            "dim-witted cat — in grotesquely detailed, surreally violent adventures. "
            "Created by John Kricfalusi, Ren and Stimpy revolutionized animation in "
            "1991 with its extreme close-ups, repulsive detail, fluid animation, "
            "and adult content. It inspired an entire generation of animators. "
            "Kricfalusi was fired by Nickelodeon in 1992 over content disputes and "
            "missed deadlines."
        ),
        character_type="Anthropomorphic animals — chihuahua and cat / surreal adult comedy",
        debut_year=1991,
        creators=[Creator("John Kricfalusi", "Series creator — fired by Nickelodeon 1992", 1955)],
        series_list=[
            Series("The Ren and Stimpy Show (Nickelodeon Spumco era)", 1991, 1992,
                   "Spumco / Nickelodeon", "TV series", episode_count=13,
                   notes="Kricfalusi's original run — considered the creative masterwork."),
            Series("The Ren and Stimpy Show (Games Animation era)", 1993, 1996,
                   "Games Animation / Nickelodeon", "TV series", episode_count=39,
                   notes="Produced without Kricfalusi after his firing."),
        ],
        eras=[
            Era(1991, 1992,
                "Spumco Kricfalusi era — extreme fluid animation, grotesque detail, "
                "groundbreaking visual style, adult content",
                art_style="Ultra-detailed hand-drawn animation",
                image_url=IMG["ren"],
                notes="Debuted August 11 1991. Kricfalusi fired in 1992. "
                      "These first seasons are considered animation masterpieces. "
                      "Directly inspired SpongeBob, Rocko, Fairly OddParents creators."),
            Era(1993, None,
                "Post-Kricfalusi era — same characters, less extreme style",
                art_style="Simplified TV animation",
                image_url=IMG["ren"],
                notes="The later seasons without Kricfalusi are generally considered inferior "
                      "but the show remained popular throughout."),
        ],
        wiki_slug="The_Ren_%26_Stimpy_Show",
    )
    lib.add_cartoon(ren_stimpy)

    # ── Invader Zim (2001) ──────────────────────────────────────────────
    invader_zim = _nick(
        name="Invader Zim",
        description=(
            "Zim — a megalomaniacal alien Invader from planet Irk — is banished "
            "to conquer Earth as punishment, aided by his defective robot GIR. "
            "Only Dib — a paranormal investigator — sees through Zim's human disguise. "
            "Created by Jhonen Vasquez, Invader Zim was Nickelodeon's darkest and "
            "most gothic series — cancelled after one season but became one of the "
            "greatest cult animated series of all time on DVD and cable."
        ),
        character_type="Alien — failed invader / dark gothic comedy",
        debut_year=2001,
        creators=[Creator("Jhonen Vasquez", "Series creator — Johnny the Homicidal Maniac comic creator", 1974)],
        series_list=[
            Series("Invader Zim", 2001, 2002,
                   "Nickelodeon Animation Studio", "TV series", episode_count=27,
                   notes="Cancelled after one season. Massive cult following on DVD."),
            Series("Invader Zim Enter the Florpus Netflix film", 2019, 2019,
                   "Nickelodeon / Netflix", "streaming feature",
                   notes="Long-awaited Netflix revival. Original cast returned."),
        ],
        eras=[
            Era(2001, None,
                "Gothic alien-invasion comedy — angular dark visual style, "
                "GIR's chaotic energy, Dib's doomed crusade for truth",
                art_style="Angular dark digital animation",
                image_url=IMG["invader"],
                notes="Debuted March 30 2001. Too dark and too expensive for Nick's demographic. "
                      "Became enormously popular after cancellation. "
                      "Enter the Florpus (2019) was a triumphant return."),
        ],
        wiki_slug="Invader_Zim",
    )
    lib.add_cartoon(invader_zim)

    # ── The Fairly OddParents (2001) ────────────────────────────────────
    fairly_odd = _nick(
        name="The Fairly OddParents",
        description=(
            "Timmy Turner — a miserable 10-year-old with neglectful parents and a "
            "sadistic babysitter Vicky — is granted fairy godparents Cosmo and Wanda "
            "who grant his wishes, usually with chaotic unintended consequences. "
            "Created by Butch Hartman, The Fairly OddParents became Nickelodeon's "
            "second-longest-running animated series. Poof the fairy baby was added "
            "in Season 6, and Sparky the dog in Season 9 — both controversial additions."
        ),
        character_type="Human / fairy — wish-granting family comedy",
        debut_year=2001,
        creators=[Creator("Butch Hartman", "Series creator — also created Danny Phantom", 1968)],
        series_list=[
            Series("The Fairly OddParents", 2001, 2017,
                   "Nickelodeon Animation Studio", "TV series", episode_count=172,
                   notes="Debuted March 30 2001. 10 seasons over 16 years."),
            Series("Fairly OddParents live-action TV movies", 2011, 2014,
                   "Nickelodeon", "TV movies", episode_count=3),
            Series("The Fairly OddParents Fairly Odder reboot", 2022, 2023,
                   "Nickelodeon / Paramount+", "streaming series"),
        ],
        eras=[
            Era(2001, 2017,
                "Original animated series — Timmy in pink hat, Cosmo and Wanda as his fish, "
                "Jorgen Von Strangle, Anti-Fairies, Mr. Crocker",
                art_style="Flat color digital animation",
                image_url=IMG["fairly"],
                notes="The series ran 10 seasons over 16 years making it Nickelodeon's "
                      "second longest-running animated series after SpongeBob."),
            Era(2022, None,
                "Live-action/CGI hybrid reboot on Paramount+",
                art_style="Live-action with CGI fairies",
                image_url=IMG["fairly"],
                notes="The 2022 reboot featured live-action with animated fairies. Mixed reception."),
        ],
        wiki_slug="The_Fairly_OddParents",
    )
    lib.add_cartoon(fairly_odd)

    # ── Danny Phantom (2004) ────────────────────────────────────────────
    danny = _nick(
        name="Danny Phantom",
        description=(
            "Danny Fenton — a 14-year-old whose ghost-hunting parents accidentally "
            "activated a ghost portal in their basement, turning Danny half-human "
            "half-ghost. As Danny Phantom he protects Amity Park with powers of "
            "invisibility, intangibility, and ghost rays. Created by Butch Hartman, "
            "Danny Phantom developed a devoted cult following and remains one of the "
            "most-requested Nickelodeon revivals."
        ),
        character_type="Human / ghost — teenage superhero",
        debut_year=2004,
        creators=[Creator("Butch Hartman", "Series creator", 1968)],
        series_list=[
            Series("Danny Phantom", 2004, 2007,
                   "Nickelodeon Animation Studio", "TV series", episode_count=53,
                   notes="Debuted April 3 2004."),
        ],
        eras=[
            Era(2004, 2007,
                "Original series — white hair and green eyes in ghost form, "
                "black and white hazmat suit, Amity Park setting",
                art_style="Flat color digital animation",
                image_url=IMG["danny"],
                notes="Created alongside Fairly OddParents by Butch Hartman. "
                      "Ember McLain became a beloved villain and fan favorite. "
                      "Fans have campaigned for a revival for over 15 years."),
        ],
        wiki_slug="Danny_Phantom",
    )
    lib.add_cartoon(danny)

    # ── Avatar: The Last Airbender (2005) ───────────────────────────────
    avatar = _nick(
        name="Avatar: The Last Airbender",
        description=(
            "Aang — a 12-year-old Air Nomad and the Avatar who can master all four "
            "elements — must stop the Fire Nation's war before Sozin's Comet arrives. "
            "Joined by Katara, Sokka, Toph, and eventually the redeemed Prince Zuko. "
            "Created by Michael DiMartino and Bryan Konietzko, Avatar is widely "
            "considered the greatest animated series ever made for children — praised "
            "for its world-building, character arcs, emotional depth, and "
            "Asian-influenced aesthetics. Three books: Water, Earth, Fire."
        ),
        character_type="Human — Avatar / elemental bender / last hope",
        debut_year=2005,
        creators=[
            Creator("Michael DiMartino", "Co-creator", 1974),
            Creator("Bryan Konietzko", "Co-creator", 1975),
        ],
        series_list=[
            Series("Avatar The Last Airbender", 2005, 2008,
                   "Nickelodeon Animation Studio", "TV series", episode_count=61,
                   notes="Three books. Debuted February 21 2005. "
                         "61 episodes of near-perfect storytelling."),
            Series("Avatar The Last Airbender live-action film", 2010, 2010,
                   "Paramount Pictures", "theatrical feature",
                   notes="M. Night Shyamalan's widely criticized live-action adaptation."),
            Series("Avatar The Last Airbender Netflix live-action", 2024, None,
                   "Netflix / Nickelodeon", "streaming series",
                   notes="Netflix live-action remake. Original creators left due to creative differences."),
        ],
        eras=[
            Era(2005, 2008,
                "Original animated series — anime-influenced hand-drawn style, "
                "Asian aesthetic, extraordinary emotional complexity",
                art_style="Anime-influenced American animation",
                image_url=IMG["avatar"],
                notes="Frequently cited as the greatest animated series ever made for children. "
                      "Won multiple Annie and Emmy Awards. "
                      "Its exploration of war, trauma, and redemption set a new standard."),
            Era(2024, None,
                "Netflix live-action era — DiMartino and Konietzko departed the project",
                art_style="Live-action",
                image_url=IMG["avatar"],
                notes="The Netflix adaptation received more positive reception than the 2010 film "
                      "but disappointed many fans of the original animated series."),
        ],
        wiki_slug="Avatar:_The_Last_Airbender",
    )
    lib.add_cartoon(avatar)

    # ── The Legend of Korra (2012) ──────────────────────────────────────
    korra = _nick(
        name="The Legend of Korra",
        description=(
            "Korra — the next Avatar after Aang — a headstrong Water Tribe girl "
            "who must master airbending in the modern industrial world of Republic City. "
            "The sequel to Avatar explores political extremism, industrialization, "
            "anarchism, fascism, and identity through four antagonists each representing "
            "a different ideology. Korra's confirmed bisexuality in the finale made her "
            "one of the first LGBTQ+ protagonists in American children's animation."
        ),
        character_type="Human — Avatar / elemental bender / modern world hero",
        debut_year=2012,
        creators=[
            Creator("Michael DiMartino", "Co-creator", 1974),
            Creator("Bryan Konietzko", "Co-creator", 1975),
        ],
        series_list=[
            Series("The Legend of Korra", 2012, 2014,
                   "Nickelodeon Animation Studio / Studio Mir", "TV series", episode_count=52,
                   notes="Four books. Books 3-4 moved to digital after ratings issues."),
        ],
        eras=[
            Era(2012, 2014,
                "Modernized Avatar world — Republic City 1920s aesthetic, "
                "mature themes of extremism and identity, LGBTQ+ representation",
                art_style="Anime-influenced American animation",
                image_url=IMG["korra"],
                notes="Korra and Asami Sato's confirmed romance in the finale "
                      "was a landmark moment for LGBTQ+ representation in children's animation."),
        ],
        wiki_slug="The_Legend_of_Korra",
    )
    lib.add_cartoon(korra)

    # ── Doug (1991) ─────────────────────────────────────────────────────
    doug = _nick(
        name="Doug",
        description=(
            "Doug Funnie — an imaginative 11-year-old who moves to Bluffington "
            "and documents his life in his journal — including his crush on Patti "
            "Mayonnaise and adventures with his friend Skeeter Valentine. "
            "One of Nickelodeon's original three Nicktoons. Doug's vivid fantasy life "
            "where he imagines himself as various heroes (Quailman, Smash Adams) "
            "was a defining feature. Later controversially acquired and altered by Disney."
        ),
        character_type="Human — suburban journal-writing kid / daydreamer",
        debut_year=1991,
        creators=[Creator("Jim Jinkins", "Series creator", 1954)],
        series_list=[
            Series("Doug Nickelodeon original", 1991, 1994,
                   "Jumbo Pictures / Nickelodeon", "TV series", episode_count=52,
                   notes="One of the original three Nicktoons. Debuted August 11 1991."),
            Series("Brand Spanking New Doug Disney", 1996, 1999,
                   "Jumbo Pictures / ABC / Disney", "TV series",
                   notes="Disney acquired Doug and rebooted it. "
                         "Fans strongly prefer the Nickelodeon version."),
            Series("Doug's 1st Movie", 1999, 1999,
                   "Walt Disney Pictures", "theatrical feature"),
        ],
        eras=[
            Era(1991, 1994,
                "Nickelodeon original — muted color palette, relatable middle school life, "
                "Quailman fantasy alter ego",
                art_style="Flat color TV animation",
                image_url=IMG["doug"],
                notes="The muted color palette was intentional to feel realistic. "
                      "Jim Jinkins created Doug as a semi-autobiographical character."),
            Era(1996, None,
                "Disney era — brighter colors, older characters, altered tone",
                art_style="Updated digital animation",
                image_url=IMG["doug"],
                notes="The Disney acquisition significantly changed the show's tone and look. "
                      "Most fans consider the Nickelodeon version the definitive one."),
        ],
        wiki_slug="Doug_(TV_series)",
    )
    lib.add_cartoon(doug)

    # ── CatDog (1998) ────────────────────────────────────────────────────
    catdog = _nick(
        name="CatDog",
        description=(
            "Cat and Dog — two very different animals sharing one conjoined body "
            "with no explanation. Cat is refined and scheming; Dog is happy and "
            "food-obsessed. Their permanent physical attachment despite fundamental "
            "incompatibility is the source of all comedy. Created by Peter Hannan, "
            "CatDog was one of Nickelodeon's most visually distinctive Nicktoons "
            "and the TV movie finally answered the origin mystery."
        ),
        character_type="Anthropomorphic animals — conjoined cat and dog",
        debut_year=1998,
        creators=[Creator("Peter Hannan", "Series creator", 0)],
        series_list=[
            Series("CatDog", 1998, 2005,
                   "Nickelodeon Animation Studio", "TV series", episode_count=68,
                   notes="Debuted April 4 1998."),
            Series("CatDog And the Great Parent Mystery TV movie", 2001, 2001,
                   "Nickelodeon", "TV movie",
                   notes="Finally revealed CatDog's parents and origin story."),
        ],
        eras=[
            Era(1998, None,
                "Cat on left, Dog on right, no tail, no explanation, "
                "Nearburg setting, Greaser Dogs as antagonists",
                art_style="Flat color digital animation",
                image_url=IMG["catdog"],
                notes="The origin mystery of how CatDog came to be "
                      "was the show's longest-running question, answered in the 2001 movie."),
        ],
        wiki_slug="CatDog",
    )
    lib.add_cartoon(catdog)

    # ── The Loud House (2016) ────────────────────────────────────────────
    loud_house = _nick(
        name="The Loud House",
        description=(
            "Lincoln Loud — the only boy among 11 siblings — navigates life in the "
            "chaotic Loud household in the fictional town of Royal Woods, Michigan. "
            "Created by Chris Savino, The Loud House features one of the most diverse "
            "sibling casts in animation and was notable for prominently featuring "
            "an interracial gay couple (Clyde's dads Harold and Howard McBride) "
            "in recurring roles. The show spawned a spinoff, a Netflix CGI film, "
            "and a live-action Netflix adaptation."
        ),
        character_type="Human — boy with 10 sisters / family comedy",
        debut_year=2016,
        creators=[Creator("Chris Savino", "Series creator", 1971)],
        series_list=[
            Series("The Loud House", 2016, None,
                   "Nickelodeon Animation Studio", "TV series",
                   notes="Debuted May 20 2016. Ongoing."),
            Series("The Loud House Movie Netflix", 2021, 2021,
                   "Nickelodeon / Netflix", "streaming feature"),
            Series("The Really Loud House live-action", 2022, None,
                   "Nickelodeon / Paramount+", "live-action series"),
            Series("The Casagrandes spinoff", 2019, 2022,
                   "Nickelodeon", "TV series"),
        ],
        eras=[
            Era(2016, None,
                "Original series — Lincoln in white hair and orange polo, "
                "11 sisters each with distinct personality, Royal Woods setting",
                art_style="Flat color digital animation",
                image_url=IMG["loud"],
                notes="The Loud House featured Clyde McBride's two dads — Harold and Howard — "
                      "as one of the earliest prominently featured gay couples in a Nick series. "
                      "The show won multiple Annie Awards."),
        ],
        wiki_slug="The_Loud_House",
    )
    lib.add_cartoon(loud_house)

    # ── Teenage Mutant Ninja Turtles Nick era (2012) ─────────────────────
    tmnt_nick = _nick(
        name="Teenage Mutant Ninja Turtles (Nickelodeon)",
        description=(
            "Leonardo, Donatello, Raphael, and Michelangelo — four mutant turtle "
            "brothers trained in ninjutsu by their rat sensei Splinter — battle "
            "the Shredder and Krang beneath New York City. "
            "Originally created by Kevin Eastman and Peter Laird as a black-and-white "
            "indie comic in 1984, TMNT became one of the largest franchises in history. "
            "Nickelodeon acquired the property in 2009 and produced a CGI animated "
            "series from 2012-2017, followed by the acclaimed Rise of the TMNT "
            "and Mutant Mayhem film."
        ),
        character_type="Anthropomorphic animals — mutant turtle ninja team",
        debut_year=2012,
        creators=[
            Creator("Kevin Eastman", "TMNT original co-creator (1984 comics)", 1962),
            Creator("Peter Laird", "TMNT original co-creator (1984 comics)", 1954),
        ],
        series_list=[
            Series("Teenage Mutant Ninja Turtles CGI series", 2012, 2017,
                   "Nickelodeon Animation Studio", "TV series", episode_count=124,
                   notes="Nickelodeon's CGI reboot. Debuted September 29 2012. "
                         "Mixed anime and Western action styles."),
            Series("Rise of the Teenage Mutant Ninja Turtles", 2018, 2020,
                   "Nickelodeon Animation Studio", "TV series", episode_count=40,
                   notes="Reimagined with new art style and Leo/Raph personality swap. "
                         "Polarizing but praised for visual creativity."),
            Series("Rise of the TMNT The Movie Netflix", 2022, 2022,
                   "Nickelodeon / Netflix", "streaming feature"),
            Series("TMNT Mutant Mayhem theatrical film", 2023, 2023,
                   "Paramount Pictures / Nickelodeon Movies", "theatrical feature",
                   notes="Critically acclaimed theatrical film with hand-drawn anime aesthetic. "
                         "Teenage voices cast from actual teenagers."),
        ],
        eras=[
            Era(2012, 2017,
                "Nickelodeon CGI series — 3D turtles with distinct head shapes, "
                "anime influence, darker storylines than 1987 series",
                art_style="CGI animation",
                image_url=IMG["ninja"],
                notes="Nickelodeon acquired TMNT from Mirage Studios for $60 million in 2009. "
                      "The CGI series was praised for its action sequences and character development."),
            Era(2018, 2022,
                "Rise of the TMNT — bold new 2D art style, "
                "Leo as red-eared slider leader instead of Raph",
                art_style="2D digital animation — bold graphic style",
                image_url=IMG["ninja"],
                notes="Rise was divisive initially but gained appreciation. "
                      "The Netflix film based on it was widely praised."),
            Era(2023, None,
                "Mutant Mayhem era — theatrical film with hand-drawn teen aesthetic, "
                "actual teenagers voicing the turtles",
                art_style="Hand-drawn anime-influenced theatrical animation",
                image_url=IMG["ninja"],
                notes="TMNT Mutant Mayhem (2023) was one of the most critically acclaimed "
                      "animated films of the year. The hand-drawn aesthetic and authentic "
                      "teenage voice performances were widely praised."),
        ],
        wiki_slug="Teenage_Mutant_Ninja_Turtles_(2012_TV_series)",
    )
    # Override — TMNT IP owned by Nickelodeon/Paramount not original creators
    tmnt_nick.ownership_history.clear()
    tmnt_nick.add_ownership_record(OwnershipRecord(
        "Mirage Studios / Kevin Eastman and Peter Laird", 1984, 2009,
        "original comic book creation"))
    tmnt_nick.add_ownership_record(OwnershipRecord(
        "Viacom / Nickelodeon", 2009, 2022,
        "Nickelodeon acquired TMNT from Mirage for $60 million"))
    tmnt_nick.add_ownership_record(OwnershipRecord(
        "Paramount Global / Nickelodeon", 2022, None,
        "ViacomCBS rebranded to Paramount Global",
        is_current_owner=True))
    lib.add_cartoon(tmnt_nick)

    print(f"Nickelodeon characters added. Library now has {len(lib.cartoons)} cartoons total.")
