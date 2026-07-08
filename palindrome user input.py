list1 = [input("Enter to check if it's a palindrome: ")]
list2 = [input("Enter to check if it's a palindrome: ")]

if list1 == list1[::-1]:
    print("The first one is a palindrome.")
else:
    print("The first one is not a palindrome.")

if list2 == list2[::-1]:
    print("The second one is a palindrome.")
else:
    print("The second one is not a palindrome.")
