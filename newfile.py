print("This program is to calculate BMI")

name = input("\nEnter name : ")
age = input("Enter age : ")
weight = float(input("Enter your weight : "))
height = float(input("Enter your height : "))

bmi = weight / (height ** 2)

if (bmi < 16) : 
    print (name, "is underweight ", bmi, "BMI")

elif (bmi >= 18.5) :
	print (name, "is healthy ", bmi, "BMI")
	
elif (bmi >= 25) :
	print (name, "is overweight ", bmi, "BMI")
		
elif (bmi >= 30) :
	print (name, "is obese ", bmi, "BMI")