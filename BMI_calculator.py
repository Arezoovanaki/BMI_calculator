import argparse
parser = argparse.ArgumentParser(description="Enter your height(cm) and weight(kg)to see your BMI")
parser.add_argument("height",default=1,type=float,help="Enter your height in cm")
parser.add_argument("weight",default=1,type=float,help="Enter your weight in km")
args = parser.parse_args()
height_m =args.height / 100
bmi = args.weight / (height_m**2)
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI is:{bmi:.2f}")
print(f"category:{category}")