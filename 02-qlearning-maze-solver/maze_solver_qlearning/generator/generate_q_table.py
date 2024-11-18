import numpy as np
import random 
from maze_solver_qlearning.env.MazeEnv import MazeEnv, MazeActions
from .build_initial_q_table import build_initial_q_table

def choose_action(q_table, state, actions, must_be_random_action=False) -> MazeActions: 
    # print(f"actions received {actions}")
    if ( must_be_random_action ):
        return np.random.choice(actions,1)[0]
    choice = actions[0]
    # TODO Se puede hacer mejorar con numpy?
    for act in actions[1:]:
        if (q_table[state,choice] < q_table[state,act]):
            choice = act
    # print(f"no random choice, chose {choice}")
    return choice

def build_initial_q_table(n_states ,n_actions, is_empty=False):
    if (is_empty):
        return np.zeros((n_states, n_actions))
    return np.random.random(size=(n_states, n_actions))

# TODO Use Ravel_index from numpy
def calculate_position_to_state(n_cols,  position : np.ndarray): 
    return (position[0]) * (n_cols)  + position[1]

def generate_q_table(
        mazeEnv : MazeEnv,
        episodes = 10000, 
        alpha = 0.9, gamma = 0.95,
        epsilon = 1.0, epsilon_decay = 0.999995, min_epsilon = 0.01,
        # Max steps no deberia ser fijo
        max_steps = 100,
        verbose = True
    ):

    cols = mazeEnv.get_dimensions()[1]

    q_table = build_initial_q_table(mazeEnv.maze.shape[0] * mazeEnv.maze.shape[1], mazeEnv.actions.shape[0], True)
    best_reward = {
        'path' : [],
        'reward' : -10000
    }    
    count_is_done = 0
    for episode in range(episodes):
        actual_position = mazeEnv.reset()
        isDone = False
        # print(f"In Episode {episode}")
        for step in range(max_steps):
            state = calculate_position_to_state(cols, mazeEnv.agent_position)
        
            valid_actions = mazeEnv.get_valid_actions(mazeEnv.agent_position)

            if (valid_actions.shape[0] == 0):
                break;
            
            action = choose_action(
                q_table, 
                state,
                valid_actions,
                (random.uniform(0,1) < epsilon)
            )

            next_position, reward, isDone = mazeEnv.step(action)

            next_state = calculate_position_to_state(cols, next_position)

            old_q_value = q_table[state,action]
            next_max_q_value = np.max(q_table[next_state, :])
            # Es lo mismo que decir>
            #  q_table[state,action] = old_q_value + alpha + (reward + gamma * next_max_q_value - old_q_value)
            q_table[state,action] = (1 - alpha) * old_q_value + alpha + (reward + gamma * next_max_q_value)
            # state = next_state Esto no creo que sea neceesario
            if ( isDone ):
                count_is_done += 1
                break
        if ( verbose ):
            print()
            print(f"Episode {episode} finisehd with {reward}, isDone {isDone}, epsilon {epsilon}")
        if (best_reward['reward'] < reward ) and (verbose):
            print(f"New Best Reward {reward}")
            best_reward['path'] = mazeEnv.path.copy()
            best_reward['reward'] = reward
        epsilon = max(min_epsilon, epsilon * epsilon_decay)
    if ( verbose ):
        print(f"Qtable generated! number of episodes with maze solved {count_is_done}")
    return (q_table, count_is_done)
