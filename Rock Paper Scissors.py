import random

user_w = 0
computer_w = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input(f'Type Rock/Paper/Scissors or Q to quit: ').lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0,2)

    computer_pick = options[random_number]
    print(f"Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print(f"You won!")
        user_w += 1
        

    elif user_input == "paper" and computer_pick == "rock":
        print(f"You won!")
        user_w += 1
        

    elif user_input == "scissors" and computer_pick == "paper":
        print(f"You won!")
        user_w += 1
        

    else:
        print(f"You lost.")
        computer_w += 1

print(f"You won", user_w, "times.")
print(f"Computer won", computer_w, "times.")
print(f"Goodbye.")