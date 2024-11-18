import numpy as np

def rotate_reward(reward: np.ndarray, n_rotations = 1):
    reward_rotated = reward.copy()
    for _ in range(n_rotations):
        reward_rotated = np.rot90(reward_rotated)
    return reward_rotated