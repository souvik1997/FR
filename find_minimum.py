from __future__ import print_function
import random
from deap import base
from deap import creator
from deap import tools
import subprocess

import sys
import math
import numpy as np
#from rbf import Rbf
from scipy.interpolate import Rbf

def train(individual_generator, rbfi):
    def evalFitness(ind):
        actual_individual = ind[0]
        value = rbfi(*actual_individual)
        print("{0} => {1}".format(actual_individual, value))
        return (value,)

    MAX_X = 100
    CXPB = 0.8
    NGEN = 20

    toolbox = base.Toolbox()
    creator.create("FitnessMax", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)
    toolbox.register("xvalue", individual_generator)
    toolbox.register("individual", tools.initRepeat,
                     creator.Individual, toolbox.xvalue, 1)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", evalFitness)
    toolbox.register("mate", tools.cxBlend, alpha=0.01)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=5, indpb=0)
    toolbox.register("select", tools.selTournament, tournsize=3)

    pop = toolbox.population(15)
    for g in xrange(NGEN):
        print("Generation {0}".format(g))
        offspring = toolbox.select(pop, len(pop))
        offspring = list(map(toolbox.clone, offspring))
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1[0], child2[0])
                del child1.fitness.values
                del child2.fitness.values
        for mutant in offspring:
            if random.random() < NGEN:
                toolbox.mutate(mutant[0])
                del mutant.fitness.values
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = list(map(toolbox.evaluate, invalid_ind))
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        pop[:] = offspring
        fits = [ind.fitness.values[0] for ind in pop]
        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x * x for x in fits)
        std = abs(sum2 / length - mean**2)**0.5
        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)
