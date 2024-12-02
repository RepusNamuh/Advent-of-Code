from collections import defaultdict
with open("Day 7\Camel_Card.txt", 'r') as f:
    data = f.read()

# Assigning card values.
card_values = {"A":13, "K":12, "Q":11, "J":10, "T": 9, "9": 8, "8":7, "7":6, "6":5, "5":4, "4":3, "3":2, "2":1}
card_values_1 = card_values.copy()
card_values_1["J"] = 0

# Assigning type/values of a hand, that is five of a kinds and so on
def score(hand):
    # Counting total value of each card in a hand
    counts = [hand.count(card) for card in hand]
    if 5 in counts:
        return 6
    if  4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0

# This function is for part 2 which identify J and turn it into the best character
def classify(hand):
    if "J" in hand: # can skip if there is no J
        key_count = defaultdict(int) 
        # Loop through hand to find letter repetition
        for char in hand:
            key_count[char] += 1

        max_key = ""
        max_count = 0

        # Through through key_count to find the character with highest repetition
        for key, values in key_count.items():
            if key == "J": # If J is included, case TTJJ1, JJ would not change into TT
                continue
            max_count = max(values, max_count)
            if max_count == values: # Get the character with the max value
                max_key = key
        if max_key != "": # In case of JJJJJ, since J is excluded, max_key = ""
            hand = hand.replace("J", max_key) 
    # Return modified hand, this doesn't affect the hand that pass through hand_strength
    return score(hand)

# Two function, they do the same thing, return the values/type of a hand along with a sortable
# value of each character in the hand
def hand_strength(hand):
    return (score(hand),[card_values.get(letter, letter) for letter in hand])

def hand_strength1(hand):
    return (classify(hand),[card_values_1.get(letter, letter) for letter in hand])

# Data manipulation: line by line
hands = []
for line in data.splitlines():
    hand, bid = line.split()
    hands.append((hand, int(bid)))


hands1 = hands.copy() # Don't have to manipulate the data again.

# Sorting function, again, they both do the same thing, sort from 
# highest hand type then sort highest hand between hand type.
hands.sort(key=lambda strength: hand_strength(strength[0]))
hands1.sort(key=lambda strength: hand_strength1(strength[0]))

total = 0
total1 = 0

# calculating the final result
for index, (hand, bid) in enumerate(hands, 1):
    total += index * bid

for index, (hand, bid) in enumerate(hands1, 1):
    print(hand, bid)
    total1 += index * bid


print(total)
print(total1)