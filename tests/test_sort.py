"""
Test module.
"""
import pytest
from src.main import sort, PackageStack


class TestSort:
    """
    Test the sort function.
    """

    @pytest.mark.parametrize(
        "width, height, length, mass, expected, description",
        [
            # STANDARD cases
            (10.0, 10.0, 10, 5.0, PackageStack.STANDARD, "Small and light package"),
            (
                100.0,
                65.0,
                149,
                19.9,
                PackageStack.STANDARD,
                "Just below bulky/heavy thresholds",
            ),
            (
                20.0,
                30.0,
                40,
                10.0,
                PackageStack.STANDARD,
                "Small volume, all dimensions < 150, mass < 20",
            ),
            (0.0, 10.0, 10, 5.0, PackageStack.STANDARD, "Package with zero dimension"),
            (10.0, 10.0, 10, 0.0, PackageStack.STANDARD, "Package with zero mass"),
            # SPECIAL cases
            (
                100.0,
                100.0,
                100,
                15.0,
                PackageStack.SPECIAL,
                "Package exactly at volume threshold",
            ),
            (
                110.0,
                110.0,
                110,
                15.0,
                PackageStack.SPECIAL,
                "Package beyond volume threshold",
            ),
            (
                150.0,
                10.0,
                10,
                15.0,
                PackageStack.SPECIAL,
                "Package with width >= 150",
            ),
            (
                10.0,
                150.0,
                10,
                15.0,
                PackageStack.SPECIAL,
                "Package with height >= 150",
            ),
            (
                10.0,
                10.0,
                150,
                15.0,
                PackageStack.SPECIAL,
                "Package with length >= 150",
            ),
            (
                10.0,
                10.0,
                10,
                20.0,
                PackageStack.SPECIAL,
                "Package exactly at mass threshold",
            ),
            (
                10.0,
                10.0,
                10,
                25.0,
                PackageStack.SPECIAL,
                "Package beyond mass threshold",
            ),
            (
                100.0,
                100.0,
                100,
                0.0,
                PackageStack.SPECIAL,
                "Package bulky by volume but zero mass",
            ),
            (
                0.0,
                0.0,
                0,
                20.0,
                PackageStack.SPECIAL,
                "Package with zero dimensions but heavy",
            ),
            # REJECTED cases
            (
                100.0,
                100.0,
                100,
                20.0,
                PackageStack.REJECTED,
                "Package that is bulky by volume and heavy",
            ),
            (
                150.0,
                10.0,
                10,
                20.0,
                PackageStack.REJECTED,
                "Package that is bulky by width and heavy",
            ),
            (
                10.0,
                150.0,
                10,
                20.0,
                PackageStack.REJECTED,
                "Package that is bulky by height and heavy",
            ),
            (
                10.0,
                10.0,
                150,
                20.0,
                PackageStack.REJECTED,
                "Package that is bulky by length and heavy",
            ),
            (
                200.0,
                200.0,
                200,
                50.0,
                PackageStack.REJECTED,
                "Extremely bulky and heavy package",
            ),
        ],
    )
    def test_package_sorting(self, width, height, length, mass, expected, description):
        """Test package sorting with various dimensions and weights."""
        result = sort(width, height, length, mass)
        assert result == expected, f"Failed: {description}"
        assert isinstance(result, str), "Result should be a string"
