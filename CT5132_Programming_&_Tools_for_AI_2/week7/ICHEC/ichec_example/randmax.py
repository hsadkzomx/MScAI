import random
import sys

# if the program is called as $ python randmax.py 3, then we have
# sys.argmax equal to ['randmax.py', '3'] so to get the seed we take
# argv[1] and convert to int.
seed = int(sys.argv[1])

# make our program deterministic, given this random seed
random.seed(seed)

# this is the main work of the program - just a placeholder for now
for i in range(10):
    print(max(random.sample(list(range(20)), 5)))
