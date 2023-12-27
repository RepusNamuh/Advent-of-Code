from collections import defaultdict
with open("Day 7\Camel_Card.txt", 'r') as f:
    data = f.read()

# Assigning card values.
card_values = {"A":13, "K":12, "Q":11, "J":10, "T": 9, "9": 8, "8":7, "7":6, "6":5, "5":4, "4":3, "3":2, "2":1}
card_values_1 = card_values.copy()
card_values_1["J"] = 0
# Creating a list for hands and its' value

def score(hand):
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

def classify(hand):
    if "J" in hand:
        key_count = defaultdict(int)
        for char in hand:
            key_count[char] += 1
        max_key = ""
        max_count = 0
        for key, values in key_count.items():
            if key == "J":
                continue
            max_count = max(values, max_count)
            if max_count == values:
                max_key = key
        if max_key != "":
            hand = hand.replace("J", max_key)
    return score(hand)

def hand_strength(hand):
    return (score(hand),[card_values.get(letter, letter) for letter in hand])

def hand_strength1(hand):
    return (classify(hand),[card_values_1.get(letter, letter) for letter in hand])

hands = []
for line in data.splitlines():
    hand, bid = line.split()
    hands.append((hand, int(bid)))

hands1 = hands.copy()


hands.sort(key=lambda strength: hand_strength(strength[0]))
hands1.sort(key=lambda strength: hand_strength1(strength[0]))

total = 0
total1 = 0

for index, (hand, bid) in enumerate(hands, 1):
    total += index * bid

for index, (hand, bid) in enumerate(hands1, 1):
    print(hand, bid)
    total1 += index * bid


print(total)
print(total1)