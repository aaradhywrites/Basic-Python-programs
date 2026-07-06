list = [input("Enter to check if it's a palindrome: ")]
list2 = [input("Enter to check if it's a palindrome: ")]

copy_list = list.copy()
copy_list2 = list2.copy()

if copy_list == list:
    print("The first one is a palindrome.")
else:
    print("The first one is not a palindrome.")

if copy_list2 == list2:
    print("The second one is a palindrome.")
else:
    print("The second one is not a palindrome.")
