"""
anime_characters.py
Adds all major Sailor Moon and Dragon Ball Z characters to the CartoonPal library.
Both franchises originated in Japan and were adapted for international audiences.

Usage:
    from anime_characters import add_anime_characters
    lib = build_library()
    add_anime_characters(lib)
"""

from cartoon_system import (
    Cartoon, Creator, ProductionCompany,
    Series, OwnershipRecord, Era, Library
)

TOEI = ProductionCompany("Toei Animation", 1948, country="Japan")
NAOKO = Creator("Naoko Takeuchi", "Sailor Moon manga creator", 1967)
AKIRA = Creator("Akira Toriyama", "Dragon Ball manga creator", 1955, 2024)


def _make_sailor(name, description, debut_year, alter_ego, planet, image_url, notes_orig, notes_modern):
    c = Cartoon(
        name=name,
        description=description,
        character_type="Human / Magical girl — Sailor Senshi",
        country_of_origin="Japan",
        debut_year=debut_year,
    )
    c.original_studio = TOEI
    c.add_creator(NAOKO)
    c.add_series(Series("Bishoujo Senshi Sailor Moon (Japan)", 1992, 1997,
        "Toei Animation / TV Asahi", "TV anime", episode_count=200))
    c.add_series(Series("Sailor Moon DiC English dub (US)", 1995, 2000,
        "DiC Entertainment / Cloverway", "TV anime dub",
        notes="Heavily edited US version; names and some storylines changed."))
    c.add_series(Series("Sailor Moon Crystal", 2014, 2016,
        "Toei Animation", "streaming anime reboot", episode_count=39))
    c.add_series(Series("Sailor Moon Cosmos films", 2023, 2023,
        "Toei Animation", "theatrical feature"))
    c.add_ownership_record(OwnershipRecord(
        "Naoko Takeuchi / Kodansha (manga)", 1991, None, "original creation",
        notes="Takeuchi retains manga rights; Toei holds animation rights under license"))
    c.add_ownership_record(OwnershipRecord(
        "Toei Animation (anime rights)", 1992, None,
        "animation production license", is_current_owner=True))
    c.add_era(Era(1992, 1997,
        f"Original 90s anime — classic hand-drawn cel, pastel palette, {alter_ego} design",
        art_style="Japanese cel animation",
        image_url=image_url,
        notes=notes_orig))
    c.add_era(Era(2014, None,
        "Crystal / Cosmos era — refined digital animation, closer to manga art style",
        art_style="Digital anime",
        image_url=image_url,
        notes=notes_modern))
    c.wiki_url = f"https://en.wikipedia.org/wiki/{name.replace(' ', '_')}"
    c.origin_location = "Tokyo, Japan — Toei Animation studio, Nerima ward"
    return c


def _make_dbz(name, description, debut_year, role, image_url, notes_orig, notes_modern):
    c = Cartoon(
        name=name,
        description=description,
        character_type=f"Anime — {role}",
        country_of_origin="Japan",
        debut_year=debut_year,
    )
    c.original_studio = TOEI
    c.add_creator(AKIRA)
    c.add_series(Series("Dragon Ball (original series)", 1986, 1989,
        "Toei Animation / Fuji TV", "TV anime", episode_count=153,
        notes="Original series before Z; follows young Goku."))
    c.add_series(Series("Dragon Ball Z", 1989, 1996,
        "Toei Animation / Fuji TV", "TV anime", episode_count=291))
    c.add_series(Series("Dragon Ball Z Kai", 2009, 2015,
        "Toei Animation / Fuji TV", "TV anime remaster", episode_count=167,
        notes="Remastered HD version with tighter pacing and new voice recordings."))
    c.add_series(Series("Dragon Ball Super", 2015, 2018,
        "Toei Animation / Fuji TV", "TV anime", episode_count=131))
    c.add_series(Series("Dragon Ball GT", 1996, 1997,
        "Toei Animation / Fuji TV", "TV anime", episode_count=64,
        notes="Non-canonical sequel not based on Toriyama's manga."))
    c.add_series(Series("Dragon Ball Super Broly film", 2018, 2018,
        "Toei Animation", "theatrical feature"))
    c.add_series(Series("Dragon Ball Super Super Hero film", 2022, 2022,
        "Toei Animation", "theatrical feature"))
    c.add_ownership_record(OwnershipRecord(
        "Akira Toriyama / Shueisha (manga)", 1984, None, "original creation",
        notes="Toriyama created the manga; Shueisha publishes; Toei licenses animation rights"))
    c.add_ownership_record(OwnershipRecord(
        "Toei Animation (anime rights)", 1986, None,
        "animation production license", is_current_owner=True,
        notes="Bird Studio / Shueisha retain overall IP; Toei Animation produces anime under license"))
    c.add_era(Era(1989, 1996,
        "Original DBZ cel era — bold outlines, dramatic power-up animations, classic character designs",
        art_style="Japanese cel animation",
        image_url=image_url,
        notes=notes_orig))
    c.add_era(Era(2009, 2018,
        "Kai / Super era — HD remaster then new animation; cleaner lines, updated color palette",
        art_style="HD digital anime",
        image_url=image_url,
        notes=notes_modern))
    c.add_era(Era(2018, None,
        "Modern CGI-enhanced era — Super Hero film used CGI; Super continues digital 2D",
        art_style="CGI / digital hybrid",
        image_url=image_url,
        notes="Dragon Ball Super: Super Hero (2022) used full CG animation. Mixed fan reception but praised visually."))
    c.wiki_url = f"https://en.wikipedia.org/wiki/{name.replace(' ', '_')}"
    c.origin_location = "Tokyo, Japan — Toei Animation studio, Nerima ward"
    return c


# ── SHARED IMAGE URLS ────────────────────────────────────────────────────────
SM_IMG  = "https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/Sailor_Moon_-_Logo.png/240px-Sailor_Moon_-_Logo.png"
DBZ_IMG = "https://upload.wikimedia.org/wikipedia/en/thumb/a/a7/Dragon_Ball_Z_Logo.png/240px-Dragon_Ball_Z_Logo.png"


def add_anime_characters(lib: Library):
    """Add all Sailor Moon and Dragon Ball Z characters to the library."""

    # ════════════════════════════════════════════════════════════════════════
    # SAILOR MOON CHARACTERS
    # ════════════════════════════════════════════════════════════════════════

    # 1. Sailor Moon / Usagi Tsukino
    sailor_moon = _make_sailor(
        name="Sailor Moon",
        description=(
            "The titular heroine and leader of the Sailor Senshi. Usagi Tsukino "
            "is a clumsy, crybaby 14-year-old schoolgirl who transforms into Sailor Moon, "
            "the Pretty Guardian of Love and Justice. She wields the Silver Crystal "
            "and is the reincarnation of Princess Serenity of the Moon Kingdom. "
            "Her ultimate form is Neo-Queen Serenity, ruler of Crystal Tokyo."
        ),
        debut_year=1992,
        alter_ego="Usagi Tsukino / Bunny in English dub",
        planet="Moon",
        image_url=SM_IMG,
        notes_orig="Debuted March 7 1992 on TV Asahi. Voiced by Kotono Mitsuishi in Japanese. DiC dub voiced by Tracey Moore then Linda Ballantyne.",
        notes_modern="Crystal redesign closely follows Takeuchi's manga art. Kotono Mitsuishi returned for all modern productions.",
    )
    lib.add_cartoon(sailor_moon)

    # 2. Sailor Mercury / Ami Mizuno
    sailor_mercury = _make_sailor(
        name="Sailor Mercury",
        description=(
            "Ami Mizuno is the smartest girl in Japan with an IQ of 300 who "
            "transforms into Sailor Mercury, guardian of water and wisdom. "
            "Shy and studious, she serves as the team's strategist and analyst "
            "using her Mercury computer and visor to assess enemies. Her attacks "
            "include Shine Aqua Illusion and Mercury Aqua Rhapsody."
        ),
        debut_year=1992,
        alter_ego="Ami Mizuno / Amy Anderson in English dub",
        planet="Mercury",
        image_url=SM_IMG,
        notes_orig="Second Sailor Senshi to be introduced. Voiced by Aya Hisakawa in Japanese. Known for her blue hair and gentle personality.",
        notes_modern="Crystal version more closely matches Takeuchi's slender manga design. Remained popular as a fan favorite across all eras.",
    )
    lib.add_cartoon(sailor_mercury)

    # 3. Sailor Mars / Rei Hino
    sailor_mars = _make_sailor(
        name="Sailor Mars",
        description=(
            "Rei Hino is a Shinto shrine maiden and miko with psychic abilities "
            "who transforms into Sailor Mars, guardian of fire and passion. "
            "Fiery and strong-willed, she frequently clashes with Usagi but is "
            "deeply loyal. Her attacks include Fire Soul and Burning Mandala. "
            "She works at the Hikawa Shrine in Sendai Hill, Tokyo."
        ),
        debut_year=1992,
        alter_ego="Rei Hino / Raye Hino in English dub",
        planet="Mars",
        image_url=SM_IMG,
        notes_orig="Third Sailor Senshi introduced. Voiced by Michie Tomizawa in Japanese. Her personality differs significantly between anime and manga.",
        notes_modern="Crystal's Rei is much closer to the manga — more serious and spiritual, less combative with Usagi than the 90s anime.",
    )
    lib.add_cartoon(sailor_mars)

    # 4. Sailor Jupiter / Makoto Kino
    sailor_jupiter = _make_sailor(
        name="Sailor Jupiter",
        description=(
            "Makoto Kino is a tall tomboyish girl known for her exceptional "
            "cooking and fighting skills who transforms into Sailor Jupiter, "
            "guardian of thunder and courage. She is the physically strongest "
            "of the inner Senshi. Her attacks include Supreme Thunder and "
            "Jupiter Oak Evolution. She dreams of running her own restaurant."
        ),
        debut_year=1992,
        alter_ego="Makoto Kino / Lita Kino in English dub",
        planet="Jupiter",
        image_url=SM_IMG,
        notes_orig="Fourth inner Senshi introduced. Voiced by Emi Shinohara in Japanese. Known for her ponytail and rose earrings.",
        notes_modern="One of the most popular Senshi with fans. Crystal retained her key personality traits and powerful attack animations.",
    )
    lib.add_cartoon(sailor_jupiter)

    # 5. Sailor Venus / Minako Aino
    sailor_venus = _make_sailor(
        name="Sailor Venus",
        description=(
            "Minako Aino is the leader of the inner Sailor Senshi and the "
            "first to awaken as a guardian, originally operating as Sailor V "
            "before joining the team. She is guardian of love and beauty with "
            "attacks including Crescent Beam and Venus Love and Beauty Shock. "
            "She aspires to be an idol singer and is the most experienced fighter."
        ),
        debut_year=1991,
        alter_ego="Minako Aino / Mina Aino in English dub",
        planet="Venus",
        image_url=SM_IMG,
        notes_orig="Actually debuted as Sailor V in 1991 manga before the Sailor Moon series. Voiced by Rika Fukami in Japanese. Blonde hair with red bow.",
        notes_modern="Crystal clarified her role as Princess Serenity's decoy and true leader of the Senshi, which the 90s anime underplayed.",
    )
    lib.add_cartoon(sailor_venus)

    # 6. Sailor Uranus / Haruka Tenou
    sailor_uranus = _make_sailor(
        name="Sailor Uranus",
        description=(
            "Haruka Tenou is an outer Sailor Senshi and one of the most iconic "
            "characters in the franchise. A talented racecar driver who presents "
            "androgynously, she transforms into Sailor Uranus, guardian of the sky "
            "and flight. Her attacks include World Shaking and Space Sword Blaster. "
            "She has a deeply committed relationship with Sailor Neptune."
        ),
        debut_year=1994,
        alter_ego="Haruka Tenou / Amara in English dub",
        planet="Uranus",
        image_url=SM_IMG,
        notes_orig="Introduced in Sailor Moon S (1994). Voiced by Megumi Ogata. DiC dub controversially altered her relationship with Neptune to cousins.",
        notes_modern="Crystal and all modern productions fully depict her relationship with Sailor Neptune as romantic, restoring the original intent.",
    )
    lib.add_cartoon(sailor_uranus)

    # 7. Sailor Neptune / Michiru Kaiou
    sailor_neptune = _make_sailor(
        name="Sailor Neptune",
        description=(
            "Michiru Kaiou is a gifted violinist and painter who transforms "
            "into Sailor Neptune, guardian of the ocean and premonition. "
            "Elegant and mysterious, she partners with Sailor Uranus both in "
            "battle and in life. Her attacks include Deep Submerge and Submarine "
            "Reflection. She wields the Deep Aqua Mirror, one of the three talismans."
        ),
        debut_year=1994,
        alter_ego="Michiru Kaiou / Michelle in English dub",
        planet="Neptune",
        image_url=SM_IMG,
        notes_orig="Introduced in Sailor Moon S alongside Uranus. Voiced by Masako Katsuki. Teal wavy hair and refined artistic personality.",
        notes_modern="Her bond with Sailor Uranus is fully restored in Crystal. Remains one of the most beloved characters in the franchise.",
    )
    lib.add_cartoon(sailor_neptune)

    # 8. Sailor Pluto / Setsuna Meiou
    sailor_pluto = _make_sailor(
        name="Sailor Pluto",
        description=(
            "Setsuna Meiou is the guardian of the Space-Time Door and one of "
            "the most powerful and mysterious Sailor Senshi. She guards the "
            "passage between time and is largely forbidden from leaving her post. "
            "She wields the Garnet Rod and the Garnet Orb talisman. Her attack "
            "Dead Scream is among the most iconic in the series."
        ),
        debut_year=1993,
        alter_ego="Setsuna Meiou / Trista in English dub",
        planet="Pluto",
        image_url=SM_IMG,
        notes_orig="Introduced in Sailor Moon R. Voiced by Chiyoko Kawashima. Dark skin, garnet red eyes and long black-green hair.",
        notes_modern="Crystal expanded her backstory significantly. Her role as Time Guardian makes her one of the most unique Senshi.",
    )
    lib.add_cartoon(sailor_pluto)

    # 9. Sailor Saturn / Hotaru Tomoe
    sailor_saturn = _make_sailor(
        name="Sailor Saturn",
        description=(
            "Hotaru Tomoe is the most powerful and feared of all the Sailor "
            "Senshi — the guardian of destruction and rebirth. As Sailor Saturn "
            "she wields the Silence Glaive and has the power to destroy entire "
            "worlds, but also to heal. Her awakening signals the end of an era. "
            "She later reincarnates as a child and is adopted by the outer Senshi."
        ),
        debut_year=1994,
        alter_ego="Hotaru Tomoe / Hotaru in English dub",
        planet="Saturn",
        image_url=SM_IMG,
        notes_orig="Introduced in Sailor Moon S. Voiced by Yuko Minaguchi. Her destruction power made her controversial among fans and other Senshi.",
        notes_modern="Crystal's Saturn is closer to the manga — her role as both destroyer and healer is given equal weight and emotional depth.",
    )
    lib.add_cartoon(sailor_saturn)

    # 10. Tuxedo Mask / Mamoru Chiba
    tuxedo_mask = _make_sailor(
        name="Tuxedo Mask",
        description=(
            "Mamoru Chiba is a university student and Usagi's great love who "
            "transforms into Tuxedo Mask, a mysterious caped figure who rescues "
            "Sailor Moon with well-timed rose throws and rousing speeches. "
            "He is the reincarnation of Prince Endymion of Earth. He later "
            "becomes King Endymion of Crystal Tokyo in the future."
        ),
        debut_year=1992,
        alter_ego="Mamoru Chiba / Darien in English dub",
        planet="Earth",
        image_url=SM_IMG,
        notes_orig="Voiced by Tohru Furuya in Japanese. DiC dub voiced by Rino Romano then Vincent Van Patten. His rose-throwing became iconic.",
        notes_modern="Crystal gave Mamoru a more active and capable role compared to the 90s anime where he was frequently incapacitated.",
    )
    lib.add_cartoon(tuxedo_mask)

    # 11. Chibiusa / Sailor Chibi Moon
    chibiusa = _make_sailor(
        name="Sailor Chibi Moon",
        description=(
            "Chibiusa is the future daughter of Sailor Moon and Tuxedo Mask "
            "who travels back in time from Crystal Tokyo. She transforms into "
            "Sailor Chibi Moon and fights alongside her mother. Nicknamed Small "
            "Lady, she has pink hair and crescent moon markings. She is in "
            "training to become a full Sailor Senshi in her own right."
        ),
        debut_year=1993,
        alter_ego="Chibiusa / Rini in English dub",
        planet="Moon (future)",
        image_url=SM_IMG,
        notes_orig="Introduced in Sailor Moon R. Voiced by Kae Araki. One of the most divisive characters — beloved by some fans, disliked by others.",
        notes_modern="Crystal gave Chibiusa a stronger arc and clearer motivation. Her Sailor Chibi Moon form is more prominent than in 90s anime.",
    )
    lib.add_cartoon(chibiusa)

    # ════════════════════════════════════════════════════════════════════════
    # DRAGON BALL Z CHARACTERS
    # ════════════════════════════════════════════════════════════════════════

    # 1. Goku
    goku = _make_dbz(
        name="Goku",
        description=(
            "The main protagonist of Dragon Ball and Dragon Ball Z. Born Kakarot, "
            "a low-class Saiyan warrior sent to Earth as an infant, he was raised "
            "by Grandpa Gohan and grew up to become Earth's greatest defender. "
            "Pure of heart and obsessed with fighting strong opponents, he achieves "
            "Super Saiyan transformation and numerous power levels beyond. "
            "One of the most recognizable fictional characters in the world."
        ),
        debut_year=1986,
        role="Saiyan warrior / protagonist",
        image_url=DBZ_IMG,
        notes_orig="Voiced by Masako Nozawa in Japanese across all series. US Funimation dub voiced by Sean Schemmel. Debuted in Dragon Ball episode 1, 1986.",
        notes_modern="Masako Nozawa has voiced Goku continuously since 1986 — one of the longest-running voice acting roles in anime history.",
    )
    lib.add_cartoon(goku)

    # 2. Vegeta
    vegeta = _make_dbz(
        name="Vegeta",
        description=(
            "The prince of the Saiyan race and one of the most beloved antiheroes "
            "in anime history. Initially a villain who comes to Earth to find the "
            "Dragon Balls, Vegeta gradually becomes an ally and later a hero while "
            "maintaining his proud, arrogant personality. His rivalry with Goku "
            "drives much of DBZ's narrative. He eventually achieves Super Saiyan "
            "and Ultra Ego transformations."
        ),
        debut_year=1989,
        role="Saiyan prince / antihero",
        image_url=DBZ_IMG,
        notes_orig="Voiced by Ryou Horikawa in Japanese; Christopher Sabat in Funimation English dub. His widow's peak hair is iconic. Introduced in Saiyan Saga.",
        notes_modern="Vegeta's evolution from villain to hero is considered one of the greatest character arcs in anime. Super gave him unique Ultra Ego form.",
    )
    lib.add_cartoon(vegeta)

    # 3. Gohan
    gohan = _make_dbz(
        name="Gohan",
        description=(
            "Goku's first son and the character with the highest latent potential "
            "in the series. As a child he unlocks Super Saiyan 2 during the Cell "
            "Games in one of the most celebrated moments in anime. Studious and "
            "gentle by nature, he struggles with his dual identity as a scholar "
            "and a fighter. His Ultimate Gohan form is among the most powerful "
            "in the franchise. He also operates as the Great Saiyaman."
        ),
        debut_year=1989,
        role="Half-Saiyan scholar and warrior",
        image_url=DBZ_IMG,
        notes_orig="Voiced by Masako Nozawa as child; Shunsuke Kikuchi score. Teen Gohan voiced by Kyle Hebert in English dub. Central character of Cell Saga.",
        notes_modern="Super Hero film (2022) brought Gohan back as lead protagonist with a new Beast Gohan transformation well received by fans.",
    )
    lib.add_cartoon(gohan)

    # 4. Piccolo
    piccolo = _make_dbz(
        name="Piccolo",
        description=(
            "A Namekian warrior and former villain who becomes Gohan's mentor and "
            "one of the most important heroes of the series. Originally the reincarnation "
            "of the Demon King Piccolo, he gradually becomes one of Earth's greatest "
            "defenders. Known for his green skin, white cape, and weighted training clothes. "
            "He fuses with Nail and Kami to increase his power and becomes Piccolo Jr."
        ),
        debut_year=1988,
        role="Namekian warrior / mentor",
        image_url=DBZ_IMG,
        notes_orig="Voiced by Toshio Furukawa in Japanese; Christopher Sabat in English. Introduced as a Dragon Ball villain then became a hero in DBZ.",
        notes_modern="Super Hero (2022) gave Piccolo a new Orange Piccolo form and the starring role — his most prominent role in decades.",
    )
    lib.add_cartoon(piccolo)

    # 5. Frieza
    frieza = _make_dbz(
        name="Frieza",
        description=(
            "The most iconic villain of Dragon Ball Z — a galactic emperor and "
            "tyrant who destroyed Planet Vegeta and enslaved countless races. "
            "His multiple transformation forms culminating in his final form "
            "shocked audiences. His battle with Goku on Planet Namek is one of "
            "the longest and most celebrated fights in anime. He later returns "
            "as Golden Frieza and Black Frieza."
        ),
        debut_year=1990,
        role="Galactic emperor / primary villain",
        image_url=DBZ_IMG,
        notes_orig="Voiced by Ryusei Nakao in Japanese; Linda Young then Chris Ayres in English. Namek saga villain. His final form reveal is one of anime's most iconic moments.",
        notes_modern="Golden Frieza introduced in Resurrection F film (2015). Black Frieza in Super manga surpasses all previous power levels.",
    )
    lib.add_cartoon(frieza)

    # 6. Cell
    cell = _make_dbz(
        name="Cell",
        description=(
            "An artificial bio-android created by Dr. Gero from the cells of "
            "Earth's greatest warriors including Goku, Vegeta, Piccolo, Frieza, "
            "and King Cold. He absorbs Androids 17 and 18 to reach his Perfect "
            "Form and hosts the Cell Games — a tournament where he fights Earth's "
            "mightiest heroes. Defeated by teen Gohan's Super Saiyan 2 transformation."
        ),
        debut_year=1992,
        role="Bio-android villain",
        image_url=DBZ_IMG,
        notes_orig="Voiced by Norio Wakamoto in Japanese; Dameon Clarke in English. Cell Saga (1992-1993) is widely considered DBZ's creative peak.",
        notes_modern="Cell Max appears in Super Hero (2022) as an unfinished giant version. Original Cell remains the fan-favorite villain of the series.",
    )
    lib.add_cartoon(cell)

    # 7. Majin Buu
    majin_buu = _make_dbz(
        name="Majin Buu",
        description=(
            "An ancient magical being of immense power who was sealed away for "
            "millions of years before being released by the wizard Babidi. "
            "Buu has multiple forms including Fat Buu, Evil Buu, Super Buu, "
            "and Kid Buu — each more powerful than the last. His ability to "
            "absorb others and his childlike innocence in his original form "
            "make him one of the most unique DBZ villains."
        ),
        debut_year=1994,
        role="Magical villain / later reformed",
        image_url=DBZ_IMG,
        notes_orig="Voiced by Kozo Shioya in Japanese; Josh Martin in English. Buu Saga is the final arc of DBZ. Fat Buu later reforms and becomes Mr. Buu.",
        notes_modern="Mr. Buu appears in Dragon Ball Super as a supporting ally. Kid Buu's reincarnation Uub is introduced at the end of DBZ.",
    )
    lib.add_cartoon(majin_buu)

    # 8. Trunks
    trunks = _make_dbz(
        name="Trunks",
        description=(
            "The son of Vegeta and Bulma who appears in two forms — Future Trunks, "
            "a teenage warrior from a devastated alternate timeline who travels back "
            "in time to warn the heroes about the Androids, and present-day Chibi "
            "Trunks, a young boy who is best friends with Goten. Future Trunks "
            "achieves Super Saiyan and later Super Saiyan Rage, while Chibi "
            "Trunks achieves Super Saiyan as a young child."
        ),
        debut_year=1991,
        role="Half-Saiyan / time traveler",
        image_url=DBZ_IMG,
        notes_orig="Voiced by Takeshi Kusao in Japanese; Eric Vale as Future Trunks in English. His surprise reveal of killing Frieza is one of DBZ's greatest moments.",
        notes_modern="Future Trunks returns in Dragon Ball Super's Goku Black arc — one of the most praised story arcs in the Super series.",
    )
    lib.add_cartoon(trunks)

    # 9. Krillin
    krillin = _make_dbz(
        name="Krillin",
        description=(
            "Goku's best friend and Earth's strongest human fighter. Bald with "
            "six dots on his forehead from his Shaolin training, Krillin provides "
            "both comic relief and genuine heroism throughout the series. He is "
            "killed multiple times yet always returns. He eventually marries Android "
            "18 and has a daughter named Marron. His Destructo Disc attack is iconic."
        ),
        debut_year=1986,
        role="Human warrior / comic relief / hero",
        image_url=DBZ_IMG,
        notes_orig="Voiced by Mayumi Tanaka in Japanese; Sonny Strait in English. Originally Goku's rival at the Kame House; became his closest friend.",
        notes_modern="Krillin's marriage to Android 18 is one of the most beloved relationship arcs in the franchise. Appears regularly in Super.",
    )
    lib.add_cartoon(krillin)

    # 10. Bulma
    bulma = _make_dbz(
        name="Bulma",
        description=(
            "A brilliant teenage scientist and the second character introduced "
            "in Dragon Ball. Bulma invented the Dragon Radar to find the Dragon "
            "Balls and has been instrumental in the heroes' success through her "
            "scientific genius. She becomes Vegeta's partner and the mother of "
            "Trunks. Heiress to Capsule Corporation, the world's most advanced "
            "technology company."
        ),
        debut_year=1986,
        role="Human scientist / supporting hero",
        image_url=DBZ_IMG,
        notes_orig="Voiced by Hiromi Tsuru in Japanese until her death in 2017; Aya Hisakawa since. Bulma's hair color changes across arcs — a running gag.",
        notes_modern="Bulma plays a larger role in Dragon Ball Super including interactions with Beerus and helping develop time travel technology.",
    )
    lib.add_cartoon(bulma)

    # 11. Android 18
    android18 = _make_dbz(
        name="Android 18",
        description=(
            "A human converted into a cyborg by the villainous Dr. Gero to "
            "serve as a weapon against Goku. Initially a villain who defeats "
            "Vegeta effortlessly, she is absorbed by Cell before being freed "
            "and eventually marrying Krillin. She becomes a protective mother "
            "to Marron and a powerful ally. One of the strongest human-derived "
            "characters in the series."
        ),
        debut_year=1992,
        role="Android / reformed villain / hero",
        image_url=DBZ_IMG,
        notes_orig="Voiced by Miki Ito in Japanese; Meredith McCoy in English. Her casual defeat of Vegeta shocked audiences during the Android Saga.",
        notes_modern="Android 18 participates in the Tournament of Power in Super as one of Universe 7's ten fighters. Remains a fan favorite.",
    )
    lib.add_cartoon(android18)

    # 12. Gotenks / Goten and Trunks fusion
    goten = _make_dbz(
        name="Goten",
        description=(
            "Goku's second son and Trunks's best friend. Goten is the youngest "
            "character to achieve Super Saiyan transformation in the series. "
            "Together with Chibi Trunks he performs the Fusion Dance to become "
            "Gotenks — a powerful but immature fusion warrior. He appears "
            "primarily in the Buu Saga and is one of the most cheerful and "
            "carefree characters in the franchise."
        ),
        debut_year=1994,
        role="Half-Saiyan / youngest Super Saiyan",
        image_url=DBZ_IMG,
        notes_orig="Voiced by Masako Nozawa in Japanese; Kara Edwards in English. Strongly resembles young Goku. Achieved Super Saiyan younger than any character.",
        notes_modern="Goten is a teenager in Dragon Ball Super. He and Trunks take a back seat to adult heroes but remain present in the story.",
    )
    lib.add_cartoon(goten)

    # 13. Piccolo / already added — adding Gotenks
    gotenks = _make_dbz(
        name="Gotenks",
        description=(
            "The fusion of Goten and Trunks using the Fusion Dance — a powerful "
            "but personality-driven warrior who combines both boys' traits into "
            "an overconfident, showboating fighter. Gotenks achieves Super Saiyan "
            "3 — a feat it took Goku years to reach — but wastes time with "
            "dramatic performances instead of fighting seriously. One of the most "
            "entertaining characters in the Buu Saga."
        ),
        debut_year=1994,
        role="Fusion warrior — Goten and Trunks combined",
        image_url=DBZ_IMG,
        notes_orig="Voiced by Masako Nozawa and Takeshi Kusao sharing the role. Known for inventing flamboyant named attacks on the spot.",
        notes_modern="Gotenks appears briefly in Super. The Fusion Dance is a recurring element used by multiple characters across the franchise.",
    )
    lib.add_cartoon(gotenks)

    # 14. Vegito / Potara fusion
    vegito = _make_dbz(
        name="Vegito",
        description=(
            "The Potara earring fusion of Goku and Vegeta — considered the most "
            "powerful warrior in the Dragon Ball universe at the time of his "
            "creation. Vegito combines Goku's pure heart and fighting instinct "
            "with Vegeta's pride and tactical intelligence. He appears twice — "
            "against Super Buu in DBZ and against Fused Zamasu in Dragon Ball "
            "Super's Future Trunks arc."
        ),
        debut_year=1994,
        role="Potara fusion warrior — Goku and Vegeta combined",
        image_url=DBZ_IMG,
        notes_orig="Voiced by Masako Nozawa and Ryou Horikawa sharing the role. Known as Vegerot in some translations. His battle with Super Buu is fan-beloved.",
        notes_modern="Returns in Dragon Ball Super against Fused Zamasu. His Blue Vegito form is one of the most visually striking in the series.",
    )
    lib.add_cartoon(vegito)

    # 15. Broly
    broly = _make_dbz(
        name="Broly",
        description=(
            "The Legendary Super Saiyan — a Saiyan of immense power born with "
            "an extraordinary power level on the same day as Goku. Originally "
            "introduced in non-canonical films, Broly was reimagined in the "
            "canonical Dragon Ball Super: Broly film as a tragic figure — a "
            "powerful but gentle Saiyan who has been conditioned into a weapon "
            "by his cruel father Paragus."
        ),
        debut_year=1993,
        role="Legendary Super Saiyan",
        image_url=DBZ_IMG,
        notes_orig="Original Broly debuted in Dragon Ball Z: Broly The Legendary Super Saiyan (1993). Non-canonical but massively popular with fans.",
        notes_modern="Canonical Broly reimagined in Super: Broly (2018) by Toriyama himself. New version is more sympathetic and better received critically.",
    )
    lib.add_cartoon(broly)

    # 16. Piccolo already added — add Yamcha
    yamcha = _make_dbz(
        name="Yamcha",
        description=(
            "A former desert bandit and one of Goku's earliest allies who becomes "
            "a recurring hero throughout the series. A skilled martial artist and "
            "former boyfriend of Bulma, Yamcha is known for the Wolf Fang Fist "
            "technique. He becomes infamous in the Dragon Ball Z fandom for being "
            "frequently overpowered by enemies — the Yamcha pose of dying face-down "
            "in a crater became an internet meme."
        ),
        debut_year=1986,
        role="Human warrior / comic relief hero",
        image_url=DBZ_IMG,
        notes_orig="Voiced by Toru Furuya in Japanese; Christopher Sabat in English. One of the original Dragon Ball characters who carries over into Z.",
        notes_modern="Yamcha is largely sidelined in Super due to power scaling. He remains beloved by fans largely through ironic appreciation of his misfortunes.",
    )
    lib.add_cartoon(yamcha)

    # 17. Piccolo already done — add Tenshinhan / Tien
    tien = _make_dbz(
        name="Tien Shinhan",
        description=(
            "A three-eyed human warrior and former student of the Crane Hermit "
            "school who transitions from rival to ally. Known for the Solar Flare "
            "and Tri-Beam techniques. Tien is considered the strongest pure human "
            "in the series alongside Krillin. He runs his own martial arts school "
            "with his lifelong companion Chiaotzu and remains deeply dedicated "
            "to improving his strength."
        ),
        debut_year=1986,
        role="Three-eyed human martial artist",
        image_url=DBZ_IMG,
        notes_orig="Voiced by Hirotaka Suzuoki then Hikaru Midorikawa in Japanese; John Burgmeier in English. Originally a villain in Dragon Ball before becoming a hero.",
        notes_modern="Tien participates in the Tournament of Power in Super despite being far weaker than Saiyan fighters — praised for his tenacity.",
    )
    lib.add_cartoon(tien)

    # 18. Piccolo skip — add Android 17
    android17 = _make_dbz(
        name="Android 17",
        description=(
            "A human converted into a cyborg alongside his twin sister Android 18 "
            "by Dr. Gero. Initially a villain with a rebellious attitude, Android 17 "
            "eventually becomes a park ranger and wildlife protector. He makes a "
            "stunning return in Dragon Ball Super's Tournament of Power where he "
            "proves himself one of the series' most powerful fighters and becomes "
            "the tournament's MVP."
        ),
        debut_year=1992,
        role="Android / reformed villain / tournament hero",
        image_url=DBZ_IMG,
        notes_orig="Voiced by Shigeru Nakahara in Japanese; Chuck Huber in English. He and Android 18 kill Future Gohan in the alternate timeline.",
        notes_modern="Android 17's Tournament of Power performance in Super surprised fans who had forgotten the character. He eliminates multiple opponents.",
    )
    lib.add_cartoon(android17)

    # 19. Whis
    whis = _make_dbz(
        name="Whis",
        description=(
            "The Angel attendant and martial arts trainer of the God of Destruction "
            "Beerus, and by extension the trainer of Goku and Vegeta in Dragon Ball "
            "Super. Whis is among the most powerful beings in the universe — "
            "far stronger than Beerus himself. Known for his calm demeanor, "
            "love of food, and the ability to reverse time up to three minutes. "
            "He carries a magical staff and wears the Angel's halo."
        ),
        debut_year=2013,
        role="Angel attendant / martial arts instructor",
        image_url=DBZ_IMG,
        notes_orig="Voiced by Masakazu Morita in Japanese; Ian Sinclair in English. Introduced in Battle of Gods film (2013). His true power level is never fully revealed.",
        notes_modern="Whis serves as a mentor figure in Super, training Goku and Vegeta in godly ki. His sister Vados is attendant to Champa of Universe 6.",
    )
    lib.add_cartoon(whis)

    # 20. Beerus
    beerus = _make_dbz(
        name="Beerus",
        description=(
            "The God of Destruction of Universe 7 — a cat-like deity whose job "
            "is to destroy planets to maintain universal balance. Introduced in "
            "Battle of Gods, Beerus becomes an unlikely recurring character who "
            "drives much of Dragon Ball Super's plot. He is powerful enough to "
            "destroy the entire universe if he chose. Known for his love of food "
            "and his unpredictable temperament."
        ),
        debut_year=2013,
        role="God of Destruction — Universe 7",
        image_url=DBZ_IMG,
        notes_orig="Voiced by Koichi Yamadera in Japanese; Jason Douglas in English. Debuted in Dragon Ball Z: Battle of Gods (2013). Visually based on an Egyptian cat deity.",
        notes_modern="Beerus becomes a reluctant ally in Super. His rivalry with his twin brother Champa (Universe 6's God of Destruction) is a recurring plot element.",
    )
    lib.add_cartoon(beerus)

    # 21. Zamasu / Goku Black
    goku_black = _make_dbz(
        name="Goku Black",
        description=(
            "A Supreme Kai apprentice named Zamasu who used the Super Dragon Balls "
            "to switch bodies with Goku and then traveled to Future Trunks's timeline "
            "to enact a Zero Mortals Plan — the genocide of all mortal life. "
            "Goku Black is considered one of Dragon Ball Super's best villains "
            "for his disturbing premise, powerful design, and connection to Future "
            "Trunks's heartbreaking storyline."
        ),
        debut_year=2016,
        role="Supreme Kai turned villain / alternate Goku",
        image_url=DBZ_IMG,
        notes_orig="Voiced by Masako Nozawa using Goku's voice in Japanese. His rose-colored Super Saiyan Rose form is visually distinctive and fan-beloved.",
        notes_modern="The Future Trunks arc featuring Goku Black is widely considered Dragon Ball Super's best story arc by the fanbase.",
    )
    lib.add_cartoon(goku_black)

    print(f"Anime characters added. Library now has {len(lib.cartoons)} cartoons total.")
