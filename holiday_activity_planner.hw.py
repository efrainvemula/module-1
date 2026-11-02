print("====================================")
print("    Welcome to Holiday Planner!     ")
print("====================================")
print()
 
print("Step 1: Pick your holiday type")
print("  1 - Beach Holiday")
print("  2 - Mountain Holiday")
print()
 
choice = int(input("Enter 1 or 2: "))
print()
 
if choice == 1:
    print("Step 2: Pick your beach activity")
    print("  1 - Swimming")
    print("  2 - Sandcastle Building")
    print()
 
    beach_activity = int(input("Enter 1 or 2: "))
    print()
 
    if beach_activity == 1:
        print("You picked  : Swimming")
        print("Best time   : Morning")
        print("Remember    : Carry sunscreen and water")
    else:
        print("You picked  : Sandcastle Building")
        print("Best time   : Evening")
        print("Remember    : Carry a bucket and spade")
 
elif choice == 2:
    print("Step 2: Pick your Mountain activity")
    print(" 1 - Hiking")
    print("2 - Camping")

    mountain_activity = int(input("Enter 1 or 2"))

    if mountain_activity == 1:
        print("You picked : Hiking")
        print("Best time : Exploring Trails")
        print("Remember : Wear comfortable shoes")
    else:
        print("You picked : Camping")
        print("Best time : Staying close to nature")
        print("Remember : Carry a tent and Flashlight")

else:
    print("That was not a valid choice.")
    print("Please enter 1 for Beach Holiday or 2 for Mountain Holiday.")

print("====================================")
print("   Your holiday plan is ready!      ")
print("   Enjoy your trip!                 ")
print("====================================")