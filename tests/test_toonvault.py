"""
ToonVault — Automated Test Suite
Run: python -m pytest tests/test_toonvault.py -v
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from toonvault_system import (
    Researcher, Cartoon, CartoonVersion, Credit, Vault,
    COPYRIGHT_PUBLIC_DOMAIN, COPYRIGHT_MIXED, COPYRIGHT_PROTECTED,
    determine_copyright_status
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def sample_version_1928():
    v = CartoonVersion(
        year=1928,
        title="Steamboat Willie",
        description="First Mickey Mouse with synchronized sound.",
        production_method="Hand-drawn cel animation"
    )
    return v

@pytest.fixture
def sample_version_1990():
    v = CartoonVersion(
        year=1990,
        title="Modern Cartoon",
        description="A modern era cartoon.",
        production_method="Computer-assisted animation"
    )
    return v

@pytest.fixture
def sample_cartoon():
    cartoon = Cartoon(
        name="Felix the Cat",
        studio="Pat Sullivan Studio",
        origin_year=1919,
        country="USA",
        genre="Slapstick"
    )
    v1 = CartoonVersion(year=1919, title="Original", description="First appearance",
                        production_method="Hand-drawn cel animation")
    v2 = CartoonVersion(year=1958, title="TV Redesign", description="TV era design",
                        production_method="Limited animation (TV style)")
    v3 = CartoonVersion(year=1928, title="Sound Era", description="Sound transition",
                        production_method="Hand-drawn cel animation")
    cartoon.add_version(v1)
    cartoon.add_version(v2)
    cartoon.add_version(v3)
    return cartoon

@pytest.fixture
def sample_researcher(sample_cartoon):
    researcher = Researcher(name="Test Researcher")
    researcher.add_cartoon(sample_cartoon)
    return researcher

@pytest.fixture
def vault(sample_researcher):
    return Vault(sample_researcher)


# ---------------------------------------------------------------------------
# Copyright Status Tests
# ---------------------------------------------------------------------------

def test_copyright_pre_1928_is_public_domain():
    assert determine_copyright_status(1919) == COPYRIGHT_PUBLIC_DOMAIN

def test_copyright_1927_is_public_domain():
    assert determine_copyright_status(1927) == COPYRIGHT_PUBLIC_DOMAIN

def test_copyright_1928_is_mixed():
    assert determine_copyright_status(1928) == COPYRIGHT_MIXED

def test_copyright_1963_is_mixed():
    assert determine_copyright_status(1963) == COPYRIGHT_MIXED

def test_copyright_1964_is_protected():
    assert determine_copyright_status(1964) == COPYRIGHT_PROTECTED

def test_copyright_2000_is_protected():
    assert determine_copyright_status(2000) == COPYRIGHT_PROTECTED

def test_version_copyright_property(sample_version_1928):
    assert sample_version_1928.copyright_status == COPYRIGHT_MIXED

def test_version_copyright_protected(sample_version_1990):
    assert sample_version_1990.copyright_status == COPYRIGHT_PROTECTED


# ---------------------------------------------------------------------------
# Image Display Tests
# ---------------------------------------------------------------------------

def test_can_show_image_false_when_no_url():
    v = CartoonVersion(year=1920, title="Test", description="Test",
                       production_method="Hand-drawn cel animation")
    assert v.can_show_image is False

def test_can_show_image_false_when_protected():
    v = CartoonVersion(year=1990, title="Test", description="Test",
                       production_method="Hand-drawn cel animation",
                       image_url="http://example.com/image.jpg")
    assert v.can_show_image is False

def test_can_show_image_true_when_public_domain_with_url():
    v = CartoonVersion(year=1920, title="Test", description="Test",
                       production_method="Hand-drawn cel animation",
                       image_url="http://example.com/image.jpg")
    assert v.can_show_image is True


# ---------------------------------------------------------------------------
# Credit Tests
# ---------------------------------------------------------------------------

def test_add_credit_increases_count():
    v = CartoonVersion(year=1930, title="Test", description="Test",
                       production_method="Hand-drawn cel animation")
    assert len(v.credits) == 0
    v.add_credit("Otto Messmer", "Animator")
    assert len(v.credits) == 1

def test_credit_str_with_notes():
    c = Credit(name="Tex Avery", role="Director", notes="Looney Tunes legend")
    assert "Tex Avery" in str(c)
    assert "Director" in str(c)
    assert "Looney Tunes legend" in str(c)

def test_credit_str_without_notes():
    c = Credit(name="Mel Blanc", role="Voice Actor")
    result = str(c)
    assert "Mel Blanc" in result
    assert "Voice Actor" in result


# ---------------------------------------------------------------------------
# Cartoon Tests
# ---------------------------------------------------------------------------

def test_cartoon_era_silent(sample_cartoon):
    assert "Silent" in sample_cartoon.era

def test_cartoon_add_version_increases_count(sample_cartoon):
    initial = len(sample_cartoon.versions)
    new_version = CartoonVersion(year=1940, title="New Version", description="Test",
                                  production_method="Hand-drawn cel animation")
    sample_cartoon.add_version(new_version)
    assert len(sample_cartoon.versions) == initial + 1

def test_cartoon_get_versions_sorted(sample_cartoon):
    sorted_versions = sample_cartoon.get_versions_sorted()
    years = [v.year for v in sorted_versions]
    assert years == sorted(years)

def test_cartoon_get_version_by_year(sample_cartoon):
    version = sample_cartoon.get_version_by_year(1919)
    assert version is not None
    assert version.title == "Original"

def test_cartoon_get_version_by_year_not_found(sample_cartoon):
    version = sample_cartoon.get_version_by_year(9999)
    assert version is None

def test_cartoon_copyright_public_domain(sample_cartoon):
    assert sample_cartoon.copyright_status == COPYRIGHT_PUBLIC_DOMAIN


# ---------------------------------------------------------------------------
# Researcher Tests
# ---------------------------------------------------------------------------

def test_researcher_add_cartoon(sample_researcher):
    initial = len(sample_researcher.cartoons)
    new_cartoon = Cartoon(name="Popeye", studio="Fleischer Studios",
                          origin_year=1933)
    sample_researcher.add_cartoon(new_cartoon)
    assert len(sample_researcher.cartoons) == initial + 1

def test_researcher_find_cartoon(sample_researcher):
    result = sample_researcher.find_cartoon("Felix")
    assert result is not None
    assert "Felix" in result.name

def test_researcher_find_cartoon_not_found(sample_researcher):
    result = sample_researcher.find_cartoon("Nonexistent Cartoon XYZ")
    assert result is None

def test_researcher_get_all_versions(sample_researcher, sample_cartoon):
    all_versions = sample_researcher.get_all_versions()
    assert len(all_versions) == len(sample_cartoon.versions)


# ---------------------------------------------------------------------------
# Vault Tests
# ---------------------------------------------------------------------------

def test_vault_sort_by_year(vault):
    sorted_pairs = vault.sort_by_year()
    years = [v.year for _, v in sorted_pairs]
    assert years == sorted(years)

def test_vault_sort_by_name(vault):
    sorted_cartoons = vault.sort_by_name()
    names = [c.name.lower() for c in sorted_cartoons]
    assert names == sorted(names)

def test_vault_filter_by_copyright_public_domain(vault):
    results = vault.filter_by_copyright(COPYRIGHT_PUBLIC_DOMAIN)
    assert all(c.copyright_status == COPYRIGHT_PUBLIC_DOMAIN for c in results)

def test_vault_filter_by_era(vault):
    results = vault.filter_by_era("Silent")
    assert len(results) >= 1

def test_vault_filter_by_studio(vault):
    results = vault.filter_by_studio("Sullivan")
    assert len(results) >= 1

def test_vault_filter_by_year_range(vault):
    results = vault.filter_by_year_range(1900, 1930)
    assert all(1900 <= c.origin_year <= 1930 for c in results)

def test_vault_detect_no_duplicates(vault, sample_cartoon):
    dupes = vault.detect_duplicate_versions(sample_cartoon)
    assert dupes == []

def test_vault_detect_duplicate_versions():
    cartoon = Cartoon(name="Test Toon", studio="Test Studio", origin_year=1930)
    v1 = CartoonVersion(year=1930, title="Version A", description="First",
                        production_method="Hand-drawn cel animation")
    v2 = CartoonVersion(year=1930, title="Version B", description="Duplicate year",
                        production_method="Hand-drawn cel animation")
    cartoon.add_version(v1)
    cartoon.add_version(v2)
    researcher = Researcher(name="Test")
    researcher.add_cartoon(cartoon)
    vault = Vault(researcher)
    dupes = vault.detect_duplicate_versions(cartoon)
    assert 1930 in dupes

def test_vault_collection_summary(vault):
    summary = vault.collection_summary()
    assert "total_cartoons" in summary
    assert "total_versions" in summary
    assert summary["total_cartoons"] >= 1

def test_vault_evolution_timeline(vault, sample_cartoon):
    timeline = vault.get_evolution_timeline(sample_cartoon)
    assert len(timeline) == len(sample_cartoon.versions)
    years = [entry["year"] for entry in timeline]
    assert years == sorted(years)

def test_vault_timeline_first_entry_is_original(vault, sample_cartoon):
    timeline = vault.get_evolution_timeline(sample_cartoon)
    assert timeline[0]["change_from_previous"] == "Original version"

def test_vault_timeline_subsequent_entries_show_evolution(vault, sample_cartoon):
    timeline = vault.get_evolution_timeline(sample_cartoon)
    assert "Evolution from" in timeline[1]["change_from_previous"]
