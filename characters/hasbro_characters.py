"""
hasbro_characters.py
Hasbro animated characters for CartoonPal.

Hasbro Inc. is an American toy and entertainment company founded in 1923.
In the 1980s Hasbro partnered with Marvel Productions and Sunbow Entertainment
to produce animated series based on their toy lines — creating some of the
most beloved cartoons of the decade.

Key productions:
- Transformers G1 (1984) — Sunbow / Marvel Productions
- G.I. Joe: A Real American Hero (1983) — Sunbow / Marvel Productions
- My Little Pony (1984) — Sunbow / Marvel Productions
- Jem and the Holograms (1985) — already in dic_characters.py

All character IP owned by Hasbro Inc. throughout.
Hasbro acquired Wizards of the Coast (1999) and various other properties.
eOne Entertainment acquired by Hasbro (2019).

Usage:
    from characters.hasbro_characters import add_hasbro_characters
    add_hasbro_characters(lib)
"""

from cartoon_system import (
    Cartoon, Creator, ProductionCompany,
    Series, OwnershipRecord, Era, Library
)

HASBRO_STUDIO = ProductionCompany("Hasbro / Sunbow Productions", 1968, country="USA", still_active=True)
SUNBOW = ProductionCompany("Sunbow Entertainment / Marvel Productions", 1980, country="USA", still_active=False)

HASBRO_OWN = [
    ("Hasbro Inc.", 1923, None,
     "original toy property — Hasbro retains all character IP worldwide"),
]

IMG = {
    "optimus":   "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Optimus_Prime_G1.png/200px-Optimus_Prime_G1.png",
    "tf":        "https://upload.wikimedia.org/wikipedia/en/thumb/2/2c/Transformers_G1_logo.png/240px-Transformers_G1_logo.png",
    "gijoe":     "https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/GI_Joe_Real_American_Hero_logo.png/240px-GI_Joe_Real_American_Hero_logo.png",
    "mlp":       "https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/My_Little_Pony_logo.png/240px-My_Little_Pony_logo.png",
    "mlp_fim":   "https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/My_Little_Pony_Friendship_is_Magic_logo.png/240px-My_Little_Pony_Friendship_is_Magic_logo.png",
    "hasbro":    "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Hasbro_logo.svg/240px-Hasbro_logo.svg.png",
    "megatron":  "https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/Megatron_G1.png/200px-Megatron_G1.png",
    "bumblebee": "https://upload.wikimedia.org/wikipedia/en/thumb/4/4e/Bumblebee_G1.png/200px-Bumblebee_G1.png",
}


def _hasbro(name, description, character_type, debut_year,
            extra_creators, series_list, eras, wiki_slug,
            origin="Pawtucket, Rhode Island, USA — Hasbro Inc."):
    c = Cartoon(name=name, description=description,
                character_type=character_type,
                country_of_origin="USA", debut_year=debut_year)
    c.original_studio = HASBRO_STUDIO
    for cr in extra_creators:
        c.add_creator(cr)
    for s in series_list:
        c.add_series(s)
    # Hasbro always owned the IP — only the animation producer changed
    c.add_ownership_record(OwnershipRecord(
        "Hasbro Inc.", 1923, None,
        "original toy property — Hasbro retains all character IP worldwide",
        is_current_owner=True,
        notes="Animation was produced by Sunbow/Marvel Productions under license. "
              "Hasbro owned all character rights throughout every production era."))
    for era in eras:
        c.add_era(era)
    c.wiki_url = f"https://en.wikipedia.org/wiki/{wiki_slug}"
    c.origin_location = origin
    return c


def add_hasbro_characters(lib: Library):

    # ══════════════════════════════════════════════════════════════════════
    # TRANSFORMERS (1984)
    # ══════════════════════════════════════════════════════════════════════

    # Optimus Prime
    optimus = _hasbro(
        name="Optimus Prime",
        description=(
            "The noble, selfless leader of the Autobots — a faction of sentient "
            "robots from the planet Cybertron who can transform into vehicles. "
            "Optimus Prime transforms into a red semi-truck and leads the Autobots "
            "against the evil Decepticons led by Megatron. His famous declaration "
            "Autobots, roll out! and his deep, authoritative voice (Peter Cullen) "
            "made him one of the most iconic animated heroes of the 1980s. "
            "His death in Transformers: The Movie (1986) traumatized a generation "
            "of children. He remains the face of the entire Transformers franchise "
            "across all 40+ years of its history."
        ),
        character_type="Transformer — Autobot leader / semi-truck",
        debut_year=1984,
        extra_creators=[
            Creator("Bob Budiansky", "Marvel Comics writer who named and characterized the Transformers", 1954),
            Creator("Peter Cullen", "Voice of Optimus Prime — original and all revivals", 1941),
        ],
        series_list=[
            Series("The Transformers Generation 1", 1984, 1987,
                   "Sunbow Productions / Marvel Productions", "TV series", episode_count=98,
                   notes="PRODUCED BY: Sunbow/Marvel under Hasbro license. "
                         "The original and most beloved animated Transformers series. "
                         "Debuted September 17 1984."),
            Series("Transformers The Movie", 1986, 1986,
                   "Sunbow Productions / DEG", "theatrical feature",
                   notes="Optimus Prime dies in this film — one of the most shocking "
                         "moments in children's animation history. "
                         "The fan outcry was so intense Hasbro reversed course."),
            Series("Transformers Generation 2", 1992, 1995,
                   "Hasbro / Claster Television", "TV series",
                   notes="Repackaged G1 episodes with new CGI segments."),
            Series("Transformers Beast Wars", 1996, 1999,
                   "Mainframe Entertainment / Hasbro", "TV series", episode_count=52,
                   notes="CGI sequel set in prehistoric times. "
                         "Featured Optimus Primal — a descendant of Optimus Prime."),
            Series("Transformers Armada / Energon / Cybertron trilogy", 2002, 2006,
                   "Hasbro / Takara / TV Tokyo", "TV anime series"),
            Series("Transformers Animated", 2007, 2009,
                   "Cartoon Network Studios / Hasbro", "TV series", episode_count=42,
                   notes="Praised for its character-driven storytelling and distinctive art style."),
            Series("Transformers Prime", 2010, 2013,
                   "Hasbro Studios / Hub Network", "TV series", episode_count=65,
                   notes="Peter Cullen returned as Optimus Prime. Won multiple Emmy Awards."),
            Series("Transformers live-action film series", 2007, 2023,
                   "Paramount Pictures / Hasbro", "theatrical features",
                   notes="Michael Bay's live-action films (2007-2017) were commercially "
                         "huge despite critical divisiveness. Peter Cullen voiced Optimus in all."),
            Series("Transformers EarthSpark", 2022, None,
                   "Hasbro / Paramount+", "streaming series"),
        ],
        eras=[
            Era(1984, 1987,
                "Generation 1 — classic flat cel animation, Cybertronian mythology established, "
                "Peter Cullen's iconic voice, Sunbow/Marvel production",
                art_style="Traditional cel animation — Toei Animation produced in Japan",
                image_url=IMG["optimus"],
                notes="The G1 animated series was produced by Sunbow/Marvel with animation "
                      "outsourced to Toei Animation in Japan. "
                      "Peter Cullen defined Optimus Prime's voice for 40 years. "
                      "The 1986 theatrical film killed Optimus to sell new toys — "
                      "the resulting fan outrage became animation legend."),
            Era(1996, 2006,
                "Beast Wars and Unicron Trilogy — CGI era, new Optimus iterations, "
                "expanded Transformers mythology",
                art_style="Early CGI animation",
                image_url=IMG["tf"],
                notes="Beast Wars (1996) is often cited as the best post-G1 Transformers series. "
                      "The Unicron Trilogy was produced with Japanese anime studio Takara."),
            Era(2007, 2016,
                "Michael Bay live-action film era — redesigned CGI robots, "
                "Peter Cullen returning as Optimus, blockbuster commercial success",
                art_style="Live-action / CGI hybrid",
                image_url=IMG["tf"],
                notes="The Bay films were divisive but made Transformers one of the "
                      "highest-grossing film franchises of the 2000s-2010s. "
                      "Optimus's darker characterization in the later films was controversial."),
            Era(2010, None,
                "Transformers Prime and modern era — Peter Cullen back, "
                "Emmy-winning storytelling, streaming continuations",
                art_style="CGI animation / streaming",
                image_url=IMG["optimus"],
                notes="Transformers Prime (2010) is widely considered the best modern "
                      "Transformers animated series. Peter Cullen's return anchored the show."),
        ],
        wiki_slug="Optimus_Prime",
    )
    lib.add_cartoon(optimus)

    # Megatron / Galvatron
    megatron = _hasbro(
        name="Megatron",
        description=(
            "The ruthless, power-hungry leader of the Decepticons — Optimus Prime's "
            "eternal nemesis. Megatron transforms into a Walther P38 pistol (in G1) "
            "and seeks to conquer Cybertron and then the universe. "
            "Frank Welker's original G1 voice performance is one of animation's "
            "most recognizable villain voices. After being defeated in Transformers: "
            "The Movie (1986) he was reformatted into Galvatron. Megatron has been "
            "reinvented in every Transformers continuity as the primary antagonist."
        ),
        character_type="Transformer — Decepticon leader / villain",
        debut_year=1984,
        extra_creators=[
            Creator("Frank Welker", "Original voice of Megatron (G1) and later Optimus Prime", 1946),
        ],
        series_list=[
            Series("The Transformers Generation 1 (as Megatron)", 1984, 1986,
                   "Sunbow Productions / Marvel Productions", "TV series"),
            Series("Transformers The Movie (reformatted to Galvatron)", 1986, 1986,
                   "Sunbow Productions", "theatrical feature",
                   notes="Megatron is defeated and reformatted into Galvatron by Unicron."),
            Series("The Transformers Season 3 (as Galvatron)", 1986, 1987,
                   "Sunbow Productions", "TV series"),
            Series("Transformers Prime (as Megatron)", 2010, 2013,
                   "Hasbro Studios", "TV series",
                   notes="Frank Welker voiced Megatron in Transformers Prime."),
        ],
        eras=[
            Era(1984, 1986,
                "G1 Megatron — grey robot transforming into Walther P38 pistol, "
                "Frank Welker's chilling performance",
                art_style="Traditional cel animation",
                image_url=IMG["megatron"],
                notes="The concept of a Decepticon leader who transforms into a gun "
                      "that other Decepticons fire was uniquely absurd and beloved. "
                      "Frank Welker's voice defined Megatron for a generation."),
            Era(1986, None,
                "Galvatron and modern iterations — redesigned across every continuity, "
                "consistently the primary Transformers villain",
                art_style="Various — CGI, live-action, animation",
                image_url=IMG["tf"],
                notes="Hugo Weaving voiced Megatron in the Bay films. "
                      "Frank Welker reclaimed the role in later animated and film productions."),
        ],
        wiki_slug="Megatron",
    )
    lib.add_cartoon(megatron)

    # Bumblebee
    bumblebee = _hasbro(
        name="Bumblebee",
        description=(
            "The smallest and most beloved Autobot — a yellow Volkswagen Beetle "
            "(later Chevrolet Camaro) who serves as the human-friendly face of the "
            "Autobots. Bumblebee's friendly personality, small stature, and loyal "
            "friendship with human characters made him the character most appealing "
            "to younger audiences. He became the lead character of the critically "
            "acclaimed Bumblebee standalone film (2018) and the Bumblebee animated series."
        ),
        character_type="Transformer — Autobot scout / yellow car",
        debut_year=1984,
        extra_creators=[],
        series_list=[
            Series("The Transformers Generation 1", 1984, 1987,
                   "Sunbow Productions / Marvel Productions", "TV series"),
            Series("Bumblebee theatrical film", 2018, 2018,
                   "Paramount Pictures / Hasbro", "theatrical feature",
                   notes="Critically acclaimed standalone film. Hailee Steinfeld starred. "
                         "Widely considered the best live-action Transformers film."),
            Series("Transformers EarthSpark", 2022, None,
                   "Hasbro / Paramount+", "streaming series"),
        ],
        eras=[
            Era(1984, 2006,
                "G1 yellow VW Beetle — smallest Autobot, friendly and loyal",
                art_style="Traditional cel animation",
                image_url=IMG["bumblebee"],
                notes="In G1 Bumblebee transformed into a Volkswagen Beetle. "
                      "He was the most human-friendly Autobot and often partnered "
                      "with human characters."),
            Era(2007, None,
                "Camaro era and beyond — redesigned as Chevrolet Camaro for Bay films, "
                "became the franchise's breakout character",
                art_style="CGI / live-action / modern animation",
                image_url=IMG["bumblebee"],
                notes="The Bay films redesigned Bumblebee as a Camaro and made him "
                      "the primary human-allied Autobot. His communication through "
                      "radio clips (due to damaged voicebox) became iconic."),
        ],
        wiki_slug="Bumblebee_(Transformers)",
    )
    lib.add_cartoon(bumblebee)

    # Transformers G1 (as a franchise record)
    transformers_g1 = _hasbro(
        name="Transformers (Generation 1)",
        description=(
            "Robots in disguise — sentient mechanical beings from the planet Cybertron "
            "divided into heroic Autobots and evil Decepticons who continue their war "
            "on Earth while disguised as ordinary vehicles and machines. "
            "Based on Hasbro's toy line (itself based on Japanese Diaclone and "
            "Microman toys), Transformers G1 debuted in 1984 and became one of the "
            "defining cartoons of the decade. The Marvel Comics run by Bob Budiansky "
            "and later Simon Furman developed the mythology beyond the cartoon. "
            "The franchise has generated over $30 billion in revenue."
        ),
        character_type="Transformers — Autobot/Decepticon robot war ensemble",
        debut_year=1984,
        extra_creators=[
            Creator("Bob Budiansky", "Marvel Comics writer — named and characterized most G1 Transformers", 1954),
            Creator("Simon Furman", "Marvel UK/US writer — expanded Transformers mythology", 1959),
        ],
        series_list=[
            Series("The Transformers G1", 1984, 1987,
                   "Sunbow Productions / Marvel Productions / Hasbro", "TV series", episode_count=98,
                   notes="PRODUCED BY: Sunbow/Marvel Productions under Hasbro license. "
                         "Animation outsourced to Toei Animation (Japan) and AKOM (Korea). "
                         "Debuted September 17 1984 as a 3-part mini-series."),
            Series("Transformers The Movie", 1986, 1986,
                   "Sunbow Productions / DEG", "theatrical feature",
                   notes="Killed major characters to introduce new toys. "
                         "The death of Optimus Prime traumatized a generation."),
        ],
        eras=[
            Era(1984, 1987,
                "G1 animated series — flat cel animation produced in Japan, "
                "established all core characters and mythology",
                art_style="Traditional cel animation — Toei and AKOM",
                image_url=IMG["tf"],
                notes="The G1 series was produced quickly and cheaply but created "
                      "one of the most enduring fictional universes in toy/animation history. "
                      "Many episodes were animation outsourcing with notable errors."),
        ],
        wiki_slug="The_Transformers_(TV_series)",
    )
    lib.add_cartoon(transformers_g1)

    # ══════════════════════════════════════════════════════════════════════
    # G.I. JOE: A REAL AMERICAN HERO (1983)
    # ══════════════════════════════════════════════════════════════════════

    gi_joe = _hasbro(
        name="G.I. Joe: A Real American Hero",
        description=(
            "An elite special operations military unit code-named G.I. Joe battles "
            "the terrorist organization Cobra for global domination. The team includes "
            "Duke, Snake Eyes, Scarlett, Roadblock, Lady Jaye, Flint, and dozens more. "
            "Cobra is led by the enigmatic Cobra Commander and includes Destro, "
            "the Baroness, Storm Shadow, and Zartan. "
            "Originally a 1964 Hasbro toy, relaunched in 1982 as 3.75-inch figures "
            "with the Real American Hero branding. The animated series produced by "
            "Sunbow/Marvel introduced the now-famous PSA public service announcements "
            "ending each episode — the source of the Knowing is Half the Battle meme. "
            "And knowing is half the battle. G.I. Joe!"
        ),
        character_type="Human — military special operations ensemble vs. terrorist organization",
        debut_year=1983,
        extra_creators=[
            Creator("Larry Hama", "Marvel Comics writer — defined the G.I. Joe mythology", 1949),
        ],
        series_list=[
            Series("G.I. Joe A Real American Hero mini-series", 1983, 1983,
                   "Sunbow Productions / Marvel Productions / Hasbro", "TV mini-series", episode_count=5,
                   notes="PRODUCED BY: Sunbow/Marvel under Hasbro license. "
                         "The Mass Device 5-part debut mini-series."),
            Series("G.I. Joe A Real American Hero animated series", 1985, 1986,
                   "Sunbow Productions / Marvel Productions / Hasbro", "TV series", episode_count=95,
                   notes="Full series run. Featured PSA public service announcements — "
                         "source of the Knowing is Half the Battle meme."),
            Series("G.I. Joe The Movie", 1987, 1987,
                   "Sunbow Productions / DEG", "theatrical feature",
                   notes="Originally intended for theatrical release but went direct to video. "
                         "Duke was meant to die (mirroring Optimus Prime) but survived "
                         "after Hasbro reversed course following the Transformers backlash."),
            Series("G.I. Joe DiC animated series", 1989, 1992,
                   "DiC Entertainment / Claster Television", "TV series", episode_count=44,
                   notes="PRODUCED BY: DIC Entertainment after Sunbow era ended."),
            Series("G.I. Joe Renegades", 2010, 2011,
                   "Hasbro Studios / Hub Network", "TV series", episode_count=26),
            Series("G.I. Joe live-action films", 2009, 2021,
                   "Paramount Pictures / Hasbro", "theatrical features",
                   notes="The Rise of Cobra (2009), Retaliation (2013), and Snake Eyes (2021)."),
        ],
        eras=[
            Era(1983, 1988,
                "Sunbow/Marvel golden era — iconic character roster established, "
                "PSA public service announcements, Cobra Commander's schemes",
                art_style="Traditional cel animation — Toei and AKOM",
                image_url=IMG["gijoe"],
                notes="The Sunbow G.I. Joe is the definitive version. "
                      "Larry Hama's concurrent Marvel Comics run gave deep characterization "
                      "that the cartoon often drew from. "
                      "Snake Eyes became the most popular character despite never speaking."),
            Era(1989, 2006,
                "DiC era and hiatus — different tone, less popular with fans",
                art_style="DiC Entertainment TV animation",
                image_url=IMG["gijoe"],
                notes="The DiC era is generally considered inferior to the Sunbow era. "
                      "The franchise was dormant for much of the 1990s."),
            Era(2007, None,
                "Modern era — live-action films, Hub Network animated series, "
                "Snake Eyes standalone film",
                art_style="Live-action CGI / modern animation",
                image_url=IMG["gijoe"],
                notes="The live-action films were commercially successful but critically mixed. "
                      "Snake Eyes (2021) was a standalone origin film for the fan-favorite character."),
        ],
        wiki_slug="G.I._Joe:_A_Real_American_Hero_(TV_series)",
    )
    lib.add_cartoon(gi_joe)

    # Snake Eyes (deserves his own entry)
    snake_eyes = _hasbro(
        name="Snake Eyes (G.I. Joe)",
        description=(
            "G.I. Joe's most popular and mysterious member — a ninja commando "
            "who never speaks, always wears a black uniform and visor, and whose "
            "face and identity are classified. Snake Eyes is a master of every "
            "martial art and the wielder of a katana alongside modern weapons. "
            "His rivalry and complicated brotherhood with Storm Shadow (a Cobra ninja) "
            "is the most beloved relationship in G.I. Joe mythology. "
            "Despite never speaking a single line of dialogue, he consistently "
            "ranked as the #1 G.I. Joe character in every poll."
        ),
        character_type="Human — silent ninja commando / G.I. Joe fan favorite",
        debut_year=1982,
        extra_creators=[Creator("Larry Hama", "Created Snake Eyes' mythology in Marvel Comics", 1949)],
        series_list=[
            Series("G.I. Joe A Real American Hero animated series", 1983, 1986,
                   "Sunbow Productions / Marvel Productions", "TV series"),
            Series("Snake Eyes G.I. Joe Origins film", 2021, 2021,
                   "Paramount Pictures / Hasbro", "theatrical feature",
                   notes="Standalone origin film starring Henry Golding. Mixed reception."),
        ],
        eras=[
            Era(1982, None,
                "Black uniform, visor, no dialogue, katana and modern weapons, "
                "complicated brotherhood with Storm Shadow",
                art_style="Various across all Transformers eras",
                image_url=IMG["gijoe"],
                notes="Snake Eyes never speaks in any animated version. "
                      "His silence is part of his mystique. "
                      "Larry Hama developed his backstory extensively in the Marvel Comics. "
                      "He has consistently been the most popular G.I. Joe character."),
        ],
        wiki_slug="Snake_Eyes_(G.I._Joe)",
    )
    lib.add_cartoon(snake_eyes)

    # ══════════════════════════════════════════════════════════════════════
    # MY LITTLE PONY (1982 / G1 animated 1984)
    # ══════════════════════════════════════════════════════════════════════

    mlp_g1 = _hasbro(
        name="My Little Pony (Generation 1)",
        description=(
            "Colorful magical ponies living in Dream Valley — led by Twilight, "
            "Firefly, Applejack, and others — who battle villains including Tirek, "
            "Catrina, and the Smooze. The original My Little Pony toy line debuted "
            "in 1982 and the animated TV special and series followed in 1984. "
            "The G1 animated content was notably darker than the toy line suggested — "
            "Rescue from Midnight Castle featured genuine horror imagery. "
            "The franchise is one of Hasbro's most valuable properties."
        ),
        character_type="Fantasy animals — magical ponies / adventure ensemble",
        debut_year=1984,
        extra_creators=[],
        series_list=[
            Series("My Little Pony G1 TV special Rescue from Midnight Castle", 1984, 1984,
                   "Sunbow Productions / Marvel Productions / Hasbro", "TV special",
                   notes="PRODUCED BY: Sunbow/Marvel. First animated MLP content. "
                         "Notably dark — featured Tirek transforming ponies into dragons."),
            Series("My Little Pony G1 animated series", 1986, 1987,
                   "Sunbow Productions / Marvel Productions / Hasbro", "TV series", episode_count=65),
            Series("My Little Pony The Movie G1", 1986, 1986,
                   "DEG / Hasbro", "theatrical feature",
                   notes="Theatrical film featuring the Smooze and Flutter Ponies."),
            Series("My Little Pony Tales G2", 1992, 1992,
                   "Sunbow Productions / Claster Television", "TV series", episode_count=26),
            Series("My Little Pony Friendship is Magic G4", 2010, 2019,
                   "DHX Media / Hasbro Studios / Hub Network", "TV series", episode_count=221,
                   notes="Created by Lauren Faust. Sparked the Brony fandom phenomenon. "
                         "Widely considered the greatest MLP series."),
            Series("My Little Pony A New Generation film G5", 2021, 2021,
                   "Netflix / Hasbro / eOne", "streaming feature"),
        ],
        eras=[
            Era(1984, 1992,
                "G1 Sunbow era — brightly colored ponies, Dream Valley, "
                "surprisingly dark threats, Rescue from Midnight Castle",
                art_style="Traditional cel animation — Toei and AKOM",
                image_url=IMG["mlp"],
                notes="The G1 specials and series were produced by Sunbow/Marvel. "
                      "Rescue from Midnight Castle (1984) was genuinely frightening "
                      "for a children's toy property. "
                      "Firefly was the fan-favorite G1 pony."),
            Era(2010, 2019,
                "G4 Friendship is Magic era — Lauren Faust's reimagining, "
                "Twilight Sparkle and the Mane Six, Brony fandom, Emmy Awards",
                art_style="Flash-based digital animation",
                image_url=IMG["mlp_fim"],
                notes="Lauren Faust's Friendship is Magic (2010) transformed My Little Pony "
                      "into a cultural phenomenon. The Brony fandom — adult male MLP fans — "
                      "became a widely discussed internet subculture. "
                      "The show won multiple Daytime Emmy Awards."),
            Era(2021, None,
                "G5 era — 3D CGI, new ponies, Netflix streaming",
                art_style="CGI animation",
                image_url=IMG["mlp"],
                notes="Generation 5 introduced new pony characters in a CGI world. "
                      "The Netflix film and subsequent series continue the franchise."),
        ],
        wiki_slug="My_Little_Pony_(Generation_1)",
    )
    lib.add_cartoon(mlp_g1)

    # Twilight Sparkle (G4 — most important MLP character)
    twilight = _hasbro(
        name="Twilight Sparkle",
        description=(
            "A studious, bookish unicorn (later alicorn princess) who is Princess "
            "Celestia's personal student and the leader of the Mane Six in Ponyville. "
            "Twilight's journey from solitary scholar to valued friend is the central "
            "arc of My Little Pony: Friendship is Magic. She represents the Element "
            "of Magic and becomes Princess of Friendship by the series' end. "
            "Created by Lauren Faust, Twilight Sparkle is the most beloved character "
            "of the G4 era and one of Hasbro's most recognizable characters globally."
        ),
        character_type="Fantasy animal — unicorn/alicorn pony / scholar and princess",
        debut_year=2010,
        extra_creators=[Creator("Lauren Faust", "Friendship is Magic creator and showrunner", 1974)],
        series_list=[
            Series("My Little Pony Friendship is Magic", 2010, 2019,
                   "DHX Media / Hasbro Studios", "TV series", episode_count=221),
            Series("My Little Pony Equestria Girls film series", 2013, 2019,
                   "DHX Media / Hasbro Studios", "theatrical / direct-to-video features",
                   notes="Twilight as a human in the human world of Canterlot High."),
        ],
        eras=[
            Era(2010, 2019,
                "G4 FiM — purple unicorn with pink streak, studious personality, "
                "later gains wings becoming an alicorn princess",
                art_style="Flash-based digital animation",
                image_url=IMG["mlp_fim"],
                notes="Voiced by Tara Strong. Twilight Sparkle becoming an alicorn in Season 3 "
                      "was one of the most discussed moments in MLP fandom history. "
                      "Her growth from antisocial scholar to Princess of Friendship "
                      "is the show's central character arc."),
        ],
        wiki_slug="Twilight_Sparkle",
    )
    lib.add_cartoon(twilight)

    # Pinkie Pie
    pinkie_pie = _hasbro(
        name="Pinkie Pie",
        description=(
            "The most exuberantly joyful pony in Ponyville — a pink earth pony "
            "who loves throwing parties, making friends laugh, and breaking the "
            "fourth wall. Pinkie Pie represents the Element of Laughter and has "
            "a supernatural ability to predict events (Pinkie Sense) and appear "
            "anywhere instantaneously. Her Smile Song became one of Friendship "
            "is Magic's most popular musical moments. "
            "She is beloved for her unpredictable energy and genuine warmth."
        ),
        character_type="Fantasy animal — earth pony / party pony",
        debut_year=2010,
        extra_creators=[Creator("Lauren Faust", "Friendship is Magic creator", 1974)],
        series_list=[
            Series("My Little Pony Friendship is Magic", 2010, 2019,
                   "DHX Media / Hasbro Studios", "TV series"),
        ],
        eras=[
            Era(2010, None,
                "Pink poofy-maned earth pony, Ponyville party planner, "
                "fourth-wall breaking, Pinkie Sense supernatural awareness",
                art_style="Flash-based digital animation",
                image_url=IMG["mlp_fim"],
                notes="Voiced by Andrea Libman (also voices Fluttershy). "
                      "Pinkie Pie's fourth-wall breaks and meta-awareness made her "
                      "a particularly beloved character for older fans."),
        ],
        wiki_slug="Pinkie_Pie",
    )
    lib.add_cartoon(pinkie_pie)

    # Rainbow Dash (not the DIC one — the G4 version)
    rainbow_dash = _hasbro(
        name="Rainbow Dash",
        description=(
            "A cyan pegasus pony who is the fastest flyer in Equestria and dreams "
            "of joining the elite aerial team the Wonderbolts. Rainbow Dash is brash, "
            "confident, and fiercely loyal — representing the Element of Loyalty. "
            "Her signature move is the Sonic Rainboom — a supersonic flight that "
            "creates a rainbow shockwave. She is one of the most popular G4 ponies "
            "and a particular fan favorite for her tomboyish personality."
        ),
        character_type="Fantasy animal — pegasus pony / fastest flyer in Equestria",
        debut_year=2010,
        extra_creators=[Creator("Lauren Faust", "Friendship is Magic creator", 1974)],
        series_list=[
            Series("My Little Pony Friendship is Magic", 2010, 2019,
                   "DHX Media / Hasbro Studios", "TV series"),
        ],
        eras=[
            Era(2010, None,
                "Cyan pegasus with rainbow mane, athletic competitive personality, "
                "Sonic Rainboom signature move, Wonderbolts dream",
                art_style="Flash-based digital animation",
                image_url=IMG["mlp_fim"],
                notes="Voiced by Ashleigh Ball (also voices Applejack). "
                      "Rainbow Dash was created partly as a tribute to the G1 pony Firefly "
                      "whom Lauren Faust wanted to include but couldn't due to trademark issues."),
        ],
        wiki_slug="Rainbow_Dash",
    )
    lib.add_cartoon(rainbow_dash)

    print(f"Hasbro characters added. Library now has {len(lib.cartoons)} cartoons total.")
