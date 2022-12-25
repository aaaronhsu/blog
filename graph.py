import matplotlib.pyplot as plt
import numpy as np

with plt.xkcd():
    # Create data
    x = np.linspace(0, 8.3)
    y = (((x-4)/3)**3 + 2.37) * 10
    # Plot data
    plt.plot(x, y)
    # Add labels
    plt.xlabel('Time Invested')
    plt.ylabel('Desirablity')
    plt.xticks([])
    plt.yticks([])
    plt.title('Investment in Time vs. Desirability')

    plt.show()