import numpy as np
from mazelib import Maze
from mazelib.generate import BacktrackingGenerator

def gen_backtracking_mazelib_maze(dimensions: tuple) -> np.ndarray:
    m = Maze()
    m.generator = BacktrackingGenerator(dimensions[0],dimensions[1])
    m.generate()
    m.generate_entrances()
    m_start = m.start
    m_end = m.end
    m.grid[m_start[0], m_start[1]] = 2
    m.grid[m_end[0], m_end[1]] = 3
    return m.grid, np.array(m_start), np.array(m_end)