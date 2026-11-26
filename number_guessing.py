import random

best_score = None

def play_game():
    global best_score
    
    print("\n--- Difficulty Levels ---")
    print("1. Easy   (1 - 50)")
    print("2. Medium (1 - 100)")
    print("3. Hard   (1 - 200)")
    
    choice = input("Choose difficulty (1/2/3): ")
    
    if choice == "1":
        max_num = 50
    elif choice == "3":
        max_num = 200
    else:
        max_num = 100
    
    secret = random.randint(1, max_num)
    attempts = 0
    
    print(f"\nI have picked a number between 1 and {max_num}. Guess it!")
    
    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        
        attempts += 1
        
        if guess < secret:
            print("Too low! Try HIGHER ⬆️")
        elif guess > secret:
            print("Too high! Try LOWER ⬇️")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            
            if best_score is None or attempts < best_score:
                best_score = attempts
                print(f"🏆 New Best Score: {best_score}")
            else:
                print(f"Best Score (lowest): {best_score}")
            break

# Main loop for replay
while True:
    play_game()
    again = input("\nDo you want to play again? (y/n): ").lower()
    if again != 'y':
        print(f"Thanks for playing! Your best score was: {best_score}")
        break
    