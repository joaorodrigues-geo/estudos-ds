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

hand = int(input("Chose between Rock (0), Paper (1) and Scissors (2): "))
if hand == 0:
    print("You chose Rock")
    print(rock)
elif hand == 1:
    print("You chose Paper")
    print(paper)
elif hand == 2:
    print("You chose Scissors")
    print(scissors)
else:
    print("Invalid input, you lose!")

robot_hand = random.randint(0, 2)
if robot_hand == 0:
    print("Computer chose Rock")
    print(rock)
elif robot_hand == 1:
    print("Computer chose Paper")
    print(paper)
elif robot_hand == 2:
    print("Computer chose Scissors")
    print(scissors)

if hand == 0 and robot_hand == 0:
    print("Draw!!")
elif hand == 0 and robot_hand == 1:
    print("You Lost!!")
elif hand == 0 and robot_hand == 2:
    print("You Won!!")
elif hand == 1 and robot_hand == 0:
    print("You Won!!")
elif hand == 1 and robot_hand == 1:
    print("Draw!!")
elif hand == 1 and robot_hand == 2:
    print("You Lost!!")
elif hand == 2 and robot_hand == 0:
    print("You Lost!!")
elif hand == 2 and robot_hand == 1:
    print("You Won!!")
elif hand == 2 and robot_hand == 2:
    print("Draw!!")
