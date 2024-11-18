import numpy as np
import matplotlib.pyplot as plt

def plot_reward(reward : np.ndarray):
    start = np.unravel_index(np.argmax(reward), shape=reward.shape)
    end = np.unravel_index(np.argmin(reward), shape=reward.shape)
    reward_to_plot = reward.copy()
    reward_to_plot[start] = -5
    reward_to_plot[end] = -100
    plt.figure()
    plt.imshow(reward_to_plot, cmap=plt.cm.Reds)
    plt.colorbar()
    plt.grid(False)
    plt.xticks(range(reward_to_plot.shape[1]))
    plt.yticks(range(reward_to_plot.shape[0]))
    plt.show()
