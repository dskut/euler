#! /usr/bin/env python

HighCard = 0
Pair = 1
TwoPairs = 2
Three = 3
Straight = 4
Flush = 5
FullHouse = 6
Four = 7
StraightFlush = 8
RankNames = {HighCard: "HighCard"
        , Pair: "Pair"
        , TwoPairs: "TwoPairs"
        , Three: "Three"
        , Straight: "Straight"
        , Flush: "Flush"
        , FullHouse: "FullHouse"
        , Four: "Four"
        , StraightFlush: "StraightFlush"
        }

class Card:
    def __init__(self, card_str):
        self.suit = card_str[1]
        if card_str[0] == 'T':
            self.value = 10
        elif card_str[0] == 'J':
            self.value = 11
        elif card_str[0] == 'Q':
            self.value = 12
        elif card_str[0] == 'K':
            self.value = 13
        elif card_str[0] == 'A':
            self.value = 14
        else:
            self.value = int(card_str[0])


class Combo:
    def __init__(self, rank, equals, cards):
        self.rank = rank
        self.equals = equals
        self.cards = cards

    def pprint(self):
        print RankNames[self.rank]

    def beats(self, other):
        if self.rank != other.rank:
            return self.rank > other.rank
        for i in xrange(0, len(self.equals)):
            if self.equals[i].value != other.equals[i].value:
                return self.equals[i].value > other.equals[i].value
        return None

class Equal:
    def __init__(self, value, count):
        self.value = value
        self.count = count

    def compare(self, other):
        if self.count != other.count:
            return self.count - other.count
        return self.value - other.value

def make_cards(card_strings):
    return [Card(card_str) for card_str in card_strings]


def check_flush(cards):
    suit = cards[0].suit
    for card in cards:
        if card.suit != suit:
            return False
    return True

def check_straight(cards):
    sorted_cards = sorted(cards, key=lambda card: card.value, reverse=True)
    for i in xrange(1, len(sorted_cards)):
        if sorted_cards[i-1].value != sorted_cards[i].value + 1:
            return False
    return True

def count_equal(cards):
    freqs = {}
    for card in cards:
        if card.value in freqs:
            freqs[card.value] += 1
        else:
            freqs[card.value] = 1
    equals = [Equal(t[0], t[1]) for t in freqs.items()]
    return sorted(equals, cmp=lambda x,y: x.compare(y), reverse=True)


def get_combo(cards):
    equals = count_equal(cards)
    is_flush = check_flush(cards)
    if equals[0].count == 1:
        is_straight = check_straight(equals)
        if is_straight and is_flush:
            return Combo(StraightFlush, equals, cards)
        elif is_flush:
            return Combo(Flush, equals, cards)
        elif is_straight:
            return Combo(Straight, equals, cards)
        else:
            return Combo(HighCard, equals, cards)
    if equals[0].count == 4:
        return Combo(Four, equals, cards)
    elif equals[0].count == 3:
        if equals[1].count == 2:
            return Combo(FullHouse, equals, cards)
        else:
            return Combo(Three, equals, cards)
    elif equals[0].count == 2:
        if equals[1].count == 2:
            return Combo(TwoPairs, equals, cards)
        else:
            return Combo(Pair, equals, cards)
    else:
        # impossible
        return None
        

count = 0
with open("54-poker.txt") as f:
    for line in f:
        cards = make_cards(line.split())
        first_cards = cards[:5]
        second_cards = cards[5:]
        first_combo = get_combo(first_cards)
        second_combo = get_combo(second_cards)
        print line.split()[:5]
        first_combo.pprint()
        print line.split()[5:]
        second_combo.pprint()
        if first_combo.beats(second_combo):
            print "first wins!"
            count += 1
        else:
            print "second wins"
print count
