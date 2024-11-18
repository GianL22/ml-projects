import numpy as np
import matplotlib.pyplot as plt


def plot_maze(maze : np.ndarray):
    
    plt.figure()
    plt.imshow(maze, cmap=plt.cm.gist_gray)
    plt.colorbar()
    plt.grid(False)
    plt.xticks(range(maze.shape[1]))
    plt.yticks(range(maze.shape[0]))
    plt.show()