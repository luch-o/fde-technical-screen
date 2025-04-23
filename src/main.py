"""
Sort packages into a package stack.
"""
from enum import StrEnum

MAX_VOLUME = 1_000_000
MAX_DIMENSION = 150
MAX_MASS = 20


class PackageStack(StrEnum):
    """
    Supported package stacks.
    """

    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"


def sort(width: float, height: float, length: int, mass: float) -> str:
    """
    Sort the package into a package stack.
    Args:
        width: float - The width of the package in cm.
        height: float - The height of the package in cm.
        length: int - The length of the package in cm.
        mass: float - The mass of the package in kg.
    Returns:
        str: The package stack.
    """
    volume = width * height * length
    bulky = any(
        (
            volume >= MAX_VOLUME,
            width >= MAX_DIMENSION,
            height >= MAX_DIMENSION,
            length >= MAX_DIMENSION,
        )
    )
    heavy = mass >= MAX_MASS
    if bulky and heavy:
        return PackageStack.REJECTED
    if bulky or heavy:
        return PackageStack.SPECIAL
    return PackageStack.STANDARD
