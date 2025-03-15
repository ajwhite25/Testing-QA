import math

def convert_weight_to_kg(weight):
    return weight * 0.45

def convert_height_to_meters(height_ft, height_in):
    total_in = (height_ft * 12) + height_in
    return total_in * 0.025

def calculate_bmi(weight, height_ft, height_in):
    pass

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        return "Normal weight"
    elif bmi >= 25 and bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    pass

if __name__ == "__main__":
    main()