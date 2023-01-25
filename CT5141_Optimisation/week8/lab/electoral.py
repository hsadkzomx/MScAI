import pandas as pd
import random
import numpy as np

def uniform_crossover(p1, p2):
    c1, c2 = [], []
    for i in range(len(p1)):
        if random.random() < 0.5:
            c1.append(p1[i]); c2.append(p2[i])
        else:
            c1.append(p2[i]); c2.append(p1[i])
    return np.array(c1), np.array(c2)


# our standard bitstring init. use lambda: init(n) to give a function
# that takes no parameters.
def init(n):
    return [random.randrange(2) for _ in range(n)]

# our usual bitstring nbr
def nbr(x):
    x = x.copy()
    i = random.randrange(len(x))
    x[i] = 1 - x[i]
    return x


# this GA is for minimisation
def GA(f, init, nbr, crossover, select, popsize, ngens, pmut):
    # make initial population, evaluate fitness, print stats
    pop = [init() for _ in range(popsize)]
    popfit = [f(x) for x in pop]
    stats(0, popfit)
    for gen in range(1, ngens):
        # make an empty new population
        newpop = []
        while len(newpop) < popsize:
            # select and crossover
            p1 = select(pop, popfit)
            p2 = select(pop, popfit)
            c1, c2 = crossover(p1, p2)
            # apply mutation to only a fraction of individuals
            if random.random() < pmut:
                c1 = nbr(c1)
            if random.random() < pmut:
                c2 = nbr(c2)
            # add the new individuals to the population
            newpop.append(c1)
            newpop.append(c2)
        # overwrite old population with new, evaluate, do stats
        pop = newpop
        popfit = [f(x) for x in pop]
        stats(gen, popfit)
    bestidx = np.argmin(popfit)
    return pop[bestidx], popfit[bestidx]

def stats(gen, popfit):
    print("Stats", gen, np.min(popfit))
    
def tournament_select(pop, popfit, size):
    # To avoid re-calculating f for same individual multiple times, we
    # put fitness evaluation in the main loop and store the result in
    # popfit. We pass that in here.  Now the candidates are just
    # indices, representing individuals in the population.
    candidates = random.sample(list(range(len(pop))), size)
    # The winner is the index of the individual with min fitness.
    winner = min(candidates, key=lambda c: popfit[c])
    return pop[winner]


def fitness(d, x):
    x = np.array(x).astype(bool)
    # minimize the difference in votes.
    vote0 = d[~x]["votes"].sum()
    vote1 = d[x]["votes"].sum()
    if vote0 == vote1:
        print(d[x])
        print(d[x].sum())
        sys.exit()
    return abs(vote0 - vote1)


d = pd.read_csv("electoral_college.csv", skiprows=1)
d.columns = ["rank", "name", "votes"]
n = d.shape[0]
popsize = 10
ngens = 20
pmut = 0.1
tsize = 2

GA(lambda x: fitness(d, x),
   lambda: init(n),
   nbr,
   uniform_crossover,
   lambda pop, popfit: tournament_select(pop, popfit, tsize),
   popsize,
   ngens,
   pmut
)
