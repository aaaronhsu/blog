import matplotlib.pyplot as plt
import numpy as np

with plt.xkcd():
    # Create data
    x = np.linspace(0, 9)
    y = (((x-4)/3)**3 + 2.37) * 10
    # Plot data
    plt.plot(x, y)
    # Add labels
    plt.xlabel('Hundreds of Hours of Practice')
    plt.ylabel('Desirablity')
    plt.title('Investment in Time vs. Desirability')

    plt.show()