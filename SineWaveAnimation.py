import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # Expand the x range to include negative values
line, = ax.plot(x, np.sin(x))

# Set axis limits to keep origin at (0, 0)
ax.set_ylim(-1.5, 1.5)
ax.set_xlim(-2 * np.pi, 2 * np.pi)  # Ensure the origin is at (0, 0)

# Add grid and labels
ax.axhline(0, color='black',linewidth=1)  # Horizontal line through y=0
ax.axvline(0, color='black',linewidth=1)  # Vertical line through x=0
ax.grid(True)

# Animation function
def animate(i):
    line.set_ydata(np.sin(x + i / 10.0))  # Update the sine wave
    return line,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Display animation
plt.show()
