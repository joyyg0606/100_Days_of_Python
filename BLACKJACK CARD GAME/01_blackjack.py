import blackjack_art
import random
import os

deck_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def ace_choices():
    player_cards.remove(11)
    player_score = sum(player_cards)
    player_ace_choice = int(input(f"\nYou recieved an Ace!{blackjack_art.ace_arts}\n❗Your cards: {player_cards}, current score: {player_score} ❗\nIf you want the ACE to represent +1 type '1', otherwise to +11 type '11': "))
    player_cards.append(player_ace_choice)

def logo_clear():
    os.system('cls||clear')
    print(blackjack_art.logo)

def final_card_displayer():
    print(f"\nYour final cards: {player_cards}, final score: {player_score}")
    print(f"Dealer's final cards: {dealer_cards}, final score: {dealer_score}\n")

bank = 0
dealer_cards = []
dealer_score = 0
player_cards = []
player_score = 0

choice_to_play = input("Do you want to play a game of Blackjack?\n\n❗❗❗Terms and Conditions Agreement ❗❗❗\nThis game is taken seriously. You must give the exact amount of money you lost to ME.\nIf you agree to the Terms and Conditions type 'y', if not, type 'n': ").lower()

if choice_to_play == 'y':
    os.system('cls||clear')
    bank = float(input(f"{blackjack_art.money_bag}\nEnter a price you're willing to put into your bank. 💲You MUST have a balance of $5 or MORE in your bank💲: $"""))
    if bank >= 5:
        play_again = True
        while play_again == True:
            deal_price = float(input(f"\n\nBank: ${bank}\nEnter a price you're willing to deal: "))
            bank = bank - deal_price
            logo_clear()

            redo = True
            while redo == True:
                player_cards += random.choices(deck_of_cards, k=2)
                if player_score < 21:
                    redo = False    
                if 11 in player_cards:
                    ace_choices()
                player_score = sum(player_cards)

            dealer_cards += random.choices(deck_of_cards, k=2)
            if 11 in dealer_cards:
                ace = [11, 1]
                position_of_ace = dealer_cards.index(11)
                dealer_cards[position_of_ace] = random.choice(ace)
            
            wants_to_add = True
            while wants_to_add == True:
                logo_clear()
                print(f"\nYour cards: {player_cards}, current score: {player_score}")
                print(f"Dealer's first card: {dealer_cards[0]}\n")
                print(f"Bank: ${bank}   Deal: ${deal_price}")
                if player_score <= 21:
                    choice_to_add = input("Type 'y' to get another card, type 'n' to pass: ")
                    if choice_to_add == 'y':
                        player_cards.append(random.choice(deck_of_cards))
                        if 11 in player_cards:
                            ace_choices()
                        player_score = sum(player_cards)
                    else:
                        wants_to_add = False
                        dealer_score = sum(dealer_cards)
                        while dealer_score < 17:
                                dealer_cards.append(random.choice(deck_of_cards))
                                dealer_score = sum(dealer_cards)
                        if dealer_score > 21:
                            logo_clear()
                            print("✅ DEALER BUST. YOU WIN.✅\n")
                            bank += deal_price * 2
                        elif dealer_score > player_score:
                            logo_clear()
                            print("❌ Dealer has a higher score. YOU LOSE.❌\n")
                        elif dealer_score == player_score:
                            logo_clear()
                            print("❗TIE GAME. ❗\n")
                            bank += deal_price
                        else:
                            logo_clear()
                            print("✅ You have a higher score. YOU WIN.✅\n")
                            bank += (deal_price * 2)
                        
                        final_card_displayer()
                        print(f"Bank: ${bank}")
                else:
                    logo_clear()
                    wants_to_add = False
                    dealer_score = sum(dealer_cards)
                    final_card_displayer()
                    print(f"❌ BUST. YOU LOSE.❌\n\nBank: ${bank}")
    
            again = input("\nDo you wish to play again? Type 'y' to replay or 'n' to end game: ").lower()
            if again == 'y':
                os.system('cls||clear')
                dealer_cards = []
                dealer_score = 0
                player_cards = []
                player_score = 0

                new_balance_choice = input(f"{blackjack_art.money_bag}\nBank: ${bank}\n\nDo you want to add a new balance to your bank? Reminder: 💲Your Bank's Balance MUST be greater than 5💲\nType 'y' to add or 'n' to keep current balance: """).lower()
                
                if new_balance_choice == 'y':
                    price_added = float(input("How much would you like to add?  $"))
                    bank += round(price_added, 2)
                    if bank < 5:
                        wants_to_add = False
                        play_again = False
                        print(f"\nBank: ${bank}\nGame Ended. Insufficient Funds. Come back when you're not this broke loser.\n")
            else:
                wants_to_add = False
                play_again = False
                print(f"\nGame Ended.\n")
    else:
        play_again = False
        print(f"\nGame Ended. Insufficient Funds. Come back when you're not this broke loser.\n")
else:
    print("\nGAME ENDED.\nYou suck. You are broke and dumb. You have no brain because you did not want to play the game. Goodbye.")