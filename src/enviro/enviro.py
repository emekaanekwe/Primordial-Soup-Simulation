import numpy as np
from config import settings

class Enviro:
    def __init__(self, settings):
        self.grid_size = settings.grid_size
        # instantiate 2d grid
        self.grid = np.zeroes(self.grid_size)
        self.agents = []
    
    def reset(self):
        self.grid = (0)
        self.agents.clear()
    
    def update(self):
        pass
    
    def mutate(self):
        print("enviro is vehicle of selection")