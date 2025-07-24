from deck import Deck
from player import Player

class Game:
    def __init__(self, player_names):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]

    def deal(self, count):
        for player in self.players:
            player.draw_cards(self.deck, count)

    def show_all_hands(self):
        for player in self.players:
            player.show_hand()

    def reset_round(self):
        self.deck = Deck()
        for player in self.players:
            player.hand = []
            player.cards_sum = 0
            player.current_bet = 0

    def cards_left(self):
        return self.deck.cards_left()
