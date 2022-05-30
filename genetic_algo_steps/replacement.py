from .helper_functions import roulette, elitist, tournament, ranking, random


def replacement(population, pool_size, strategy="ranking"):
    # this could be replaced with match-case introduced in python 3.10
    return {
        "roulette": roulette(population),
        "elitist": elitist(population),
        "tournament": tournament(population),
        "ranking": ranking(population, pool_size=pool_size),
        "random": random(population),
    }[strategy]
