import random


def play():
    user = input("Enter 'r' for Rock, 'p' for Paper, and 's' for Scissors: ").lower()
    while user not in ('r', 'p', 's'):
        print("Invalid input. Please try again.")
        user = input("Enter 'r' for Rock, 'p' for Paper, and 's' for Scissors: ").lower()

    computer = random.choice(['r', 'p', 's'])
    return user, computer


def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return 'user'
    else:
        return 'computer'


def main():
    global user_score, computer_score
    rounds = 5
    user_score = 0
    computer_score = 0

    for _ in range(rounds):
        user_choice, computer_choice = play()
        winner = determine_winner(user_choice, computer_choice)

        if winner == 'user':
            user_score += 1
            print("User Wins")
        elif winner == 'computer':
            computer_score += 1
            print("Computer wins")
        else:
            user_score += 0.5
            computer_score += 0.5
            print("It's a tie")

    print("\nCalculating Final score")
    print(f"Yourscore = {user_score} and Computer score = {computer_score}")

    if user_score < computer_score:
        print(f"Computer wins by {computer_score - user_score} points")
    elif user_score > computer_score:
        print(f"User wins by {user_score - computer_score} points")
    else:
        print(f"Result is a draw {user_score} : {computer_score}")


if __name__ == "__main__":
    main()
