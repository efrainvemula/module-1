string = input("Please enter your own name: ")

string2 = ('')
for i in string:
    string2 = i + string2

print("\nThe Original Name = ", string)
print("The Reversed String = ", string2)