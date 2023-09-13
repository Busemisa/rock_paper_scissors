import random
#We made a rock paper scissors game


def game():
    n=random.randint(1,3)
    if n==1:
        return "rock"
    elif n==2:
        return "paper"
    else:
        return "scissors"

user_choice = input("rock? or paper? or scissors?")
choice =game()
print("Computer : ",choice)
