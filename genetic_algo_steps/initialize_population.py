import time
from random import randint, seed

seed(time.time())


def init_population(g, pool_size):
    initial_population = [
        [randint(0, g.num_vertices) for __ in range(g.num_vertices)]
        for _ in range(pool_size)
    ]
    return initial_population
