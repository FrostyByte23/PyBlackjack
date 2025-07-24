import time
import random
from game import Game

def wait(sleeptime):
    time.sleep(sleeptime)

player_name = input("What is your name? ").title()
dealer_names = ["Alice", "Bob", "Carol", "Bill", "Mia", "Max", "Leo"]
dealer_name = random.choice(dealer_names)

game = Game([player_name, dealer_name])
dealer = game.players[1]
human = game.players[0]

def final_calculation():
    dealer_calc = 21 - dealer.cards_sum
    human_calc = 21 - human.cards_sum

    if abs(dealer_calc) > abs(human_calc):
        print("Player Wins!")
        human.balance += human.current_bet * 2
    elif abs(dealer_calc) < abs(human_calc):
        print("Dealer Wins!")
        human.current_bet = 0
    else:
        print("You Tied!")
        human.balance += human.current_bet

    game.reset_round()
    player_bet()

def end_phase():
    wait(1)
    dealer.card_sum()

    if dealer.cards_sum == 21 and human.cards_sum == 21 and len(dealer.hand) == 2 and len(human.hand) == 2:
        print("You Tied")
        human.balance += human.current_bet
        game.reset_round()
        player_bet()
    elif dealer.cards_sum > 21:
        print("Dealer busted!")
        human.balance += human.current_bet * 2
        game.reset_round()
        player_bet()
    elif dealer.cards_sum >= 17:
        final_calculation()
    else:
        dealer.draw_cards(game.deck, 1)
        print("Dealer Drew a card")
        wait(1)
        dealer.show_hand()
        end_phase()

def h_or_s():
    while True:
        human.card_sum()
        if human.cards_sum > 21:
            print("You busted!")
            game.reset_round()
            player_bet()
            return
        hit_stand = input("Hit or Stand? ").lower()
        if hit_stand == "hit":
            human.draw_cards(game.deck, 1)
            print("You now have:")
            human.show_hand()
        elif hit_stand == "stand":
            game.show_all_hands()
            end_phase()
            break

def initial_deal():
    game.deal(2)
    human.card_sum()
    human.show_hand()
    dealer.show_partial(1)
    if human.cards_sum == 21:
        print("You just doubled your money! ")
        human.balance += human.current_bet * 2
        game.reset_round()
        player_bet()
    else:
        h_or_s()

def player_bet():
    while True:
        if human.balance == 0:
            print("You're out of money!")
            exit(0)
        print(f"Your balance: {human.balance}")
        bet_amount = input("How much do you want to bet? ")
        if bet_amount.isdigit() and int(bet_amount) > 0:
            if human.bet(int(bet_amount)):
                initial_deal()
                break
        else:
            print("Please enter a valid number.")

# Start the game
print("Cards:", game.cards_left())
player_bet()
