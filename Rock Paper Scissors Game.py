import random
choices = {1: "stone", 2: "scissors", 3: "paper"}
user_score = 0
computer_score = 0
def get_computer_choice():
    return random.randint(1, 3)
def get_user_choice():
    while True:
        try:
            choice = int(input("Choose 1 (stone), 2 (scissors), 3 (paper), or 0 to exit: "))
            if choice in [0, 1, 2, 3]:
                return choice
            else:
                print("Invalid input. Please enter 1, 2, 3 or 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def determine_winner(user, computer):
    global user_score, computer_score
    print(f"\nYou chose: {choices[user]}")
    print(f"Computer chose: {choices[computer]}")
    if user == computer:
        print("Result: It's a tie!")
    elif (user == 1 and computer == 2) or \
         (user == 2 and computer == 3) or \
         (user == 3 and computer == 1):
        print("Result: You win this round!")
        user_score += 1
    else:
        print("Result: Computer wins this round!")
        computer_score += 1
def play_game():
    print("Welcome to Rock (Stone), Scissors, Paper!")
    print("Instructions:")
    print("Enter 1 for Stone")
    print("Enter 2 for Scissors")
    print("Enter 3 for Paper")
    print("Enter 0 to Exit")
    while True:
        user_choice = get_user_choice()
        if user_choice == 0:
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("You won the game!")
            elif user_score < computer_score:
                print("Computer won the game!")
            else:
                print("It's a draw overall!")
            break
        computer_choice = get_computer_choice()
        determine_winner(user_choice, computer_choice)
        print(f"\nScore => You: {user_score} | Computer: {computer_score}")
play_game()
