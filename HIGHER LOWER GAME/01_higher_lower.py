import os, higher_lower_art, random
from game_data import data

PLAY_AGAIN = True
while PLAY_AGAIN == True:

    NO_WRONG_GUESS = True
    PLAYER_SCORE = 0
    COMPARE_A = random.choice(data)

    def comparing_answer(compare_guess, other_choice):
        global NO_WRONG_GUESS, COMPARE_A, PLAYER_SCORE, PLAY_AGAIN
        if compare_guess['follower_count'] > other_choice['follower_count']:
            COMPARE_A = compare_guess
            PLAYER_SCORE += 1
            os.system('cls')
        else:
            NO_WRONG_GUESS = False
            print(f"\nIncorrect. Final score: {PLAYER_SCORE}")

            replay_choice = input("Do you want to play again? Type 'y' to replay or 'n' to end game: ").lower()
            if replay_choice == 'n':
                PLAY_AGAIN = False
            else:
                PLAYER_SCORE = 0
                NO_WRONG_GUESS = True
                COMPARE_A = random.choice(data)
                os.system('cls')

    while NO_WRONG_GUESS == True:
        print(higher_lower_art.logo)
        compare_b = random.choice(data)

        while COMPARE_A == compare_b:
            compare_b = random.choice(data)
            COMPARE_A = random.choice(data)

        print(f"A: {COMPARE_A['name']}, a {COMPARE_A['description']}, from {COMPARE_A['country']}.\n{higher_lower_art.vs_sign}")
        print(f"B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")
        player_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        if player_guess == 'a':
            comparing_answer(compare_guess=COMPARE_A, other_choice=compare_b)
        else:
            comparing_answer(compare_guess=compare_b, other_choice=COMPARE_A)
print("\nGoodbye")