'''
Let's make an application which is called BMI Calculator. The program will calculates the Body Mass Index(BMI) from a users weight and height.
BMI is calculated by dividing a persons weight(in kg) by the square of their height(in m).

BMI = weight(kg) / (height * height)          # height * height => height**2

'''

#========== User's Code Starts Here ==========
print("Hey there! Welcome to the BMI calculator!")
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

BMI = int(weight) / float(height) ** 2
BMI_as_int = int(BMI)
print(f"Your BMI is: {BMI_as_int}")

#Let's round the value 2 decimal number after the BMI answer
BMI_round_final = "{:.2f}".format(BMI)
print(f"Your exact BMI is: {BMI_round_final}")

#========== User's Code Ends Here ==========

