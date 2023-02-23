# Write a program that calculates a user's BMI using the user's weight and height.
# BMI is calculated by dividing the person's weight in kg by the square of the person's height in meters. Round the result to a whole number.

# Sample : 
# height = 1.85
# weight = 75

# Output: 22


def cal_bmi(height,weight):
    bmi=round(weight/(height*height),2)
    return bmi


height =float(input("please input the height in meters: "))
weight = float(input("please input the weight in kg:  "))

print(f"Person with height {height} and weight {weight} has BMI of ",cal_bmi(height,weight))