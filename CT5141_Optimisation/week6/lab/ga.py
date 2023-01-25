import random

"""
This is a very simple GA implementation. It uses pure Python,
no Numpy. It maximises (see 'max' in tournament, stats, and GA).

The pop data structure is a list of tuples, and each tuple
is (fitness, genome), and fitness is a float, and a
genome is a list of 0s and 1s. So like this:

[
  (fitness, [gene0, gene1, gene2, ... gene n-1]),
  (fitness, [gene0, gene1, gene2, ... gene n-1]),
  (fitness, [gene0, gene1, gene2, ... gene n-1]),
  ...
]
"""

def GA(f, init, nbr, crossover, select, popsize, ngens, tsize):
    
    # make initial population, evaluate fitness, print stats
    inds = [init() for _ in range(popsize)]
    pop = [(f(x), x) for x in inds]
    stats(0, pop)
    
    for gen in range(1, ngens):
        # make a new population, evaluate fitness, print stats
        inds = [nbr(crossover(select(pop, tsize), select(pop, tsize)))
                  for _ in range(popsize)]
        pop = [(f(x), x) for x in inds]
        stats(gen, pop)
        
    return max(pop)

def stats(gen, pop):
    fbest, xbest = max(pop)
    print(f"{gen} {fbest} {xbest}")
    
def tournament_select(pop, size):
    candidates = random.sample(pop, size)
    # The winner is the index of the individual with max fitness, ie c[0]
    winner = max(candidates, key=lambda c: c[0])
    return winner[1] # return the genome only

def init():
    return [random.randrange(2) for _ in range(genome_length)]

def bitflips(p):
    return [(1 - pi if random.random() < 1.0 / len(p) else pi)
            for pi in p]

def uniform_crossover(p1, p2):
    return [(p1i if random.random() < 0.5 else p2i)
            for p1i, p2i in zip(p1, p2)]

eval_budget = 5000
popsize = 100
ngens = eval_budget // popsize
tsize = 3

##### Simplest test function
genome_length = 30
f = sum # test problem: find the string of all 1s
#####

##### Harder test functions
from knapsack import read_knapsack_data
problem_filename = "knapsack_data/f1_l-d_kp_10_269"
problem_filename = "knapsack_data/f8_l-d_kp_23_10000"
genome_length, f = read_knapsack_data(problem_filename)
#####

GA(f,
   init,
   bitflips,
   uniform_crossover,
   tournament_select,
   popsize,
   ngens,
   tsize
)

