import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

hand_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if hand_user >= 3 or hand_user < 0:
    print("You typed an invalid number, you lose;)")
else:
    print(f"\nYour choice:\n {game_images[hand_user]}")

    hand_computer = random.randint(0, 2)

    print(f"Computer choice:\n {game_images[hand_computer]}")


    if (hand_user == 0 and hand_computer == 0) or (hand_user == 1 and hand_computer == 1) or (hand_user == 2 and hand_computer == 2):
        print("It's a draw:)")
    elif hand_user == 0 and hand_computer == 1:
        print("You lose..")
    elif hand_user == 0 and hand_computer == 2:
        print("You win!")
    elif hand_user == 1 and hand_computer == 2:
        print("You lose..")
    elif hand_user == 1 and hand_computer == 0:
        print("You win!")
    elif hand_user == 2 and hand_computer == 0:
        print("You lose..")
    elif hand_user == 2 and hand_computer == 1:
        print("You win!")
