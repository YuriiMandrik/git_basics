import random


class Cards:
    RANKS = list(range(2, 11)) + list('JQKA')
    SUITS = ['\u2660', '\u2665', '\u2666', '\u2663']

    def __init__(self):
        self.rank = self.RANKS
        self.suits = self.SUITS

    def __repr__(self):
        return f"{self.magic_cards()}"

    @classmethod
    def create_deck(cls):
        deck = []
        deck_list = [(str(i), j) for i in cls.RANKS for j in cls.SUITS]
        for i in deck_list:
            deck.append("".join(i))
        return deck

    @classmethod
    def generate_card(cls, n=1):
        cards_list = []
        for i in range(n):
            cards_list.append(random.choice(cls.create_deck()))
        return cards_list

    def magic_cards(self):
        from datetime import datetime
        print(f"Pick from one to four cards from the deck and I'll tell you what tomorrow should be. \n"
              f"How many cards will you get?\n -->")
        num_cards = input()
        try:
            int(num_cards)
            if 0 < int(num_cards) < 5:
                week_days_list = ['monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                get_cards = self.generate_card(int(num_cards))
                num_cards -= 1
                print(f"You got the following cards : \n {' '.join(get_cards)}\nand tomorrow...... \nshould be.........\n"
                  f"--->>>{week_days_list[datetime.now().weekday()]}<<<---")
            else:
                print('too many cards you probably need to see a fortune teller')
        except ValueError:
            print("it seems that tomorrow......\n you will learn how letters differ from numbers")

x = Cards()
print(x.generate_card())
print(x.magic_cards())
