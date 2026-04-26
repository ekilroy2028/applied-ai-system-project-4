"""
filmation_characters.py
Major Filmation Associates cartoon characters for CartoonPal.

Filmation Associates was an American animation studio founded in 1962
by Lou Scheimer, Hal Sutherland, and Norm Prescott in Los Angeles.
The studio was famous for its distinctive limited animation style,
its heavy use of recycled animation sequences (to keep budgets low),
and its insistence on positive, educational content.

Filmation closed in 1989 when its parent company Group W (Westinghouse)
sold the library rather than continuing operations.

Ownership:
- Filmation Associates (1962–1989): original production
- Group W / Westinghouse (1985–1996): corporate owner during final years
- Entertainment Rights (1996–2009): acquired Filmation library
- Classic Media (2009–2012): acquired Entertainment Rights
- DreamWorks Classics / NBCUniversal (2012–present): acquired Classic Media

Usage:
    from filmation_characters import add_filmation_characters
    add_filmation_characters(lib)
"""

from cartoon_system import (
    Cartoon, Creator, ProductionCompany,
    Series, OwnershipRecord, Era, Library
)

FILMATION_STUDIO = ProductionCompany("Filmation Associates", 1962, still_active=False)
LOU_SCHEIMER    = Creator("Lou Scheimer", "Filmation co-founder, producer & voice actor", 1928, 2013)
HAL_SUTHERLAND  = Creator("Hal Sutherland", "Filmation co-founder & director", 1929, 2014)
NORM_PRESCOTT   = Creator("Norm Prescott", "Filmation co-founder & producer", 1927, 2005)

FILMATION_OWNERSHIP = [
    ("Filmation Associates / Group W (Westinghouse)", 1962, 1996, "original creation"),
    ("Entertainment Rights plc", 1996, 2009, "acquisition of Filmation library"),
    ("Classic Media", 2009, 2012, "acquisition of Entertainment Rights"),
    ("DreamWorks Classics / NBCUniversal", 2012, None, "acquisition of Classic Media"),
]

IMG = {
    "heman":    "https://upload.wikimedia.org/wikipedia/en/thumb/e/e1/He-Man_and_the_Masters_of_the_Universe_title.png/240px-He-Man_and_the_Masters_of_the_Universe_title.png",
    "shera":    "https://upload.wikimedia.org/wikipedia/en/thumb/7/7b/She-Ra_Princess_of_Power_title.png/240px-She-Ra_Princess_of_Power_title.png",
    "filmation":"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Filmation_logo.svg/240px-Filmation_logo.svg.png",
    "star":     "https://upload.wikimedia.org/wikipedia/en/thumb/4/4b/Star_Trek_The_Animated_Series_title_card.png/240px-Star_Trek_The_Animated_Series_title_card.png",
    "fat":      "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Fat_Albert_title_card.png/240px-Fat_Albert_title_card.png",
    "archie":   "https://upload.wikimedia.org/wikipedia/en/thumb/7/7c/Archie_Show_title_card.png/240px-Archie_Show_title_card.png",
    "brave":    "https://upload.wikimedia.org/wikipedia/en/thumb/5/5d/BraveStarr_title_card.png/200px-BraveStarr_title_card.png",
    "ghostbusters": "https://upload.wikimedia.org/wikipedia/en/thumb/2/2f/The_Real_Ghostbusters_logo.png/240px-The_Real_Ghostbusters_logo.png",
}


def _filmation(name, description, character_type, debut_year,
               extra_creators, series_list, eras, wiki_slug,
               origin="Los Angeles, California, USA — Filmation Associates studio"):
    c = Cartoon(name=name, description=description,
                character_type=character_type,
                country_of_origin="USA", debut_year=debut_year)
    c.original_studio = FILMATION_STUDIO
    c.add_creator(LOU_SCHEIMER)
    c.add_creator(HAL_SUTHERLAND)
    for ec in extra_creators:
        c.add_creator(ec)
    for s in series_list:
        c.add_series(s)
    for i, rec in enumerate(FILMATION_OWNERSHIP):
        is_cur = (i == len(FILMATION_OWNERSHIP) - 1)
        c.add_ownership_record(OwnershipRecord(rec[0], rec[1], rec[2], rec[3], is_current_owner=is_cur))
    for era in eras:
        c.add_era(era)
    c.wiki_url = f"https://en.wikipedia.org/wiki/{wiki_slug}"
    c.origin_location = origin
    return c


def add_filmation_characters(lib: Library):

    # He-Man and the Masters of the Universe (1983)
    heman = _filmation(
        name="He-Man",
        description=(
            "Prince Adam of Eternia transforms into He-Man — the most powerful "
            "man in the universe — by raising his Power Sword and declaring "
            "By the power of Grayskull! He battles the evil Skeletor alongside "
            "the heroic warriors of Castle Grayskull. He-Man was created to "
            "sell Mattel's Masters of the Universe toy line and became the "
            "defining animated property of the early 1980s, notable for its "
            "moral lessons delivered at each episode's end."
        ),
        character_type="Human / superhero — fantasy warrior",
        debut_year=1983,
        extra_creators=[Creator("Roger Sweet", "Mattel toy designer who created the concept", 1944)],
        series_list=[
            Series("He-Man and the Masters of the Universe (Filmation)", 1983, 1985,
                   "Filmation Associates / Mattel / syndicated", "TV series", episode_count=130),
            Series("The New Adventures of He-Man", 1990, 1991,
                   "Jetlag Productions / Mattel", "TV series", episode_count=65),
            Series("He-Man and the Masters of the Universe (2002 reboot)", 2002, 2004,
                   "Mike Young Productions / Cartoon Network", "TV series", episode_count=39),
            Series("Masters of the Universe Revelation", 2021, 2022,
                   "Netflix / Mattel Television", "streaming series", episode_count=10),
            Series("He-Man and the Masters of the Universe CGI", 2021, 2023,
                   "Netflix / Mattel Television", "streaming series"),
        ],
        eras=[
            Era(1983, 1985, "Original Filmation design — muscular blond warrior in fur loincloth and cross harness, Power Sword",
                art_style="Limited TV animation with heavy cel recycling",
                image_url=IMG["heman"],
                notes="Debuted September 5 1983. Voiced by John Erwin. "
                      "Filmation produced 130 episodes in two years using heavy animation recycling. "
                      "Each episode ended with a moral lesson — unusual for action cartoons. "
                      "He-Man was the first toy-based animated series of the 1980s boom."),
            Era(1990, 2001, "New Adventures era — updated space-themed costume, same fundamental character",
                art_style="Updated TV cel animation",
                image_url=IMG["heman"],
                notes="The 1990 sequel moved He-Man to a space setting and was not well received by fans."),
            Era(2002, 2020, "2002 reboot — more detailed anime-influenced art style, darker tone",
                art_style="Detailed digital animation",
                image_url=IMG["heman"],
                notes="The 2002 Mike Young Productions reboot was praised for its animation quality. "
                      "It was cancelled after two seasons despite strong critical reception."),
            Era(2021, None, "Netflix era — Kevin Smith's Revelation and CGI kids series ran simultaneously",
                art_style="CGI / modern digital",
                image_url=IMG["heman"],
                notes="Kevin Smith's Masters of the Universe: Revelation (2021) generated significant fan debate. "
                      "A separate CGI kids series targeting a new generation ran concurrently."),
        ],
        wiki_slug="He-Man_and_the_Masters_of_the_Universe_(1983_TV_series)",
    )
    heman.ownership_history.clear()
    heman.add_ownership_record(OwnershipRecord("Mattel Inc.", 1981, None,
                                                "original toy property — Filmation produced under license",
                                                is_current_owner=True,
                                                notes="Mattel owns all Masters of the Universe IP. "
                                                      "Filmation's specific scripts and animation are owned by NBCUniversal."))
    lib.add_cartoon(heman)

    # Skeletor
    skeletor = _filmation(
        name="Skeletor",
        description=(
            "The skull-faced sorcerer and primary villain of He-Man — once Keldor, "
            "a power-hungry warrior whose face was destroyed by acid, leaving him "
            "with a blue skull for a head. Skeletor commands Snake Mountain and "
            "endlessly schemes to steal the secrets of Castle Grayskull. "
            "Despite his constant failures, Skeletor is beloved as one of animation's "
            "greatest villains — a genuinely menacing presence with unexpected "
            "comedic qualities. Alan Oppenheimer's voice performance is iconic."
        ),
        character_type="Supernatural — skull-faced sorcerer villain",
        debut_year=1983,
        extra_creators=[],
        series_list=[
            Series("He-Man and the Masters of the Universe (Filmation)", 1983, 1985,
                   "Filmation Associates", "TV series"),
            Series("Masters of the Universe Revelation", 2021, 2022, "Netflix", "streaming series"),
        ],
        eras=[
            Era(1983, None, "Blue skull head, purple hood and armor, Havoc Staff — instantly iconic villain design",
                art_style="Limited TV animation / various modern",
                image_url=IMG["heman"],
                notes="Voiced by Alan Oppenheimer in the original series. "
                      "Mark Hamill voiced Skeletor in Masters of the Universe: Revelation (2021). "
                      "Skeletor is consistently ranked among the greatest cartoon villains of the 1980s."),
        ],
        wiki_slug="Skeletor",
    )
    skeletor.ownership_history.clear()
    skeletor.add_ownership_record(OwnershipRecord("Mattel Inc.", 1981, None,
                                                   "original toy property", is_current_owner=True))
    lib.add_cartoon(skeletor)

    # She-Ra: Princess of Power (1985)
    shera = _filmation(
        name="She-Ra",
        description=(
            "Princess Adora — He-Man's twin sister — who was kidnapped as an infant "
            "and raised by the evil Horde before learning her true identity. "
            "She transforms into She-Ra the Princess of Power using the Sword of "
            "Protection. She-Ra leads the Great Rebellion against Hordak's Horde "
            "on the planet Etheria. Created specifically to expand the Masters of "
            "the Universe brand to female audiences, She-Ra became one of the most "
            "important feminist icons in 1980s animation."
        ),
        character_type="Human / superhero — fantasy warrior princess",
        debut_year=1985,
        extra_creators=[Creator("Larry DiTillio", "Head writer & story editor", 1940, 2020)],
        series_list=[
            Series("She-Ra Princess of Power (Filmation)", 1985, 1987,
                   "Filmation Associates / Mattel / syndicated", "TV series", episode_count=93),
            Series("She-Ra and the Princesses of Power (Netflix reboot)", 2018, 2020,
                   "Netflix / DreamWorks Animation", "streaming series", episode_count=52),
        ],
        eras=[
            Era(1985, 1987, "Original Filmation design — white costume with gold accents, tiara, Sword of Protection, winged horse Swift Wind",
                art_style="Limited TV animation",
                image_url=IMG["shera"],
                notes="Debuted as a film (Secret of the Sword) before the TV series. "
                      "Voiced by Melendy Britt. Created to sell a female Masters of the Universe toy line. "
                      "She-Ra was more popular than expected and outlasted the toy line."),
            Era(2018, 2020, "Netflix reboot — completely reimagined by Noelle Stevenson, diverse cast of princesses",
                art_style="Modern digital animation",
                image_url=IMG["shera"],
                notes="Noelle Stevenson's reboot (2018-2020) reimagined She-Ra with a diverse cast, "
                      "LGBTQ+ representation, and deeper character development. "
                      "Considered one of the best animated series of the 2010s."),
        ],
        wiki_slug="She-Ra:_Princess_of_Power",
    )
    shera.ownership_history.clear()
    shera.add_ownership_record(OwnershipRecord("Mattel Inc.", 1985, None,
                                                "original toy property — Filmation produced under license",
                                                is_current_owner=True))
    lib.add_cartoon(shera)

    # Fat Albert and the Cosby Kids (1972)
    fat_albert = _filmation(
        name="Fat Albert and the Cosby Kids",
        description=(
            "Fat Albert is the lovable, rotund leader of a gang of Philadelphia kids "
            "who navigate growing up in an urban neighborhood with humor and heart. "
            "Based on Bill Cosby's childhood friends and stand-up comedy material, "
            "the series was one of the first animated shows to feature a primarily "
            "Black cast and to address serious social issues through entertainment. "
            "Each episode included an educational message. Hey hey hey!"
        ),
        character_type="Human — urban children ensemble",
        debut_year=1972,
        extra_creators=[Creator("Bill Cosby", "Creator, executive producer & narrator", 1937)],
        series_list=[
            Series("Fat Albert and the Cosby Kids", 1972, 1985,
                   "Filmation Associates / CBS", "TV series", episode_count=110),
            Series("The Fat Albert Christmas Special", 1977, 1977,
                   "Filmation / CBS", "TV special"),
            Series("Fat Albert live-action film", 2004, 2004,
                   "20th Century Fox", "theatrical feature"),
        ],
        eras=[
            Era(1972, 1985, "Original Filmation design — large round Albert in red sweater, gang of diverse Philadelphia kids",
                art_style="Limited TV animation",
                image_url=IMG["fat"],
                notes="Debuted September 9 1972. Bill Cosby was closely involved in production. "
                      "One of the first animated series centered on Black characters in urban America. "
                      "CBS required Cosby's involvement as a condition of airing the show."),
            Era(2004, None, "Live-action film era — Kenan Thompson as Fat Albert in live-action/animated hybrid",
                art_style="Live-action / CGI hybrid",
                image_url=IMG["fat"],
                notes="The 2004 Fox film grossed $41 million. "
                      "Note: Bill Cosby's association with the property became complicated "
                      "following his 2018 conviction (overturned in 2021)."),
        ],
        wiki_slug="Fat_Albert_and_the_Cosby_Kids",
    )
    lib.add_cartoon(fat_albert)

    # Star Trek: The Animated Series (1973)
    star_trek_anim = _filmation(
        name="Star Trek: The Animated Series",
        description=(
            "The animated continuation of the original Star Trek television series — "
            "reuniting the entire original cast including William Shatner, Leonard Nimoy, "
            "and DeForest Kelley for new adventures of the USS Enterprise crew. "
            "The animated format allowed for alien designs and cosmic concepts "
            "impossible on the live-action show's budget. It won the first Daytime "
            "Emmy Award for Outstanding Children's Entertainment Series and is now "
            "considered canonical by Paramount."
        ),
        character_type="Science fiction — starship crew ensemble",
        debut_year=1973,
        extra_creators=[Creator("Gene Roddenberry", "Original series creator & executive producer", 1921, 1991)],
        series_list=[
            Series("Star Trek The Animated Series", 1973, 1974,
                   "Filmation Associates / NBC / Paramount", "TV series", episode_count=22),
        ],
        eras=[
            Era(1973, 1974, "Animated versions of Kirk Spock McCoy and crew — same character designs as live-action actors",
                art_style="Limited TV animation",
                image_url=IMG["star"],
                notes="Debuted September 8 1973. Won the Daytime Emmy for Outstanding Children's Entertainment. "
                      "D.C. Fontana and David Gerrold wrote several episodes. "
                      "Filmation's limited animation style was actually an advantage for alien designs. "
                      "Paramount now considers it part of the official Star Trek canon."),
        ],
        wiki_slug="Star_Trek:_The_Animated_Series",
    )
    star_trek_anim.ownership_history.clear()
    star_trek_anim.add_ownership_record(OwnershipRecord("Paramount Pictures / CBS Studios", 1966, None,
                                                         "Star Trek IP owned by Paramount — Filmation produced under license",
                                                         is_current_owner=True))
    lib.add_cartoon(star_trek_anim)

    # The Archie Show / Archie's Funhouse (1968)
    archie = _filmation(
        name="Archie (Filmation animated series)",
        description=(
            "Archie Andrews, Betty Cooper, Veronica Lodge, Jughead Jones, and Reggie "
            "Mantle — the teenagers of Riverdale — star in animated adventures that "
            "also featured musical performances by The Archies, the show's fictional "
            "band. The Archies produced the genuine #1 hit Sugar Sugar (1969) — "
            "one of the best-selling singles of that year — making them the first "
            "fictional animated band to top the real music charts. "
            "Filmation produced multiple Archie series throughout the late 1960s."
        ),
        character_type="Human — teenage ensemble / pop band",
        debut_year=1968,
        extra_creators=[Creator("Bob Montana", "Original Archie Comics creator", 1920, 1975)],
        series_list=[
            Series("The Archie Show (Filmation)", 1968, 1969,
                   "Filmation Associates / CBS", "TV series", episode_count=17),
            Series("Archies Funhouse", 1970, 1971,
                   "Filmation Associates / CBS", "TV series"),
            Series("The Archie Comedy Hour", 1969, 1970,
                   "Filmation / CBS", "TV series"),
        ],
        eras=[
            Era(1968, 1971, "Filmation Archie design — classic red-headed all-American teen, 1960s mod fashion for the gang",
                art_style="Limited TV animation",
                image_url=IMG["archie"],
                notes="Debuted September 14 1968 on CBS. "
                      "The Archies' Sugar Sugar (1969) reached #1 on the Billboard Hot 100, "
                      "outselling the Beatles and Rolling Stones that year. "
                      "The band concept was created specifically for the TV show."),
        ],
        wiki_slug="The_Archie_Show",
    )
    archie.ownership_history.clear()
    archie.add_ownership_record(OwnershipRecord("Archie Comics Publications", 1941, None,
                                                 "original comic book property — Filmation produced under license",
                                                 is_current_owner=True))
    lib.add_cartoon(archie)

    # BraveStarr (1987) — Filmation's last original creation
    bravestarr = _filmation(
        name="BraveStarr",
        description=(
            "Marshal BraveStarr is a Native American lawman on the futuristic "
            "frontier planet New Texas who channels the powers of spirit animals — "
            "Eyes of the Hawk, Ears of the Wolf, Strength of the Bear, Speed of "
            "the Puma — to battle the villain Tex Hex and his outlaw gang. "
            "BraveStarr was Filmation's final original animated series before "
            "the studio closed in 1989. It was notable for having a Native American "
            "hero at a time when such representation was extremely rare."
        ),
        character_type="Human — Native American space marshal / superhero",
        debut_year=1987,
        extra_creators=[],
        series_list=[
            Series("BraveStarr", 1987, 1988,
                   "Filmation Associates / syndicated", "TV series", episode_count=65),
            Series("BraveStarr: The Legend film", 1988, 1988,
                   "Filmation Associates", "theatrical feature",
                   notes="The theatrical film was released after the series ended."),
        ],
        eras=[
            Era(1987, 1989, "Space western setting — Native American marshal in futuristic armor on alien frontier planet",
                art_style="Limited TV animation",
                image_url=IMG["brave"],
                notes="BraveStarr was Filmation's last original series. "
                      "The studio closed in 1989 after Westinghouse sold the library. "
                      "Native American actors and consultants were involved in production — "
                      "unusual attention to representation for 1987."),
        ],
        wiki_slug="BraveStarr",
    )
    lib.add_cartoon(bravestarr)

    # Ghostbusters (Filmation, 1975/1986) — Note: different from The Real Ghostbusters
    filmation_ghostbusters = _filmation(
        name="Filmation's Ghostbusters",
        description=(
            "The ORIGINAL Ghostbusters — Jake Kong Jr. and Eddie Spencer Jr., "
            "sons of the original Ghostbusters from Filmation's 1975 live-action "
            "TV show, who battle Prime Evil and his ghosts with their gorilla "
            "companion Tracy. When Columbia Pictures released Ghostbusters (1984), "
            "Filmation held the trademark and licensed it to Columbia while "
            "producing their own animated sequel. This led to the confusing "
            "situation of two simultaneous Ghostbusters animated series — "
            "DIC's The Real Ghostbusters (based on the film) and this series."
        ),
        character_type="Human — ghost-busting duo with gorilla",
        debut_year=1986,
        extra_creators=[],
        series_list=[
            Series("The Ghost Busters live-action TV show", 1975, 1975,
                   "Filmation Associates / CBS", "TV series", episode_count=15,
                   notes="Original live-action show that established Filmation's trademark."),
            Series("Filmation's Ghostbusters animated series", 1986, 1988,
                   "Filmation Associates / syndicated", "TV series", episode_count=65),
        ],
        eras=[
            Era(1975, 1975, "Live-action original — two bumbling ghost hunters and their trained gorilla Tracy",
                art_style="Live-action TV",
                image_url=IMG["ghostbusters"],
                notes="The 1975 live-action show starred Forrest Tucker and Larry Storch. "
                      "Filmation held the Ghostbusters trademark before the 1984 Columbia film."),
            Era(1986, 1988, "Animated sequel — son characters of original live-action heroes, futuristic ghost-busting equipment",
                art_style="Limited TV animation",
                image_url=IMG["ghostbusters"],
                notes="Filmation deliberately produced this animated sequel to assert their trademark rights. "
                      "The simultaneous DIC series based on the Columbia film was called The Real Ghostbusters "
                      "specifically because Columbia had to license the Ghostbusters name from Filmation."),
        ],
        wiki_slug="Filmation%27s_Ghostbusters",
    )
    lib.add_cartoon(filmation_ghostbusters)

    # The Batman/Superman Hour (1968) — Filmation's DC adaptations
    filmation_batman = _filmation(
        name="Batman and Superman (Filmation animated)",
        description=(
            "Filmation produced the first animated adaptations of Batman and Superman "
            "for television in the late 1960s. "
            "BATMAN was created by Bob Kane and Bill Finger for Detective Comics #27 (1939). "
            "Bill Finger co-created virtually everything recognizable about Batman — "
            "the costume, Bruce Wayne, Gotham City, the Joker, Alfred, Commissioner Gordon — "
            "but was not officially credited until 2015. "
            "SUPERMAN was created by Jerry Siegel and Joe Shuster for Action Comics #1 (1938). "
            "The Batman/Superman Hour featured the Caped Crusader in animated form "
            "for the first time since the 1940s theatrical shorts. "
            "The series used limited animation but faithful interpretations of the comics designs."
        ),
        character_type="Superhero — DC Comics animated adaptations",
        debut_year=1968,
        extra_creators=[
            Creator("Bob Kane", "Batman co-creator — conceived original concept", 1915, 1998),
            Creator("Bill Finger", "Batman co-creator — costume, Bruce Wayne, Gotham, Joker, Alfred. Credited 2015.", 1914, 1974),
            Creator("Jerry Siegel", "Superman co-creator", 1914, 1996),
            Creator("Joe Shuster", "Superman co-creator", 1914, 1992),
        ],
        series_list=[
            Series("The Batman Superman Hour", 1968, 1969,
                   "Filmation Associates / CBS", "TV series", episode_count=34),
            Series("The Superman Aquaman Hour of Adventure", 1967, 1968,
                   "Filmation Associates / CBS", "TV series"),
            Series("Batman with Robin the Boy Wonder segments", 1968, 1969,
                   "Filmation Associates / CBS", "TV series"),
        ],
        eras=[
            Era(1968, 1969, "Filmation DC designs — faithful to Neal Adams-era comics, limited animation but recognizable",
                art_style="Limited TV animation",
                image_url=IMG["filmation"],
                notes="The 1968 Filmation Batman was the first animated Batman since 1968. "
                      "Bud Collyer reprised his radio Superman role. "
                      "These series established the template for superhero TV animation "
                      "that Hanna-Barbera and others would develop throughout the 1970s."),
        ],
        wiki_slug="The_Batman%2FSuperman_Hour",
    )
    filmation_batman.ownership_history.clear()
    filmation_batman.add_ownership_record(OwnershipRecord("DC Comics / Warner Bros.", 1938, None,
                                                           "DC characters — Filmation produced under license",
                                                           is_current_owner=True))
    lib.add_cartoon(filmation_batman)

    print(f"Filmation characters added. Library now has {len(lib.cartoons)} cartoons total.")
