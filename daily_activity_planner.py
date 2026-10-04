homework = int(input("Enter your homework time in minutes:"))
if homework > 60:
    plan = "Start your homework now immediately!" 
else:   
    plan = "Finish it up quickly"  

free_time = input("Is there any free time after homework? yes/no")
if free_time == "yes":
    print("Remember to pick a hobby!")

print("===== Daily Plan =====")
print("Homework Minutes:", homework)
print("Plan:", plan)
print("Free time:", free_time)
print("======================")