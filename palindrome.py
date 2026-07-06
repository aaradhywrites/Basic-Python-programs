stg3 = (input("Enter to check if it's a palindrome "))

list1 = [stg3]

listc = list1.copy()
listc.reverse()


if list1 == listc:
    print("The first one is a palindrome.")
else:
    print("The first one is not a palindrome.")



