"""File used to test functions defined in dictionary.py"""

__author__: str = "730464690"

import pytest
from exercises.ex03.dictionary import invert, favorite_color, count, bin_len

"""Tests for invert"""


def test_invert_use_case1():
    """Test inverting a simple dictionary"""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_edge_case():
    """Test inverting an empty dictionary"""
    assert invert({}) == {}


def test_invert_use_case2():
    """Test whether a KeyError is being raised"""
    with pytest.raises(KeyError):
        invert({"kris": "jordan", "michael": "jordan"})


"""Tests for count"""


def test_count_use_case1():
    """Test counting occurrences in list with repetition"""
    assert count(["red", "orange", "yellow", "orange", "red", "orange"]) == {
        "red": 2,
        "orange": 3,
        "yellow": 1,
    }


def test_count_edge_case():
    """Test counting an empty list"""
    assert count([]) == {}


def test_count_use_case2():
    """Test counting a completely normal list with one occurrence per entry"""
    assert count(["Hydrogen", "Lithium", "Sodium", "Potassium"]) == {
        "Hydrogen": 1,
        "Lithium": 1,
        "Sodium": 1,
        "Potassium": 1,
    }


"""Tests for favorite_color"""


def test_favorite_color_edge_case():
    """Test the function if there's a tie"""
    assert (
        favorite_color(
            {"Mason": "green", "Jack": "blue", "Mom": "blue", "Papa": "green"}
        )
        == "green"
    )


def test_favorite_color_use_case2():
    """Test the function if there's only one entry"""
    assert favorite_color({"Mason": "green"}) == "green"


def test_favorite_color_use_case1():
    """Test favorite color in a normal list"""
    assert (
        favorite_color(
            {"Mason": "green", "Jack": "blue", "Mom": "blue", "Trina": "yellow"}
        )
        == "blue"
    )


"""Tests for bin_len"""


def test_bin_len_edge_case():
    """Test bin length on an empty list"""
    assert bin_len([]) == {}


def test_bin_len_use_case1():
    """Test usage of bin length function when some words have the same length"""
    assert bin_len(["hello", "how", "are", "you"]) == {
        5: {"hello"},
        3: {"how", "are", "you"},
    }


def test_bin_len_use_case2():
    """Test usage of bin length function when all words have different lengths"""
    assert bin_len(["one", "four", "three", "if", "I", "eleven"]) == {
        3: {"one"},
        4: {"four"},
        5: {"three"},
        2: {"if"},
        1: {"I"},
        6: {"eleven"},
    }
