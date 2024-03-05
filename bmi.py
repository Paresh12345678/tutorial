def calculate_bmi(weight_kg, height_m):
    """
    Calculate the Body Mass Index (BMI) given weight in kilograms and height in meters.
    BMI = weight / (height^2)
    """
    bmi = weight_kg / (height_m ** 2)
    return bmi

def main():
    # Get user input for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Print the BMI and corresponding category
    print("Your BMI is: {:.2f}".format(bmi))
    if bmi < 18.5:
        print("You are underweight.")
    elif bmi < 25:
        print("You are normal weight.")
    elif bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")

if __name__ == "__main__":
    main()
