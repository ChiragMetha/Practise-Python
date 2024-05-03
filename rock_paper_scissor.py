import random
# Rock paper Scissor game!
print("Lets play")
user_action = input("enter a choice (rock,paper,scissor) : ").lower()
if user_action not in ['rock','paper','scissor']:
    print("Invalid choice. Please enter choice : rock, paper, or scissor.")
    exit()
possible_action = ["rock","paper","scissor"]
computer_action = random.choice(possible_action)
print(f"user choice is {user_action} and computer choice is {computer_action}")

if user_action == computer_action:
    print("Its a Tie")
elif user_action == "rock":
    if computer_action == "scissor":
        print("Rock win has scissor gets smash ! You win...")
    else:
        print("paper covers rock! You lose")
elif user_action == "paper":
    if computer_action == "rock":
        print("paper win has rock gets cover ! You win...")
    else:
        print("scissor cuts paper ! You lose...")
elif user_action == "scissor":
    if computer_action == "paper":
        print("scissor cuts paper! You win!")
    else:
        print("rock smashes scissors! You lose.")

