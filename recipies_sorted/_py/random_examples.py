import random
my_list = ['A'] * 5 + ['B'] * 5 + ['C'] * 90
random.choice(my_list)

=================================
from collections import Counter
from random import randint

def weighted_random(pairs):
    total = sum(pair[0] for pair in pairs)
    r = randint(1, total)
    for (weight, value) in pairs:
        r -= weight
        if r <= 0: return value

results = Counter(weighted_random([(1,'a'),(1,'b'),(18,'c')])
                  for _ in range(20000))
print(results)






#If you want to use weighted random and not percentile random, you can make your own Randomizer class:
import random

class WeightedRandomizer:
    def __init__ (self, weights):
        self.__max = .0
        self.__weights = []
        for value, weight in weights.items ():
            self.__max += weight
            self.__weights.append ( (self.__max, value) )

    def random (self):
        r = random.random () * self.__max
        for ceil, value in self.__weights:
            if ceil > r: return value

w = {'A': 1.0, 'B': 1.0, 'C': 18.0}
#or w = {'A': 5, 'B': 5, 'C': 90}
#or w = {'A': 1.0/18, 'B': 1.0/18, 'C': 1.0}
#or or or

wr = WeightedRandomizer (w)
results = {'A': 0, 'B': 0, 'C': 0}
for i in range (10000):
    results [wr.random () ] += 1

print ('After 10000 rounds the distribution is:')
print (results)


#Use random seed and sample function together
fruit_list = ["Apple", "Mango", "Banana", "Apricot", "Cherries", "Grape", "Kiwi"]
random.seed(3)
sample_list = random.sample(fruit_list, 3)
print("First sample fruit list ", sample_list)
random.seed(3)
sample_list = random.sample(fruit_list, 3)
print("Second sample fruit list ", sample_list)
random.seed(3)
sample_list = random.sample(fruit_list, 3)
print("Third sample fruit list ", sample_list)

#Use the random’s seed and shuffle function together
import random
numbers = [10, 20, 30, 40, 50, 60]
print ("Original list: ", numbers )
random.seed(4)
random.shuffle(numbers)
print("reshuffled list ", numbers)
numbers = [10, 20, 30, 40, 50, 60]
random.seed(4)
random.shuffle(numbers)
print("reshuffled list ", numbers)