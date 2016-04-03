from __future__ import print_function
import random
from deap import base
from deap import creator
from deap import tools
import subprocess

def evalFitness(ind):
    with open("cutinfo.txt", "w") as tf:
        tf.write("0, 0, {0}, 50.0, 43.5, 1.0, 0.0, 0.0".format(ind[0]))
    p = subprocess.Popen(["./slicing", "Colonel.obj", "cutinfo.txt"], stdout=subprocess.PIPE)
    output, _ = p.communicate()
    print("{0}: {1}".format(ind[0], float(output)))
    return (float(output),)

MAX_X = 400
CXPB = 0.8
NGEN = 20

toolbox = base.Toolbox()
creator.create("FitnessMax", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)
toolbox.register("xvalue", lambda: MAX_X*random.random())
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.xvalue, 1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evalFitness)
toolbox.register("mate", tools.cxBlend, alpha=0.01)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=5, indpb=1)
toolbox.register("select", tools.selTournament, tournsize=3)

pop = toolbox.population(15)
for g in xrange(NGEN):
    print("Generation {0}".format(g))
    offspring = toolbox.select(pop, len(pop))
    offspring = list(map(toolbox.clone, offspring))
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < CXPB:
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values
    for mutant in offspring:
        if random.random() < NGEN:
            toolbox.mutate(mutant)
            del mutant.fitness.values
    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    fitnesses = list(map(toolbox.evaluate, invalid_ind))
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit
    pop[:] = offspring
    fits = [ind.fitness.values[0] for ind in pop]
    length = len(pop)
    mean = sum(fits) / length
    sum2 = sum(x*x for x in fits)
    std = abs(sum2 / length - mean**2)**0.5
    print("  Min %s" % min(fits))
    print("  Max %s" % max(fits))
    print("  Avg %s" % mean)
    print("  Std %s" % std)
