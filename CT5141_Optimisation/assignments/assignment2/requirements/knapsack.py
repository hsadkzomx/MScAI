import numpy as np

def eval_knapsack(weights, values, max_weight, x):
    """Knapsack evaluation function. Return both weight sum and value sum.

    `x` is a bool list specifying *which knapsack items we choose*

    Notice this is not a suitable *objective* function, because an
    objective function is a function of x only, and the objective
    is really just the value.

    But see below for a "closure" function which solves this.

    """

    # convert to np array for fancy indexing below
    x = np.array(x, dtype=bool)
    weight_sum = weights[x].sum()
    value_sum = values[x].sum()
    return weight_sum, value_sum

def read_knapsack_data(filename):
    """Read a knapsack data file.

    In these data files, the first line gives n_items and max_weight
    and remaining lines give the value and weight of each item.
    """
    
    data = np.genfromtxt(filename, delimiter=" ", dtype=int)
    n_items, max_weight = data[0]
    data = data[1:]
    values = data[:, 0]
    weights = data[:, 1]
    print(f"n_items {n_items}; max_weight {max_weight}")
    print(f"weight value")
    for w, v in zip(weights, values):
        print(f"{w} {v}")

    # Make a "closure", ie a function that has access to the necessary
    # variables define above. But it's a function of x only, so it's
    # suitable as a GA fitness function.
    def f(x):
        weight_sum, value_sum = eval_knapsack(weights, values, max_weight, x)
        if weight_sum > max_weight:
            return 0 # over-weight
        else:
            return value_sum

    return n_items, f
