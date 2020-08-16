import re
card1, card2 = map(lambda x: list(filter(lambda y: y != '', re.split(r'(\d*)(\w)', x))), input().split())
trump_card: str = input()
rules: dict = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def is_trump(suit):
    return suit == trump_card


card1[0] = rules[card1[0]]
card2[0] = rules[card2[0]]

if is_trump(card1[1]) and not is_trump(card2[1]):
    print('First')
elif not is_trump(card1[1]) and is_trump(card2[1]):
    print('Second')
elif card1[1] != card2[1]:
    print('Error')
else:  # if cards have same suit:
    if card1[0] > card2[0]:
        print('First')
    else:
        print('Second')
