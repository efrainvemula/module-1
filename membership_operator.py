print("Enter Marks Obtained in 3 Subjects:")

markOne = int(input())
markTwo = int(input())
markThree = int(input())

tot = markOne + markTwo + markThree
avg = int(tot / 3)

validRange = range(0, 101)

if avg not in validRange:
    print("Invalid Input!")

elif avg in range(91, 101):
    print("Your Grade is A1")

elif avg in range(81, 91):
    print("Your Grade is A2")

elif avg in range(71, 81):
    print("Your Grade is B1")