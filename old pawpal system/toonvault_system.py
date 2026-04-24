"""
ToonVault System - Core Logic Layer
Tracks 20th century cartoons (1900-2000) including version history,
copyright status, production methods, credits, and public domain images.
"""

from dataclasses import dataclass, field
from typing import Optional
import logging
import requests

# Configure logging
logging.basicConfig(
    filename="toonvault.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Copyright Status Constants
# ---------------------------------------------------------------------------
COPYRIGHT_PUBLIC_DOMAIN = "Public Domain"
COPYRIGHT_MIXED = "Mixed / Verify Case-by-Case"
COPYRIGHT_PROTECTED = "Copyrighted"

def determine_copyright_status(year: int) -> str:
    """Determine copyright status based on release year."""
    if year <= 1927:
        return COPYRIGHT_PUBLIC_DOMAIN
    elif year <= 1963:
        return COPYRIGHT_MIXED
    else:
        return COPYRIGHT_PROTECTED


# ---------------------------------------------------------------------------
# Production Method Constants
# ---------------------------------------------------------------------------
PRODUCTION_METHODS = [
    "Hand-drawn cel animation",
    "Watercolor / gouache painted backgrounds",
    "Rotoscoping (tracing live action)",
    "Stop motion / puppet animation",
    "Cutout animation",
    "Combination methods",
    "Computer-assisted animation",
    "Xerography (photocopied cels)",
    "Limited animation (TV style)",
    "Full animation (theatrical style)",
]


# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------

@dataclass
class Credit:
    """Represents a credited individual on a cartoon production."""
    name: str
    role: str  # e.g. "Director", "Animator", "Voice Actor", "Creator", "Producer"
    notes: str = ""

    def __str__(self):
        base = f"{self.name} ({self.role})"
        return f"{base} — {self.notes}" if self.notes else base


@dataclass
class CartoonVersion:
    """
    Represents a specific version or iteration of a cartoon at a point in time.
    Equivalent to PawPal's Task — a discrete, dateable record entry.
    """
    year: int
    title: str                          # Version title or episode name
    description: str                    # What changed or what this version represents
    production_method: str              # How it was made
    credits: list[Credit] = field(default_factory=list)
    image_url: str = ""                 # URL to a verified public domain image
    image_source: str = ""             # e.g. "Internet Archive", "Wikimedia Commons"
    image_license: str = ""            # e.g. "Public Domain", "CC0"
    notes: str = ""

    @property
    def copyright_status(self) -> str:
        """Auto-determine copyright status based on year."""
        return determine_copyright_status(self.year)

    @property
    def can_show_image(self) -> bool:
        """Only show images if public domain or mixed status with a verified source."""
        return self.copyright_status == COPYRIGHT_PUBLIC_DOMAIN and bool(self.image_url)

    def add_credit(self, name: str, role: str, notes: str = ""):
        """Add a credited individual to this version."""
        self.credits.append(Credit(name=name, role=role, notes=notes))
        logger.info(f"Added credit: {name} ({role}) to version {self.year} - {self.title}")

    def __str__(self):
        return (
            f"[{self.year}] {self.title} | {self.production_method} | "
            f"{self.copyright_status}"
        )


@dataclass
class Cartoon:
    """
    Represents a cartoon franchise, character, or series.
    Equivalent to PawPal's Pet — the main entity being tracked.
    """
    name: str                           # e.g. "Bugs Bunny", "Betty Boop"
    studio: str                         # e.g. "Warner Bros.", "Fleischer Studios"
    origin_year: int                    # Year first created/released
    country: str = "USA"
    genre: str = ""                     # e.g. "Slapstick", "Musical", "Adventure"
    versions: list[CartoonVersion] = field(default_factory=list)
    notes: str = ""

    @property
    def copyright_status(self) -> str:
        """Copyright status based on origin year."""
        return determine_copyright_status(self.origin_year)

    @property
    def era(self) -> str:
        """Return the animation era based on origin year."""
        if self.origin_year < 1928:
            return "Silent Era (1900–1927)"
        elif self.origin_year < 1935:
            return "Early Sound Era (1928–1934)"
        elif self.origin_year < 1946:
            return "Golden Age (1935–1945)"
        elif self.origin_year < 1964:
            return "Post-War Era (1946–1963)"
        elif self.origin_year < 1978:
            return "TV Animation Era (1964–1977)"
        elif self.origin_year < 1990:
            return "Saturday Morning Era (1978–1989)"
        else:
            return "Renaissance Era (1990–2000)"

    def add_version(self, version: CartoonVersion):
        """Add a new version/record to this cartoon's history."""
        self.versions.append(version)
        logger.info(f"Added version [{version.year}] to cartoon: {self.name}")

    def get_versions_sorted(self) -> list[CartoonVersion]:
        """Return versions sorted chronologically by year."""
        return sorted(self.versions, key=lambda v: v.year)

    def get_version_by_year(self, year: int) -> Optional[CartoonVersion]:
        """Retrieve a specific version by year."""
        matches = [v for v in self.versions if v.year == year]
        return matches[0] if matches else None

    def __str__(self):
        return f"{self.name} ({self.origin_year}) — {self.studio} | {self.era}"


@dataclass
class Researcher:
    """
    Represents a ToonVault user/researcher with a saved collection.
    Equivalent to PawPal's Owner.
    """
    name: str
    cartoons: list[Cartoon] = field(default_factory=list)

    def add_cartoon(self, cartoon: Cartoon):
        """Add a cartoon to this researcher's collection."""
        self.cartoons.append(cartoon)
        logger.info(f"Researcher '{self.name}' added cartoon: {cartoon.name}")

    def get_all_versions(self) -> list[tuple[Cartoon, CartoonVersion]]:
        """Return all versions across all cartoons as (cartoon, version) pairs."""
        result = []
        for cartoon in self.cartoons:
            for version in cartoon.versions:
                result.append((cartoon, version))
        return result

    def find_cartoon(self, name: str) -> Optional[Cartoon]:
        """Find a cartoon by name (case-insensitive)."""
        name_lower = name.lower()
        for cartoon in self.cartoons:
            if name_lower in cartoon.name.lower():
                return cartoon
        return None

    def __str__(self):
        return f"Researcher: {self.name} | Collection: {len(self.cartoons)} cartoons"


# ---------------------------------------------------------------------------
# Vault — The Brain (replaces Scheduler)
# ---------------------------------------------------------------------------

class Vault:
    """
    The central intelligence of ToonVault.
    Organizes, searches, filters, and analyzes the cartoon collection.
    Equivalent to PawPal's Scheduler.
    """

    def __init__(self, researcher: Researcher):
        self.researcher = researcher
        logger.info(f"Vault initialized for researcher: {researcher.name}")

    # --- Sorting ---

    def sort_by_year(self) -> list[tuple[Cartoon, CartoonVersion]]:
        """Sort all versions chronologically across the entire collection."""
        all_versions = self.researcher.get_all_versions()
        return sorted(all_versions, key=lambda pair: pair[1].year)

    def sort_by_name(self) -> list[Cartoon]:
        """Sort cartoons alphabetically by name."""
        return sorted(self.researcher.cartoons, key=lambda c: c.name.lower())

    # --- Filtering ---

    def filter_by_copyright(self, status: str) -> list[Cartoon]:
        """Filter cartoons by copyright status."""
        return [c for c in self.researcher.cartoons if c.copyright_status == status]

    def filter_by_era(self, era_keyword: str) -> list[Cartoon]:
        """Filter cartoons by era keyword (e.g. 'Golden', 'Silent')."""
        return [c for c in self.researcher.cartoons if era_keyword.lower() in c.era.lower()]

    def filter_by_studio(self, studio: str) -> list[Cartoon]:
        """Filter cartoons by studio name (case-insensitive)."""
        return [c for c in self.researcher.cartoons if studio.lower() in c.studio.lower()]

    def filter_by_year_range(self, start: int, end: int) -> list[Cartoon]:
        """Filter cartoons with origin year within a range."""
        return [c for c in self.researcher.cartoons if start <= c.origin_year <= end]

    # --- Duplicate / Conflict Detection ---

    def detect_duplicate_versions(self, cartoon: Cartoon) -> list[int]:
        """
        Detect if a cartoon has two versions with the same year.
        Returns list of duplicate years found.
        """
        years = [v.year for v in cartoon.versions]
        duplicates = [y for y in set(years) if years.count(y) > 1]
        if duplicates:
            logger.warning(f"Duplicate versions found in '{cartoon.name}': years {duplicates}")
        return duplicates

    def detect_all_duplicates(self) -> dict[str, list[int]]:
        """Check all cartoons for duplicate version years."""
        results = {}
        for cartoon in self.researcher.cartoons:
            dupes = self.detect_duplicate_versions(cartoon)
            if dupes:
                results[cartoon.name] = dupes
        return results

    # --- Image Retrieval (RAG Feature) ---

    def fetch_internet_archive_image(self, cartoon_name: str) -> dict:
        """
        Search Internet Archive for a public domain image of the cartoon.
        Returns image URL, source, and license info.
        """
        try:
            query = f"{cartoon_name} cartoon animation"
            url = (
                f"https://archive.org/advancedsearch.php"
                f"?q={requests.utils.quote(query)}"
                f"&mediatype=image&output=json&rows=5&fl[]=identifier,title,mediatype"
            )
            response = requests.get(url, timeout=8)
            response.raise_for_status()
            data = response.json()
            docs = data.get("response", {}).get("docs", [])
            if docs:
                identifier = docs[0].get("identifier", "")
                image_url = f"https://archive.org/download/{identifier}/{identifier}.jpg"
                logger.info(f"Found Internet Archive image for '{cartoon_name}': {image_url}")
                return {
                    "image_url": image_url,
                    "image_source": "Internet Archive",
                    "image_license": "Public Domain",
                    "identifier": identifier
                }
        except Exception as e:
            logger.error(f"Internet Archive fetch failed for '{cartoon_name}': {e}")
        return {}

    def fetch_wikimedia_image(self, cartoon_name: str) -> dict:
        """
        Search Wikimedia Commons for a public domain image.
        Returns image URL, source, and license info.
        """
        try:
            url = (
                f"https://en.wikipedia.org/api/rest_v1/page/summary/"
                f"{requests.utils.quote(cartoon_name.replace(' ', '_'))}"
            )
            response = requests.get(url, timeout=8)
            response.raise_for_status()
            data = response.json()
            thumbnail = data.get("thumbnail", {})
            if thumbnail:
                image_url = thumbnail.get("source", "")
                logger.info(f"Found Wikimedia image for '{cartoon_name}': {image_url}")
                return {
                    "image_url": image_url,
                    "image_source": "Wikimedia Commons / Wikipedia",
                    "image_license": "Verify on Wikimedia"
                }
        except Exception as e:
            logger.error(f"Wikimedia fetch failed for '{cartoon_name}': {e}")
        return {}

    def auto_fetch_image(self, cartoon: Cartoon, version: CartoonVersion) -> bool:
        """
        Attempt to auto-fetch a public domain image for a version.
        Only fetches for pre-1964 cartoons (likely public domain).
        Returns True if image was found and assigned.
        """
        if version.copyright_status == COPYRIGHT_PROTECTED:
            logger.info(f"Skipping image fetch for protected cartoon: {cartoon.name} ({version.year})")
            return False

        result = self.fetch_wikimedia_image(cartoon.name)
        if not result:
            result = self.fetch_internet_archive_image(cartoon.name)

        if result:
            version.image_url = result.get("image_url", "")
            version.image_source = result.get("image_source", "")
            version.image_license = result.get("image_license", "")
            return True
        return False

    # --- Summary & Reporting ---

    def collection_summary(self) -> dict:
        """Return a summary of the entire collection."""
        all_versions = self.researcher.get_all_versions()
        public_domain = len(self.filter_by_copyright(COPYRIGHT_PUBLIC_DOMAIN))
        mixed = len(self.filter_by_copyright(COPYRIGHT_MIXED))
        protected = len(self.filter_by_copyright(COPYRIGHT_PROTECTED))
        return {
            "total_cartoons": len(self.researcher.cartoons),
            "total_versions": len(all_versions),
            "public_domain": public_domain,
            "mixed_status": mixed,
            "copyrighted": protected,
            "duplicates_detected": len(self.detect_all_duplicates()),
        }

    def get_evolution_timeline(self, cartoon: Cartoon) -> list[dict]:
        """
        Return a structured timeline of a cartoon's visual/production evolution.
        """
        timeline = []
        sorted_versions = cartoon.get_versions_sorted()
        for i, version in enumerate(sorted_versions):
            entry = {
                "year": version.year,
                "title": version.title,
                "description": version.description,
                "production_method": version.production_method,
                "copyright_status": version.copyright_status,
                "credits": [str(c) for c in version.credits],
                "image_url": version.image_url if version.can_show_image else "",
                "image_source": version.image_source,
                "change_from_previous": (
                    f"Evolution from {sorted_versions[i-1].year}"
                    if i > 0 else "Original version"
                )
            }
            timeline.append(entry)
        return timeline
