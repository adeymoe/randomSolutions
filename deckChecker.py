def define_suit(card):
    cards = list(card)
    if cards[-1] == "C":
        return "clubs"
    elif cards[-1] == "H":
        return "hearts"
    elif cards[-1] == "D":
        return "diamonds"
    elif cards[-1] == "S":
        return "spades"
    else:
        return "not valid"
    pass