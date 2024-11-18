import numpy as np


def __rotate_actions(row_actions):
    return np.roll(row_actions, -1)

# TODO : Esta implementacion puede ser mejor
def __rotate_90(q_table, n_dimension):
    q_table_rotated = q_table.copy()
    for i in range(n_dimension):
        for j in range(n_dimension):
            
            index_in_qtable = i  * n_dimension + j
            
            index_of_new_value = (j + 1) * n_dimension - (i + 1)
            q_table_rotated[index_in_qtable , : ] = __rotate_actions(q_table[index_of_new_value, :].copy())

    return q_table_rotated

def rotate_q_table(q_table : np.ndarray, n_dimension, rotations = 1):
    q_table_rotated = q_table.copy()
    for _ in range(rotations):
        q_table_rotated = __rotate_90(q_table_rotated, n_dimension)
    return q_table_rotated
