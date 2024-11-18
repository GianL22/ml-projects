import numpy as np

def rotate_maze(maze: np.ndarray, m_start : np.ndarray , m_end : np.ndarray, n_rotations = 1):
    maze_rotated = maze.copy()
    maze_rotated = np.rot90(maze_rotated, n_rotations)
    new_m_start = np.where(maze_rotated == maze[m_start[0], m_start[1]])
    new_m_start = np.array([new_m_start[0][0], new_m_start[1][0]])
    new_m_end = np.where(maze_rotated == maze[m_end[0], m_end[1]])
    new_m_end = np.array([new_m_end[0][0], new_m_end[1][0]])
    return (maze_rotated, new_m_start, new_m_end)