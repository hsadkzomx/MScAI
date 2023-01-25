import itertools
import random
import numpy as np
import matplotlib.pyplot as plt

def NSGA2(f, init, mutate, crossover, popsize, ngens, pmut):
    """Non-dominated sorting genetic algorithm 2 (Deb et al.).

    An elitist multi-objective optimisation algorithm with selection
    by Pareto front ranking and then sparsity.

    Minimisation, not maximisation.
    
    f(x) should return a tuple or list, one numerical value for each
    objective.  popsize indicates the number of new individuals
    created per generation.

    numpy is used in several places throughout these functions, and
    the population is stored as an array. however, these functions
    work ok even if the individuals themselves are not arrays or
    lists. they can be (eg) sets or trees or other objects. Numpy can
    store an array of objects of arbitrary types. its array indexing
    is still useful to us. on the other hand, the objective values
    must be floats. we store them in a numpy array also.

    # TODO: add hypervolume indicator
    # TODO: compare to simple algorithms like a Pareto Archive
    # TODO: plot
    # TODO: we should really remove p1 p2 after using them
    """

    # NSGA2 concatenates parents and children at each generation. we
    # want to keep the nice equation popsize * ngens == budget. so we
    # create popsize new individuals per generation. therefore when we
    # concatenate parents and children, we'll have 2*popsize from
    # which we select popsize to become parents. to make the initial
    # generation consistent (no parents or children, just init()), we
    # should create 2*popsize in the initial generation. to take
    # account of this (to avoid exceeding our budget), we start
    # generations at 2, not 1: we have range(2, ngens) below.
    pop = np.array([init() for _ in range(2 * popsize)]) 
    popfit = np.array([f(x) for x in pop])
    stats(0, popfit)
    history = []
    history.append(popfit)
    for gen in range(2, ngens):
        # select parents: popsize
        parents, parentsfit = selection_NSGA2(pop, popfit, popsize)

        # generate the children from the parents.
        children = []
        while len(children) < popsize:
            # parents are *good*, so no further selection
            p1, p2 = random.sample(parents, 2) 
            # crossover
            c1, c2 = crossover(p1, p2)
            # apply mutation to only a fraction of individuals
            # and add to set
            if random.random() < pmut:
                c1 = mutate(c1)
            children.append(c1)
            # add the second to set only if not full
            if len(children) < popsize:
                if random.random() < pmut:
                    c2 = mutate(c2)
                children.append(c2)
                
        # merge old population with new, evaluate, do stats
        children = np.array(children)
        childrenfit = np.array([f(x) for x in children])
        pop = np.concatenate((parents, children))
        popfit = np.concatenate((parentsfit, childrenfit))
        history.append(popfit)
        stats(gen, popfit)
    return history
        

def selection_NSGA2(pop, popfit, k):

    """The NSGA2 selection operator. Given a population, we will select k
    to become parents of the next generation. We are given their
    fitness values, that is one fitness value per objective per
    individual, in an array of shape (popsize, n_objs).

    We firstly select all those of Pareto Rank 1, then all of Rank 2,
    etc until in some later rank, it would give us more than k
    individuals in total. Within that rank, we select according to
    sparsity.

    We return the selected items and their fitness values, so
    that we don't need to re-run fitness on them later.

    Our implementation calculates successive Pareto fronts. This is
    more understandable but may be slower than the
    fast-nondominated-sort algorithm proposed by Deb et al.

    # PF1 = [1, 2] and [2, 1]; PF2 = the rest; [7, 2], [4, 4], [2, 7] are the sparsest
    >>> selection_NSGA2(np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
    ...                 np.array([[1, 2], [2, 1], [7, 2], [6, 3], [4, 4], [3, 6], [2, 7]]), 5)
    (['a', 'b', 'e', 'c', 'g'], [array([1, 2]), array([2, 1]), array([4, 4]), array([7, 2]), array([2, 7])])

    """

    assert pop.shape[0] == popfit.shape[0] > k
    parents = []
    parentsfit = []
    
    # find the first Pareto front (*minimising*)
    pf = is_pareto_efficient_simple(popfit) # a bool array
    
    while len(parents) + pf.sum() <= k: 
        # if this front would not make parents over-full, then select
        # it, and remove it from further consideration
        parents.extend(pop[pf])
        parentsfit.extend(popfit[pf])
        pop = pop[~pf] # ~ means choose positions where pf is False
        popfit = popfit[~pf]

        # find the next front and iterate
        pf = is_pareto_efficient_simple(popfit)

    # how many more do we need, to fill parents?
    k_ = k - len(parents) 
    if k_ > 0:

        # get this last front and its sparsity values
        last_front = pop[pf]
        last_front_fit = popfit[pf]
        last_front_sparsity = sparsity(last_front_fit)
        
        # use argsort to get the indexes of the most sparse items in
        # this front, and select them
        idx = np.argsort(last_front_sparsity)[-k_:]
        parents.extend(last_front[idx])
        parentsfit.extend(last_front_fit[idx])

    assert len(parents) == k
    return parents, parentsfit

def sparsity(inds):
    """Given the objective values for a set of points, calculate their
    sparsity values. For a single objective, for a single point,
    sparsity is the difference between the previous and next values of
    that objective, scaled by the (max - min) range of that
    objective. For each point we sum this over all objectives.

    # See crowding-distance-assignment (Deb et al)

    1. Start at the first objective
    2. Sort individuals according to the current objective
    3. The first and last items get += $\infty$ for sparsity
    4. Intermediate items get += (next - previous) / range
    5. Move to next objective and go to 2.

    # [6, 0] -> infinity
    # [5, 1] -> (6-3)/6 + (3-0)/6 = 1
    # [3, 3] -> (5-1)/6 + (5-1)/6 = 1.33
    
    >>> sparsity(np.array([[6, 0], [5, 1], [3, 3], [1, 5], [0, 6]]))
    [inf, 1.0, 1.3333333333333333, 1.0, inf]

    """

    # main ideas from https://github.com/DEAP/deap/blob/master/deap/tools/emo.py

    n_inds = inds.shape[0]
    n_objs = inds.shape[1]
    distances = [0.0] * n_inds
    # useful data structure for our computation:
    # [(obj0, obj1, ...), i]
    inds = [(ind, i) for i, ind in enumerate(inds)]

    for i in range(n_objs):
        
        inds.sort(key=lambda element: element[0][i]) # sort by obj i
        first, last = inds[0][0], inds[-1][0]
        firstidx, lastidx = inds[0][1], inds[-1][1]

        # calculate the max-min range of this objective. DEAP multiply
        # by n_objs here, but I think that is incorrect (but makes no
        # difference).
        maxmin = last[i] - first[i]
        
        if maxmin <= 10**-10:
            # inds are constant in this objective, so it makes no
            # contribution to sparsity. notice a common pattern in
            # numerical programming: if we're going to divide by
            # something, then there's often a good reason (eg a
            # special case) why, if it's zero, we actually don't need
            # to divide after all.
            continue          
        distances[firstidx] = float("inf") # first and last elements:
        distances[lastidx] = float("inf") # highly sparse
        
        for prev, cur, nxt in zip(inds[:-2], inds[1:-1], inds[2:]):
            # notice use of zip() with three args: get the whole list
            # in chunks of 3, stepping forward by 1 each time.
            # we divide by maxmin here so that all objectives have the
            # same influence on sparsity, even if one objective is in the
            # range [0, 1], another in [0, 1000], etc.
            distances[cur[1]] += (nxt[0][i] - prev[0][i]) / maxmin
    return distances
    

def is_pareto_efficient_simple(costs):
    """https://stackoverflow.com/questions/32791911/fast-calculation-of-pareto-front-in-python
    
    Find the pareto-efficient points.

    Fairly fast for many datapoints, less fast for many costs,
    somewhat readable.

    :param costs: An (n_points, n_costs) array
    :return: A (n_points, ) boolean array, indicating whether
    each point is Pareto efficient

    """
    is_efficient = np.ones(costs.shape[0], dtype = bool)
    for i, c in enumerate(costs):
        if is_efficient[i]:
            # Keep any point with a lower cost
            is_efficient[is_efficient] = np.any(costs[is_efficient]<c,
                                                axis=1)  
            is_efficient[i] = True  # And keep self
    return is_efficient
            

def plot_history(xs, filename):
    """Plot each population in xs as a scatter plot taking just the first
    two objectives (if there are only two, we'll take both).
    
    xs: a list of objective values of individuals of # populations.
    """

    for i, x in enumerate(xs):
        if i == len(xs) - 1:
            c = "black"; label = "final generation"
        else:
            c = "orange"; label = ""
        plt.scatter(x[:, 0], x[:, 1], alpha=0.5, c=c, label=label)
    plt.xlabel("f0")
    plt.ylabel("f1")
    plt.legend()
    plt.savefig(filename)
    plt.close()

def stats(gen, popfit):
    print(f"Stats: {gen:3d} {np.min(popfit[:, 0]):.2f} {np.min(popfit[:, 1]):.2f} {np.mean(popfit[:, 0]):.2f} {np.mean(popfit[:, 1]):.2f}")


def init():
    return np.random.random(D)

def mut(x):
    delta = 0.3
    x = x.copy()
    idx = np.random.randint(0, D)
    x[idx] = np.clip(x[idx] + delta * np.random.random(), 0, 1)
    return x

def uniform_crossover(p1, p2):
    c1, c2 = [], []
    for i in range(len(p1)):
        if random.random() < 0.5:
            c1.append(p1[i]); c2.append(p2[i])
        else:
            c1.append(p2[i]); c2.append(p1[i])
    return np.array(c1), np.array(c2)


def ZDT1(x):
    # from https://datacrayon.com/posts/search-and-optimisation/practical-evolutionary-algorithms/synthetic-objective-functions-and-zdt1/
    f1 = x[0]  # objective 1
    g = 1 + 9 * np.sum(x[1:D] / (D-1))
    h = 1 - np.sqrt(f1 / g)
    f2 = g * h  # objective 2
    return np.array([f1, f2])


D = 20
pmut = 0.1
popsize = 100
ngens = 50
NSGA2(ZDT1, init, mut, uniform_crossover, popsize, ngens, pmut)
