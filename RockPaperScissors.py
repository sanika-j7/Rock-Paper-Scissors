import random
print("ROCK-PAPER-SCISSORS!\nType 0 for Rock, 1 for Paper and 2 for Scissors!")
n=int(input())
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
symbols=[rock,paper,scissors]
l=["Rock","Paper","Scissors"]
if(n>=0 and n<=2):
    print(f"You chose {l[n]}")
    print(symbols[n])
comp=random.randint(0,2)
print(f"Computer chose {l[comp]}")
print(symbols[comp])
if(n==comp):
    print("It's a draw!")
elif((n==0 and comp==1)or(n==1 and comp==2)or(n==2 and comp==0)):
    print("You lose!")
elif((n==0 and comp==2)or(n==1 and comp==0)or(n==2 and comp==1)):
    print("You win!")
else:
    print("Please enter a valid input")











