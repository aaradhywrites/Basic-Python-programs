num1 = float(input("Enter first number"))
num2 = float(input("Enter 2nd number"))
num3= float(input("Enter 3rd number"))

if num1>num2 and num1>num3:
    print ("First number is greatest")
elif num2>num1 and num2>num3:
    print ("2nd number is the greatest")
elif num3>num1 and num3>num1:
    print ("3rd number is the greatest" )
else:
    print ("Wrong Input")