import math

def convert_weight_to_kg(weight):
    if weight <=0:
        raise ValueError("Weight must be greater than 0.")
    return weight * 0.45

def convert_height_to_meters(height_ft, height_in):
    if height_in >= 12:
        raise ValueError("Inches must fall between 0 and 11.")
    total_in = (height_ft * 12) + height_in
    return total_in * 0.025

def calculate_bmi(weight, height_ft, height_in):
    weight_kg = convert_weight_to_kg(weight)
    height_m = convert_height_to_meters(height_ft, height_in)

    if height_m == 0:
        raise ValueError("Height cannot be zero")
    
    return weight_kg / (height_m ** 2)

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
    print("\nWelcome to BMI Calculator. Let's Begin!\n")

    try:
        height = input("Enter a height(ft' in): ").split("'")
        weight = float(input("Enter a weight(Ibs): "))
    
        if len(height) != 2:
            print("Invalid height format. Use format: 5'10")

        feet = int(height[0].strip())
        inches = int(height[1].strip())
        bmi = round(calculate_bmi(weight, feet, inches),1)
        category = bmi_category(bmi)
        print(f"The BMI for a person who is {feet}'{inches} and weighs {weight} Ibs is {bmi}.")
        print(f"With this BMI, they would be categorized as {category}.\n")

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()