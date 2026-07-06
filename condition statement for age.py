age = input("Please enter your age: ")
age = float(age)

if age < 18:
    print("You are a minor not allowed to vote.")
    print("You are a minor not allowed to drive.")
elif age >= 18 and age < 65:
    print("You are an adult and allowed to vote.")
    print("You are an adult and allowed to drive.")
else:
    print("You are a senior citizen and allowed to vote.")
<<<<<<< Updated upstream
    print("You are a senior citizen and not allowed to drive.")
=======
    print("You are a senior citizen and not allowed to drive.") 
>>>>>>> Stashed changes
