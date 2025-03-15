#bmi.py
from unittest.mock import patch
import pytest
from calculatebmi import convert_height_to_meters, convert_weight_to_kg, calculate_bmi, bmi_category

def test_convert_weight_to_kg(weight, conversion):
    assert convert_weight_to_kg (weight) == conversion

def test_convert_height_to_meters(height_ft, height_in, conversion):
    assert convert_height_to_meters(height_ft, height_in) == conversion

def test_calculate_bmi(weight, height_ft, height_in):
    pass

@pytest.mark.parametrize("bmi, category",[
(18.0, "Underweight"),
(18.4, "Underweight"),
(18.5, "Normal weight"),
(20, "Normal weight"),
(25, "Overweight"),
(30, "Obese"),
])
def test_bmi_category(bmi, category):
    assert bmi_category(bmi) == category