# Creating the images/frames is seperated from creating the gif.
# To be modified to become more generally applicable...

# Imports
import pynbody
import matplotlib.pyplot as plt
import numpy as np
import imageio.v3 as iio

# Simulation data
simulation = pynbody.load('run708main.01000')
pynbody.analysis.angmom.faceon(simulation)

# Function to seperate stars by age.
def star_ages (sim):
    
    stars = sim.stars
    current_time = sim.properties['time'].in_units('Gyr')
    star_ages = current_time - stars['tform'].in_units('Gyr')
    y_stars = stars[star_ages < 1]
    i_stars = stars[(star_ages > 1) & (star_ages < 5)]
    o_stars = stars[star_ages > 5]
    
    return y_stars, i_stars, o_stars

# Function to save images based on certain properties (e.g., star age)...set to test a limited scope...to be adjusted to take in a arbitrary amount of frames
def save_images(sim):
    
    young_stars, intermediate_stars, old_stars = star_ages (sim)
    
    pynbody.plot.stars.render(young_stars, width='10 kpc')
    plt.savefig('frame_1.png', dpi=150)
    plt.close()
    
    pynbody.plot.stars.render(intermediate_stars, width='10 kpc')
    plt.savefig('frame_2.png', dpi=150)
    plt.close()

    pynbody.plot.stars.render(old_stars, width='10 kpc')
    plt.savefig('frame_3.png', dpi=150)
    plt.close()

# Creating the GIF  
def create_gif(duration_ms=500):  # Able to set the duration in milliseconds (ie, this is 500ms per frame)
    frames = np.stack([iio.imread(f"frame_{i}.png") for i in range(1, 4)], axis=0)
    iio.imwrite('test.gif', frames, duration=duration_ms)
    
# Generating the images/frames
save_images(simulation)

# Creating the GIF from them
create_gif()
