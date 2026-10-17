import random

def guess_the_number():
    print("=======================================")
    print("🎮 Welcome to the Number Guessing Game! 🎮")
    print("=======================================")
    print("I am thinking of a number between 1 and 100.")
    
    # The computer generates a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    # Game loop
    while True:
        try:
            # Ask the player for their guess
            user_guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            # Check the player's guess against the secret number
            if user_guess < secret_number:
                print("Too low! 📉 Try guessing a higher number.")
            elif user_guess > secret_number:
                print("Too high! 📈 Try guessing a lower number.")
            else:
                print(f"\n🎉 Congratulations! You guessed the number in {attempts} attempts!")
                break # Exit the loop and end the game
                
        except ValueError:
            print("❌ Invalid input! Please enter a whole number.")

if __name__ == "__main__":
    guess_the_number()
