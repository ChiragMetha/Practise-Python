import itertools, random
deck = list(itertools.product(range(1,14),['Spade', 'Heart', 'Diamond', 'Club']))
random.shuffle(deck)
print("The random cards are : ")
for i in range(5):
    print(deck[i][0],deck[i][1])