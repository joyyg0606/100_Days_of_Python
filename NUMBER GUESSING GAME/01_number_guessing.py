import number_guessing_art
import random

print(number_guessing_art.welcome_message_icon + "\nI'm thinking of a number between 1 and 100...")
random_number = random.randint(1, 100)
      
print(f"{random_number} <= answer")

difficulty_lvl = input("\nChoose a difficulty level. Type 'easy' or 'hard': ").lower()

def game_steps():
    global num_of_attempts
    while num_of_attempts >= 0:
        user_guess = int(input("\nEnter a guess: "))    
        print(f"You have {num_of_attempts} attempts remaining")
        if num_of_attempts == 0:
            print(f"\nYou ran out of attempts, you lose\n{number_guessing_art.out_of_attempts_icon}")
            return
        elif user_guess == random_number:
            print(f"\nCorrect! The answer was {random_number}\n{number_guessing_art.correct_word_icon}")
            return
        elif user_guess > random_number:
                print("\nToo High /ᐠ •ヮ• マ Ⳋ")
                num_of_attempts -= 1
        elif user_guess < random_number:
                print("\nToo Low /ᐠ - ˕ -マ Ⳋ")
                num_of_attempts -= 1

if difficulty_lvl == 'hard':
    print("\nHARD MODE\nYou have 5 attemps remaining to guess the number")
    num_of_attempts = 5
else:
    print("\nEASY MODE\nYou have 10 attemps remaining to guess the number")
    num_of_attempts = 10
    
game_steps()