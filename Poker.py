import numpy as np
import random

anz_paar = 0
anz_drilling = 0
anz_straight = 0
def create_card_deck(count):
    cards_per_suit = count // 4
    card_deck = np.arange(1, count+1)
    # print(card_deck)
    return card_deck, cards_per_suit

def draw_five_cards(card_deck):
    random.shuffle(card_deck)  # Das Deck mischen
    selected_cards = card_deck[:5]
    # print(selected_cards)
    return selected_cards

def paar(selected_cards, cards_per_suit):
    for i in range(len(selected_cards)):
        for j in range(i + 1, len(selected_cards)):
            if selected_cards[i] % cards_per_suit == selected_cards[j] % cards_per_suit:
                # print(selected_cards[i], selected_cards[j])
                # print("Paar gezogen")
                return True
    # print("kein Paar gezogen")
    return False

def drillinge(selected_cards, cards_per_suit):
    for i in range(len(selected_cards)):
        for j in range(i + 1, len(selected_cards)):
            for x in range(j + 1, len(selected_cards)):
                if selected_cards[i] % cards_per_suit == selected_cards[j] % cards_per_suit == selected_cards[x] % cards_per_suit:
                    #print(selected_cards[i], selected_cards[j], selected_cards[x])
                    #print("Drilling gezogen")
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

def royal_flush(selected_cards, cards_per_suit):
    if(flush(selected_cards, cards_per_suit)):
        sorted_cards = sorted(selected_cards)
        if(straight(selected_cards)):
            if(sorted_cards[0] == cards_per_suit-4 or sorted_cards[0] == cards_per_suit*2-4 or sorted_cards[0] == cards_per_suit*3-4 or sorted_cards[0] == cards_per_suit*4-4):
                # print("Royal Flush")
                return True
    return False

def straight(selected_cards):
    sorted_cards = sorted(selected_cards)
    #print(sorted_cards)
    for i in range(len(sorted_cards) - 1):
        if sorted_cards[i] + 1 != sorted_cards[i + 1]:
            return False
    # print("Street")
    return True

games = 100000
for i in range(games):
    card_deck, cards_per_suit = create_card_deck(52)
    on_hand = draw_five_cards(card_deck)
    if(paar(on_hand, cards_per_suit)):
         anz_paar+= 1
    if(drillinge(on_hand, cards_per_suit)):
        anz_drilling+=1
    # if(flush(on_hand, cards_per_suit)):
    #     flush+=1
    if(straight(on_hand)):
        anz_straight+= 1
    # if(royal_flush(on_hand,cards_per_suit)):
    #     royal_flush+=1
print(anz_paar/games*100)
print(anz_drilling/games*100)
print(anz_straight/games*100)