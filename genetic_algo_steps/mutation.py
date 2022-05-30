import time
from random import randint, seed, uniform

from .helper_functions import individual_dies

seed(time.time())


def mutation(individual):
    colors = list(set(individual))
    gene = randint(0, len(individual) - 1)
    new_gene = randint(0, len(colors) - 1)
    while colors[new_gene] == individual[gene]:
        new_gene = randint(0, len(colors) - 1)

    individual[gene] = colors[new_gene]


def mutation_in_pool(g, population, mutation_proba):
    new = []
    for individual in population:
        proba = uniform(0.0, 0.99)
        if proba <= mutation_proba:
            mutation(individual)
        if not individual_dies(g, individual):
            new.append(individual)
            # check if individual is the best fitting to update the solution
            if g.update_solution(individual):
                print("solution updated!")
    return new
