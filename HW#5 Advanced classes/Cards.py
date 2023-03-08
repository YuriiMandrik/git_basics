import random


class Cards():
    RANKS = list(range(2, 11)) + list('JQKA')
    SUITS = ['\u2660', '\u2665', '\u2666', '\u2663']

    def __init__(self):
        self.rank = self.RANKS
        self.suits = self.SUITS

    def __repr__(self):
        return f"{self.magic_cards()}"

    def create_deck(self):
        deck = []
        deck_list = [(str(i), j) for i in self.RANKS for j in self.SUITS]
        for i in deck_list:
            deck.append("".join(i))
        return deck

    def generate_card(self, n=1):
        cards_list = []
        for i in range(n):
            cards_list.append(random.choice(self.create_deck()))
        return cards_list

    def magic_cards():
        card = Cards()
        from datetime import datetime
        print(f"Pick from one to four cards from the deck and I'll tell you what tomorrow should be. \n"
              f"How many cards will you get?\n -->")
        num_cards = input()
        try:
            num_cards = int(num_cards)
            if 0 < int(num_cards) < 5:
                week_days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                get_cards = card.generate_card(int(num_cards))
                num_cards -= 1
                print(f"You got the following cards : \n {' '.join(get_cards)}\nand tomorrow...... \nshould be.........\n"
                  f"--->>>{week_days_list[datetime.now().weekday() + 1]}<<<---")
            else:
                print('too many cards, you probably need to see a fortune teller')
        except ValueError:
            print("it seems that tomorrow......\n you will learn how letters differ from numbers")

if __name__ == '__main__':
    Cards()
x = Cards()
