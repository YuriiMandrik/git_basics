import random
import shelve

class CardDeck():
    LOW_CARDS = list(range(2, 11))
    HI_CARDS = list('JQKA')
    SUITS = ['\u2660', '\u2665', '\u2666', '\u2663']

    def __init__(self):
        self.suits = self.SUITS
        self.ranks = self.LOW_CARDS + self.HI_CARDS
        self.shufle_count = 0
        self.deck = self.create_deck()

    def __repr__(self):
        return f'{self.deck}'

    def create_deck(self):
        deck = []
        deck_list = [(str(i), j) for i in self.ranks for j in self.suits]
        for i in deck_list:
            deck.append("".join(i))
        return deck

    def generate_card(self, n=1):
        # Метод що вибирає мінімум одну рандомну карту з колоди
        cards_list = []
        for i in range(n):
            cards_list.append(random.choice(self.deck))
        return cards_list

    def shuffle(self):
        random.shuffle(self.deck)
        self.shufle_count += 1

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, out_card):
        if isinstance(out_card, int):
            if out_card < len(self.deck):
                return self.deck.pop(out_card)
            else:
                print('Колода менша за ваші амбіції')
        else:
            raise TypeError('Потрібно вказати номер карти')

    def __add__(self, add_card):
        if isinstance(add_card, list):
            return self.deck + list(add_card)
        else:
            print('додати можна лише список')

    def __sub__(self, out_cards):
        if isinstance(out_cards, list):
            for i in out_cards:
                if self.__contains__(i):
                    self.deck.remove(i)

                else:
                    print(f'Карта {i} мабуть десь в рукаві')
            return self.deck
        else:
            print('потрібен список карт')

    def __contains__(self, card):
        return card in self.deck

    def __eq__(self, other):
        return sorted(self.deck) < sorted(other.deck)

    def __gt__(self, other):
        return sorted(self.deck) < sorted(other.deck)

    def __lt__(self, other):
        return sorted(self.deck) > sorted(other.deck)

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
                print(
                    f"You got the following cards : \n {' '.join(get_cards)}\nand tomorrow...... \nshould be.........\n"
                    f"--->>>{week_days_list[datetime.now().weekday()]}<<<---")
            else:
                print('too many cards you probably need to see a fortune teller')
        except ValueError:
            print("it seems that tomorrow......\n you will learn how letters differ from numbers")

    def __bool__(self):
        return bool(self.deck) > 0 and self.shufle_count > 0

    def deck_write(self, deck_name, format='shelve'):
        if format == 'shelve':
            with shelve.open(str(deck_name)) as file:
                file[deck_name] = self.deck
                print(f'Deck {deck_name} is saved in shelve format')
        elif format == 'txt':
            with open('DeckFile', 'w') as file:
                file.write(f'{self.deck}')
                print(f'Deck {deck_name} is saved in txt format')
        else:
            print('Write format can be only shelve or txt')



    @classmethod
    def deck_load(self, deck_name, format='shelve'):
        if format == 'shelve':
            with shelve.open(str(deck_name)) as file:
                print(file[deck_name])
                return file[deck_name]
        elif format == 'txt':
            with open('DeckFile', 'r') as file:
                print(file.read())
                return file.read()
        else:
            print('Format can be only shelve or txt')


class SmallDeck(CardDeck):
    LOW_CARDS = list(range(6, 11))

    def __init__(self):
        super().__init__()


class ClassicDeck(CardDeck):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    x = ClassicDeck()
    y = ClassicDeck()
    s = SmallDeck()
    n = ['2♠', '2♦', '3♠']
    n2 = ['2♠']

    # #для перевірки shuffle()
    # print(x)
    # x.shuffle()
    # print(x)

    # #для перевірки __len__()
    # print(len(x))

    # #для перевірки __getitem__()
    # print(x[2])
    # print(x[55])

    # #для перевірки __add__
    # print (x + n)

    # #для перевірки __sub__()
    # print(x-n)
    # x-n2

    # #для перевірки __contains__()
    # print(x)
    # n = '2♠'
    # print(n)
    # print(n in x)

    # # для перевірки __eq__()
    # y.shuffle()
    # print(x)
    # print(y)
    # print (x == y)
    # print(x)
    # print(s)
    # print (x == s)

    # #для перевірки __gt__() та __lt__
    # print(x < s)
    # print(x > s)

    # #для перевірки __bool__
    # print(bool(x))
    # x.shuffle()
    # print(bool(x))

    # #ітерація колоди
    # i = iter(x)
    # print(next(i))
    # print(next(i))
    # print(next(i))
    # print(next(i))
    # print(next(i))
    # print(type(x))
    ## наскільки я зрозумів ітератор працює завдяки наякності метода __getitem__() що дозволяє переберати елементи.

    #перевірка запису в форматі txt
    x.deck_write('classic', 'txt')
    x.deck_load('classic', 'txt')

    # # перевірка запису в форматі shalve
    # s.deck_write('small')
    # s.deck_load('small')



