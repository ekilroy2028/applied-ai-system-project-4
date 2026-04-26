"""
dc_characters.py
DC Comics animated characters for CartoonPal.

Important distinction for all DC characters:
- DC Comics / Warner Bros. Discovery ALWAYS owns the characters
- Different studios PRODUCED animated series under LICENSE at different times
- Hanna-Barbera produced Super Friends (1973-1986) under DC license
- Filmation produced Batman/Superman (1966-1969) under DC license
- Warner Bros. Animation produced DCAU (1992-2006) in-house
- Each production era is tracked as a separate Era with its producing studio noted

Ownership chain for all DC characters:
- DC Comics (1938/1939/etc.) — original creation
- DC Comics / Warner Bros. (1990) — Time Warner acquired DC's parent
- DC Comics / Warner Bros. Discovery (2022) — current

Usage:
    from characters.dc_characters import add_dc_characters
    add_dc_characters(lib)
"""

from cartoon_system import (
    Cartoon, Creator, ProductionCompany,
    Series, OwnershipRecord, Era, Library
)

DC_STUDIO = ProductionCompany("DC Comics / Warner Bros. Animation", 1938, country="USA")

BOB_KANE    = Creator("Bob Kane", "Batman co-creator (credited)", 1915, 1998)
BILL_FINGER = Creator("Bill Finger", "Batman co-creator (uncredited until 2015)", 1914, 1974)
JERRY_SIEGEL = Creator("Jerry Siegel", "Superman co-creator", 1914, 1996)
JOE_SHUSTER  = Creator("Joe Shuster", "Superman co-creator", 1914, 1992)
BRUCE_TIMM   = Creator("Bruce Timm", "DCAU creator & producer", 1961)
PAUL_DINI    = Creator("Paul Dini", "DCAU writer & producer", 1957)
WILLIAM_M    = Creator("William Moulton Marston", "Wonder Woman creator", 1893, 1947)
GARDNER_FOX  = Creator("Gardner Fox", "Flash & Justice Society creator", 1911, 1986)
MARTIN_NODELL = Creator("Martin Nodell", "Green Lantern (original) creator", 1915, 2006)
PAUL_NORRIS   = Creator("Paul Norris", "Aquaman creator", 1914, 2007)
BOB_FINGER    = Creator("Bob Haney", "Teen Titans co-creator", 1926, 2004)

DC_OWNERSHIP = [
    ("DC Comics / National Allied Publications", 1934, 1969,
     "original creation — various characters created 1938-1960s"),
    ("DC Comics / Kinney National Company", 1969, 1990,
     "Warner Communications / Kinney acquired DC's parent"),
    ("DC Comics / Time Warner / Warner Bros.", 1990, 2022,
     "Time Warner acquired Warner Communications"),
    ("DC Comics / Warner Bros. Discovery", 2022, None,
     "Discovery merger with WarnerMedia", ),
]

IMG = {
    "batman":    "https://upload.wikimedia.org/wikipedia/en/thumb/1/10/Batman_The_Animated_Series_logo.png/240px-Batman_The_Animated_Series_logo.png",
    "superman":  "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Superman_The_Animated_Series_logo.png/240px-Superman_The_Animated_Series_logo.png",
    "superfriends": "https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/Super_Friends_title_card.png/240px-Super_Friends_title_card.png",
    "wonder":    "https://upload.wikimedia.org/wikipedia/en/thumb/9/93/Wonder_Woman_logo.png/240px-Wonder_Woman_logo.png",
    "flash":     "https://upload.wikimedia.org/wikipedia/en/thumb/7/7f/The_Flash_logo.png/240px-The_Flash_logo.png",
    "justice":   "https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Justice_League_animated_logo.png/240px-Justice_League_animated_logo.png",
    "dc":        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/DC_Comics_logo.svg/240px-DC_Comics_logo.svg.png",
    "teen":      "https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Teen_Titans_logo.png/240px-Teen_Titans_logo.png",
    "aquaman":   "https://upload.wikimedia.org/wikipedia/en/thumb/8/8b/Aquaman_animated.png/200px-Aquaman_animated.png",
    "green":     "https://upload.wikimedia.org/wikipedia/en/thumb/4/forty/Green_Lantern_animated.png/200px-Green_Lantern_animated.png",
}


def _dc(name, description, character_type, debut_year,
        creators, series_list, eras, wiki_slug,
        origin="Burbank, California, USA — DC Comics / Warner Bros."):
    c = Cartoon(name=name, description=description,
                character_type=character_type,
                country_of_origin="USA", debut_year=debut_year)
    c.original_studio = DC_STUDIO
    for cr in creators:
        c.add_creator(cr)
    for s in series_list:
        c.add_series(s)
    # DC ownership chain — character IP never changed hands, only production licenses did
    for i, rec in enumerate(DC_OWNERSHIP):
        is_cur = (i == len(DC_OWNERSHIP) - 1)
        c.add_ownership_record(OwnershipRecord(
            rec[0], rec[1], rec[2], rec[3], is_current_owner=is_cur,
        ))
    for era in eras:
        c.add_era(era)
    c.wiki_url = f"https://en.wikipedia.org/wiki/{wiki_slug}"
    c.origin_location = origin
    return c


def add_dc_characters(lib: Library):

    # ══════════════════════════════════════════════════════════════════════
    # BATMAN (1939)
    # ══════════════════════════════════════════════════════════════════════
    batman = _dc(
        name="Batman (animated history)",
        description=(
            "Bruce Wayne — billionaire orphan who witnessed his parents' murder "
            "and dedicated his life to fighting crime as the Dark Knight. "
            "Batman has appeared in more animated series than any other DC character, "
            "produced by different studios across six decades. Each production "
            "reflected the culture of its era: Filmation's campy 1968 version, "
            "Hanna-Barbera's Super Friends adventure format, and Bruce Timm's "
            "celebrated noir-influenced 1992 masterpiece that defined Batman "
            "for a generation. NOTE: DC Comics has always owned the Batman character — "
            "different studios produced animated versions under license at different times."
        ),
        character_type="Human — DC Comics superhero / Dark Knight",
        debut_year=1939,
        creators=[BOB_KANE, BILL_FINGER, BRUCE_TIMM, PAUL_DINI],
        series_list=[
            Series("The New Adventures of Batman (Filmation)", 1977, 1978,
                   "Filmation Associates / CBS", "TV series", episode_count=16,
                   notes="PRODUCER: Filmation under DC license. Followed the 1966 live-action show's campy tone. "
                         "Bat-Mite appeared as a regular character."),
            Series("Super Friends (Batman as team member)", 1973, 1986,
                   "Hanna-Barbera / ABC", "TV series",
                   notes="PRODUCER: Hanna-Barbera under DC license. Batman and Robin joined Superman, "
                         "Wonder Woman, Aquaman and the Wonder Twins. Ran under several titles including "
                         "The All-New Super Friends Hour, Challenge of the SuperFriends, and Super Friends: "
                         "The Legendary Super Powers Show."),
            Series("Batman: The Animated Series", 1992, 1995,
                   "Warner Bros. Animation / Fox Kids", "TV series", episode_count=85,
                   notes="PRODUCER: Warner Bros. Animation in-house. Created by Bruce Timm and Paul Dini. "
                         "Revolutionary noir art deco style. Kevin Conroy as definitive Batman voice. "
                         "Mark Hamill as the Joker. Created Harley Quinn. Won 4 Emmy Awards."),
            Series("Batman: Mask of the Phantasm (theatrical film)", 1993, 1993,
                   "Warner Bros. Animation / Warner Bros. Pictures", "theatrical feature",
                   notes="PRODUCER: Warner Bros. Animation. Theatrical spinoff of BTAS. "
                         "Widely considered the greatest Batman film ever made."),
            Series("The New Batman Adventures", 1997, 1999,
                   "Warner Bros. Animation / Kids WB", "TV series", episode_count=24,
                   notes="PRODUCER: Warner Bros. Animation. Direct continuation of BTAS with redesigned characters. "
                         "Introduced new Batgirl and replaced Robin with Tim Drake."),
            Series("Batman Beyond", 1999, 2001,
                   "Warner Bros. Animation / Kids WB", "TV series", episode_count=52,
                   notes="PRODUCER: Warner Bros. Animation. Set in 2039 Gotham — teenager Terry McGinnis "
                         "becomes the new Batman under elderly Bruce Wayne's mentorship."),
            Series("Justice League / Justice League Unlimited", 2001, 2006,
                   "Warner Bros. Animation / Cartoon Network", "TV series", episode_count=91,
                   notes="PRODUCER: Warner Bros. Animation. Batman as founding member of the Justice League. "
                         "Kevin Conroy continued as Batman throughout the entire DCAU."),
            Series("Batman: The Brave and the Bold", 2008, 2011,
                   "Warner Bros. Animation / Cartoon Network", "TV series", episode_count=65,
                   notes="PRODUCER: Warner Bros. Animation. Lighter Silver Age tone — "
                         "Batman teams with a different DC hero each episode."),
            Series("Beware the Batman", 2013, 2014,
                   "Warner Bros. Animation / Cartoon Network", "TV series", episode_count=26,
                   notes="PRODUCER: Warner Bros. Animation. CGI series featuring lesser-known villains. "
                         "Cancelled after one season."),
            Series("Batman vs. TMNT and DC animated films", 2010, None,
                   "Warner Bros. Animation", "direct-to-video features",
                   notes="PRODUCER: Warner Bros. Animation. Ongoing series of DC animated films "
                         "featuring Batman in various storylines."),
        ],
        eras=[
            Era(1968, 1976,
                "Filmation era — campy bright colors, influenced by 1966 live-action TV show, "
                "Adam West visual style. PRODUCED BY: Filmation Associates under DC license.",
                art_style="Flat bright color TV cel",
                image_url=IMG["batman"],
                notes="Filmation's Batman closely followed the campy aesthetic of the Adam West TV series. "
                      "The studio produced The Batman/Superman Hour (1968) and The New Adventures of Batman (1977)."),
            Era(1973, 1986,
                "Super Friends / Hanna-Barbera era — simplified adventure format, "
                "Batman as team player rather than solo detective. "
                "PRODUCED BY: Hanna-Barbera Productions under DC license.",
                art_style="Hanna-Barbera limited TV cel animation",
                image_url=IMG["superfriends"],
                notes="Hanna-Barbera's Super Friends ran under multiple titles from 1973-1986. "
                      "Challenge of the SuperFriends (1978) introduced the Legion of Doom. "
                      "Batman's design was simplified and brightened for the adventure format."),
            Era(1992, 1999,
                "Batman: The Animated Series / DCAU era — revolutionary noir art deco design, "
                "dark retro-futurist Gotham, the definitive animated Batman. "
                "PRODUCED BY: Warner Bros. Animation in-house (not a license — WB owns DC).",
                art_style="Noir-influenced flat color animation — art deco aesthetic",
                image_url=IMG["batman"],
                notes="Bruce Timm and Paul Dini's masterpiece. Kevin Conroy as Batman. "
                      "The show created Harley Quinn who became a major DC character. "
                      "Widely considered the greatest superhero animated series ever made."),
            Era(1999, 2006,
                "Batman Beyond / Justice League era — futuristic 2039 setting for Beyond, "
                "ensemble team dynamic in Justice League. "
                "PRODUCED BY: Warner Bros. Animation.",
                art_style="DCAU evolved style — sleeker future aesthetic for Beyond",
                image_url=IMG["batman"],
                notes="Batman Beyond gave Bruce Wayne a mentorship role as elderly man. "
                      "Justice League expanded Batman into a team context while preserving his loner nature."),
            Era(2008, None,
                "Modern era — multiple simultaneous interpretations: Brave and the Bold's "
                "Silver Age fun, CGI experiments, and ongoing DC animated films. "
                "PRODUCED BY: Warner Bros. Animation.",
                art_style="Various — Silver Age color, CGI, modern digital",
                image_url=IMG["batman"],
                notes="Batman: The Brave and the Bold deliberately lightened the tone after "
                      "years of dark interpretations. Multiple DC animated films continue "
                      "to feature Batman in various art styles."),
        ],
        wiki_slug="Batman_in_other_media",
        origin="New York City, USA — DC Comics (character created 1939) / "
               "Various animation studios produced under license",
    )
    lib.add_cartoon(batman)

    # ══════════════════════════════════════════════════════════════════════
    # SUPERMAN (1938)
    # ══════════════════════════════════════════════════════════════════════
    superman = _dc(
        name="Superman (animated history)",
        description=(
            "Kal-El of Krypton — last survivor of a doomed planet, raised as "
            "Clark Kent in Smallville, Kansas, working as a reporter at the "
            "Daily Planet in Metropolis while secretly defending the world as "
            "the Man of Steel. Superman is the original superhero and has been "
            "continuously animated since 1941 — longer than any other superhero. "
            "Each animated era reflected its time: the Fleischer Studios art deco "
            "masterpieces of the 1940s, the Filmation adventure series, the "
            "Hanna-Barbera Super Friends era, and Bruce Timm's acclaimed 1996 series. "
            "NOTE: DC Comics has always owned Superman — different studios "
            "produced animated versions under license at different times."
        ),
        character_type="Human / alien — DC Comics superhero / Man of Steel",
        debut_year=1938,
        creators=[JERRY_SIEGEL, JOE_SHUSTER, BRUCE_TIMM],
        series_list=[
            Series("Superman Fleischer / Famous Studios theatrical shorts", 1941, 1943,
                   "Fleischer Studios / Famous Studios / Paramount", "theatrical short", episode_count=17,
                   notes="PRODUCER: Fleischer Studios (then Famous Studios) under DC/Superman Inc. license. "
                         "Considered among the greatest animation ever produced. "
                         "Revolutionary rotoscoping and realistic action sequences. "
                         "These 17 shorts set the visual standard for Superman adaptations."),
            Series("The New Adventures of Superman (Filmation)", 1966, 1970,
                   "Filmation Associates / CBS", "TV series", episode_count=68,
                   notes="PRODUCER: Filmation Associates under DC license. "
                         "First Superman animated TV series. Bud Collyer reprised his radio Superman role. "
                         "Part of The Superman/Aquaman Hour of Adventure."),
            Series("Super Friends (Superman as team leader)", 1973, 1986,
                   "Hanna-Barbera / ABC", "TV series",
                   notes="PRODUCER: Hanna-Barbera under DC license. Superman served as de facto leader "
                         "of the Super Friends. Ran under multiple titles across 13 years."),
            Series("Superman: The Animated Series", 1996, 2000,
                   "Warner Bros. Animation / Kids WB", "TV series", episode_count=54,
                   notes="PRODUCER: Warner Bros. Animation in-house. Created by Bruce Timm, Paul Dini, "
                         "Alan Burnett. Tim Daly as Clark Kent / Superman. Dana Delany as Lois Lane. "
                         "Introduced Livewire as an original villain. Brainiac reimagined as a Kryptonian AI."),
            Series("Justice League / Justice League Unlimited", 2001, 2006,
                   "Warner Bros. Animation / Cartoon Network", "TV series",
                   notes="PRODUCER: Warner Bros. Animation. Superman as founding Justice League member. "
                         "George Newbern replaced Tim Daly as the voice of Superman."),
            Series("Superman: Doomsday (animated film)", 2007, 2007,
                   "Warner Bros. Animation", "direct-to-video feature",
                   notes="PRODUCER: Warner Bros. Animation. First DC Universe Animated Original Movie. "
                         "Adapted The Death of Superman storyline."),
            Series("Superman and the Legion of Super Heroes", 2006, 2008,
                   "Warner Bros. Animation / Cartoon Network", "TV series", episode_count=26,
                   notes="PRODUCER: Warner Bros. Animation. Young Clark Kent / Superboy teams with "
                         "the Legion of Super Heroes in the 31st century."),
            Series("My Adventures with Superman", 2023, None,
                   "Warner Bros. Animation / Adult Swim", "streaming series",
                   notes="PRODUCER: Warner Bros. Animation. Fresh take with young Clark and Lois "
                         "in anime-influenced style. Critically acclaimed reboot for new generation."),
        ],
        eras=[
            Era(1941, 1943,
                "Fleischer Studios theatrical era — stunning art deco animation, "
                "rotoscoped realistic movement, the gold standard of Superman animation. "
                "PRODUCED BY: Fleischer Studios / Famous Studios under license.",
                art_style="Paramount Technicolor theatrical animation — art deco",
                image_url=IMG["superman"],
                notes="The 17 Fleischer/Famous Superman shorts (1941-1943) are considered "
                      "masterpieces of animation. The budget per short was extraordinary for the era. "
                      "They established the visual language of Superman that all subsequent adaptations reference."),
            Era(1966, 1970,
                "Filmation TV era — limited animation, faithful comic book colors, "
                "first animated Superman TV series. PRODUCED BY: Filmation Associates.",
                art_style="Limited TV cel animation",
                image_url=IMG["superman"],
                notes="Bud Collyer reprised his radio role from the 1940s Superman radio show. "
                      "The series was produced cheaply using heavy animation recycling — "
                      "a Filmation trademark."),
            Era(1973, 1986,
                "Super Friends / Hanna-Barbera era — adventure team format, "
                "Superman as moral leader and most powerful member. "
                "PRODUCED BY: Hanna-Barbera under DC license.",
                art_style="Hanna-Barbera limited TV animation",
                image_url=IMG["superfriends"],
                notes="Superman's design was simplified for the Super Friends format. "
                      "He was consistently depicted as the most powerful member "
                      "and de facto moral authority of the team."),
            Era(1996, 2006,
                "DCAU era — bright primary colors contrast to Batman's noir, "
                "art deco Metropolis, Tim Daly / George Newbern as definitive animated voices. "
                "PRODUCED BY: Warner Bros. Animation in-house.",
                art_style="DCAU flat color animation — bright Metropolis aesthetic",
                image_url=IMG["superman"],
                notes="Bruce Timm deliberately made Superman's color palette brighter "
                      "than Batman's to reflect the character's optimistic nature. "
                      "Tim Daly's performance is widely considered the definitive animated Superman."),
            Era(2007, None,
                "Modern era — multiple DC animated films and new series "
                "reimagining Superman for each generation. PRODUCED BY: Warner Bros. Animation.",
                art_style="Various — CGI, digital, anime-influenced",
                image_url=IMG["superman"],
                notes="My Adventures with Superman (2023) brought a fresh anime-influenced take. "
                      "Ongoing DC animated films continue to feature Superman in various adaptations."),
        ],
        wiki_slug="Superman_in_other_media",
        origin="New York City, USA — DC Comics (character created 1938) / "
               "Various animation studios produced under license",
    )
    lib.add_cartoon(superman)

    # ══════════════════════════════════════════════════════════════════════
    # WONDER WOMAN (1941)
    # ══════════════════════════════════════════════════════════════════════
    wonder_woman = _dc(
        name="Wonder Woman (animated history)",
        description=(
            "Princess Diana of Themyscira — an Amazonian warrior princess who "
            "comes to the outside world as an ambassador of peace and protector "
            "of humanity. Wonder Woman is DC's most prominent female superhero "
            "and one of the most recognizable fictional characters in the world. "
            "Her animated history spans from Super Friends where she was a founding "
            "member, to the DCAU Justice League where she was reimagined as a "
            "fierce warrior princess, to her acclaimed 2009 animated film. "
            "NOTE: DC Comics has always owned Wonder Woman — different studios "
            "produced animated versions under license."
        ),
        character_type="Amazonian — DC Comics superhero / Princess of Themyscira",
        debut_year=1941,
        creators=[WILLIAM_M,
                  Creator("H.G. Peter", "Original Wonder Woman artist", 1880, 1958)],
        series_list=[
            Series("Super Friends (Wonder Woman as founding member)", 1973, 1986,
                   "Hanna-Barbera / ABC", "TV series",
                   notes="PRODUCER: Hanna-Barbera under DC license. Wonder Woman was one of "
                         "the original five Super Friends alongside Superman, Batman, Robin, and Aquaman. "
                         "Her depiction was significantly less powerful than in comics."),
            Series("Justice League / Justice League Unlimited", 2001, 2006,
                   "Warner Bros. Animation / Cartoon Network", "TV series",
                   notes="PRODUCER: Warner Bros. Animation. Susan Eisenberg voiced Wonder Woman. "
                         "The DCAU reimagined her as a fierce Amazonian warrior newly arrived in Man's World — "
                         "widely considered the best animated Wonder Woman characterization."),
            Series("Wonder Woman animated film", 2009, 2009,
                   "Warner Bros. Animation", "direct-to-video feature",
                   notes="PRODUCER: Warner Bros. Animation. Keri Russell voiced Wonder Woman. "
                         "Critically acclaimed retelling of her origin story. "
                         "Nathan Fillion as Steve Trevor."),
            Series("DC Super Hero Girls", 2019, 2021,
                   "Warner Bros. Animation / Cartoon Network", "TV series", episode_count=52,
                   notes="PRODUCER: Warner Bros. Animation. Younger comedic take on Wonder Woman "
                         "as a high school student alongside other DC heroines."),
        ],
        eras=[
            Era(1973, 1986,
                "Super Friends era — simplified adventure heroine, golden tiara and lasso, "
                "less warrior and more team player. PRODUCED BY: Hanna-Barbera.",
                art_style="Hanna-Barbera limited TV animation",
                image_url=IMG["superfriends"],
                notes="The Super Friends version of Wonder Woman was significantly less powerful "
                      "than her comic counterpart. Her invisible jet appeared frequently "
                      "even though she could fly unaided in the comics."),
            Era(2001, 2006,
                "DCAU Justice League era — fierce Amazonian warrior, Susan Eisenberg's "
                "commanding performance, finest animated Wonder Woman. "
                "PRODUCED BY: Warner Bros. Animation.",
                art_style="DCAU flat color animation",
                image_url=IMG["justice"],
                notes="Bruce Timm and Paul Dini reimagined Wonder Woman as a genuine warrior "
                      "who found Man's World bewildering but fascinating. "
                      "Her fish-out-of-water dynamic with the modern world was a highlight of Justice League."),
            Era(2009, None,
                "Modern era — standalone film and various productions reimagining "
                "Wonder Woman across DC animated universe. PRODUCED BY: Warner Bros. Animation.",
                art_style="Various modern digital animation",
                image_url=IMG["wonder"],
                notes="The 2009 animated film is widely considered the best Wonder Woman adaptation "
                      "in any medium prior to the 2017 Patty Jenkins live-action film."),
        ],
        wiki_slug="Wonder_Woman_in_other_media",
        origin="New York City, USA — DC Comics (character created 1941)",
    )
    lib.add_cartoon(wonder_woman)

    # ══════════════════════════════════════════════════════════════════════
    # SUPER FRIENDS (1973) — The ensemble series
    # ══════════════════════════════════════════════════════════════════════
    super_friends = _dc(
        name="Super Friends",
        description=(
            "The animated team of DC's greatest heroes — Superman, Batman and Robin, "
            "Wonder Woman, Aquaman, and later the Wonder Twins Zan and Jayna with "
            "their space monkey Gleek. Super Friends was produced by Hanna-Barbera "
            "under license from DC Comics and ran from 1973 to 1986 under multiple "
            "titles. It introduced millions of children to DC characters and remains "
            "a touchstone of 1970s-80s Saturday morning television. "
            "The 1978 Challenge of the SuperFriends season introduced the Legion of Doom "
            "— a supervillain team led by Lex Luthor — and is the most beloved season."
        ),
        character_type="Superhero ensemble — DC Comics characters / Hanna-Barbera production",
        debut_year=1973,
        creators=[
            Creator("William Hanna", "Executive producer (Hanna-Barbera)", 1910, 2001),
            Creator("Joseph Barbera", "Executive producer (Hanna-Barbera)", 1911, 2006),
            Creator("Norman Maurer", "Producer", 1926, 1986),
        ],
        series_list=[
            Series("Super Friends", 1973, 1974,
                   "Hanna-Barbera / ABC", "TV series", episode_count=16,
                   notes="PRODUCER: Hanna-Barbera under DC license. Original run — "
                         "Superman, Batman & Robin, Wonder Woman, Aquaman, plus three original teen heroes "
                         "Wendy, Marvin and Wonder Dog."),
            Series("The All-New Super Friends Hour", 1977, 1978,
                   "Hanna-Barbera / ABC", "TV series", episode_count=16,
                   notes="PRODUCER: Hanna-Barbera. Introduced the Wonder Twins — Zan, Jayna and Gleek — "
                         "replacing Wendy and Marvin."),
            Series("Challenge of the SuperFriends", 1978, 1979,
                   "Hanna-Barbera / ABC", "TV series", episode_count=16,
                   notes="PRODUCER: Hanna-Barbera. The most beloved season. Introduced the Legion of Doom — "
                         "13 supervil lains including Lex Luthor, Joker, Riddler, Cheetah, Black Manta, "
                         "Gorilla Grodd and Sinestro."),
            Series("The World's Greatest Super Friends", 1979, 1980,
                   "Hanna-Barbera / ABC", "TV series", episode_count=8,
                   notes="PRODUCER: Hanna-Barbera. Reduced episode order, longer format stories."),
            Series("Super Friends: The Legendary Super Powers Show", 1984, 1985,
                   "Hanna-Barbera / ABC", "TV series", episode_count=16,
                   notes="PRODUCER: Hanna-Barbera. Introduced Firestorm. Tied to Kenner Super Powers toy line."),
            Series("The Super Powers Team: Galactic Guardians", 1985, 1986,
                   "Hanna-Barbera / ABC", "TV series", episode_count=8,
                   notes="PRODUCER: Hanna-Barbera. Final season. Introduced Cyborg to animation "
                         "and featured the origin of Batman for the first time in animation."),
        ],
        eras=[
            Era(1973, 1977,
                "Original Super Friends era — Wendy, Marvin and Wonder Dog as teen sidekicks, "
                "lighter adventure tone, no supervillains. PRODUCED BY: Hanna-Barbera.",
                art_style="Hanna-Barbera limited TV animation",
                image_url=IMG["superfriends"],
                notes="The original 1973 season avoided supervillains entirely — "
                      "the team fought natural disasters and alien threats. "
                      "ABC requested this to avoid violence complaints."),
            Era(1977, 1983,
                "Wonder Twins era — Zan, Jayna and Gleek replace teen sidekicks, "
                "more adventure-focused stories. PRODUCED BY: Hanna-Barbera.",
                art_style="Hanna-Barbera limited TV animation",
                image_url=IMG["superfriends"],
                notes="Wonder Twin powers activate! became one of the most parodied "
                      "catchphrases in animation history. "
                      "Challenge of the SuperFriends (1978) is the fan-favorite season."),
            Era(1984, 1986,
                "Super Powers era — tied to Kenner toy line, more dramatic stories, "
                "introduced Firestorm and Cyborg. PRODUCED BY: Hanna-Barbera.",
                art_style="Hanna-Barbera improved TV animation",
                image_url=IMG["superfriends"],
                notes="The final two seasons showed improved animation quality. "
                      "The Batman origin story in Galactic Guardians was "
                      "the first time Batman's origin appeared in animation."),
        ],
        wiki_slug="Super_Friends_(TV_series)",
        origin="Hollywood, California, USA — Hanna-Barbera Productions under DC Comics license",
    )
    # Override ownership for Super Friends — HB produced it, DC owns the characters
    super_friends.ownership_history.clear()
    super_friends.add_ownership_record(OwnershipRecord(
        "DC Comics — characters / Hanna-Barbera — production", 1973, 1986,
        "DC licensed characters to Hanna-Barbera for production",
        notes="DC Comics owned all character rights throughout. "
              "Hanna-Barbera held only the production license, not the characters."))
    super_friends.add_ownership_record(OwnershipRecord(
        "DC Comics / Warner Bros. Discovery", 1986, None,
        "Turner acquired Hanna-Barbera; Warner Bros. owns both DC and HB now",
        is_current_owner=True,
        notes="Warner Bros. Discovery now owns both DC Comics and the Hanna-Barbera library, "
              "so all Super Friends content is under one roof."))
    lib.add_cartoon(super_friends)

    # ══════════════════════════════════════════════════════════════════════
    # THE FLASH (1940)
    # ══════════════════════════════════════════════════════════════════════
    flash = _dc(
        name="The Flash (animated history)",
        description=(
            "The Fastest Man Alive — Barry Allen (and later Wally West) who can "
            "run at superhuman speeds after being struck by lightning while covered "
            "in chemicals. The Flash has appeared across multiple animated series "
            "from Super Friends through the DCAU Justice League where Wally West's "
            "Flash became a fan favorite for his humor and heart, to his own "
            "acclaimed 2024 animated series. "
            "NOTE: DC Comics has always owned The Flash — different studios "
            "produced animated versions under license."
        ),
        character_type="Human — DC Comics superhero / Fastest Man Alive",
        debut_year=1940,
        creators=[GARDNER_FOX,
                  Creator("Harry Lampert", "Original Flash artist", 1916, 2004)],
        series_list=[
            Series("Super Friends (Flash occasional appearances)", 1973, 1986,
                   "Hanna-Barbera / ABC", "TV series",
                   notes="PRODUCER: Hanna-Barbera. Flash appeared in Challenge of the SuperFriends "
                         "as a core member battling the Legion of Doom."),
            Series("Justice League / Justice League Unlimited", 2001, 2006,
                   "Warner Bros. Animation / Cartoon Network", "TV series",
                   notes="PRODUCER: Warner Bros. Animation. Wally West Flash voiced by Michael Rosenbaum. "
                         "Fan-favorite character known for humor and surprising depth. "
                         "The episode The Flash and Substance is widely considered the greatest Flash story."),
            Series("The Flash animated series", 2024, None,
                   "Warner Bros. Animation", "streaming series",
                   notes="PRODUCER: Warner Bros. Animation. New animated series for the streaming era."),
        ],
        eras=[
            Era(1973, 1986,
                "Super Friends era — primarily Barry Allen Flash in red costume. "
                "PRODUCED BY: Hanna-Barbera.",
                art_style="Hanna-Barbera limited TV animation",
                image_url=IMG["superfriends"],
                notes="Flash's speed powers were difficult to animate on HB's limited budget — "
                      "speed lines and blurs were the primary visual shorthand."),
            Era(2001, 2006,
                "DCAU Justice League era — Wally West Flash, humor and heart, "
                "Michael Rosenbaum's beloved performance. PRODUCED BY: Warner Bros. Animation.",
                art_style="DCAU flat color animation",
                image_url=IMG["justice"],
                notes="The DCAU Flash became the heart of the Justice League team. "
                      "His comedic scenes with Hawkgirl and Green Lantern "
                      "were highlights of the series."),
            Era(2024, None,
                "Modern streaming era — new animated series. PRODUCED BY: Warner Bros. Animation.",
                art_style="Modern digital animation",
                image_url=IMG["flash"],
                notes="The 2024 series brings the Flash to a new generation of viewers."),
        ],
        wiki_slug="The_Flash_in_other_media",
        origin="New York City, USA — DC Comics (character created 1940)",
    )
    lib.add_cartoon(flash)

    # ══════════════════════════════════════════════════════════════════════
    # AQUAMAN (1941)
    # ══════════════════════════════════════════════════════════════════════
    aquaman = _dc(
        name="Aquaman (animated history)",
        description=(
            "Arthur Curry — King of Atlantis, protector of the seas, and the "
            "most mocked member of the Super Friends. Aquaman has had a remarkable "
            "rehabilitation across animated history — from the limited Super Friends "
            "version whose powers seemed useless on land, to a genuinely powerful "
            "king in the DCAU. His 1967 Filmation series was actually quite popular "
            "and one of the earliest superhero TV cartoons. "
            "NOTE: DC Comics has always owned Aquaman — different studios "
            "produced animated versions under license."
        ),
        character_type="Human / Atlantean — DC Comics superhero / King of Atlantis",
        debut_year=1941,
        creators=[PAUL_NORRIS,
                  Creator("Mort Weisinger", "Aquaman co-creator / writer", 1915, 1978)],
        series_list=[
            Series("The Superman/Aquaman Hour of Adventure (Filmation)", 1967, 1968,
                   "Filmation Associates / CBS", "TV series", episode_count=36,
                   notes="PRODUCER: Filmation under DC license. One of the earliest Aquaman animated appearances. "
                         "Aquaman teamed with Aqualad and Mera against undersea threats."),
            Series("Super Friends (Aquaman as founding member)", 1973, 1986,
                   "Hanna-Barbera / ABC", "TV series",
                   notes="PRODUCER: Hanna-Barbera under DC license. Aquaman was an original Super Friend "
                         "but became infamous for limited usefulness in non-water situations. "
                         "His repeated cry of outrageous! became a pop culture touchstone."),
            Series("Justice League Unlimited (Aquaman appearances)", 2004, 2006,
                   "Warner Bros. Animation / Cartoon Network", "TV series",
                   notes="PRODUCER: Warner Bros. Animation. Aquaman appeared in select JLU episodes "
                         "as the king of Atlantis — a more serious and powerful portrayal."),
            Series("Batman: The Brave and the Bold (Aquaman)", 2008, 2011,
                   "Warner Bros. Animation / Cartoon Network", "TV series",
                   notes="PRODUCER: Warner Bros. Animation. John DiMaggio voiced an exuberantly joyful Aquaman — "
                         "widely considered the most fun Aquaman characterization ever. "
                         "OUTRAGEOUS! became his catchphrase."),
        ],
        eras=[
            Era(1967, 1972,
                "Filmation era — blue and orange classic costume, Atlantean king with Aqualad. "
                "PRODUCED BY: Filmation Associates.",
                art_style="Limited TV cel animation",
                image_url=IMG["aquaman"],
                notes="The Filmation Aquaman was more faithful to the Silver Age comics "
                      "than the later Super Friends version."),
            Era(1973, 1986,
                "Super Friends era — founding member but increasingly sidelined, "
                "outrageous! catchphrase, the infamous useless on land reputation. "
                "PRODUCED BY: Hanna-Barbera.",
                art_style="Hanna-Barbera limited TV animation",
                image_url=IMG["superfriends"],
                notes="Super Friends Aquaman became the template for years of Aquaman jokes. "
                      "His limited usefulness outside water became a running cultural reference."),
            Era(2008, None,
                "Brave and the Bold rehabilitation — John DiMaggio's joyfully bombastic performance "
                "reclaimed Aquaman as genuinely fun. PRODUCED BY: Warner Bros. Animation.",
                art_style="Silver Age-inspired digital animation",
                image_url=IMG["aquaman"],
                notes="Batman: The Brave and the Bold is credited with beginning Aquaman's "
                      "cultural rehabilitation before the Jason Momoa films completed it."),
        ],
        wiki_slug="Aquaman_in_other_media",
        origin="New York City, USA — DC Comics (character created 1941)",
    )
    lib.add_cartoon(aquaman)

    # ══════════════════════════════════════════════════════════════════════
    # GREEN LANTERN (1940)
    # ══════════════════════════════════════════════════════════════════════
    green_lantern = _dc(
        name="Green Lantern (animated history)",
        description=(
            "A space police officer wielding a power ring that can create anything "
            "the wearer can imagine, fueled by willpower. Multiple humans have held "
            "the title: Hal Jordan (Silver Age), John Stewart (DCAU — a significant "
            "representation milestone as a Black superhero lead), Kyle Rayner, and "
            "Guy Gardner. The DCAU's choice of John Stewart as the primary animated "
            "Green Lantern introduced millions of children to a Black superhero lead — "
            "one of animated television's most important representation decisions. "
            "NOTE: DC Comics has always owned Green Lantern."
        ),
        character_type="Human — DC Comics superhero / space police officer",
        debut_year=1940,
        creators=[MARTIN_NODELL,
                  Creator("Bill Finger", "Original Green Lantern writer", 1914, 1974),
                  Creator("John Broome", "Hal Jordan Green Lantern creator", 1913, 1999)],
        series_list=[
            Series("Super Friends (Green Lantern occasional)", 1973, 1986,
                   "Hanna-Barbera / ABC", "TV series",
                   notes="PRODUCER: Hanna-Barbera. Hal Jordan GL appeared occasionally in Super Friends. "
                         "Not a core member due to rights complications."),
            Series("Justice League / Justice League Unlimited", 2001, 2006,
                   "Warner Bros. Animation / Cartoon Network", "TV series",
                   notes="PRODUCER: Warner Bros. Animation. JOHN STEWART chosen as Green Lantern — "
                         "voiced by Phil LaMarr. One of the most significant representation decisions "
                         "in animated TV history. Introduced millions of children to a Black superhero lead. "
                         "John Stewart became more recognizable than Hal Jordan for an entire generation."),
            Series("Green Lantern: The Animated Series", 2011, 2013,
                   "Warner Bros. Animation / Cartoon Network", "TV series", episode_count=26,
                   notes="PRODUCER: Warner Bros. Animation. CGI series featuring Hal Jordan GL "
                         "patrolling the outer reaches of Guardian space. Critically acclaimed "
                         "but cancelled after one season alongside Young Justice."),
        ],
        eras=[
            Era(1973, 1986,
                "Super Friends occasional appearances — Hal Jordan, limited characterization. "
                "PRODUCED BY: Hanna-Barbera.",
                art_style="Hanna-Barbera limited TV animation",
                image_url=IMG["superfriends"],
                notes="Green Lantern was not a core Super Friends member. Rights issues "
                      "limited his appearances in the early seasons."),
            Era(2001, 2006,
                "DCAU Justice League era — JOHN STEWART as GL, Phil LaMarr's performance, "
                "landmark representation milestone. PRODUCED BY: Warner Bros. Animation.",
                art_style="DCAU flat color animation",
                image_url=IMG["justice"],
                notes="The decision to use John Stewart rather than Hal Jordan as the animated "
                      "Green Lantern is one of the most consequential choices in superhero animation. "
                      "A generation grew up believing John Stewart was THE Green Lantern."),
            Era(2011, None,
                "CGI era and beyond — Hal Jordan returns as lead in CGI series. "
                "PRODUCED BY: Warner Bros. Animation.",
                art_style="CGI animation",
                image_url=IMG["green"],
                notes="Green Lantern: The Animated Series was praised but cancelled. "
                      "Young Justice's simultaneous cancellation caused fan outcry "
                      "that led to both shows being revived on streaming."),
        ],
        wiki_slug="Green_Lantern_in_other_media",
        origin="New York City, USA — DC Comics (character created 1940)",
    )
    lib.add_cartoon(green_lantern)

    # ══════════════════════════════════════════════════════════════════════
    # ROBIN (1940)
    # ══════════════════════════════════════════════════════════════════════
    robin = _dc(
        name="Robin (animated history)",
        description=(
            "Batman's young ward and crime-fighting partner — the Boy Wonder. "
            "Multiple people have held the Robin identity: Dick Grayson (the original, "
            "who later became Nightwing), Jason Todd, Tim Drake, and Damian Wayne. "
            "In animation, Robin appeared alongside Batman in virtually every "
            "Batman animated series from 1968 onward. The DCAU's New Batman Adventures "
            "replaced Dick Grayson with Tim Drake and introduced a more mature "
            "take on the character. Teen Titans centered Dick Grayson's Robin "
            "as the team leader."
        ),
        character_type="Human — DC Comics superhero / Batman's partner",
        debut_year=1940,
        creators=[BOB_KANE, BILL_FINGER,
                  Creator("Jerry Robinson", "Robin co-creator", 1922, 2011)],
        series_list=[
            Series("The Batman/Superman Hour (Robin with Batman)", 1968, 1969,
                   "Filmation Associates / CBS", "TV series",
                   notes="PRODUCER: Filmation. Dick Grayson Robin alongside Adam West-influenced Batman."),
            Series("Super Friends (Robin as Batman's partner)", 1973, 1986,
                   "Hanna-Barbera / ABC", "TV series",
                   notes="PRODUCER: Hanna-Barbera. Robin appeared consistently alongside Batman "
                         "as his partner. Holy catchphrases Batman! tone matched the era."),
            Series("Batman: The Animated Series (Dick Grayson Robin)", 1992, 1995,
                   "Warner Bros. Animation / Fox Kids", "TV series",
                   notes="PRODUCER: Warner Bros. Animation. Loren Lester voiced Dick Grayson. "
                         "Robin was given genuine emotional depth and a complicated relationship with Batman."),
            Series("The New Batman Adventures (Tim Drake Robin)", 1997, 1999,
                   "Warner Bros. Animation / Kids WB", "TV series",
                   notes="PRODUCER: Warner Bros. Animation. Dick Grayson became Nightwing. "
                         "Tim Drake became the new Robin with a redesigned costume. "
                         "Mathew Valencia voiced Tim Drake."),
            Series("Teen Titans (Dick Grayson as team leader)", 2003, 2006,
                   "Warner Bros. Animation / Cartoon Network", "TV series",
                   notes="PRODUCER: Warner Bros. Animation. Scott Menville voiced Robin. "
                         "Dick Grayson leads the Teen Titans in this anime-influenced series. "
                         "The series ends with Robin becoming Nightwing implied but not shown."),
        ],
        eras=[
            Era(1968, 1986,
                "Classic sidekick era — Dick Grayson in red green and yellow, "
                "Holy [noun] Batman! exclamations, faithful comic adaptation. "
                "PRODUCED BY: Filmation then Hanna-Barbera.",
                art_style="Limited TV cel animation",
                image_url=IMG["batman"],
                notes="The Filmation and Super Friends Robin was based on the Silver Age Dick Grayson. "
                      "His famous exclamations became a cultural reference for the era."),
            Era(1992, 1999,
                "DCAU era — Dick Grayson then Tim Drake, genuine emotional complexity, "
                "strained relationship with Batman explored. PRODUCED BY: Warner Bros. Animation.",
                art_style="DCAU noir-influenced animation",
                image_url=IMG["batman"],
                notes="BTAS gave Robin genuine emotional depth for the first time in animation. "
                      "The transition to Tim Drake in New Batman Adventures reflected "
                      "the comics continuity of the era."),
            Era(2003, None,
                "Teen Titans era and beyond — Robin as team leader, "
                "anime-influenced style, path toward Nightwing. PRODUCED BY: Warner Bros. Animation.",
                art_style="Anime-influenced American digital animation",
                image_url=IMG["teen"],
                notes="Teen Titans centered Robin as the protagonist rather than Batman's sidekick — "
                      "a significant shift. The series implied his eventual evolution into Nightwing."),
        ],
        wiki_slug="Robin_(DC_Comics)#In_animation",
        origin="New York City, USA — DC Comics (character created 1940)",
    )
    lib.add_cartoon(robin)

    print(f"DC characters added. Library now has {len(lib.cartoons)} cartoons total.")
