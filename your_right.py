print("====================================")
print("      Welcome to ride builder!      ")
print("====================================")

print("Step 1. Pick your vehicle")
print("Bike = 1")
print("Car = 2")

choice = int(input("Enter your chosen vehicle (Type 1 or 2)"))

if choice == 1:
    print("Step 2. Pick your bike type")
    print("Scooty = 1")
    print("Mountain bike = 2")

    bike_type = int(input("Enter your chosen bike type (Type 1 or 2)"))

    if bike_type == 1:
        print("You Have chosen: Scooty")
        print("Top speed: 80 km/h")
        print("Best for: City roads")

    else:
        print("You have chosen: Mountain Bike")
        print("Top speed: 40 km/h")
        print("Best for: Off-Road Trails")
elif choice == 2:
    print("Step 2. Pick your car type")
    print("Sedan = 1")
    print("SUV = 2")

    car_type = int(input("Enter your chosen car type (Type 1 or 2)"))

    if car_type == 1:
        print("You picked: Sedan")
        print("Seats: 5 Passengers")
        print("Best for: Family trips")

    else:
        print("You picked: SUV")
        print("Seats: 7 Passengers")
        print("Best for: Off-Road Adventures")

else:
    print("That was not a valid choice")
    print("Please enter 1 for bike and 2 for car")

print("======================================")
print("      Your custom ride is ready!      ")
print("      Enjoy the journey!              ")
print("======================================")