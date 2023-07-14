# Databricks notebook source
bmiindex = -1

# Loop until a valid BMI index is provided
while bmiindex < 0:
    # In this area your input the your weight in lbs
    weight = float(input("Enter the weight in pounds: "))
    # In this area your input the your height in inches
    height = float(input("Enter the height in inches: "))
    # Calculate your BMI index
    bmiindex = (weight * 703) / (height ** 2)

    if bmiindex < 0:
        print("Invalid input. Please enter valid weight and height.")

# Prints your BMI index
print("BMI:", bmiindex)

# Determine the BMI category based on the index
# If statement undergrows under 18.5 it says your under weight
if 0 <= bmiindex < 18.5:
    category = "Underweight"
# Elif statement undergrows between 18.5 - 25 it says your normal weight
elif 18.5 <= bmiindex < 25:
    category = "Normal Weight"
# Elif statement undergrows between 25-30 it says your overweight
elif 25 <= bmiindex < 30:
    category = "Overweight"
# Elif statement undergrows between 30 - 35 it says your class 1 obesity    
elif 30 <= bmiindex < 35:
    category = "Obesity (Class 1)"
# Elif statement undergrows between 35 - 40 it says your class 2 obesity    
elif 35 <= bmiindex < 40:
    category = "Obesity (Class 2)"
#This else statement outputs the value of the catogory if your above 40 which is class 3 obesity
else:
    category = "Extreme Obesity (Class 3)"

# This outputs the catogery of what you belong in
print("Category:", category)


# COMMAND ----------



# COMMAND ----------


