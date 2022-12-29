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

#Write your code below this line 👇
import random

game=[rock,paper,scissors]
random_computer= random.randint(1,3)
user=int(input("choose 1 for rock, 2 for paper and 3 for scissors\n"))
print(f"Your choice:\n{game[user-1]}")
print(f"computer's choice: {game[random_computer-1]}")

if user >3 or user < 0: 
  print("You typed an invalid number, you lose!") 
elif user == 0 and random_computer == 2:
  print("You win!")
elif random_computer == 0 and user == 2:
  print("You lose")
elif random_computer > user:
  print("You lose")
elif user > random_computer:
  print("You win!")
elif random_computer == user:
  print("It's a draw")
