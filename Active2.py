height = float(input("Enter your heidht in cm: "))
weight = float(input("Enter your heidht in kg: "))

BMI = weight / (height/100)**2

print("Your BMI is",BMI)

if BMI <= 18.4:
    print("Your are underweight.")
elif BMI <= 24.9:
    print("Your are healthy.")
elif BMI <= 29.9:
    print("Your are over weight.")
elif BMI <= 34.9:
    print("Your are severely over weigt")    
elif BMI <= 39.9:
    print("Your are odese.")
else :
    print("Your are severel odese")        