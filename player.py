class Player:
    def __init__(self, name, balance=100):
        self.name = name
        self.hand = []
        self.balance = balance
        self.current_bet = 0
        self.cards_sum = 0

    def bet(self, amount):
        if amount > self.balance:
            print("Sorry, you don't have enough money, bet again")
            return False
        self.balance -= amount
        self.current_bet = amount
        return True

    def card_sum(self):
        total = 0
        aces_count = 0
        for card in self.hand:
            rank = card.split(" ")[0]
            if rank in ["Jack", "Queen", "King"]:
                total += 10
            elif rank == "Ace":
                aces_count += 1
            else:
                total += int(rank)

        if total >= 11:
            total += aces_count
        elif aces_count == 1:
            total += 11
        else:
            total += aces_count

        self.cards_sum = total

    def draw_cards(self, deck, count):
        for _ in range(count):
            card = deck.draw_card()
            if card:
                self.hand.append(card)
            else:
                print(f"{self.name}: Deck is empty")

    def show_hand(self):
        print(f"{self.name}'s hand:")
        for card in self.hand:
            print(" -", card)
        print()

    def show_partial(self, reveal):
        print(f"{self.name}'s hand:")
        for i, card in enumerate(self.hand):
            if i < reveal:
                print(" -", card)
            else:
                print(" - [Face Down]")

