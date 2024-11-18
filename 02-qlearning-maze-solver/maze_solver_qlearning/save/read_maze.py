import numpy as np
from maze_solver_qlearning.save.io_matrix_csv import read_matrix_csv
from maze_solver_qlearning.generator.make_reward_from_maze import make_reward_from_maze

def read_maze(path, start_symbol = 2, end_symbol = 3):
    maze = read_matrix_csv(path)
    m_start = np.where(maze == start_symbol)
    m_start = np.array([m_start[0][0], m_start[1][0]])
    m_end = np.where(maze == end_symbol)
    m_end = np.array([m_end[0][0], m_end[1][0]])
    reward = make_reward_from_maze(maze,m_start,m_end)
    return (maze, m_start, m_end, reward)
