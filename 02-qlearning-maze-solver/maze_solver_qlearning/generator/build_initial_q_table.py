import numpy as np


def build_initial_q_table(n_states ,n_actions, is_empty=False):
    if (is_empty):
        return np.zeros((n_states, n_actions))
    return np.random.random(size=(n_states, n_actions))