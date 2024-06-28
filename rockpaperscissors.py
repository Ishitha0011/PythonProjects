import random

# ASCII Art for rock, paper, scissors
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

game_images = [rock, paper, scissors]

def get_user_choice():
    while True:
        try:
            user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
            if user_choice in [0, 1, 2]:
                return user_choice
            else:
                print("Invalid number. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return "You win!"
    else:
        return "You lose"

def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        print("You chose:")
        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(game_images[computer_choice])

        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose":
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer")

        play_again = input("Do you want to play again? Type 'yes' to continue or 'no' to exit: ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing! Final Score:")
    print(f"You: {user_score} - Computer: {computer_score}")

play_game()
