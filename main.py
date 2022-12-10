import random


class Console:
    def clear(self):
        print("\n" * 15)

    def wait(self):
        a = input()


operate = Console()

counter = {
    '9': 0,
    '10': 10,
    'j': 2,
    'd': 3,
    'k': 4,
    'a': 11
}
suits_nums = {
    'h': 0,
    'd': 1,
    's': 2,
    'c': 3
}
num_suts = ['h', 'd', 's', 'c']


class Card:
    __slots__ = ["_nom", "_suit", "_trump"]

    def __init__(self, nom='', suit=''):
        if suit == '':
            nom, suit = nom.split()
        self._nom = nom
        self._suit = suit
        self._trump = False

    def trumpify(self):
        self._trump = True

    def untrumpify(self):
        self._trump = False

    def get_suit(self):
        return self._suit

    def get_nom(self):
        return self._nom

    def __str__(self):
        return self._nom + ' ' + self._suit

    def __lt__(self, other):
        if self._trump and not other._trump:
            return False
        elif not self._trump and other._trump:
            return True
        elif self._suit == other._suit:
            return self.get_nom() < other.get_nom()
        else:
            return NotImplemented

    def __eq__(self, other):
        return self.get_nom() == other.get_nom() and self.get_suit() == other.get_suit()

    def __gt__(self, other):
        return not self < other


class CardSet:
    __slots__ = ["_cards"]

    def __init__(self, h):
        self._cards = []
        for i in h:
            self.add(i)

    def get_size(self):
        return len(self.get_cards())

    def add(self, c):
        self._cards.append(c)

    def shuffle(self):
        random.shuffle(self._cards)

    def pull_top(self):
        t = self._cards[-1]
        self._cards.pop()
        return t

    def get_cards(self):
        return self._cards

    def empty(self):
        return len(self._cards) == 0

    def extr(self, c):
        self._cards.remove(c)

    def loot(self, sett):
        while not sett.empty():
            self.add(sett.pull_top())


class Deck(CardSet):

    def __init__(self):
        self._cards = []
        for i in ['9', '10', 'j', 'd', 'k', 'a']:
            for j in ['h', 'c', 's', 'd']:
                self.add(Card(i, j))
        self.shuffle()


class Hand(CardSet):

    def trumpify(self, trump):
        for i in range(len(self._cards)):
            if self._cards[i].get_suit() == trump:
                self._cards[i].trumpify()
            else:
                self._cards[i].untrumpify()

    def show(self):
        for i in self._cards:
            print(i)


class Player:
    __slots__ = ["_hand", "_bet", "_starts", "_loot", "_marriage", "_res"]

    def __init__(self, hand=""):
        if type(hand) == str:
            hand = list(map(Card, hand.split()))
            return
        self._hand = Hand(hand)
        self._loot = CardSet([])
        self._bet = 0
        self._starts = 0
        self._res = 0
        self._marriage = {
            'h': 0,
            'c': 0,
            's': 0,
            'd': 0
        }

    def make_bet(self, g):
        t = input()
        if not t.isdigit():
            self._bet = t
            return
        t = int(t)
        if t < g.cur_bet:
            raise ValueError
        g.cur_bet = t
        self._bet = t

    def first(self):
        self._bet = 100
        self._starts = True

    def get_bet(self):
        return self._bet

    def stop(self):
        self._starts = False

    def add(self, c):
        self._hand.add(c)

    def give(self, other):
        C = input()
        marriage = False
        if C.endswith("марьяж"):
            C = C[:-7]
            marriage = True
        c = Card(C)
        self._hand.extr(c)
        other.add(c)
        if marriage:
            self._marriage[c.get_suit()] += 1
            return True

    def is_empty(self):
        return len(self._hand.get_cards()) == 0

    def starts(self):
        return self._starts

    def show_hand(self):
        self._hand.show()

    def loot(self, sett):
        self._hand.loot(sett)

    def trumpify(self, trump):
        self._hand.trumpify(trump)

    def halava(self, sett):
        self._loot.loot(sett)

    def count_total(self):
        for i in self._loot:
            self._res += counter[i.get_suit()]
        for key, val in self._marriage.items():
            if val == 1:
                self._res += counter[key]

    def show_res(self):
        return self._res


class Bot(Player):

    def eval(self, g):
        subhand = [[0]]
        for i in self._hand.get_cards():
            if subhand[]

    def make_bet(self, g):
        t = self.eval(g)
        self._bet = t
        if t.isdigit():
            g.cur_bet = t


class Game:
    __slots__ = ["_table", "cur_bet", "_plays", "_stack", "_players", "_trump"]

    def __init__(self, num=0):
        self._trump = 'none'
        self._table = CardSet([])
        self.cur_bet = -1
        self._plays = -1
        self._stack = Deck()
        if num not in range(3, 5):
            raise (ValueError)
        self._players = [Player()] * num
        ll = (self._stack.get_size() - num) // num
        for i in range(num):
            h = []
            for j in range(ll):
                h.append(self._stack.pull_top())
            self._players[i] = Player(h)
        for i in range(len(self._players)):
            print(str(i + 1) + ':')
            self._players[i].show_hand()
            operate.wait()
            operate.clear()

    def trumpify(self, trump):
        self._trump = trump
        for i in self._players:
            i.trumpify(trump)

    def bet(self):
        self._players[0].first()
        self.cur_bet = 100
        self._plays = 0
        cnt = 1
        for i in range(1, len(self._players)):
            if self._players[i].get_bet() == "пас":
                print("пас")
                operate.wait()
                continue
            print(str(i + 1) + ':')
            self._players[i].show_hand()
            self._players[i].make_bet(self)
            if type(self._players[i].get_bet()) == int:
                cnt += 1
                self._plays = i
                self._players[i].first()
            operate.clear()
        while cnt > 1:
            cnt = 0
            for i in range(len(self._players)):
                if self._players[i].get_bet() == "пас":
                    operate.wait()
                    continue
                print(str(i + 1) + ':')
                self._players[i].show_hand()
                self._players[i].make_bet(self)
                if type(self._players[i].get_bet()) == int:
                    cnt += 1
                    self._plays = i
                    self._players[i].first()
                operate.clear()

        self._players[self._plays].loot(self._stack)
        print(str(self._plays + 1) + ':')
        self._players[self._plays].show_hand()
        self._players[self._plays].make_bet(self)
        operate.clear()
        self._players[self._plays].show_hand()
        for i in range(len(self._players)):
            if i != self._plays:
                print(str(i + 1) + ":")
                self._players[self._plays].give(self._players[i])

    def show_table(self):
        if len(self._table.get_cards()) == 0:
            print("empty")
            return
        for i in self._table.get_cards():
            print(str(i) + ' ')

    def play(self):
        while not self._players[0].is_empty():
            mx = 0
            t = self._plays
            poss = 0
            for i in range(t, len(self._players) + t):
                cur_ind = i % len(self._players) + 1
                operate.clear()
                print(str(cur_ind) + ':')
                self._players[cur_ind - 1].show_hand()
                print("Стол:")
                self.show_table()
                print("Козырь:")
                print(self._trump)
                mar = self._players[cur_ind - 1].give(self._table)
                if i == t:
                    mx = self._table.get_cards()[-1]
                    poss = self._table.get_cards()[-1].get_suit()
                if mar:
                    self.trumpify(self._table.get_cards()[-1].get_suit())
                if poss == self._table.get_cards()[-1].get_suit() and self._table.get_cards()[-1] > mx:
                    mx = self._table.get_cards()[-1]
                    self._plays = cur_ind - 1
            self._players[self._plays].halava(self._table)

    def show_res(self):
        for i in range(len(self._players)):
            print(str(i) + ':')
            if self._plays == i:
                if self._players[i].show_res() >= self._players[i].get_bet():
                    print(self._players[i].get_bet())
                else:
                    print(-self._players[i].get_bet())
            else:
                print(self._players[i].show_res())


if __name__ == "__main__":
    n = int(input())
    g = Game(n)
    g.bet()
    g.play()
    g.show_res()
