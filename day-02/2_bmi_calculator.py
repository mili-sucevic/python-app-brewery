# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# BMI = weight (kg) ÷ height2 (meters)

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# SOLUTION 1
# height_float = float(height)
# weight_float = float(weight)

# bmi = weight_float / (height_float * height_float)

# print(int(bmi)) 

# SOLUTION 2
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi)
