import random
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

popsize=50
generations=100
colors=[0,1,2,3,4,5,6,7]



def random_population():
  pop = []
  for i in range(popsize):
    chromo = []
    for c in range(lenchromo):
        x=random.choice(colors)
        chromo.append(x)
    pop.append(chromo)
  return pop

def fitness(chromo):
  fitness = 0
  for key,value in graph.items():
      for x in value:
          if (chromo[x]!=chromo[key]):
              fitness+=1
  return fitness


def mutate1(chromo):
    for noeud in range(lenchromo):
        adjacents=graph.get(noeud)
        adjacents_colors = []
        for adjacent in adjacents:
            adjacents_colors.append(chromo[adjacent])
            if (chromo[noeud]==chromo[adjacent]):
                valid_colors=list(set(colors) - set(adjacents_colors))
                if(len(valid_colors)!=0):
                    newcolor=random.choice(valid_colors)
                    chromo[noeud]=newcolor
                else:
                    newcolor = random.choice(colors)
                    chromo[noeud] = newcolor
    return chromo

def selection1(population):
    tmpparent1, tmpparent2 =(random.choice(population),random.choice(population))
    if (fitness(tmpparent1)>fitness(tmpparent2)):
        parent1=tmpparent1
    else:
        parent1=tmpparent2
    tmpparent1, tmpparent2 = (random.choice(population), random.choice(population))
    if (fitness(tmpparent1) > fitness(tmpparent2)):
        parent2 = tmpparent1
    else:
        parent2 = tmpparent2
    return parent1,parent2

def selection2(population):
    best1=[0]*lenchromo
    best2=[0]*lenchromo
    for chromo in population:
        if(fitness(chromo)>fitness(best1)):
            best1=chromo
        if (fitness(chromo)>fitness(best2) and fitness(best2)<fitness(best1)):
            best2=chromo
    return best1,best2

def crossover(chromo1,chromo2):
    pos = random.randint(0,lenchromo)
    child=chromo1[:pos]+chromo2[pos:]
    return child


def run():
    population=random_population()
    parent1,parent2=selection1(population)
    child=crossover(parent1,parent2)
    child=mutate1(child)
    population.append(child)
    return child

