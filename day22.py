import sys
from copy import deepcopy
sys.path.append("./")

def init_decks(filename="./puzzle_inputs/day22.input"):
    deck1 = []
    deck2 = []
    f = open(filename)
    line = f.readline().strip()
    line = f.readline().strip()
    while line:
        deck1.append(int(line))
        line = f.readline().strip()
    line = f.readline().strip()
    line = f.readline().strip()
    while line:
        deck2.append(int(line))
        line = f.readline().strip()
    return deck1,deck2

def play_game(deck1, deck2):
    while deck1 and deck2:
        # do game logic here 
        drawn_card_1 = deck1.pop(0)
        drawn_card_2 = deck2.pop(0)
        if drawn_card_1>drawn_card_2:
            deck1.append(drawn_card_1)
            deck1.append(drawn_card_2)
        else:
            deck2.append(drawn_card_2)
            deck2.append(drawn_card_1)
        continue
    return deck1 if deck1 else deck2

def play_recurrsive_combat(deck1, deck2, recurrsive_depth = 0):
    seen_decks = []
    while deck1 and deck2:
        # catch previous rounds
        if [deepcopy(deck1),deepcopy(deck2)] in seen_decks:
            return deck1, "Player 1", True
        else:
            seen_decks.append([deepcopy(deck1),deepcopy(deck2)])
        # draw cards
        p1_card = deck1.pop(0)
        p2_card = deck2.pop(0)
        play_recursive = len(deck1)>=p1_card and len(deck2)>=p2_card
        winner = ""
        if play_recursive:
            _,winner,_ = play_recurrsive_combat(deck1[:p1_card], deck2[:p2_card],recurrsive_depth+1)
        else:
            winner = "Player 1" if p1_card>p2_card else "Player 2"
        if winner == "Player 1":
            deck1.append(p1_card)
            deck1.append(p2_card)
        else:
            deck2.append(p2_card)
            deck2.append(p1_card)
    return (deck1,"Player 1",False) if deck1 else (deck2,"Player 2",False)

def score_deck(deck):
    score = 0
    while deck:
        score += len(deck)*deck[0]
        deck.pop(0)
    return score

decks = init_decks()
winning_deck = play_game(decks[0], decks[1])
score = score_deck(winning_deck)
print(score)

decks2 = init_decks()
winning_deck = play_recurrsive_combat(decks2[0], decks2[1])
score = score_deck(winning_deck[0])
print(score)