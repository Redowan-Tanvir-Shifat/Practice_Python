import random

item_list   =["Rock", "paper", "Scissor"]

user_choice = input("Enter your move (Rock, Paper, Scissor): ")
bot_choice = random.choice(item_list)

print(f"\nUser choice: {user_choice}, Bot choice: {bot_choice}")

if user_choice == bot_choice:
    print("Match Tie")

elif user_choice == "Rock":
    if bot_choice == "Paper":
        print("Paper covers rock: Bot win")
    else:
        print("Rock breaks scissor: You win")

elif user_choice == "Paper":
    if bot_choice == "Rock":
        print("Paper covers rock: You win")
    else:
        print("Scissor cuts paper: Bot win")

elif user_choice == "Scissor":
    if bot_choice == "Paper":
        print("Scissor cuts paper: You win")
    else:
        print("Rock breaks scissor: Bot win")