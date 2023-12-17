import numpy as np
import matplotlib.pyplot as plt

def plot_pixelated_watermelon_slice(pixel_size=0.05):
    # Create a grid of points using meshgrid
    x = np.linspace(-1, 1, 400)
    y = np.linspace(-1, 1, 400)
    X, Y = np.meshgrid(x, y)

    # Define the watermelon slice shape using a mathematical expression
    watermelon_slice = (X**2 + Y**2 - (X**2 * Y**2) - 0.5) * (X > 0)  # Add condition for the slice

    # Create a pixelated version by rounding to the nearest pixel_size
    watermelon_slice_pixelated = np.round(watermelon_slice / pixel_size) * pixel_size

    # Plot the pixelated watermelon slice
    plt.figure(figsize=(8, 8))
    plt.imshow(watermelon_slice_pixelated, cmap='RdYlGn', extent=[-1, 1, -1, 1])
    plt.title('Pixelated Watermelon Slice')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

# Call the function to plot the pixelated watermelon slice
plot_pixelated_watermelon_slice(pixel_size=0.05)
