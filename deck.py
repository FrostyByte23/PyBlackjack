import random

class Deck:
    def __init__(self):
        self.cards = self.create_deck()
        self.shuffle()

    @staticmethod
    def create_deck():
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        return [f"{rank} of {suit}" for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop() if self.cards else None

    def cards_left(self):
        return len(self.cards)
