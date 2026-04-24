"""
cartoon_system.py
CartoonPal — core logic layer.
All classes follow OOP principles mirroring the original PawPal architecture.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ─────────────────────────────────────────────────────────────────────────────
# CREATOR
# The individual human(s) who created or co-created the character.
# Separate from the studio — many creators had no ownership rights at all.
# ─────────────────────────────────────────────────────────────────────────────
@dataclass
class Creator:
    """A human creator — the person who conceived, designed, or animated the character."""
    full_name: str
    role: str                        # e.g. "Character designer", "Writer", "Director"
    birth_year: Optional[int] = None
    death_year: Optional[int] = None

    def __str__(self):
        return f"{self.full_name} ({self.role})"


# ─────────────────────────────────────────────────────────────────────────────
# PRODUCTION COMPANY
# The studio that produced the cartoon.
# Separate from ownership — the producer may never have held the copyright.
# ─────────────────────────────────────────────────────────────────────────────
@dataclass
class ProductionCompany:
    """The studio or company that physically produced the cartoon."""
    company_name: str
    founded_year: Optional[int] = None
    country: str = "USA"
    still_active: bool = True

    def __str__(self):
        status = "active" if self.still_active else "defunct"
        return f"{self.company_name} ({status})"


# ─────────────────────────────────────────────────────────────────────────────
# SERIES
# One distinct production run. A character (Bugs Bunny, Mickey) typically
# appears across many separate series over the decades.
# ─────────────────────────────────────────────────────────────────────────────
@dataclass
class Series:
    """One distinct animated series or production run for a cartoon character."""
    title: str
    year_started: int
    year_ended: Optional[int]        # None = still airing
    produced_by: str                 # Studio name for this specific run
    medium: str = "theatrical short" # e.g. theatrical short, TV series, streaming
    episode_count: Optional[int] = None
    notes: str = ""

    @property
    def duration_label(self) -> str:
        end = str(self.year_ended) if self.year_ended else "present"
        years = (self.year_ended or datetime.now().year) - self.year_started
        return f"{self.year_started}–{end} ({years} yrs)"

    def __str__(self):
        return f"{self.title} | {self.duration_label} | {self.medium}"


# ─────────────────────────────────────────────────────────────────────────────
# OWNERSHIP RECORD
# One entry in the chain of ownership from original creation to today.
# "Original owner" = who held rights at first creation/publication.
# "Current owner" = is_current_owner=True entry.
# ─────────────────────────────────────────────────────────────────────────────
@dataclass
class OwnershipRecord:
    """One link in the ownership chain of a cartoon property."""
    owner_name: str
    year_acquired: int
    year_relinquished: Optional[int]   # None if still held
    acquisition_method: str            # "original creation", "purchase", "merger", etc.
    is_current_owner: bool = False
    notes: str = ""

    def __str__(self):
        end = str(self.year_relinquished) if self.year_relinquished else "present"
        tag = " ← CURRENT" if self.is_current_owner else ""
        return f"{self.owner_name} ({self.year_acquired}–{end}) via {self.acquisition_method}{tag}"


# ─────────────────────────────────────────────────────────────────────────────
# ERA
# A distinct visual period in a character's history.
# Used to build the image timeline in the UI.
# ─────────────────────────────────────────────────────────────────────────────
@dataclass
class Era:
    """A visual snapshot of a cartoon character during a specific time period."""
    year_start: int
    year_end: Optional[int]            # None = current look
    visual_description: str
    art_style: str = ""                # e.g. "black & white", "Technicolor", "CGI"
    image_url: str = ""                # URL to a representative image
    notes: str = ""

    def __str__(self):
        end = str(self.year_end) if self.year_end else "present"
        return f"{self.year_start}–{end}: {self.visual_description}"


# ─────────────────────────────────────────────────────────────────────────────
# CARTOON
# Central model. Holds full provenance: who created it, what studio produced
# it, every series it appeared in, complete ownership chain, and visual eras.
# ─────────────────────────────────────────────────────────────────────────────
@dataclass
class Cartoon:
    """
    A cartoon character or franchise with complete provenance.

    Tracks:
      - What the cartoon is (description, type)
      - Who created it (individual creators)
      - What company produced it (original studio)
      - Every series it appeared in (series_list)
      - Who owned it originally and who owns it now (ownership_history)
      - How it looked across the decades (eras)
    """

    # Identity
    name: str
    description: str
    character_type: str                # e.g. "anthropomorphic animal", "human child"
    country_of_origin: str = "USA"
    debut_year: int = 0

    # Human creators (can be multiple)
    creators: list[Creator] = field(default_factory=list)

    # The studio that originally produced it
    original_studio: Optional[ProductionCompany] = None

    # Every series this character appeared in, sorted by year
    series_list: list[Series] = field(default_factory=list)

    # Full ownership chain from first to current
    ownership_history: list[OwnershipRecord] = field(default_factory=list)

    # Visual history — how the character looked over time
    eras: list[Era] = field(default_factory=list)

    # Where it was created and Wikipedia reference
    origin_location: str = ""
    wiki_url: str = ""

    # ── Computed properties ────────────────────────────────────────────────

    @property
    def original_owner(self) -> Optional[OwnershipRecord]:
        """The very first ownership record."""
        return min(self.ownership_history, key=lambda o: o.year_acquired, default=None)

    @property
    def current_owner(self) -> Optional[OwnershipRecord]:
        """The current rights holder (is_current_owner=True)."""
        return next((o for o in self.ownership_history if o.is_current_owner), None)

    @property
    def ownership_changed(self) -> bool:
        """True if the property changed hands at any point."""
        if not self.ownership_history:
            return False
        orig = self.original_owner
        curr = self.current_owner
        if orig and curr:
            return orig.owner_name != curr.owner_name
        return len(self.ownership_history) > 1

    @property
    def is_public_domain(self) -> bool:
        """
        US copyright determination:
        - Published before 1928: public domain.
        - Corporate-owned works: protected 95 years from first publication.
        - No current owner on record: treated as public domain.
        """
        if self.current_owner is None:
            return True
        return self.debut_year < (datetime.now().year - 95)

    @property
    def copyright_status(self) -> str:
        if self.is_public_domain:
            return "Public Domain"
        owner = self.current_owner
        return f"Protected — © {owner.owner_name}" if owner else "Status unknown"

    @property
    def years_until_public_domain(self) -> int:
        if self.is_public_domain:
            return 0
        pd_year = self.debut_year + 95
        return max(0, pd_year - datetime.now().year)

    @property
    def copyright_badge(self) -> str:
        """Short badge string for UI display."""
        if self.is_public_domain:
            return "PUBLIC DOMAIN"
        yrs = self.years_until_public_domain
        if yrs <= 10:
            return f"PROTECTED (~{yrs} yrs left)"
        return "PROTECTED"

    # ── Mutation methods ───────────────────────────────────────────────────

    def add_creator(self, creator: Creator):
        """Add a human creator to this cartoon."""
        self.creators.append(creator)
        logging.info(f"[{self.name}] Added creator: {creator.full_name}")

    def add_series(self, series: Series):
        """Add a production series and keep sorted by start year."""
        self.series_list.append(series)
        self.series_list.sort(key=lambda s: s.year_started)
        logging.info(f"[{self.name}] Added series: {series.title}")

    def add_ownership_record(self, record: OwnershipRecord):
        """
        Add an ownership record.
        If the new record is marked current, all others are de-flagged.
        """
        if record.is_current_owner:
            for existing in self.ownership_history:
                existing.is_current_owner = False
        self.ownership_history.append(record)
        self.ownership_history.sort(key=lambda o: o.year_acquired)
        logging.info(f"[{self.name}] Added ownership: {record.owner_name}")

    def add_era(self, era: Era):
        """Add a visual era and keep sorted by start year."""
        self.eras.append(era)
        self.eras.sort(key=lambda e: e.year_start)
        logging.info(f"[{self.name}] Added era: {era.year_start}")

    def get_era_at(self, year: int) -> Optional[Era]:
        """Return the visual era active during a given year."""
        for era in reversed(self.eras):
            if era.year_start <= year:
                return era
        return None

    def summary(self) -> str:
        """Multi-line summary string for CLI display."""
        orig = self.original_owner.owner_name if self.original_owner else "Unknown"
        curr = self.current_owner.owner_name if self.current_owner else "Public domain / unknown"
        creator_names = ", ".join(c.full_name for c in self.creators) or "Unknown"
        studio = self.original_studio.company_name if self.original_studio else "Unknown"
        return (
            f"\n{'─'*56}\n"
            f"  {self.name}  ({self.debut_year})\n"
            f"{'─'*56}\n"
            f"  What it is    : {self.description}\n"
            f"  Type          : {self.character_type}\n"
            f"  Country       : {self.country_of_origin}\n"
            f"  Creator(s)    : {creator_names}\n"
            f"  Original studio: {studio}\n"
            f"  Original owner : {orig}\n"
            f"  Current owner  : {curr}\n"
            f"  Copyright      : {self.copyright_status}\n"
            f"  Series         : {len(self.series_list)} run(s)\n"
            f"  Visual eras    : {len(self.eras)}"
        )


# ─────────────────────────────────────────────────────────────────────────────
# LIBRARY
# Manages the full collection of Cartoon records.
# ─────────────────────────────────────────────────────────────────────────────
class Library:
    """Manages a searchable, filterable collection of Cartoon records."""

    def __init__(self):
        self.cartoons: list[Cartoon] = []

    def add_cartoon(self, cartoon: Cartoon):
        self.cartoons.append(cartoon)
        logging.info(f"Library: added '{cartoon.name}'")

    def find(self, name: str) -> Optional[Cartoon]:
        """Case-insensitive partial name search."""
        name_lower = name.lower().strip()
        return next((c for c in self.cartoons if name_lower in c.name.lower()), None)

    def all_public_domain(self) -> list[Cartoon]:
        return [c for c in self.cartoons if c.is_public_domain]

    def all_protected(self) -> list[Cartoon]:
        return [c for c in self.cartoons if not c.is_public_domain]

    def filter_by_studio(self, studio: str) -> list[Cartoon]:
        return [
            c for c in self.cartoons
            if c.original_studio and studio.lower() in c.original_studio.company_name.lower()
        ]

    def filter_by_creator(self, name: str) -> list[Cartoon]:
        return [
            c for c in self.cartoons
            if any(name.lower() in cr.full_name.lower() for cr in c.creators)
        ]

    def filter_by_decade(self, decade: int) -> list[Cartoon]:
        """Return cartoons that debuted in a given decade, e.g. 1930 for the 1930s."""
        return [c for c in self.cartoons if decade <= c.debut_year < decade + 10]


# ─────────────────────────────────────────────────────────────────────────────
# CARTOON ANALYZER
# Sorting, filtering, copyright analysis, and flagging.
# ─────────────────────────────────────────────────────────────────────────────
class CartoonAnalyzer:
    """Analyzes, sorts, and flags cartoons in a Library."""

    def __init__(self, library: Library):
        self.library = library

    def sort_by_debut(self, ascending: bool = True) -> list[Cartoon]:
        return sorted(self.library.cartoons, key=lambda c: c.debut_year, reverse=not ascending)

    def sort_by_name(self) -> list[Cartoon]:
        return sorted(self.library.cartoons, key=lambda c: c.name.lower())

    def get_copyright_summary(self) -> dict:
        total = len(self.library.cartoons)
        pd = len(self.library.all_public_domain())
        return {
            "total": total,
            "public_domain": pd,
            "protected": total - pd,
            "pd_percent": round(pd / total * 100, 1) if total else 0,
        }

    def flag_approaching_public_domain(self, within_years: int = 15) -> list[Cartoon]:
        """Protected cartoons that will enter public domain within N years."""
        return [
            c for c in self.library.cartoons
            if not c.is_public_domain and 0 < c.years_until_public_domain <= within_years
        ]

    def ownership_changed_cartoons(self) -> list[Cartoon]:
        """Cartoons where current owner differs from original owner."""
        return [c for c in self.library.cartoons if c.ownership_changed]

    def detect_series_overlap(self, cartoon: Cartoon) -> list[tuple[Series, Series]]:
        """
        Detect if any two series for this cartoon ran at the same time.
        Returns list of conflicting pairs.
        """
        conflicts = []
        series = cartoon.series_list
        for i in range(len(series)):
            for j in range(i + 1, len(series)):
                a, b = series[i], series[j]
                a_end = a.year_ended or datetime.now().year
                b_end = b.year_ended or datetime.now().year
                if a.year_started <= b_end and b.year_started <= a_end:
                    conflicts.append((a, b))
        return conflicts