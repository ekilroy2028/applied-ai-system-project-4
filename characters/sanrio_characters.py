"""
sanrio_characters.py
Hello Kitty and all major Sanrio characters for CartoonPal.

Sanrio Co., Ltd. was founded in 1960 by Shintaro Tsuji in Tokyo, Japan.
The company creates "social communication" characters designed to be gifted
on greeting cards and merchandise. Hello Kitty debuted in 1974 and became
one of the highest-grossing character franchises in history.

All characters are owned by Sanrio Co., Ltd. (Tokyo, Japan).
Sanrio is publicly traded on the Tokyo Stock Exchange.

Key ownership note:
- Sanrio Co., Ltd. owns ALL character IP outright
- Characters are licensed to manufacturers worldwide
- No major ownership transfers — Sanrio has retained all rights since founding
- Hello Kitty is simultaneously a Japanese character (Sanrio) and a global
pop culture icon licensed in virtually every country

Usage:
    from characters.sanrio_characters import add_sanrio_characters
    add_sanrio_characters(lib)
"""

from cartoon_system import (
    Cartoon, Creator, ProductionCompany,
    Series, OwnershipRecord, Era, Library
)

SANRIO_STUDIO = ProductionCompany("Sanrio Co., Ltd.", 1960, country="Japan", still_active=True)

SHINTARO_TSUJI = Creator("Shintaro Tsuji", "Sanrio founder & chairman", 1927)
YUKO_SHIMIZU   = Creator("Yuko Shimizu", "Hello Kitty original character designer (1974)", 1956)
YUKO_YAMAGUCHI = Creator("Yuko Yamaguchi", "Hello Kitty lead designer (1980-2017)", 1956)
MIYUKI_OKUMURA = Creator("Miyuki Okumura", "Hello Kitty current lead designer (2017-present)", 0)

SANRIO_OWNERSHIP = [
    ("Sanrio Co., Ltd.", 1960, None,
    "original creation — Sanrio retains all character IP worldwide",
    ),
]

IMG = {
    "kitty":    "https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Hello_kitty_character_portrait.png/200px-Hello_kitty_character_portrait.png",
    "sanrio":   "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Sanrio_logo.svg/240px-Sanrio_logo.svg.png",
    "my_melody":"https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/My_Melody_character_portrait.png/200px-My_Melody_character_portrait.png",
    "cinnamoroll":"https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Cinnamoroll_character_portrait.png/200px-Cinnamoroll_character_portrait.png",
    "kuromi":   "https://upload.wikimedia.org/wikipedia/en/thumb/4/4e/Kuromi_character_portrait.png/200px-Kuromi_character_portrait.png",
    "pompom":   "https://upload.wikimedia.org/wikipedia/en/thumb/8/8c/Pompompurin_character_portrait.png/200px-Pompompurin_character_portrait.png",
    "pochacco": "https://upload.wikimedia.org/wikipedia/en/thumb/5/5a/Pochacco_character_portrait.png/200px-Pochacco_character_portrait.png",
    "chococat": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/Chococat_character_portrait.png/200px-Chococat_character_portrait.png",
    "badtz":    "https://upload.wikimedia.org/wikipedia/en/thumb/3/3d/Badtz-Maru_character_portrait.png/200px-Badtz-Maru_character_portrait.png",
    "keroppi":  "https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/Keroppi_character_portrait.png/200px-Keroppi_character_portrait.png",
    "tuxedo":   "https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/Tuxedosam_character_portrait.png/200px-Tuxedosam_character_portrait.png",
    "little":   "https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/Little_Twin_Stars_character_portrait.png/200px-Little_Twin_Stars_character_portrait.png",
    "gudetama": "https://upload.wikimedia.org/wikipedia/en/thumb/4/4e/Gudetama_character_portrait.png/200px-Gudetama_character_portrait.png",
    "aggretsuko":"https://upload.wikimedia.org/wikipedia/en/thumb/5/5a/Aggretsuko_character_portrait.png/200px-Aggretsuko_character_portrait.png",
    "sega":     "https://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Hello_Kitty_animated_series.png/200px-Hello_Kitty_animated_series.png",
}


def _sanrio(name, description, character_type, debut_year,
            extra_creators, series_list, eras, wiki_slug,
            origin="Tokyo, Japan — Sanrio Co., Ltd."):
    c = Cartoon(name=name, description=description,
                character_type=character_type,
                country_of_origin="Japan",
                debut_year=debut_year)
    c.original_studio = SANRIO_STUDIO
    c.add_creator(SHINTARO_TSUJI)
    for ec in extra_creators:
        c.add_creator(ec)
    for s in series_list:
        c.add_series(s)
    for i, rec in enumerate(SANRIO_OWNERSHIP):
        c.add_ownership_record(OwnershipRecord(
            rec[0], rec[1], rec[2], rec[3],
            is_current_owner=True
        ))
    for era in eras:
        c.add_era(era)
    c.wiki_url = f"https://en.wikipedia.org/wiki/{wiki_slug}"
    c.origin_location = origin
    return c


def add_sanrio_characters(lib: Library):

    # ══════════════════════════════════════════════════════════════════════
    # HELLO KITTY (1974) — the flagship
    # ══════════════════════════════════════════════════════════════════════
    hello_kitty = _sanrio(
        name="Hello Kitty",
        description=(
            "Kitty White — a small white cat-like girl with no mouth, a red bow, "
            "and a simple dot nose who lives in London with her family. Hello Kitty "
            "was designed in 1974 by Yuko Shimizu and is one of the most globally "
            "recognized fictional characters ever created. She has no mouth because "
            "Sanrio wanted people to project their own emotions onto her — she is "
            "happy when you are happy. Hello Kitty generates over $8 billion in "
            "annual merchandise revenue, making her one of the highest-grossing "
            "character franchises in history. She is technically not a cat but a "
            "little girl — a fact Sanrio clarified in 2014 to widespread surprise. "
            "She is the twin sister of Mimmy White."
        ),
        character_type="Sanrio character — Japanese kawaii icon",
        debut_year=1974,
        extra_creators=[YUKO_SHIMIZU, YUKO_YAMAGUCHI, MIYUKI_OKUMURA],
        series_list=[
            Series("Hello Kitty merchandise debut (coin purse)", 1974, 1974,
                "Sanrio Co., Ltd.", "product merchandise",
                notes="First appeared on a vinyl coin purse in Japan in 1974. "
                        "No animated content initially — pure merchandise character."),
            Series("Hello Kitty's Furry Tale Theater (DiC animated series)", 1987, 1987,
                "DiC Entertainment / Sanrio / CBS", "TV series", episode_count=13,
                notes="First major animated series in English. "
                        "DiC Entertainment produced under Sanrio license for CBS."),
            Series("Hello Kitty and Friends (Sega / Sanrio animated)", 1991, 1992,
                "Sega / Sanrio", "TV anime", episode_count=26,
                notes="Japanese animated series featuring Hello Kitty and Sanrio friends."),
            Series("Hello Kitty's Paradise (Japanese anime)", 1999, 2001,
                "Sanrio / OLM Inc.", "TV anime", episode_count=30),
            Series("Hello Kitty and Friends Supercute Adventures", 2020, None,
                "Sanrio / Dentsu Entertainment USA / Netflix", "streaming series",
                notes="Modern CGI animated series on YouTube and Netflix. "
                        "Updated design for global streaming audience."),
            Series("Hello Kitty live-action film", 2025, None,
                "Sanrio / New Line Cinema / Warner Bros.", "theatrical feature",
                notes="Live-action/CGI hybrid film announced — first theatrical feature."),
        ],
        eras=[
            Era(1974, 1979,
                "Original design — simple white cat face, red bow on left ear, "
                "blue eyes, no mouth, sitting pose on merchandise",
                art_style="Flat graphic illustration for merchandise",
                image_url=IMG["kitty"],
                notes="Designed by Yuko Shimizu. First appeared on a vinyl coin purse. "
                    "The design was intentionally simple for easy reproduction on merchandise. "
                    "The no-mouth design was deliberate — allowing emotional projection."),
            Era(1980, 1999,
                "Classic refinement era — same fundamental design refined by Yuko Yamaguchi, "
                "more varied poses and expressions, global expansion",
                art_style="Refined flat graphic illustration",
                image_url=IMG["kitty"],
                notes="Yuko Yamaguchi became lead designer in 1980. "
                    "Hello Kitty became a global phenomenon in the 1990s. "
                    "First introduced in the US in 1976 — initially failed, "
                    "relaunched successfully in the 1980s."),
            Era(2000, 2018,
                "Global icon era — design adapted for countless collaborations, "
                "collabs with luxury brands, pop stars, and global retailers",
                art_style="Versatile flat graphic across multiple media",
                image_url=IMG["kitty"],
                notes="Hello Kitty collaborated with brands from Louis Vuitton to McDonald's. "
                    "In 2014 Sanrio clarified Hello Kitty is not a cat but a little girl "
                    "— a statement that confused and delighted the internet. "
                    "Annual merchandise revenue exceeded $8 billion by 2010."),
            Era(2019, None,
                "Modern streaming and live-action era — CGI updates for streaming content, "
                "50th anniversary celebrations, first theatrical film in development",
                art_style="CGI and updated digital illustration",
                image_url=IMG["kitty"],
                notes="50th anniversary in 2024 marked with major global celebrations. "
                    "Live-action film in development at Warner Bros. "
                    "Sanrio reported record revenues in 2023-2024."),
        ],
        wiki_slug="Hello_Kitty",
    )
    lib.add_cartoon(hello_kitty)

    # ══════════════════════════════════════════════════════════════════════
    # MIMMY WHITE (1974) — Hello Kitty's twin sister
    # ══════════════════════════════════════════════════════════════════════
    mimmy = _sanrio(
        name="Mimmy White",
        description=(
            "Hello Kitty's twin sister — identical in design but distinguished "
            "by a yellow bow on her right ear (Hello Kitty's bow is on her left). "
            "Mimmy is described as shy, girly, and fond of sewing — the quieter "
            "counterpart to Hello Kitty. She rarely appears without her twin and "
            "is primarily a supporting character in Hello Kitty's world. "
            "The mirror-image bow placement is the only visual distinction between "
            "the twins — a simple but effective design choice."
        ),
        character_type="Sanrio character — Hello Kitty's twin sister",
        debut_year=1974,
        extra_creators=[YUKO_SHIMIZU, YUKO_YAMAGUCHI],
        series_list=[
            Series("Hello Kitty merchandise and media appearances", 1974, None,
                "Sanrio Co., Ltd.", "merchandise / various",
                notes="Mimmy appears alongside Hello Kitty in merchandise and animated content. "
                        "Yellow bow on right ear distinguishes her from Hello Kitty."),
        ],
        eras=[
            Era(1974, None,
                "Identical to Hello Kitty with yellow bow on right ear instead of red bow on left",
                art_style="Flat graphic illustration",
                image_url=IMG["kitty"],
                notes="Mimmy is intentionally kept as Hello Kitty's mirror — "
                    "the two are inseparable in Sanrio's world."),
        ],
        wiki_slug="Hello_Kitty",
    )
    lib.add_cartoon(mimmy)

    # ══════════════════════════════════════════════════════════════════════
    # MY MELODY (1975)
    # ══════════════════════════════════════════════════════════════════════
    my_melody = _sanrio(
        name="My Melody",
        description=(
            "A white rabbit always wearing a pink or red hood who lives in "
            "Mariland in the forest of Mary Land. My Melody is sweet, kind, "
            "and loves baking cookies with her grandmother. She debuted in 1975 "
            "and is one of Sanrio's oldest characters. She gained enormous popularity "
            "through the Onegai My Melody anime series (2005) which gave her a "
            "full narrative world and introduced her rival Kuromi. "
            "My Melody is consistently one of Sanrio's top-ranking characters "
            "in annual popularity polls."
        ),
        character_type="Sanrio character — white rabbit in pink hood",
        debut_year=1975,
        extra_creators=[],
        series_list=[
            Series("My Melody merchandise debut", 1975, None,
                "Sanrio Co., Ltd.", "merchandise",
                notes="Debuted in 1975 as a merchandise character inspired by Little Red Riding Hood."),
            Series("Onegai My Melody (anime series)", 2005, 2008,
                "Studio Comet / TV Tokyo", "TV anime", episode_count=76,
                notes="Four-season anime series that gave My Melody a full story world. "
                        "Introduced Kuromi as her rival. Hugely popular in Japan."),
            Series("My Melody and Kuromi (Netflix anime)", 2022, None,
                "Sanrio / Netflix", "streaming anime",
                notes="Modern streaming series featuring My Melody and Kuromi."),
        ],
        eras=[
            Era(1975, 2004,
                "Classic merchandise design — white rabbit face in pink hood, "
                "simple oval eyes, small pink nose",
                art_style="Flat graphic illustration for merchandise",
                image_url=IMG["my_melody"],
                notes="My Melody is inspired by Little Red Riding Hood. "
                    "Her hood is her most distinctive feature — she is rarely seen without it."),
            Era(2005, None,
                "Anime era — same design animated for Onegai My Melody series, "
                "full character personality and story world developed",
                art_style="Japanese TV anime / digital illustration",
                image_url=IMG["my_melody"],
                notes="The Onegai My Melody anime (2005) transformed My Melody from "
                    "a simple merchandise character into a fully realized protagonist. "
                    "Her rivalry with Kuromi became a beloved dynamic."),
        ],
        wiki_slug="My_Melody",
    )
    lib.add_cartoon(my_melody)

    # ══════════════════════════════════════════════════════════════════════
    # KUROMI (1990s / popularized 2005)
    # ══════════════════════════════════════════════════════════════════════
    kuromi = _sanrio(
        name="Kuromi",
        description=(
            "My Melody's self-described rival — a white rabbit wearing a black "
            "jester's hat with a pink skull on it and a black mask. Kuromi presents "
            "herself as tough and mischievous but is secretly a hopeless romantic "
            "who loves writing in her diary and reading shojo manga. "
            "She became massively popular in the 2010s and 2020s as the "
            "edgy dark alternative to Hello Kitty's sweetness — beloved by "
            "fans who wanted Sanrio's aesthetic with a gothic twist. "
            "By 2021 Kuromi had overtaken Hello Kitty in Sanrio annual popularity polls."
        ),
        character_type="Sanrio character — My Melody's rival / gothic kawaii",
        debut_year=2005,
        extra_creators=[],
        series_list=[
            Series("Onegai My Melody anime (Kuromi as rival)", 2005, 2008,
                "Studio Comet / TV Tokyo", "TV anime", episode_count=76,
                notes="Kuromi was introduced as My Melody's rival in the Onegai My Melody anime. "
                        "Her popularity exploded after the series aired."),
            Series("My Melody and Kuromi (Netflix)", 2022, None,
                "Sanrio / Netflix", "streaming anime"),
            Series("Kuromi merchandise expansion", 2018, None,
                "Sanrio Co., Ltd.", "merchandise",
                notes="Kuromi merchandise sales exploded globally from 2018 onward, "
                        "particularly popular in the US, Southeast Asia, and Latin America."),
        ],
        eras=[
            Era(2005, 2017,
                "Original anime design — white rabbit in black jester hat with pink skull, "
                "black mask, mischievous expression",
                art_style="Japanese TV anime illustration",
                image_url=IMG["kuromi"],
                notes="Kuromi debuted in the Onegai My Melody anime (2005). "
                    "Her gothic kawaii aesthetic set her apart from Sanrio's typical cute characters."),
            Era(2018, None,
                "Global popularity era — same design, explosive worldwide merchandise growth, "
                "number one in Sanrio popularity polls",
                art_style="Digital illustration / merchandise",
                image_url=IMG["kuromi"],
                notes="Kuromi overtook Hello Kitty in Sanrio's 2021 annual character poll. "
                    "Her popularity with Western audiences who embraced 'dark kawaii' aesthetics "
                    "made her Sanrio's fastest-growing character in the 2020s."),
        ],
        wiki_slug="Kuromi",
    )
    lib.add_cartoon(kuromi)

    # ══════════════════════════════════════════════════════════════════════
    # CINNAMOROLL (2001)
    # ══════════════════════════════════════════════════════════════════════
    cinnamoroll = _sanrio(
        name="Cinnamoroll",
        description=(
            "A chubby white puppy with big blue eyes, pink cheeks, and a plump "
            "curly tail that resembles a cinnamon roll — giving him his name. "
            "Cinnamoroll lives in the sky and can fly using his large ears. "
            "He was found by a cafe owner and now lives at Cafe Cinnamon. "
            "He won the Sanrio Character Grand Prix in 2017, 2018, 2019, 2020, "
            "2021, and 2022 — six consecutive years — making him the most award-winning "
            "Sanrio character after Hello Kitty and the first male character to "
            "top the polls. Enormously popular in Japan, China, and Southeast Asia."
        ),
        character_type="Sanrio character — white puppy / sky dweller",
        debut_year=2001,
        extra_creators=[Creator("Miyuki Okumura", "Cinnamoroll character designer", 0)],
        series_list=[
            Series("Cinnamoroll merchandise debut", 2001, None,
                "Sanrio Co., Ltd.", "merchandise"),
            Series("Cinnamoroll anime shorts", 2007, 2009,
                "Sanrio / OLM Inc.", "TV anime shorts"),
            Series("Cinnamoroll: Moko Moko Friends (anime)", 2017, 2018,
                "Sanrio", "streaming anime"),
        ],
        eras=[
            Era(2001, 2016,
                "Original design — round chubby white puppy, large floppy ears, "
                "pink cheeks, cinnamon roll tail curled upward",
                art_style="Flat graphic illustration",
                image_url=IMG["cinnamoroll"],
                notes="Debuted in 2001. Won the Sanrio Grand Prix six consecutive years "
                    "(2017-2022) — a record in Sanrio history."),
            Era(2017, None,
                "Grand Prix champion era — same design, global mainstream recognition, "
                "major presence in China and Southeast Asian markets",
                art_style="Digital illustration / CGI merchandise",
                image_url=IMG["cinnamoroll"],
                notes="Cinnamoroll's dominance of the Sanrio polls from 2017-2022 "
                    "was unprecedented. His popularity in China and Korea "
                    "made him Sanrio's most valuable character in Asian markets."),
        ],
        wiki_slug="Cinnamoroll",
    )
    lib.add_cartoon(cinnamoroll)

    # ══════════════════════════════════════════════════════════════════════
    # POMPOMPURIN (1996)
    # ══════════════════════════════════════════════════════════════════════
    pompompurin = _sanrio(
        name="Pompompurin",
        description=(
            "A golden retriever puppy who always wears a brown beret and loves "
            "pudding — his name is a combination of pompom and purin (the Japanese "
            "word for pudding/flan). He lives with his owner and sleeps in "
            "his owner's hat. Pompompurin has a laid-back, easygoing personality "
            "and is always looking for his next nap or snack. "
            "He is one of Sanrio's most beloved classic characters and won "
            "the Sanrio Character Grand Prix in 1996 and 1997."
        ),
        character_type="Sanrio character — golden retriever puppy",
        debut_year=1996,
        extra_creators=[],
        series_list=[
            Series("Pompompurin merchandise debut", 1996, None,
                "Sanrio Co., Ltd.", "merchandise"),
            Series("Pompompurin anime shorts", 1998, 2000,
                "Sanrio / OLM Inc.", "anime shorts"),
        ],
        eras=[
            Era(1996, None,
                "Classic design — round golden yellow puppy in brown beret, "
                "small black eyes, simple cheerful expression",
                art_style="Flat graphic illustration",
                image_url=IMG["pompom"],
                notes="Debuted in 1996. Won Sanrio Grand Prix in 1996 and 1997. "
                    "Pompompurin is inspired by his creator's love of pudding — "
                    "his coloring matches the golden yellow of custard pudding."),
        ],
        wiki_slug="Pompompurin",
    )
    lib.add_cartoon(pompompurin)

    # ══════════════════════════════════════════════════════════════════════
    # KEROPPI (1988)
    # ══════════════════════════════════════════════════════════════════════
    keroppi = _sanrio(
        name="Keroppi",
        description=(
            "A cheerful green frog with big crosshatch eyes and a V-shaped mouth "
            "who lives in a big house on the shore of Donut Pond with his family. "
            "Keroppi is adventurous, optimistic, and loves to swim, sing, and act. "
            "He was one of Sanrio's most popular characters in the late 1980s and "
            "1990s, particularly beloved in the United States where he rivaled "
            "Hello Kitty in popularity during the early 1990s."
        ),
        character_type="Sanrio character — green frog",
        debut_year=1988,
        extra_creators=[],
        series_list=[
            Series("Keroppi merchandise debut", 1988, None,
                "Sanrio Co., Ltd.", "merchandise"),
            Series("Keroppi anime shorts", 1989, 1994,
                "Sanrio / Group TAC", "anime shorts", episode_count=5),
        ],
        eras=[
            Era(1988, None,
                "Classic design — bright green frog, large round crosshatch eyes, "
                "wide V-shaped smile, no visible nose",
                art_style="Flat graphic illustration",
                image_url=IMG["keroppi"],
                notes="Keroppi was one of Sanrio's biggest US hits in the early 1990s. "
                    "His crosshatch eyes are one of Sanrio's most distinctive design choices. "
                    "He was particularly popular with American children aged 6-12."),
        ],
        wiki_slug="Keroppi",
    )
    lib.add_cartoon(keroppi)

    # ══════════════════════════════════════════════════════════════════════
    # BADTZ-MARU (1993)
    # ══════════════════════════════════════════════════════════════════════
    badtz_maru = _sanrio(
        name="Badtz-Maru",
        description=(
            "A black penguin with spiky hair and a perpetual scowl who dreams "
            "of becoming the boss of everything. Badtz-Maru's name means "
            "bad mark in Japanese — his parents named him hoping he would "
            "reform his attitude. He lives in Gorgeoustown with his pet "
            "alligator Pochi. Despite his tough exterior he has a good heart. "
            "He was Sanrio's first explicitly edgy character and became hugely "
            "popular in the 1990s, particularly beloved by teenagers and young adults "
            "who found him a relatable antidote to Sanrio's usual sweetness."
        ),
        character_type="Sanrio character — spiky black penguin / antihero",
        debut_year=1993,
        extra_creators=[],
        series_list=[
            Series("Badtz-Maru merchandise debut", 1993, None,
                "Sanrio Co., Ltd.", "merchandise"),
            Series("Badtz-Maru anime shorts", 1997, 1999,
                "Sanrio", "anime shorts"),
        ],
        eras=[
            Era(1993, None,
                "Classic design — black penguin body, spiky black hair, frowning expression, "
                "small white belly, arms crossed or hands on hips",
                art_style="Flat graphic illustration",
                image_url=IMG["badtz"],
                notes="Badtz-Maru was Sanrio's first attempt at a character with attitude. "
                    "His popularity with teenagers proved Sanrio could appeal beyond young children. "
                    "He is considered the predecessor to Kuromi's edgier modern aesthetic."),
        ],
        wiki_slug="Badtz-Maru",
    )
    lib.add_cartoon(badtz_maru)

    # ══════════════════════════════════════════════════════════════════════
    # POCHACCO (1989)
    # ══════════════════════════════════════════════════════════════════════
    pochacco = _sanrio(
        name="Pochacco",
        description=(
            "A white dog with floppy ears and a blue beret who loves sports — "
            "especially soccer — and eating. Pochacco is athletic, cheerful, and "
            "carefree. He was born on February 29 (Leap Day) making his birthdays "
            "extra rare. Pochacco won the Sanrio Character Grand Prix in 1993 and 1994. "
            "He experienced a major revival in the 2020s as Y2K and 1990s aesthetics "
            "returned to popularity, particularly on social media."
        ),
        character_type="Sanrio character — white dog / sports lover",
        debut_year=1989,
        extra_creators=[],
        series_list=[
            Series("Pochacco merchandise debut", 1989, None,
                "Sanrio Co., Ltd.", "merchandise"),
        ],
        eras=[
            Era(1989, None,
                "Classic design — white round-headed dog, blue beret, floppy ears, "
                "athletic cheerful expression",
                art_style="Flat graphic illustration",
                image_url=IMG["pochacco"],
                notes="Won Sanrio Grand Prix in 1993 and 1994. "
                    "Pochacco's athletic personality made him unusual among Sanrio characters "
                    "who tend toward domestic or passive activities. "
                    "His Y2K revival made him one of Sanrio's fastest-growing characters "
                    "in the early 2020s."),
        ],
        wiki_slug="Pochacco",
    )
    lib.add_cartoon(pochacco)

    # ══════════════════════════════════════════════════════════════════════
    # CHOCOCAT (1996)
    # ══════════════════════════════════════════════════════════════════════
    chococat = _sanrio(
        name="Chococat",
        description=(
            "A black cat with huge round chocolate-brown eyes, four whiskers, "
            "and a shiny black nose that can detect smells from miles away. "
            "Chococat uses the information his nose detects to help his friends "
            "get out of trouble. He is curious, spontaneous, and a little clumsy. "
            "His name combines chocolate (his eye color) and cat. "
            "Chococat was Sanrio's 1990s answer to the demand for a cool cat "
            "character alongside Hello Kitty."
        ),
        character_type="Sanrio character — black cat with big chocolate eyes",
        debut_year=1996,
        extra_creators=[],
        series_list=[
            Series("Chococat merchandise debut", 1996, None,
                "Sanrio Co., Ltd.", "merchandise"),
            Series("Chococat anime shorts", 2002, 2005,
                "Sanrio", "anime shorts"),
        ],
        eras=[
            Era(1996, None,
                "Classic design — solid black cat body, enormous round chocolate-brown eyes, "
                "four whiskers, simple cheerful design",
                art_style="Flat graphic illustration",
                image_url=IMG["chococat"],
                notes="Chococat's enormous eyes are his most distinctive feature. "
                    "He is one of the few Sanrio characters whose special ability "
                    "(super-sensitive nose) is a plot device in his stories."),
        ],
        wiki_slug="Chococat",
    )
    lib.add_cartoon(chococat)

    # ══════════════════════════════════════════════════════════════════════
    # TUXEDOSAM (1979)
    # ══════════════════════════════════════════════════════════════════════
    tuxedosam = _sanrio(
        name="Tuxedosam",
        description=(
            "A round blue and white penguin who always wears a formal bow tie "
            "— his name references both tuxedos and his penguin coloring. "
            "Tuxedosam lives in Antartica and loves to cook, especially "
            "hamburgers. He is one of Sanrio's oldest characters, debuting "
            "in 1979. He was particularly popular in the United States in the "
            "1980s and early 1990s, and experienced a significant revival "
            "in the 2020s as vintage Sanrio aesthetics returned to fashion."
        ),
        character_type="Sanrio character — blue penguin in bow tie",
        debut_year=1979,
        extra_creators=[],
        series_list=[
            Series("Tuxedosam merchandise debut", 1979, None,
                "Sanrio Co., Ltd.", "merchandise"),
        ],
        eras=[
            Era(1979, None,
                "Classic design — round blue-white penguin, red bow tie, small flippers, "
                "cheerful face",
                art_style="Flat graphic illustration",
                image_url=IMG["tuxedo"],
                notes="One of Sanrio's oldest surviving characters after Hello Kitty. "
                    "Tuxedosam's formal bow tie gives him a distinguished air unusual "
                    "among Sanrio's typically casual characters."),
        ],
        wiki_slug="Tuxedosam",
    )
    lib.add_cartoon(tuxedosam)

    # ══════════════════════════════════════════════════════════════════════
    # LITTLE TWIN STARS / KIKI AND LALA (1975)
    # ══════════════════════════════════════════════════════════════════════
    twin_stars = _sanrio(
        name="Little Twin Stars (Kiki and Lala)",
        description=(
            "Kiki (blue star boy) and Lala (pink star girl) — twin angels who "
            "live on a star in the Milky Way and came to Earth to find their dream. "
            "Kiki loves sports, reading, and building things. Lala loves cooking, "
            "drawing, and singing. Together they represent a dreamy pastel celestial "
            "world. The Little Twin Stars debuted in 1975 and are among Sanrio's "
            "most enduring classic characters, beloved for their soft rainbow "
            "pastel aesthetic and celestial mythology."
        ),
        character_type="Sanrio characters — twin angel star children",
        debut_year=1975,
        extra_creators=[Creator("Akiko Yazawa", "Little Twin Stars original designer", 0)],
        series_list=[
            Series("Little Twin Stars merchandise debut", 1975, None,
                "Sanrio Co., Ltd.", "merchandise"),
            Series("Kiki and Lala no Hoshi no Tabi anime", 1981, 1984,
                "Sanrio / Mushi Production", "anime film series", episode_count=3),
        ],
        eras=[
            Era(1975, None,
                "Classic design — Kiki in blue star motif, Lala in pink star motif, "
                "both with big rounded heads, star accessories, pastel rainbow palette",
                art_style="Soft pastel graphic illustration",
                image_url=IMG["little"],
                notes="Little Twin Stars are among Sanrio's oldest characters alongside Hello Kitty. "
                    "Their celestial star theme and soft pastel colors made them particularly "
                    "popular in the 1970s-80s and again during the pastel rainbow aesthetic revival of the 2010s-20s."),
        ],
        wiki_slug="Little_Twin_Stars",
    )
    lib.add_cartoon(twin_stars)

    # ══════════════════════════════════════════════════════════════════════
    # GUDETAMA (2013)
    # ══════════════════════════════════════════════════════════════════════
    gudetama = _sanrio(
        name="Gudetama",
        description=(
            "A lazy egg yolk who finds existence exhausting and would rather "
            "stay in bed (the egg white) than do anything at all. Gudetama's "
            "name combines gude gude (Japanese for lazy) and tamago (egg). "
            "Created in 2013 as the runner-up in a Sanrio character design contest "
            "(the winner was quickly forgotten; Gudetama became one of Sanrio's "
            "most successful characters ever). Gudetama's profound laziness and "
            "existential exhaustion resonated deeply with millennials and Gen Z "
            "who saw their own feelings reflected in an egg. "
            "A live-action/anime hybrid Netflix series aired in 2022."
        ),
        character_type="Sanrio character — lazy egg yolk / existential icon",
        debut_year=2013,
        extra_creators=[Creator("Amy Sato", "Gudetama character designer", 0)],
        series_list=[
            Series("Gudetama anime shorts", 2014, 2020,
                "Sanrio", "anime shorts / web series", episode_count=100,
                notes="Short-form anime featuring Gudetama's reluctant daily existence."),
            Series("Gudetama An Eggcellent Adventure (Netflix)", 2022, 2022,
                "Sanrio / Netflix", "streaming series", episode_count=10,
                notes="Live-action/anime hybrid Netflix series — Gudetama and a newly hatched chick "
                        "search for their mother. Critical darling for its absurdist comedy."),
        ],
        eras=[
            Era(2013, None,
                "Original design — pale yellow egg yolk with a tiny face and droopy eyes, "
                "perpetually slumped in the egg white, occasionally wearing the shell as a blanket",
                art_style="Flat digital illustration",
                image_url=IMG["gudetama"],
                notes="Created as a runner-up in a 2013 Sanrio character design contest. "
                    "The winning character is largely forgotten. "
                    "Gudetama became a global phenomenon beloved for its relatable apathy. "
                    "Featured in major marketing campaigns for McDonald's Japan and other brands."),
        ],
        wiki_slug="Gudetama",
    )
    lib.add_cartoon(gudetama)

    # ══════════════════════════════════════════════════════════════════════
    # AGGRETSUKO (2016)
    # ══════════════════════════════════════════════════════════════════════
    aggretsuko = _sanrio(
        name="Aggretsuko",
        description=(
            "Retsuko — a 25-year-old red panda who works a soul-crushing office job "
            "and copes with workplace frustration by secretly singing death metal "
            "karaoke after hours. Aggretsuko (combining aggressive and Retsuko) "
            "is Sanrio's most adult-oriented character and one of their most "
            "critically acclaimed. The Netflix animated series ran for five seasons "
            "and was praised for its honest portrayal of millennial work anxiety, "
            "toxic workplace dynamics, and the search for authenticity. "
            "A radical departure from Sanrio's typical kawaii formula."
        ),
        character_type="Sanrio character — red panda / office worker / death metal singer",
        debut_year=2016,
        extra_creators=[Creator("Yeti", "Aggretsuko character creator & series director", 0)],
        series_list=[
            Series("Aggretsuko TBS anime shorts", 2016, 2018,
                "Fanworks / TBS", "TV anime shorts", episode_count=100,
                notes="Original 1-minute shorts aired on TBS in Japan. "
                        "Each episode depicts a workplace frustration and karaoke release."),
            Series("Aggretsuko Netflix series", 2018, 2023,
                "Fanworks / Netflix", "streaming series", episode_count=50,
                notes="Five-season Netflix series expanding Retsuko's world dramatically. "
                        "Seasons 3-5 tackle increasingly mature themes including social media, "
                        "parasocial relationships, and career burnout. Won Annie Award nominations."),
        ],
        eras=[
            Era(2016, 2017,
                "Original TBS short format — simple character design, "
                "workplace comedy in 1-minute episodes",
                art_style="Simple digital animation for shorts",
                image_url=IMG["aggretsuko"],
                notes="The original TBS shorts established the core premise: "
                    "sweet exterior, death metal interior."),
            Era(2018, None,
                "Netflix expansion — same character with much deeper storytelling, "
                "complex relationships, mature workplace themes",
                art_style="Polished digital animation",
                image_url=IMG["aggretsuko"],
                notes="The Netflix series was Sanrio's most critically acclaimed animated production. "
                    "It addressed burnout, toxic masculinity, social media addiction, and "
                    "workplace harassment with surprising nuance for a Sanrio property."),
        ],
        wiki_slug="Aggretsuko",
    )
    lib.add_cartoon(aggretsuko)

    # ══════════════════════════════════════════════════════════════════════
    # HANGYODON (1985)
    # ══════════════════════════════════════════════════════════════════════
    hangyodon = _sanrio(
        name="Hangyodon",
        description=(
            "A creature that is half human, half fish — his name combines "
            "hangyo (half-fish in Japanese) and don (a suffix of endearment). "
            "Hangyodon lives in the sea and dreams of living on land. He is "
            "awkward, self-deprecating, and frequently unsuccessful at his goals — "
            "but endlessly optimistic. He experienced a massive global viral revival "
            "in 2020-2022 when social media users discovered the obscure character "
            "and fell in love with his relatable loser energy. "
            "One of Sanrio's most unexpected cult characters."
        ),
        character_type="Sanrio character — half fish half human / underdog",
        debut_year=1985,
        extra_creators=[],
        series_list=[
            Series("Hangyodon merchandise debut", 1985, None,
                "Sanrio Co., Ltd.", "merchandise"),
        ],
        eras=[
            Era(1985, 2019,
                "Classic obscure design — blue-green fish creature with human-like posture, "
                "rarely seen outside Japan",
                art_style="Flat graphic illustration",
                image_url=IMG["sanrio"],
                notes="Hangyodon was a minor Sanrio character for 35 years. "
                    "His obscurity became part of his appeal when he went viral."),
            Era(2020, None,
                "Viral revival era — same classic design embraced globally as "
                "relatable underdog, massive merchandise expansion",
                art_style="Digital illustration / merchandise revival",
                image_url=IMG["sanrio"],
                notes="Hangyodon went viral on TikTok and Twitter in 2020-2021. "
                    "Sanrio responded by dramatically expanding Hangyodon merchandise. "
                    "His comeback is one of the most unexpected in kawaii character history."),
        ],
        wiki_slug="Hangyodon",
    )
    lib.add_cartoon(hangyodon)

    # ══════════════════════════════════════════════════════════════════════
    # WISH ME MELL (1989 / revived 2013)
    # ══════════════════════════════════════════════════════════════════════
    wish_me_mell = _sanrio(
        name="Wish Me Mell",
        description=(
            "A white rabbit girl who loves making wishes come true for others. "
            "Wish Me Mell originally debuted in 1989 but was revived and redesigned "
            "in 2013 with a softer, more modern pastel aesthetic. She carries "
            "a magical four-leaf clover and lives in a meadow. "
            "She is known for her gentle, giving personality and her belief "
            "that wishes can come true through kindness."
        ),
        character_type="Sanrio character — white rabbit / wish-maker",
        debut_year=1989,
        extra_creators=[],
        series_list=[
            Series("Wish Me Mell merchandise debut", 1989, None,
                "Sanrio Co., Ltd.", "merchandise"),
            Series("Wish Me Mell revival merchandise", 2013, None,
                "Sanrio Co., Ltd.", "merchandise",
                notes="Redesigned with softer pastel aesthetic for modern audience."),
        ],
        eras=[
            Era(1989, 2012,
                "Original design — white rabbit with four-leaf clover motif, "
                "classic Sanrio illustration style",
                art_style="Flat graphic illustration",
                image_url=IMG["sanrio"],
                notes="Original Wish Me Mell debuted in 1989 as a minor Sanrio character."),
            Era(2013, None,
                "Revival design — softer pastel palette, more refined modern illustration, "
                "stronger personality and backstory",
                art_style="Modern digital pastel illustration",
                image_url=IMG["sanrio"],
                notes="The 2013 redesign gave Wish Me Mell a cleaner, more contemporary look "
                    "that resonated with the pastel kawaii aesthetic trend of the 2010s."),
        ],
        wiki_slug="Sanrio",
    )
    lib.add_cartoon(wish_me_mell)

    print(f"Sanrio characters added. Library now has {len(lib.cartoons)} cartoons total.")