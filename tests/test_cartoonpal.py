import pytest
from cartoon_system import Cartoon, Creator, Series, OwnershipRecord, Era, Library, CartoonAnalyzer
from seed_data import build_library

def test_library_loads():
    lib = build_library()
    assert len(lib.cartoons) >= 4

def test_find_cartoon():
    lib = build_library()
    assert lib.find("bugs") is not None

def test_copyright_status():
    lib = build_library()
    bugs = lib.find("bugs")
    assert not bugs.is_public_domain

def test_public_domain():
    lib = build_library()
    felix = lib.find("felix")
    assert felix.is_public_domain

def test_sort_by_debut():
    lib = build_library()
    analyzer = CartoonAnalyzer(lib)
    sorted_list = analyzer.sort_by_debut()
    years = [c.debut_year for c in sorted_list]
    assert years == sorted(years)
