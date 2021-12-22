import random
#strength
#intelligence
#dexterity
#wisdom
#charisma

points = 250

print("Welcome, adventurer! Skill point time! (250 skill points available)")

strength = int(input("How strong are you? (0-100)\n>"))
if strength > 100 or strength < 0 or strength > points:
    print("You can't do that! You LOSE!")
    exit()
points = points - strength
print("Wow such stronk! STRENGTH SET TO " + str(strength))
print("You have " + str(points) + " skill points remaining.")

#First encounter
print("You encounter a menacing wall. Wat do?")
print("1. punch wall")
print("2. reason with wall")
print("3. climb wall")
print("4. magic wall")
choice = input(">")

if choice == "1":
    roll = random.randrange(0, strength)
    if roll > 20:
        print("The wall shatters in awe of your divine strength")

    else:
        print("Your fist shatters in awe of the wall's divine strength")
        exit()

elif choice == "2":
    print("cool")
elif choice == "3":
    print("cool")
elif choice == "4":
    print("cool")

else:
    print("You can't do that! You LOSE!")
    exit()



