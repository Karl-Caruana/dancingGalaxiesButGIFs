# Imports
import pynbody
import matplotlib.pyplot as plt
import numpy as np
import imageio.v3 as iio

# Simulation data
simulation = pynbody.load('run708main.01000')
pynbody.analysis.angmom.faceon(simulation)

# Function to create images based on certain properties (e.g.; star age) then create the 'gif'
def create_gif(sim, num_frames=20, fps=5):
    for i in range(num_frames):
        
        # Initializing list
        frames = []
        
        # Example: filter based on star age
        # Add in...
        
        # Can also add subpart to visualize different properties (e.g., color filters)
        # Tangential to simply being a diff property in of itself...
        
        pynbody.plot.stars.render(stars, width='20 kpc')

        # Storing the image
        filename = f'frame_{i}.png'
        plt.savefig(filename, dpi=150)
        plt.close()
        frames.append(iio.imread(filename))
        
    iio.imwrite('test.gif', frames)

# Creating the images and then the GIF from the images...
create_gif(simulation)
