total_chores = 4
original_count = total_chores
# f means formated string and to use it when you want to put a variable inside a print statement
print(f"You have {original_count} chores to finish today\n")

completed_count = 0
chore_num = 1

while chore_num <= total_chores:
    if chore_num == 1: next_chore = "Make your bed"
    elif chore_num == 2: next_chore = "Feed the pet"
    elif chore_num == 3: "Take the ttrash out"
    else: next_chore = "Wash the dishes"

    answer = input(f"Have you finished: {next_chore}? (yes/no): ")

    if answer == "yes":
        completed_count += 1
        chore_num += 1
        print("Great job! Chore completed")
    else:
        print("Okay, finish it and check again.")

    print("Chores remaining:", total_chores - completed_count)

print("===== ALL CHORES COMPLETED! =====")
print("Great work finishing your entire checklist today\n")


print("\n===== CHORE CHECKLIST SUMMARY =====")
print("Chores assigned today:", original_count)
("Chores completed:", completed_count)
("Chores remaining", total_chores - completed_count)
print("=================================")