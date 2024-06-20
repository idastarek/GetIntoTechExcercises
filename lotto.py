import random

# generating 6 unique random lottery numbers from 1 to 50
# storing them in a set and displaying them 

lotto_set = set()
while len(lotto_set) < 6:
    lotto_set.add(random.randint(0,50))
    if len(lotto_set) == 6:
        print(lotto_set)