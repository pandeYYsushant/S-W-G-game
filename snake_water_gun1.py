import random

def get_user_choice():
    """
    Function to get the user's choice (Snake, Water, or Gun)
    """
    while True:
        user_choice = input("Enter your choice (Snake, Water, Gun): ").strip().lower()
        if user_choice in ['snake', 'water', 'gun']:
            return user_choice
        else:
            print("Invalid choice! Please enter Snake, Water, or Gun.")

def get_computer_choice():
    """
    Function to randomly generate the computer's choice
    """
    choices = ['snake', 'water', 'gun']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Function to determine the winner of the game
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'snake':
        return "You win!" if computer_choice == 'water' else "Computer wins!"
    elif user_choice == 'water':
        return "You win!" if computer_choice == 'gun' else "Computer wins!"
    elif user_choice == 'gun':
        return "You win!" if computer_choice == 'snake' else "Computer wins!"

def play_game():
    """
    Function to play the Snake Water Gun game
    """
    print("Welcome to Snake Water Gun Game!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    play_game()
