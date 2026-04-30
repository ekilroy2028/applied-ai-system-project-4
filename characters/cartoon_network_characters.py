"""
cartoon_network_characters.py
Cartoon Network original animated characters for CartoonPal.

Cartoon Network launched October 1, 1992 as a Turner Broadcasting channel
showing classic cartoons. In 1994 it began producing original content under
the Cartoon Cartoons brand. After Warner Bros. acquired Turner in 1996,
Cartoon Network became part of Warner Bros. and ultimately Warner Bros. Discovery in 2022.

All Cartoon Network originals are owned by Warner Bros. Discovery.

NOTE: Teen Titans is already in wb_characters.py.
Batman: The Animated Series and other DCAU content is in wb_characters.py.

Usage:
    from characters.cartoon_network_characters import add_cartoon_network_characters
    add_cartoon_network_characters(lib)
"""

from cartoon_system import (
    Cartoon, Creator, ProductionCompany,
    Series, OwnershipRecord, Era, Library
)

CN_STUDIO = ProductionCompany("Cartoon Network Studios", 1994, country="USA", still_active=True)

CN_OWN = [
    ("Turner Broadcasting / Cartoon Network", 1992, 1996,
     "original creation — Turner founded Cartoon Network"),
    ("Time Warner / Warner Bros. / Cartoon Network", 1996, 2022,
     "Turner acquired by Time Warner / Warner Bros."),
    ("Warner Bros. Discovery", 2022, None,
     "Discovery merger with WarnerMedia"),
]

IMG = {
    "dexter":    "https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/Dexter%27s_Laboratory_title.png/240px-Dexter%27s_Laboratory_title.png",
    "ppg":       "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Powerpuff_Girls_logo.png/240px-Powerpuff_Girls_logo.png",
    "johnny":    "https://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Johnny_Bravo_title.png/200px-Johnny_Bravo_title.png",
    "courage":   "https://upload.wikimedia.org/wikipedia/en/thumb/6/6e/Courage_the_Cowardly_Dog.png/240px-Courage_the_Cowardly_Dog.png",
    "ed":        "https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/Ed_Edd_n_Eddy_title.png/240px-Ed_Edd_n_Eddy_title.png",
    "samurai":   "https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/Samurai_Jack_title_card.png/240px-Samurai_Jack_title_card.png",
    "foster":    "https://upload.wikimedia.org/wikipedia/en/thumb/4/4e/Foster%27s_Home_for_Imaginary_Friends_title.png/240px-Foster%27s_Home_for_Imaginary_Friends_title.png",
    "regular":   "https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/Regular_Show_title_card.png/240px-Regular_Show_title_card.png",
    "adventure": "https://upload.wikimedia.org/wikipedia/en/thumb/5/5a/Adventure_Time_-_Title_card.png/240px-Adventure_Time_-_Title_card.png",
    "steven":    "https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/Steven_Universe_title_card.png/240px-Steven_Universe_title_card.png",
    "gumball":   "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/The_Amazing_World_of_Gumball_title.png/240px-The_Amazing_World_of_Gumball_title.png",
    "bears":     "https://upload.wikimedia.org/wikipedia/en/thumb/3/3e/We_Bare_Bears_title_card.png/240px-We_Bare_Bears_title_card.png",
    "ok_ko":     "https://upload.wikimedia.org/wikipedia/en/thumb/4/4e/OK_K.O._Let%27s_Be_Heroes_title_card.png/240px-OK_K.O._Let%27s_Be_Heroes_title_card.png",
    "primal":    "https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/Primal_title_card.png/240px-Primal_title_card.png",
    "owl":       "https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/The_Owl_House_logo.png/240px-The_Owl_House_logo.png",
    "amphibia":  "https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/Amphibia_logo.png/240px-Amphibia_logo.png",
    "cn":        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Cartoon_Network_2010_logo.svg/240px-Cartoon_Network_2010_logo.svg.png",
    "infinity":  "https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/Infinity_Train_logo.png/240px-Infinity_Train_logo.png",
}


def _cn(name, description, character_type, debut_year,
        creators, series_list, eras, wiki_slug,
        origin="Burbank, California, USA — Cartoon Network Studios"):
    c = Cartoon(name=name, description=description,
                character_type=character_type,
                country_of_origin="USA", debut_year=debut_year)
    c.original_studio = CN_STUDIO
    for cr in creators:
        c.add_creator(cr)
    for s in series_list:
        c.add_series(s)
    for i, rec in enumerate(CN_OWN):
        is_cur = (i == len(CN_OWN) - 1)
        c.add_ownership_record(OwnershipRecord(
            rec[0], rec[1], rec[2], rec[3], is_current_owner=is_cur))
    for era in eras:
        c.add_era(era)
    c.wiki_url = f"https://en.wikipedia.org/wiki/{wiki_slug}"
    c.origin_location = origin
    return c


def add_cartoon_network_characters(lib: Library):

    # ── Dexter's Laboratory (1996) ────────────────────────────────────────
    dexter = _cn(
        name="Dexter's Laboratory",
        description=(
            "Dexter — a boy genius with a secret laboratory hidden behind his "
            "bookshelf — conducts elaborate scientific experiments that are "
            "constantly destroyed by his bubbly, well-meaning sister Dee Dee "
            "who loves to ruin everything he builds. "
            "Created by Genndy Tartakovsky, Dexter's Laboratory was Cartoon "
            "Network's first major original hit and launched one of animation's "
            "greatest directorial careers. Dexter speaks with an inexplicable "
            "Eastern European accent despite his completely American family — "
            "a joke the show never explains."
        ),
        character_type="Human — boy genius / secret laboratory / sister nemesis",
        debut_year=1996,
        creators=[Creator("Genndy Tartakovsky", "Series creator — also created Samurai Jack, Clone Wars, and Primal", 1970)],
        series_list=[
            Series("Dexter's Laboratory What a Cartoon shorts", 1995, 1996,
                   "Cartoon Network Studios", "animated shorts",
                   notes="Debuted as shorts on the What a Cartoon! showcase before the full series."),
            Series("Dexter's Laboratory original run", 1996, 1999,
                   "Cartoon Network Studios", "TV series", episode_count=52,
                   notes="Genndy Tartakovsky's original 2-season run. Considered the creative peak."),
            Series("Dexter's Laboratory revival seasons", 2001, 2003,
                   "Cartoon Network Studios", "TV series", episode_count=26,
                   notes="Produced without Tartakovsky. Generally considered inferior to original."),
        ],
        eras=[
            Era(1996, 1999,
                "Tartakovsky original — thick outlines, bold flat colors, "
                "cinematic timing, inexplicable Eastern European accent",
                art_style="Flat color digital animation — bold graphic style",
                image_url=IMG["dexter"],
                notes="Debuted April 28 1996. Tartakovsky left after Season 2. "
                      "The original run is considered a masterpiece of animated comedy timing. "
                      "Dee Dee's catchphrase Ooh what does this button do? became iconic."),
            Era(2001, 2003,
                "Revival without Tartakovsky — same characters, different creative team",
                art_style="Flat color digital animation",
                image_url=IMG["dexter"],
                notes="The revival seasons are generally considered inferior to the original. "
                      "Tartakovsky had moved on to Samurai Jack by this point."),
        ],
        wiki_slug="Dexter%27s_Laboratory",
    )
    lib.add_cartoon(dexter)

    # ── The Powerpuff Girls (1998) ─────────────────────────────────────────
    ppg = _cn(
        name="The Powerpuff Girls",
        description=(
            "Blossom (the leader), Bubbles (the joy), and Buttercup (the toughness) — "
            "three kindergarteners created from sugar, spice, everything nice, "
            "and the accidental Chemical X — who protect the city of Townsville "
            "from villains including Mojo Jojo, Him, Fuzzy Lumpkins, and the Gangreen Gang. "
            "Created by Craig McCracken, The Powerpuff Girls was a deliberate "
            "subversion of superhero tropes — the most powerful heroes in Townsville "
            "are kindergarteners in pastel dresses. "
            "Became one of Cartoon Network's most successful franchises globally."
        ),
        character_type="Human / superhero — kindergartener crime-fighters / Townsville protectors",
        debut_year=1998,
        creators=[Creator("Craig McCracken", "Series creator — also created Foster's Home for Imaginary Friends", 1971)],
        series_list=[
            Series("Powerpuff Girls What a Cartoon shorts", 1995, 1997,
                   "Cartoon Network Studios", "animated shorts",
                   notes="Originally titled Whoopass Stew! — Craig McCracken's student film concept."),
            Series("The Powerpuff Girls original series", 1998, 2005,
                   "Cartoon Network Studios", "TV series", episode_count=78,
                   notes="Debuted November 18 1998. Ran for 6 seasons."),
            Series("The Powerpuff Girls Movie", 2002, 2002,
                   "Warner Bros. Pictures / Cartoon Network Movies", "theatrical feature"),
            Series("The Powerpuff Girls 2016 reboot", 2016, 2019,
                   "Cartoon Network Studios", "TV series", episode_count=96,
                   notes="New voice cast, updated designs. Mixed reception from fans of original."),
            Series("Powerpuff Girls live-action CW pilot", 2021, 2021,
                   "The CW / Warner Bros. Television", "TV pilot",
                   notes="Live-action pilot not picked up to series."),
        ],
        eras=[
            Era(1998, 2005,
                "Original series — round-headed girls with huge eyes and no fingers, "
                "primary color dresses, Townsville setting, Professor Utonium",
                art_style="Flat color digital animation — bold graphic design",
                image_url=IMG["ppg"],
                notes="Craig McCracken created the show from his student film Whoopass Stew! "
                      "The Powerpuff Girls was influential for centering female superheroes "
                      "in a genre dominated by male characters. "
                      "Mojo Jojo's elaborate speech patterns became a pop culture reference."),
            Era(2016, None,
                "Reboot era — updated designs, new voice cast, more contemporary references",
                art_style="Updated digital animation",
                image_url=IMG["ppg"],
                notes="The 2016 reboot received mixed reception. "
                      "The original voice actresses were not brought back, "
                      "which disappointed many fans."),
        ],
        wiki_slug="The_Powerpuff_Girls",
    )
    lib.add_cartoon(ppg)

    # ── Johnny Bravo (1997) ────────────────────────────────────────────────
    johnny_bravo = _cn(
        name="Johnny Bravo",
        description=(
            "Johnny Bravo — a massively muscled, elaborately coiffed, dim-witted "
            "young man who constantly attempts to impress women and invariably fails "
            "spectacularly. A parody of 1950s rock-and-roll machismo — Elvis hair, "
            "Schwarzenegger physique, and the unshakeable confidence of someone "
            "who has never processed a single rejection. "
            "Created by Van Partible, Johnny Bravo was one of Cartoon Network's "
            "earliest original hits and is notable for its celebrity guest appearances "
            "including Donny Osmond, Adam West, and Farrah Fawcett."
        ),
        character_type="Human — dim-witted muscular pretty boy / 1950s machismo parody",
        debut_year=1997,
        creators=[Creator("Van Partible", "Series creator", 1973)],
        series_list=[
            Series("Johnny Bravo What a Cartoon short", 1997, 1997,
                   "Cartoon Network Studios", "animated short",
                   notes="Debuted on the What a Cartoon! showcase."),
            Series("Johnny Bravo", 1997, 2004,
                   "Cartoon Network Studios", "TV series", episode_count=67,
                   notes="Debuted July 7 1997. 4 seasons."),
        ],
        eras=[
            Era(1997, 2004,
                "Blonde Elvis-haired bodybuilder in tight black shirt, "
                "mirror-gazing, perpetually unsuccessful with women",
                art_style="Flat color digital animation",
                image_url=IMG["johnny"],
                notes="Van Partible based Johnny on 1950s rock-and-roll culture "
                      "and bodybuilder stereotypes. "
                      "The show was notable for A-list celebrity guest appearances. "
                      "Johnny's catchphrase Do the monkey with me! became well-known."),
        ],
        wiki_slug="Johnny_Bravo",
    )
    lib.add_cartoon(johnny_bravo)

    # ── Courage the Cowardly Dog (1999) ───────────────────────────────────
    courage = _cn(
        name="Courage the Cowardly Dog",
        description=(
            "Courage — a timid pink dog — lives with elderly couple Muriel and "
            "Eustace Bagge in the middle of Nowhere (literally — the town is called "
            "Nowhere, Kansas) and must repeatedly save them from supernatural horrors "
            "despite being terrified of absolutely everything. "
            "Created by John R. Dilworth, Courage the Cowardly Dog is one of the "
            "most genuinely frightening children's cartoons ever produced — its "
            "surreal horror imagery and unsettling computer-generated nightmare "
            "sequences traumatized and delighted an entire generation. "
            "King Ramses' Curse is legendary for its uncanny CGI villain."
        ),
        character_type="Anthropomorphic animal — cowardly dog / horror comedy / Nowhere Kansas",
        debut_year=1999,
        creators=[Creator("John R. Dilworth", "Series creator", 1960)],
        series_list=[
            Series("The Chicken from Outer Space What a Cartoon short", 1995, 1995,
                   "Cartoon Network Studios", "animated short",
                   notes="Academy Award-nominated short that introduced Courage."),
            Series("Courage the Cowardly Dog", 1999, 2002,
                   "Cartoon Network Studios", "TV series", episode_count=52,
                   notes="Debuted November 12 1999. 4 seasons."),
            Series("The Fog of Courage short film", 2014, 2014,
                   "Cartoon Network Studios", "CGI short film"),
        ],
        eras=[
            Era(1999, 2002,
                "Original series — pink dog in the middle of nowhere, "
                "genuinely disturbing horror imagery, surrealist nightmare fuel, "
                "memorable CGI villain sequences",
                art_style="Hand-drawn with CGI horror elements",
                image_url=IMG["courage"],
                notes="Debuted November 12 1999. The episodes King Ramses' Curse, "
                      "The Tower of Dr. Zalost, and Perfect are legendary for their "
                      "nightmare-inducing imagery. "
                      "Courage's owner Muriel was one of animation's most beloved "
                      "gentle characters. Eustace Bagge remains one of animation's "
                      "great lovable grumps."),
        ],
        wiki_slug="Courage_the_Cowardly_Dog",
    )
    lib.add_cartoon(courage)

    # ── Ed, Edd n Eddy (1999) ─────────────────────────────────────────────
    ed_edd_eddy = _cn(
        name="Ed, Edd n Eddy",
        description=(
            "Three boys named Ed (dim but lovable), Edd/Double D (neat and nervous), "
            "and Eddy (scheming and short) who live in a suburban cul-de-sac and "
            "constantly run scams to earn quarters to buy jawbreakers — invariably "
            "failing and being beaten up by the other neighborhood kids. "
            "Created by Danny Antonucci and produced in Canada, Ed, Edd n Eddy "
            "was the longest-running Cartoon Network original series (1999-2009) "
            "and the only original Cartoon Cartoon to span the network's entire "
            "first creative era. Its deliberate retro aesthetic — no cell phones, "
            "no internet — gave it a timeless quality."
        ),
        character_type="Human — suburban scammer trio / jawbreaker obsession",
        debut_year=1999,
        creators=[Creator("Danny Antonucci", "Series creator — previously made adult animation", 1957)],
        series_list=[
            Series("Ed Edd n Eddy", 1999, 2009,
                   "a.k.a. Cartoon Studio / Cartoon Network", "TV series", episode_count=68,
                   notes="Debuted January 4 1999. 6 seasons over 10 years. "
                         "Produced in Canada by Danny Antonucci's studio a.k.a. Cartoon Studio."),
            Series("Ed Edd n Eddy's Big Picture Show", 2009, 2009,
                   "Cartoon Network Studios", "TV movie",
                   notes="Series finale movie. Revealed Eddy's brother and gave the show "
                         "a beloved proper conclusion. Widely praised by fans."),
        ],
        eras=[
            Era(1999, 2009,
                "10-year original run — rubbery hand-drawn style with wobbly lines, "
                "retro 1950s-60s aesthetic, suburban cul-de-sac, no adults clearly shown",
                art_style="Hand-drawn animation with rubber hose elements and squiggly lines",
                image_url=IMG["ed"],
                notes="Ed Edd n Eddy was produced in Canada — unusual for CN at the time. "
                      "The show's deliberate retro aesthetic included no cell phones or internet. "
                      "The Big Picture Show finale (2009) was deeply satisfying for long-time fans — "
                      "revealing Eddy's brother and showing the kids accept the Eds at last."),
        ],
        wiki_slug="Ed,_Edd_n_Eddy",
    )
    lib.add_cartoon(ed_edd_eddy)

    # ── Samurai Jack (2001) ────────────────────────────────────────────────
    samurai_jack = _cn(
        name="Samurai Jack",
        description=(
            "A Japanese samurai prince hurled into the far future by the shape-shifting "
            "demon Aku — where Aku rules a dystopian world — who must find a time "
            "portal to return and prevent Aku from ever taking over. Known only as Jack, "
            "he wanders a strange futuristic landscape battling Aku's bounty hunters "
            "and alien forces. Created by Genndy Tartakovsky, Samurai Jack is one of "
            "the most visually stunning animated series ever made — cinematic compositions "
            "influenced by Kurosawa, minimal dialogue, and extraordinary action sequences. "
            "Left unfinished for 13 years before Adult Swim gave it a proper finale."
        ),
        character_type="Human — time-displaced samurai / lone warrior against Aku",
        debut_year=2001,
        creators=[Creator("Genndy Tartakovsky", "Series creator", 1970)],
        series_list=[
            Series("Samurai Jack original CN run", 2001, 2004,
                   "Cartoon Network Studios", "TV series", episode_count=52,
                   notes="Debuted August 10 2001. Won 4 Emmy Awards. "
                         "Ended without resolution after Season 4."),
            Series("Samurai Jack Season 5 Adult Swim revival", 2017, 2017,
                   "Cartoon Network Studios / Adult Swim", "TV series", episode_count=10,
                   notes="13-year-later revival with TV-14 rating on Adult Swim. "
                         "Phil LaMarr returned. Finally gave Jack his ending."),
        ],
        eras=[
            Era(2001, 2004,
                "Original CN run — widescreen cinematic compositions, "
                "Kurosawa and UPA graphic art influences, minimal dialogue, "
                "extraordinary action animation",
                art_style="Graphic limited animation — UPA, Kurosawa, and anime influenced",
                image_url=IMG["samurai"],
                notes="Tartakovsky used cinema language in TV animation — widescreen frames, "
                      "long silent sequences, bold graphic compositions. "
                      "Won 4 Emmy Awards. Ended abruptly without resolution."),
            Era(2017, None,
                "Adult Swim Season 5 — older Jack in darker world, "
                "TV-14 rating, blood shown for first time, proper finale",
                art_style="Updated version of original graphic style",
                image_url=IMG["samurai"],
                notes="The Adult Swim revival is widely considered one of the greatest "
                      "animated revivals ever produced. "
                      "The ending divided fans but gave the series a definitive conclusion "
                      "after 13 years of waiting."),
        ],
        wiki_slug="Samurai_Jack",
    )
    lib.add_cartoon(samurai_jack)

    # ── Foster's Home for Imaginary Friends (2004) ─────────────────────────
    fosters = _cn(
        name="Foster's Home for Imaginary Friends",
        description=(
            "Mac — an 8-year-old boy whose imaginary friend Bloo must move to "
            "Foster's Home for Imaginary Friends (a Victorian mansion where outgrown "
            "imaginary friends live until adopted by new children) when Mac's mother "
            "says he's too old for imaginary friends. Mac visits Bloo every day. "
            "Created by Craig McCracken, Foster's Home featured extraordinary creative "
            "freedom — any imaginable character design could appear as an imaginary friend — "
            "and dealt with themes of friendship, growing up, and letting go."
        ),
        character_type="Human / imaginary — boy and his imaginary friend / found family",
        debut_year=2004,
        creators=[Creator("Craig McCracken", "Series creator", 1971)],
        series_list=[
            Series("Foster's Home for Imaginary Friends", 2004, 2009,
                   "Cartoon Network Studios", "TV series", episode_count=79,
                   notes="Debuted August 13 2004. 6 seasons."),
            Series("Foster's Home for Imaginary Friends Good Wilt Hunting", 2006, 2006,
                   "Cartoon Network Studios", "TV movie",
                   notes="Feature-length TV movie following Wilt's origin story."),
        ],
        eras=[
            Era(2004, 2009,
                "Mac in red jacket, Bloo as a blue blob, Wilt, Eduardo, Coco, "
                "Mr. Herriman running Foster's mansion",
                art_style="Flat color digital animation",
                image_url=IMG["foster"],
                notes="Debuted August 13 2004. Craig McCracken's follow-up to Powerpuff Girls. "
                      "The premise — a retirement home for outgrown imaginary friends — "
                      "allowed unlimited character creativity. "
                      "Cheese (introduced in Season 2) became a fan favorite despite being "
                      "one of the most irritating characters ever created."),
        ],
        wiki_slug="Foster%27s_Home_for_Imaginary_Friends",
    )
    lib.add_cartoon(fosters)

    # ── Regular Show (2010) ────────────────────────────────────────────────
    regular_show = _cn(
        name="Regular Show",
        description=(
            "Mordecai (a blue jay) and Rigby (a raccoon) — two slacker groundskeepers "
            "at a park run by their boss Benson (a living gumball machine) — whose "
            "attempts to avoid work invariably escalate into supernatural, apocalyptic "
            "or time-traveling adventures. Created by J.G. Quintel, Regular Show was "
            "deceptively simple — a show about slackers at work that regularly featured "
            "cosmic villains, death battles, and existential threats. "
            "Won six Emmy Awards. 261 episodes over 8 seasons."
        ),
        character_type="Anthropomorphic animals — blue jay and raccoon slackers / supernatural adventures",
        debut_year=2010,
        creators=[Creator("J.G. Quintel", "Series creator — based on his CalArts thesis film", 1982)],
        series_list=[
            Series("Regular Show", 2010, 2017,
                   "Cartoon Network Studios", "TV series", episode_count=261,
                   notes="Debuted September 6 2010. 8 seasons. Won 6 Emmy Awards."),
            Series("Regular Show The Movie", 2015, 2015,
                   "Cartoon Network Studios", "TV movie"),
        ],
        eras=[
            Era(2010, 2017,
                "Original run — mundane premise escalating to cosmic stakes, "
                "Mordecai and Rigby vs. the universe, Benson's endless frustration",
                art_style="Flat color digital animation",
                image_url=IMG["regular"],
                notes="Debuted September 6 2010. J.G. Quintel voiced Mordecai himself. "
                      "The show's formula — slackers encounter something weird, "
                      "it escalates to world-ending stakes, they barely survive — "
                      "was executed with remarkable consistency for 8 seasons. "
                      "The final season sent the park crew into space."),
        ],
        wiki_slug="Regular_Show",
    )
    lib.add_cartoon(regular_show)

    # ── Adventure Time (2010) ─────────────────────────────────────────────
    adventure_time = _cn(
        name="Adventure Time",
        description=(
            "Finn the Human — the only human in the post-apocalyptic Land of Ooo — "
            "and his magical shape-shifting dog Jake go on adventures in a world "
            "rebuilt after a nuclear catastrophe called the Mushroom War. "
            "Created by Pendleton Ward, Adventure Time began as absurdist comedy "
            "but evolved into one of the most emotionally complex animated series "
            "ever made — exploring trauma, mortality, identity, love, and cosmic "
            "horror beneath its candy-colored surface. "
            "The Lich remains one of animation's most genuinely terrifying villains."
        ),
        character_type="Human / magical dog — post-apocalyptic adventurers / emotional depth",
        debut_year=2010,
        creators=[Creator("Pendleton Ward", "Series creator", 1982)],
        series_list=[
            Series("Adventure Time", 2010, 2018,
                   "Cartoon Network Studios", "TV series", episode_count=283,
                   notes="Debuted April 5 2010. 10 seasons. 283 episodes."),
            Series("Adventure Time Distant Lands HBO Max specials", 2020, 2021,
                   "Cartoon Network Studios / HBO Max", "streaming specials", episode_count=4),
            Series("Adventure Time Fionna and Cake HBO Max series", 2023, None,
                   "Cartoon Network Studios / HBO Max", "streaming series",
                   notes="Gender-swapped alternate universe characters from the show's mythology."),
        ],
        eras=[
            Era(2010, 2014,
                "Early era — absurdist adventure comedy, candy-colored world, "
                "mathematical! catchphrase, Finn and Jake friendship",
                art_style="Flat color digital animation with hand-drawn warmth",
                image_url=IMG["adventure"],
                notes="Debuted April 5 2010. Adventure Time's mythology — the Mushroom War, "
                      "the Lich, the cosmic horror beneath the candy surface — "
                      "was built gradually across years of episodes."),
            Era(2015, 2018,
                "Mature era — Finn aging, losing his arm, cosmic horror fully revealed, "
                "Islands miniseries, Stakes miniseries, emotional complexity at peak",
                art_style="Flat color digital animation",
                image_url=IMG["adventure"],
                notes="The final seasons dealt with aging, legacy, death, and cosmic existential themes. "
                      "Come Along With Me (the finale) was widely praised. "
                      "The Lich's monologue in The Lich episode is one of animation's "
                      "most genuinely frightening moments."),
            Era(2020, None,
                "HBO Max continuation — Distant Lands specials expanding supporting characters, "
                "Fionna and Cake series exploring the alternate universe",
                art_style="Updated digital animation",
                image_url=IMG["adventure"],
                notes="Distant Lands gave BMO, Obsidian (Marceline and PB), "
                      "Wizard City, and Together Again their own specials. "
                      "Fionna and Cake explored themes of escapism and fan fiction."),
        ],
        wiki_slug="Adventure_Time",
    )
    lib.add_cartoon(adventure_time)

    # ── Steven Universe (2013) ─────────────────────────────────────────────
    steven_universe = _cn(
        name="Steven Universe",
        description=(
            "Steven Universe — a half-human half-Crystal Gem boy — grows up alongside "
            "the Crystal Gems (Garnet, Amethyst, and Pearl) in Beach City while "
            "uncovering the truth about his mother Rose Quartz and his own identity. "
            "Created by Rebecca Sugar — the first woman to solely create a Cartoon "
            "Network series — Steven Universe was a landmark for LGBTQ+ representation "
            "in animation. Garnet was revealed to be a fusion of two gems in love "
            "(Ruby and Sapphire) — the first same-sex couple depicted onscreen "
            "in a Cartoon Network series."
        ),
        character_type="Human / gem hybrid — Crystal Gem warrior / self-discovery",
        debut_year=2013,
        creators=[Creator("Rebecca Sugar", "Series creator — first woman to solely create a CN series, non-binary", 1987)],
        series_list=[
            Series("Steven Universe", 2013, 2019,
                   "Cartoon Network Studios", "TV series", episode_count=160,
                   notes="Debuted November 4 2013. 5 seasons."),
            Series("Steven Universe The Movie", 2019, 2019,
                   "Cartoon Network Studios", "TV movie",
                   notes="Musical movie set two years after the series. Spinel introduced."),
            Series("Steven Universe Future limited series", 2019, 2020,
                   "Cartoon Network Studios", "TV series", episode_count=20,
                   notes="Epilogue series dealing with Steven's PTSD and identity post-war."),
        ],
        eras=[
            Era(2013, 2019,
                "Original series — Steven in pink star shirt, Crystal Gems as found family, "
                "Beach City slice-of-life mixed with cosmic Gem War stakes",
                art_style="Flat color digital animation with watercolor-influenced backgrounds",
                image_url=IMG["steven"],
                notes="Debuted November 4 2013. Rebecca Sugar confirmed as non-binary in 2020. "
                      "Ruby and Sapphire's relationship was the first same-sex couple shown onscreen on CN. "
                      "The show handled abusive relationships, trauma, and grief with extraordinary nuance."),
            Era(2019, None,
                "Movie and Future era — post-war Steven dealing with PTSD, "
                "psychological complexity rarely seen in animated TV",
                art_style="Updated digital animation",
                image_url=IMG["steven"],
                notes="Steven Universe Future dealt with PTSD and the cost of always being "
                      "the savior — genuinely unusual psychological territory for animation. "
                      "The finale showed Steven choosing to get help rather than sacrifice himself."),
        ],
        wiki_slug="Steven_Universe",
    )
    lib.add_cartoon(steven_universe)

    # ── The Amazing World of Gumball (2011) ────────────────────────────────
    gumball = _cn(
        name="The Amazing World of Gumball",
        description=(
            "Gumball Watterson — a blue cat — lives in Elmore with his goldfish "
            "brother Darwin, sister Anais, and parents Nicole and Richard. "
            "The show's defining feature is its revolutionary mixed-media approach — "
            "characters rendered in 2D, 3D CGI, stop-motion, live-action puppets, "
            "and pixelated sprites coexist in the same world and same episode. "
            "Created by Ben Bocquelet for Cartoon Network Europe, Gumball won "
            "multiple BAFTA and Annie Awards and became increasingly meta "
            "and self-aware as it progressed."
        ),
        character_type="Anthropomorphic animal — blue cat / mixed-media family comedy",
        debut_year=2011,
        creators=[Creator("Ben Bocquelet", "Series creator — Cartoon Network Europe development", 1983)],
        series_list=[
            Series("The Amazing World of Gumball", 2011, 2019,
                   "Cartoon Network Studios Europe", "TV series", episode_count=240,
                   notes="Debuted May 3 2011. 6 seasons. "
                         "Produced at Cartoon Network's UK/European studio."),
            Series("The Amazing World of Gumball The Movie", 2024, None,
                   "Cartoon Network Studios / Max", "streaming feature",
                   notes="Long-awaited movie conclusion announced for Max streaming."),
        ],
        eras=[
            Era(2011, 2019,
                "Original series — mixed-media world where 2D, CGI, stop-motion "
                "and live-action characters interact naturally",
                art_style="Mixed media — 2D, CGI, stop-motion, live-action backgrounds",
                image_url=IMG["gumball"],
                notes="Debuted May 3 2011. The mixed-media approach was genuinely revolutionary — "
                      "characters in completely different art styles shared single frames. "
                      "Won 2 BAFTAs and 3 Annie Awards. "
                      "The show grew increasingly self-aware about being a cartoon "
                      "in its later seasons."),
            Era(2024, None,
                "Movie continuation on Max",
                art_style="Mixed media updated",
                image_url=IMG["gumball"],
                notes="The long-awaited movie was announced to give the series a proper conclusion."),
        ],
        wiki_slug="The_Amazing_World_of_Gumball",
    )
    lib.add_cartoon(gumball)

    # ── We Bare Bears (2015) ──────────────────────────────────────────────
    we_bare_bears = _cn(
        name="We Bare Bears",
        description=(
            "Three bear brothers — Grizzly (social and enthusiastic), Panda "
            "(anxious and internet-obsessed), and Ice Bear (stoic, multilingual, "
            "and mysterious) — attempt to integrate into modern human society "
            "in the San Francisco Bay Area with limited success. "
            "Created by Daniel Chong based on his webcomic, We Bare Bears was "
            "notable for its diverse cast, gentle humor, and touching examination "
            "of what it means to be an outsider trying to belong. "
            "Resonated strongly with Asian-American viewers."
        ),
        character_type="Anthropomorphic animals — three bear brothers / belonging and modern life",
        debut_year=2015,
        creators=[Creator("Daniel Chong", "Series creator — based on his webcomic The Three Bare Bears", 0)],
        series_list=[
            Series("We Bare Bears", 2015, 2019,
                   "Cartoon Network Studios", "TV series", episode_count=140,
                   notes="Debuted July 27 2015. 4 seasons."),
            Series("We Bare Bears The Movie", 2020, 2020,
                   "Cartoon Network Studios", "streaming feature",
                   notes="Series finale movie. The bears must flee to Canada to escape ICE detention."),
            Series("We Baby Bears spinoff", 2021, None,
                   "Cartoon Network Studios", "TV series",
                   notes="CGI prequel showing the bears as babies adventuring through different worlds."),
        ],
        eras=[
            Era(2015, 2019,
                "Original series — bears stacking in signature vertical pile, "
                "Bay Area setting, food obsession, social media anxiety",
                art_style="Flat color digital animation",
                image_url=IMG["bears"],
                notes="Debuted July 27 2015. We Bare Bears featured one of CN's "
                      "most diverse voice and writing casts. "
                      "The bears' attempts to fit into human society by stacking "
                      "on top of each other became iconic. "
                      "The movie's plot — immigration authorities chasing the bears — "
                      "was surprisingly politically bold."),
            Era(2020, None,
                "Movie and We Baby Bears spinoff era",
                art_style="CGI for spinoff / digital for movie",
                image_url=IMG["bears"],
                notes="The movie gave the series a meaningful ending. "
                      "We Baby Bears took the characters to a CGI format."),
        ],
        wiki_slug="We_Bare_Bears",
    )
    lib.add_cartoon(we_bare_bears)

    # ── Infinity Train (2019) ─────────────────────────────────────────────
    infinity_train = _cn(
        name="Infinity Train",
        description=(
            "A mysterious train of infinite cars — each containing its own world — "
            "that picks up people who have unresolved problems in their lives. "
            "Passengers must solve their personal issues to decrease the number "
            "on their hand and eventually find the exit. Each of the four books "
            "follows a different protagonist on the same train. "
            "Created by Owen Dennis, Infinity Train is one of the most inventive "
            "and emotionally sophisticated animated series of the 2010s — "
            "cancelled by HBO Max in 2021 before completion."
        ),
        character_type="Human — anthology passengers on mysterious infinite train",
        debut_year=2019,
        creators=[Creator("Owen Dennis", "Series creator", 0)],
        series_list=[
            Series("Infinity Train Book 1 Tulip's Odyssey", 2019, 2019,
                   "Cartoon Network Studios", "TV series", episode_count=10),
            Series("Infinity Train Book 2 Cracked Reflection", 2020, 2020,
                   "Cartoon Network Studios", "TV series", episode_count=10),
            Series("Infinity Train Book 3 Cult of the Conductor", 2020, 2020,
                   "Cartoon Network Studios / HBO Max", "streaming series", episode_count=10),
            Series("Infinity Train Book 4 Dueling Mirrors", 2021, 2021,
                   "Cartoon Network Studios / HBO Max", "streaming series", episode_count=10,
                   notes="Final book. Series cancelled by HBO Max before planned continuation."),
        ],
        eras=[
            Era(2019, 2021,
                "Four books following different passengers — Tulip, MT, Grace, "
                "and Ryan and Min-Gi — on the mysterious infinite train",
                art_style="Flat color digital animation",
                image_url=IMG["infinity"],
                notes="Owen Dennis created Infinity Train as a pilot in 2016 that went viral. "
                      "Each book could be watched independently. "
                      "The show was cancelled by HBO Max in 2021 — "
                      "one of the most mourned cancellations in recent animation history."),
        ],
        wiki_slug="Infinity_Train",
    )
    lib.add_cartoon(infinity_train)

    # ── Primal (2019) ─────────────────────────────────────────────────────
    primal = _cn(
        name="Primal",
        description=(
            "A caveman named Spear and a Tyrannosaurus Rex named Fang — both "
            "having lost their families to predators — form an unlikely partnership "
            "to survive in a brutal prehistoric world. "
            "Created by Genndy Tartakovsky, Primal has no dialogue — "
            "it communicates entirely through action, expression, and sound. "
            "It won the Emmy Award for Outstanding Animated Program in 2020 and 2022 — "
            "making Tartakovsky the only person to win that award for three different series "
            "(also Samurai Jack and Star Wars: Clone Wars)."
        ),
        character_type="Human / animal — caveman and dinosaur / wordless survival bond",
        debut_year=2019,
        creators=[Creator("Genndy Tartakovsky", "Series creator", 1970)],
        series_list=[
            Series("Primal Season 1", 2019, 2020,
                   "Cartoon Network Studios / Adult Swim", "TV series", episode_count=10,
                   notes="Won Emmy Award for Outstanding Animated Program 2020."),
            Series("Primal Season 2", 2022, 2023,
                   "Cartoon Network Studios / Adult Swim", "TV series", episode_count=10,
                   notes="Won Emmy Award for Outstanding Animated Program 2022."),
        ],
        eras=[
            Era(2019, None,
                "No dialogue — pure visual storytelling, brutal prehistoric world, "
                "Spear the caveman and Fang the T-Rex",
                art_style="Fluid detailed hand-drawn animation — Tartakovsky's most technically accomplished work",
                image_url=IMG["primal"],
                notes="Primal debuted October 7 2019. The complete absence of dialogue "
                      "is the show's boldest creative choice — and its greatest strength. "
                      "Tartakovsky's third Emmy Award for Outstanding Animated Program "
                      "made him the record holder in that category."),
        ],
        wiki_slug="Primal_(TV_series)",
    )
    lib.add_cartoon(primal)

    # ── OK K.O.! Let's Be Heroes (2017) ──────────────────────────────────
    ok_ko = _cn(
        name="OK K.O.! Let's Be Heroes",
        description=(
            "K.O. — an enthusiastic young boy working at Gar's Bodega in Lakewood "
            "Plaza Turbo — dreams of becoming a great hero while battling the "
            "villainous Lord Boxman and his robot army. Created by Ian Jones-Quartey, "
            "OK K.O. was a love letter to 1980s anime, fighting games, and superhero "
            "culture — filled with callbacks, crossovers, and genuine heart. "
            "Notable for crossing over with Steven Universe, Regular Show, "
            "and multiple other CN properties."
        ),
        character_type="Human — enthusiastic young hero / bodega worker",
        debut_year=2017,
        creators=[Creator("Ian Jones-Quartey", "Series creator — previously worked on Steven Universe", 0)],
        series_list=[
            Series("OK K.O. Let's Be Heroes", 2017, 2019,
                   "Cartoon Network Studios", "TV series", episode_count=119,
                   notes="Debuted August 1 2017. 3 seasons."),
        ],
        eras=[
            Era(2017, 2019,
                "Anime-influenced superhero comedy — K.O. leveling up, "
                "Gar's Bodega crew, Lord Boxman's robots",
                art_style="Anime-influenced flat color digital animation",
                image_url=IMG["ok_ko"],
                notes="Ian Jones-Quartey worked on Steven Universe before creating OK K.O. "
                      "The show featured crossovers with Steven Universe, Regular Show, "
                      "and even Street Fighter characters. "
                      "Its cancellation before planned story completion disappointed fans."),
        ],
        wiki_slug="OK_K.O.!_Let%27s_Be_Heroes",
    )
    lib.add_cartoon(ok_ko)

    # ── The Owl House (2020) ─────────────────────────────────────────────
    owl_house = _cn(
        name="The Owl House",
        description=(
            "Luz Noceda — a Dominican-American teenage girl — accidentally ends up "
            "in the Boiling Isles, a magical demon realm, where she becomes the "
            "apprentice of the rebellious witch Eda Clawthorne and befriends the "
            "tiny demon King. Created by Dana Terrace, The Owl House made history "
            "as the first Disney Channel animated series to feature a bisexual "
            "lead character — Luz's bisexuality is confirmed on-screen. "
            "The show was controversially shortened by Disney from its planned run "
            "despite critical acclaim and audience enthusiasm."
        ),
        character_type="Human — teenage girl in magical demon realm / witch apprentice",
        debut_year=2020,
        creators=[Creator("Dana Terrace", "Series creator", 1990)],
        series_list=[
            Series("The Owl House", 2020, 2023,
                   "Disney Television Animation", "TV series", episode_count=40,
                   notes="Debuted January 10 2020. Originally planned for more episodes — "
                         "Disney shortened the series to three 45-minute specials for Season 3."),
        ],
        eras=[
            Era(2020, 2023,
                "Luz in the Boiling Isles — glyphs magic system, Eda the Owl Lady, "
                "King the Titan, Emperor Belos as villain",
                art_style="Flat color digital animation with dark fantasy aesthetic",
                image_url=IMG["owl"],
                notes="The Owl House is a Disney Channel show but included here for completeness "
                      "as it aired alongside CN content in the modern streaming era. "
                      "Dana Terrace publicly stated Disney shortened the show due to its "
                      "LGBTQ+ content — though Disney disputed this. "
                      "The show's cancellation mid-story generated significant fan backlash."),
        ],
        wiki_slug="The_Owl_House",
    )
    # Override ownership — Owl House is Disney Channel not CN
    owl_house.ownership_history.clear()
    owl_house.add_ownership_record(OwnershipRecord(
        "The Walt Disney Company / Disney Television Animation", 2020, None,
        "original creation — Disney Channel series, not Cartoon Network",
        is_current_owner=True,
        notes="The Owl House aired on Disney Channel, not Cartoon Network. "
              "Included in CN file for thematic grouping with modern animation era."))
    lib.add_cartoon(owl_house)

    print(f"Cartoon Network characters added. Library now has {len(lib.cartoons)} cartoons total.")
