"""Simple example showing organisms moving in 3D space."""

import numpy as np
from src.enviro.visualizer import Visualizer


# Create 5 organisms at random starting positions
num_organisms = 6
positions = np.random.uniform(0, 10)

# Create visualizer
viz = Visualizer(bounds=10)

# Generate frames of movement
frames = []
for step in range(100):
    # Move organisms randomly (small random walk)
    positions += np.random.uniform(-0.2, 0.2, size=(num_organisms, 3))

    # Keep organisms in bounds
    positions = np.clip(positions, 0, 10)

    # Store this frame
    frames.append(positions.copy())

# Create animation
viz.animate(frames, fps=30)
print("===Animation saved as animation.mp4===")
