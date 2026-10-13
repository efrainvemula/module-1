print("SMART SCHOOL DAY PLANNER")
("Please answer the following 3 questions and i can make your day")

day = input("What day is it? (Sunday to Saturday)").strip().capitalize()
weather = input("How is the weather outside?(cloudy, rainy, sunny)").strip().lower()
homework = input("Is all your homework completed?(yes or no) ").strip().lower

print()
print(f"=== your plan for {day} ===")
print("-" * 35)

if day in ("Saturday", "Sunday"):
    print("Day type: Weekend - enjoy your free time!")
elif day == "Monday":
    print("Day type: First day of the weeek. Pack your weekly planner.")
elif day == "Friday": 
    print("Day type: Last school day return library books today")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type: Regular school day. Stay focused")
else:
    print("Day type: day not recognised. Please check the spelling.")

if weather == "sunny" and homework == "yes":
    print("After school head to the park - Great weather and homework is done!")
if weather == "rainy" or weather == "cloudy":
    print("Weather tip: Pack your umbrella - It may get wet outside.")
if not (homework == "yes"):
    print("Homework : Not done yet. Finish it before going out!")

if weather == "rainy" and not (homework == "yes"):
    print("Best plan   : Stay in, finish homework, then watch your favourite show.")
elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan   : All set for a great school day - you are prepared!")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan   : Perfect weekend weather - head outside and have fun!")
else:
    print("Best plan   : Take it one step at a time - you have got this!")

print()
print("Plan complete! Have a wonderful day!")