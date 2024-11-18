import numpy as np
from typing import Callable

def build_make_maze(gen_maze: Callable[[tuple], np.ndarray]):
    def make_maze(dimensions = (5,5)):
        m, m_start, m_end = gen_maze((dimensions[0], dimensions[1]))
        return m, m_start, m_end
    return make_maze