"""Simplest possible 3D visualization example."""

from src.enviro.visualizer import Visualizer

# Define positions for 3 organisms
positions = [
    [2, 3, 4],  # organism 1 at (2, 3, 4)
    [5, 6, 7],  # organism 2 at (5, 6, 7)
    [8, 1, 3],  # organism 3 at (8, 1, 3)
    ]

# Create and show
viz = Visualizer(bounds=10)
viz.update(positions)
viz.show()
