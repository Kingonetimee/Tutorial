h = float(input("Enter your height in m: "))
w = float(input("Enter your weight in kg: "))
bmi = float(w / (h ** 2))
print(bmi)
if bmi <= 18.5:
    print("You are underweight")
elif bmi <= 25:
    print("You have normal weight")   
elif bmi <= 30:
    print("you are overweight")
elif bmi <= 35:
    print("you are obese")
else:
    print("You are clinically obese")