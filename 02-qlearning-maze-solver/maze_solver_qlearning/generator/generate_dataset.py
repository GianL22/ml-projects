
from .build_make_maze import build_make_maze 
from .plugin.gen_backtracking_mazelib_maze import gen_backtracking_mazelib_maze
from .make_reward_from_maze import make_reward_from_maze
from maze_solver_qlearning.env.MazeEnv import MazeEnv
from maze_solver_qlearning.save.io_matrix_csv import save_matrix_to_csv
import numpy as np
import pathlib
from typing import Callable


def generate_dataset(generate_q_table: Callable[[MazeEnv, int, int, int, int, int, int, int, bool], np.ndarray], n_samples = 10, dimensions = (5,5), verbose = True, path_csv='', start_n_sample = 100):
    envs = []
    q_tables = []
    if ( path_csv != ''):
        pathlib.Path(path_csv + '/q_tables' + f'/{dimensions[0]}x{dimensions[1]}/').mkdir(parents=True, exist_ok=True)
        pathlib.Path(path_csv + '/mazes' + f'/{dimensions[0]}x{dimensions[1]}/').mkdir(parents=True, exist_ok=True)

    while(n_samples > 0):

        make_maze = build_make_maze(gen_backtracking_mazelib_maze)

        maze, start_position, end_position = make_maze(dimensions)
        reward = make_reward_from_maze(maze, start_position, end_position)

        env = MazeEnv(maze, reward, start_position, end_position)

        if ( verbose ):
            print(f"{n_samples} samples remain")
            print(f"generating q_table...")

        q_table, count_is_done = generate_q_table(
            env,
            episodes=6000,
            epsilon=1,
            epsilon_decay=0.9995,
            min_epsilon=0.01,
            alpha= 0.9,
            gamma= 1.8,
            verbose=False
        )
        q_tables.append(q_table.copy())
        envs.append(env)

        if ( verbose ):
            print(f"Sample generated with {count_is_done} dones!")

        if ( path_csv != ''):
            if ( verbose ):
                print(f"Saving {dimensions[0]}x{dimensions[1]}/{n_samples}.csv...")
    
            save_matrix_to_csv(q_table, path_csv + f'/q_tables/{dimensions[0]}x{dimensions[1]}/{start_n_sample + n_samples}.csv')
            save_matrix_to_csv(maze, path_csv + f'/mazes/{dimensions[0]}x{dimensions[1]}/{start_n_sample + n_samples}.csv')
    
            if ( verbose ):
                print(f"{dimensions[0]}x{dimensions[1]}/{n_samples}.csv saved!")
        n_samples -= 1

    return envs, q_tables