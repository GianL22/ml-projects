import numpy as np
import matplotlib.pyplot as plt


def plot_maze_with_path(maze : np.ndarray, path : np.ndarray):

    def make_maze_with_path(intensity = 5):
        path_with_maze = np.copy(maze)
        
        for i, position in enumerate(path):
            path_with_maze[position[0],position[1]] = intensity
        return path_with_maze

    _,ax = plt.subplots()
    pa = ax.imshow(make_maze_with_path(),interpolation='nearest')
    plt.colorbar(pa,shrink=0.25)
    plt.xticks(range(maze.shape[1]))
    plt.yticks(range(maze.shape[0]))
    plt.show()
