import random

print("Welcome to my Rock Paper Scissors game! By Rafael Donner!")
Prompt = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))
if Prompt > 2 or Prompt < 0:
    print("Invalid prompt, you lose!")
else:    


    RPSASCII = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''','''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''','''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

    print(RPSASCII[Prompt] + "\nComputer chose:\n")

    ComputerChoice = random.randint(0,2)

    print(RPSASCII[ComputerChoice])

    if Prompt == ComputerChoice:
        print("It is a Draw!")

    elif Prompt == 0 and ComputerChoice == 1:
        print("You Lose!")

    elif Prompt == 1 and ComputerChoice == 0:
        print("You Win!")

    elif Prompt == 0 and ComputerChoice == 2:
        print("You Win!")

    elif Prompt == 2 and ComputerChoice == 0:
        print("You Lose")

    elif Prompt == 1 and ComputerChoice == 2:
        print("You Lose!")

    elif Prompt == 2 and ComputerChoice == 1:
        print("You Win!")
