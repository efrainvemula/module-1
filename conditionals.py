temperature = int(input("Enter the temperature in celcius:"))
if temperature < 20: 
    outfit = "jacket" 
    print("It is cold today")
    print("You should wear a", outfit)
else:
    outfit = "t-shirt"
    print("It is warm today")
    print("You should wear a", outfit)

rain = input("Is it raining? (yes/no)")
if rain == "yes":
    print("Take an umbrella with you")

wind_speed = int(input("Enter the wind speed in km/h:"))
if wind_speed > 30:
    wind_breaker = "yes"
    print("It is really windy")
    print("You should wear a windbreaker over your", outfit)
else:
    wind_breaker = "no"
    print("It is a calm day")
    print("There is no need for any windbreaker")

print("Weather check complete")
print("="*25)
print("Temperature:", temperature)
print("Outfit:", outfit)
print("Rain:", rain)
print("Wind Breaker Needed:", wind_breaker)