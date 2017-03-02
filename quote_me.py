import pickle
import random

with open ('quotes.txt', 'rb') as fp:
    quote_list = pickle.load(fp)

index = random.randint(0, len(quote_list))
print quote_list[index][0], quote_list[index][1]
