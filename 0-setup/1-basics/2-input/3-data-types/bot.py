startbmi = input("Hello, would you like me to calculate your BMI? \n YES or NO \n")
if startbmi.upper() == "YES":
    name = input("what is your name?")
    height = float(input("what is your height(in meters)"))
    weight = int(input("whats your weight (in kg)"))
    bmi = weight / (height*2)
    print(bmi)

else:
    print("okay :)")
