from app import percentage
import pytest

@pytest.mark.parametrize("classes_conducted,total_classes,expected", [
    (10, 10, 100),
    (0, 10, 0),
    (5, 10, 50)
])
def test_percentage(classes_conducted, total_classes, expected):
    assert percentage(classes_conducted, total_classes) == expected
