import numpy as np
import random

anz_pair = 0
anz_drilling = 0
anz_vierling = 0
anz_straight = 0
anz_two_pair = 0
anz_high_card = 0
anz_flush = 0
anz_straight = 0
anz_royal_flush = 0
anz_full_house = 0
anz_straight_flush = 0


def create_card_deck(count):
    cards_per_suit = count // 4
    card_deck = np.arange(1, count+1)
    # print(card_deck)
    return card_deck, cards_per_suit

def draw_five_cards(card_deck):
    random.shuffle(card_deck)  # Das Deck mischen
    selected_cards = card_deck[:5]
    #print(selected_cards)
    return selected_cards

def paar(selected_cards, cards_per_suit):
    for i in range(len(selected_cards)):
        for j in range(i + 1, len(selected_cards)):
            if selected_cards[i] % cards_per_suit == selected_cards[j] % cards_per_suit:
                #print(selected_cards[i], selected_cards[j])
                #print("pairgezogen")
                return True
    #print("kein pairgezogen")
    return False
def two_paare(selected_cards, cards_per_suit):
    pairs = set()
    for i in range(len(selected_cards)):
        for j in range(i + 1, len(selected_cards)):
            if selected_cards[i] % cards_per_suit == selected_cards[j] % cards_per_suit:
                pairs.add(selected_cards[i] % cards_per_suit)

    if len(pairs) == 2:
        return True
    else:
        return False

def three_of_a_kind(selected_cards, cards_per_suit):
    for i in range(len(selected_cards)):
        for j in range(i + 1, len(selected_cards)):
            for x in range(j + 1, len(selected_cards)):
                if selected_cards[i] % cards_per_suit == selected_cards[j] % cards_per_suit == selected_cards[x] % cards_per_suit:
                    #print(selected_cards[i], selected_cards[j], selected_cards[x])
                    #print("Drilling gezogen")
                    return True
    #print("kein Drilling gezogen")
    return False
def four_of_a_kind(selected_cards, cards_per_suit):
    for i in range(len(selected_cards)):
        for j in range(i + 1, len(selected_cards)):
            for x in range(j + 1, len(selected_cards)):
                for z in range(x + 1, len(selected_cards)):
                    if selected_cards[i] % cards_per_suit == selected_cards[j] % cards_per_suit == selected_cards[x] % cards_per_suit == selected_cards[z] % cards_per_suit:
                        return True
    #print("kein Drilling gezogen")
    return False
def flush(selected_cards, cards_per_suit):
    suits = [i // (cards_per_suit + 0.01) for i in selected_cards] #erstellen Liste die die Farben enthält
    if all(suit == suits[0] for suit in suits): # überprüft, ob alle Elemente der Liste suits gleich sind
        # print("Flush gezogen")
        return True
    return False
    # first_suit = selected_cards[0] // (cards_per_suit +0.01)
    # second_suit = selected_cards[1] // (cards_per_suit + 0.01)
    # third_suit = selected_cards[2] // (cards_per_suit +0.01)
    # fourth_suit = selected_cards[3] // (cards_per_suit + 0.01)
    # fifth_suit = selected_cards[4] // (cards_per_suit + 0.01)
    # if(first_suit == second_suit == third_suit == fourth_suit == fifth_suit):
    #     print("flush")
    #     return True
    # return False

def royal_flush(selected_cards,cards_per_suit):
    sorted_cards = sorted(selected_cards)
    if(straight_flush(sorted_cards) and sorted_cards[4] % cards_per_suit == 0):
        return True
    return False

def straight(selected_cards, cards_per_suit):
    # Sortiere die ausgewählten Karten
    # Extrahiere nur die Werte der Karten, um die Farbe zu ignorieren
    values = [card % cards_per_suit for card in selected_cards]
    sorted_cards = sorted(values)
    # Iteriere über die Werte und überprüfe, ob es sich um eine Straße handelt
    for i in range(len(sorted_cards) - 1):
        if sorted_cards[i] + 1 != sorted_cards[i + 1]:
            return False
    return True

def straight_flush(selected_cards):
    sorted_cards = sorted(selected_cards)
    # Iteriere über die Werte und überprüfe, ob es sich um eine Straße handelt
    for i in range(len(sorted_cards) - 1):
        if sorted_cards[i] + 1 != sorted_cards[i + 1]:
            return False
    return True

def full_house(selected_cards, cards_per_suit):
    value = 0
    if three_of_a_kind(selected_cards, cards_per_suit):
        value +=1
        if two_paare(selected_cards, cards_per_suit):
            value +=1
            if(value == 2):
                return True

games = 100000
for i in range(games):
    card_deck, cards_per_suit = create_card_deck(52)
    on_hand = draw_five_cards(card_deck)
    # on_hand = selected_cards = [26, 25, 24, 23, 22]
    # on_hand = selected_cards = [1, 14, 27, 2, 15]

    if(royal_flush(on_hand,cards_per_suit)):
        anz_royal_flush+=1
    elif(straight_flush(on_hand)):
        anz_straight_flush+=1
    elif (four_of_a_kind(on_hand, cards_per_suit)):
        anz_vierling += 1
    elif(full_house(on_hand, cards_per_suit)):
        anz_full_house+=1
    elif(flush(on_hand, cards_per_suit)):
        anz_flush+=1
    elif(straight(on_hand, cards_per_suit)):
        anz_straight+=1
    elif(three_of_a_kind(on_hand, cards_per_suit)):
        anz_drilling+=1
    elif(two_paare(on_hand, cards_per_suit)):
        anz_two_pair+=1
    elif(paar(on_hand, cards_per_suit)):
        anz_pair+= 1

print("Royal Flush: {:.6f}%".format(anz_royal_flush / games * 100))
print("Straight Flush:", anz_straight_flush/games*100)
print("4-of-a-Kind:", anz_vierling / games * 100)
print("Full House:", anz_full_house/games*100)
print("Flush:", anz_flush/games*100)
print("Straight:", anz_straight/games*100)
print("3-of-a-Kind:", anz_drilling/games*100)
print("Two Pair:", anz_two_pair/games*100)
print("One Pair:", anz_pair/games*100)




