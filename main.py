import random

while True:
    try:
        isplaying = int(input("Press 1 to play. Press 2 to quit\n"))
        if isplaying ==1:
            print("The wizard is looking for a new apprentice and would like to test your intuition\n")
            playerchoice= int(input("Pick a number 1-10...\n"))
            computerchoice = random.randint(1,10)
            if playerchoice != computerchoice or playerchoice > 10:
                print(f"You have failed the Wizards test. He selected {computerchoice} while you selected {playerchoice}\nClear your mind and try again")
            else:
                if playerchoice == computerchoice:
                    print("The Wizard is pleased with your innate abilities.\nExpect a letter sometime next century")
    except:
        print("Invalid response. Please try again\n")
    else:
        if isplaying==2:
            break

print("Until We Meet Again...")
