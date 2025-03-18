#calculatebmi.py
import unittest
from unittest.mock import patch
import pytest
from calculatebmi import convert_height_to_meters, convert_weight_to_kg, calculate_bmi, bmi_category, main

@pytest.mark.parametrize( "weight, conversion", [
    (1, 0.45),
    (1.1, 0.495),
    (125, 56.25),
    (1000, 450),
])
def test_convert_weight_to_kg(weight, conversion):
    assert convert_weight_to_kg (weight) ==  pytest.approx(conversion, rel=1e-3) # Pytest documentation

# ensure out of bounds test cases are caught and fail!
@pytest.mark.parametrize("weight", [
    0, -1, -10
])
def test_invalid_weight(weight):
    with pytest.raises(ValueError):
        convert_weight_to_kg(weight)

@pytest.mark.parametrize( "ft, inches, conversion", [
    (0, 1, 0.025),
    (0, 2, 0.05),
    (5, 3, 1.575),
    (10, 10, 3.25),
    (10, 11, 3.275),
])
def test_convert_height_to_meters(ft, inches, conversion):
    assert convert_height_to_meters(ft, inches) == pytest.approx(conversion, rel=1e-3)

@pytest.mark.parametrize("ft, inches", [
    (5,12),
    (10, 14),
])
def test_invalid_height(ft, inches):
    with pytest.raises(ValueError):
        convert_height_to_meters(ft, inches)

@pytest.mark.parametrize("weight, ft, inches, expected", [
    (125, 5, 3, 22.7),
    (165, 5, 8, 25.7),
    (90, 5, 5, 15.3),
    (200, 5, 11, 28.6),
    (250, 5, 0, 50),
])
def test_calculate_bmi(weight, ft, inches, expected):
    assert calculate_bmi(weight, ft, inches) == pytest.approx(expected, rel=1e-1)

@pytest.mark.parametrize("bmi, category",[
(18.0, "Underweight"),
(18.4, "Underweight"),
(18.5, "Normal weight"),
(20, "Normal weight"),
(24.9, "Normal weight"),
(25, "Overweight"),
(29.9, "Overweight"),
(30, "Obese"),
])
def test_bmi_category(bmi, category):
    assert bmi_category(bmi) == category
