"""
Test Sample Functions
"""
import pytest

from sample import add, sub


@pytest.mark.parametrize(
    ("x", "y", "z"),
    [
        (1, 2, 3),
        (0, 1, 1),
    ],
)
def test_add(x: int, y: int, z: int) -> None:
    """
    Test add
    """
    assert z == add(x, y)


@pytest.mark.parametrize(
    ("x", "y", "z"),
    [
        (3, 2, 1),
        (1, 0, 1),
    ],
)
def test_sub(x: int, y: int, z: int) -> None:
    """
    Test Sub
    """
    assert z == sub(x, y)
