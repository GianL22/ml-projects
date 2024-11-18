import numpy as np
from maze_solver_qlearning.env.MazeEnv import MazeActions, MazeEnv
from maze_solver_qlearning.generator.generate_q_table import calculate_position_to_state, choose_action


def solve_maze_from_q_table(mazeEnv : MazeEnv, q_table : np.ndarray, episodes = 1, max_steps = 100, verbose = True):
    cols = mazeEnv.get_dimensions()[1]
    actions = np.array([
        MazeActions.UP,
        MazeActions.RIGHT,
        MazeActions.DOWN,
        MazeActions.LEFT
    ])
    
    for episode in range(episodes):
        mazeEnv.reset()
        isDone = False
        if ( verbose ):
            print(f"In Episode {episode}")
        for step in range(max_steps):
            
            state = calculate_position_to_state(cols, mazeEnv.agent_position)
            valid_actions = mazeEnv.get_valid_actions(mazeEnv.agent_position)

            if (valid_actions.shape[0] == 0):
                break;
            action = choose_action(
                q_table, 
                state,
                valid_actions,
                False
            )
            next_state,  reward, isDone = mazeEnv.step(action)
            # state = next_state
            if (not isDone and verbose):
                print(f"{step} Finished not correcty!")
                break
        if ( verbose ):
            print(f"Episode {episode} finisehd with {reward} and isDone {isDone}")
    if ( verbose ):
        print("Finished!")
        
    return mazeEnv.path.copy()