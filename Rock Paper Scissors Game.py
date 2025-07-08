import random
user_score = 0
computer_score = 0
rounds = 0
def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors or q to quit): ").lower()
    while choice not in ["rock", "paper", "scissors", "q"]:
        print("Invalid input!")
        choice = input("Enter again (rock, paper, scissors or q to quit): ").lower()
    return choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"
print("=== Rock Paper Scissors Game ===")
while True:
    user_choice = get_user_choice()
    if user_choice == "q":
        print("\nFinal Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        print("Thanks for playing!")
        break
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1
    rounds += 1
    print(f"Score after {rounds} round(s): You - {user_score} | Computer - {computer_score}\n")
