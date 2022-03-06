import random

thirst = 0
camelTired = 0
natives = -20
canteen = 3
milesTraveled = 0
oasis = 0
done = False

#menu
print("---Camel Game---")
print()
print("1) Start Game")
print("2) Credits")
print("3) Exit")
print()
choice = input("--->")
if choice == '3':
    exit
#credits    
elif choice == '2':
    print()
    print("----Credits----")
    print()
    print("Programmer: Geoffrey Gomlak")
    print()
    print("Based on the Original Game by: Heath Users Group")
    print()
    print("Program Date: 10/21/21")
    print()
    print("---------------")
#game
elif choice == '1':
    print()
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and outrun the natives.")
    print()
    go = input("continue (y) --->")
    if go == 'y':
        while done is False:
            nativesBehind = milesTraveled - natives
            fullSpeed = random.randrange(10, 21)
            moderateSpeed = random.randrange(5, 13)
            print()
            print("1) Drink from your canteen.")
            print("2) Ahead moderate speed.")
            print("3) Ahead full speed.")
            print("4) Stop and rest.")
            print("5) Status check.")
            print("6) Quit.")
            start = input("--->")
            if start == '6':
                done = True
            elif start == '5':
                print()
                print("____Stats____")
                print("-------------")
                print()
                print("Your Thirst:", thirst)
                print("Drinks Left:", canteen)
                print("Camel Drowssiness:", camelTired)
                print("Natives:", natives, "miles behind you")
                print("Miles Travled:", milesTraveled, "miles")
                print()
                print("------------")
            elif start == '4':
                print()
                print("You rested for the night")
                camelTired *= 0
                natives = natives + 3
            elif start == '3':
                print()
                print("You traveled ",fullSpeed,"miles!")
                milesTraveled += fullSpeed
                thirst += 1
                camelTired += random.randrange(1, 10)
                natives += random.randrange(7, 15)
                oasis = random.randrange(1, 21)
            elif start == '2':
                print()
                print("You traveled ",moderateSpeed,"miles!")
                milesTraveled += moderateSpeed
                thirst += 1
                camelTired += 1
                natives += random.randrange(7, 15)
                oasis = random.randrange(1, 21)
            elif start == '1':
                if canteen == 0:
                    print()
                    print("You're out of water.")
                else:
                    canteen -= 1
                    thirst *= 0
                    print()
                    print("You have ",canteen,"drinks left and you are no longer thirsty.")

                    
            #check if done
            if oasis == 20:
                camelTired *= 0
                thirst *= 0
                canteen = 3
                print()
                print("You found an oasis! After taking a drink you filled your canteen and the camel is refreshed.")
            if nativesBehind <= 15:
                print()
                print("The natives are drawing near!")
                print()
            if milesTraveled >= 200 and not done:
                print()
                print("You made it across the desert, you win!")
                done = True
            if natives >= milesTraveled:
                print()
                print("The natives caught and beheaded you.")
                print()
                print("You're dead!")
                done = True
            if thirst > 4 and thirst <= 6 and not done:
                print()
                print("You are thirsty")
            if thirst > 6:
                print()
                print("You died of dehydration!")
                done = True
            if camelTired > 5 and camelTired <= 15 and not done:
                print()
                print("Your camel is getting tired.")
            if camelTired > 20:
                print()
                print("Your camel is dead.")
                done = True
else:
        print("Error...try again")
        



