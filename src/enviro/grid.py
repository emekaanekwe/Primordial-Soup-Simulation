"""create an evolving grid that agents can evolve on
    kwargs: (need to import)
    agents
    
    Returns:
        tuple: a grid
    """

import numpy as np

def initialize_grid(max_food, max_obstacle, grid_size):
    return {
        "food": [tuple(np.random.ranint(0, grid_size, 2)) for _ in range(max_food)],
        "obstacle": [tuple(np.random.ranint(0, grid_size, 2)) for _ in range(max_obstacle)],
    }

def grid_fitness(grid, agents):
    fitness = 0
    for agent in agents:
        fitness += 10*len(grid["food"]) - len(grid["obstacle"])
    return fitness

def evolve_grid(grid, agents, grid_size, max_food, max_obstacles, mutation_rate):
    for _ in range(max_food):
        if random.random() < mutation_rate:
            grid["food"].append(tuple(np.random.randint))