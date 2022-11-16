from leapyears import is_leap_year
import pytest


@pytest.mark.parametrize(
    "year, expected",
    [
        (2000, True),
        (400, True),
        (1600, True),
    ],
)
def test_should_be_leap_year_when_year_is_divisible_by_400(year, expected):
    actual = is_leap_year(year)
    assert actual == expected


@pytest.mark.parametrize(
    "year, expected",
    [
        (1700, False),
        (1800, False),
        (1900, False),
    ],
)
def test_should_not_be_leap_year_when_year_is_divisible_by_100_but_not_by_400(
    year, expected
):
    actual = is_leap_year(year)
    assert actual == expected


@pytest.mark.parametrize(
    "year, expected",
    [
        (2008, True),
        (2012, True),
        (2016, True),
    ],
)
def test_should_be_leap_year_when_year_is_divisible_by_4_but_not_by_100(year, expected):
    actual = is_leap_year(year)
    assert actual == expected


@pytest.mark.parametrize(
    "year, expected",
    [
        (2017, False),
        (2018, False),
        (2019, False),
    ],
)
def test_should_not_be_leap_year_when_year_is_not_divisible_by_4(year, expected):
    actual = is_leap_year(year)
    assert actual == expected
