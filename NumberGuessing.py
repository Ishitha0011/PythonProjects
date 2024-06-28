from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """Check user's guess against actual answer. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return 0

def set_difficulty():
    """Set difficulty level and return number of turns."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()

    while turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")

        try:
            guess = int(input("Make a guess: "))
            if guess < 1 or guess > 100:
                raise ValueError("Please enter a number between 1 and 100.")
        except ValueError as ve:
            print(ve)
            continue

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print(f"Sorry, you've run out of guesses. The correct answer was {answer}.")
            break
        elif turns > 0 and guess != answer:
            print("Guess again.\n")

def main():
    play_again = True
    while play_again:
        game()
        play_again_input = input("\nDo you want to play again? Type 'yes' or 'no': ").lower()
        if play_again_input != 'yes':
            play_again = False
            print("Thanks for playing!")

if __name__ == "__main__":
    main()
