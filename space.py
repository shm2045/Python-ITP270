print("I have information for the following planets:\n")
print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

weight = 160
planet = 3

if planet == 1:
    weight *= 0.91
    print("Your weight on Venus would be " + str(weight) + " pounds.")
elif planet == 2:
    weight *= 0.38
    print("Your weight on Mars would be " + str(weight) + " pounds.")
elif planet == 3:
    weight *= 2.34
    print("Your weight on Jupiter would be " + str(weight) + " pounds.")
elif planet == 4:
    weight *= 1.06
    print("Your weight on Saturn would be " + str(weight) + " pounds.")
elif planet == 5:
    weight *= 0.92
    print("Your weight on Uranus would be " + str(weight) + " pounds.")
elif planet == 6:
    weight *= 1.19
    print("Your weight on Neptune would be " + str(weight) + " pounds.")
else:
    print("Invalid planet number. Please choose a number between 1 and 6.")


