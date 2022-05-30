import time
from random import randint, seed, uniform

from .helper_functions import individual_dies

seed(time.time())


def crossing(father, mother, manner="1"):
    def uniform_crossing(father, mother):
        first_child, second_child = father.copy(), mother.copy()
        for i in range(len(father)):
            if randint(0, 1) == 1:
                first_child[i], second_child[i] = second_child[i], first_child[i]
        return first_child, second_child

    def k_points_crossing(father, mother, k):
        # to avoid infinite loop when looking for random points
        assert k <= len(father) - 1

        segments = [0, len(father)]
        while len(segments) < k + 2:
            random_point = randint(1, len(father) - 1)
            if random_point not in segments:
                segments.append(random_point)
        segments.sort()

        first_child, second_child = father.copy(), mother.copy()
        cross = False
        for i in range(len(segments) - 1):
            if cross:
                (
                    first_child[segments[i] : segments[i + 1]],
                    second_child[segments[i] : segments[i + 1]],
                ) = (
                    second_child[segments[i] : segments[i + 1]],
                    first_child[segments[i] : segments[i + 1]],
                )
            cross = not cross
        return first_child, second_child

    assert len(father) == len(mother)
    return (
        uniform_crossing(father, mother)
        if manner == "uniforme"
        else k_points_crossing(father, mother, int(manner))
    )


def crossing_in_pool(g, population, crossing_proba, manner="uniform"):
    initial_pop_size = len(population)
    # will_cross = [i for i in range(initial_pop_size) if uniform(0.0, 0.99) < crossing_proba]

    for father in range(initial_pop_size // 2):
        for mother in range(initial_pop_size // 2, initial_pop_size):
            if uniform(0.0, 0.99) >= crossing_proba:
                continue

            children = crossing(population[father], population[mother], manner)
            for child in children:
                if not individual_dies(g, child) and child not in population:
                    population.append(child)
