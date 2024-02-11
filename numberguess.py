import random

def welcome_message():
    print("Welcome to the Mystic Number Game!")
    print("Can you guess the secret number? Let's find out!\n")

def generate_secret_number():
    return random.randint(1, 100)

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Oh no! Your guess is soaring beyond the mystic range of 1 to 100. "
                      "Let's try to keep it within bounds, shall we?")
        except ValueError:
            print("Please enter a valid number.")

def check_guess(secret_number, user_guess):
    if user_guess < secret_number:
        print("Too low! Try again.")
    elif user_guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the secret number!")

def play_game():
    welcome_message()
    secret_number = generate_secret_number()
    
    attempts = 0
    while True:
        user_guess = get_user_guess()
        attempts += 1
        check_guess(secret_number, user_guess)

        if user_guess == secret_number:
            print(f"It took you {attempts} attempts to guess the secret number.")
            break

def main():
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        main()
    else:
        print("Thanks for playing the Mystic Number Game!")

if __name__ == "__main__":
    main()
