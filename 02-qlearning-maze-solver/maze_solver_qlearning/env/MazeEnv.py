import numpy as np
from enum import IntEnum
# class syntax
class MazeActions(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

# TODO estafoso
MAZE_ACTIONS_MAPPER = np.array([[-1,0],[0,1],[1,0],[0,-1]])

class MazeEnv:

    agent_position :np.ndarray = None
    start_position = None
    end_position = None
    maze = None
    path = None
    reward_matrix = None    
    reward = 0
    out_of_bounds_reward = -1000
    actions = np.array([
        MazeActions.UP,
        MazeActions.RIGHT,
        MazeActions.DOWN,
        MazeActions.LEFT
    ])
    wall_symbol = None
    def __init__(self, maze : np.ndarray, reward_matrix : np.ndarray, start_position : np.ndarray, end_position : np.ndarray, wall_symnbol = 1):
        self.maze = maze.copy()
        self.reward_matrix = reward_matrix.copy()
        self.start_position = start_position.copy()
        self.end_position = end_position.copy()
        self.agent_position = start_position.copy()
        self.path = [self.start_position.copy()]
        self.wall_symbol = wall_symnbol 

    def get_dimensions(self):
        return self.maze.shape

    def isDone(self):
        return (np.array_equal(self.end_position, self.agent_position))
    
    def __is_visited(self, position):
        # print(f"isvisited with {position}")
        for step in self.path:
            if (np.array_equal(step, position)):
                # print(True)
                return True
        # print(False)
        return False
    
    def __is_out_of_bounds(self, position):
        # print(f"isoutofbounds with {position}")
        # print(not ((-1 < position[0] <  maze.shape[0]) and (-1 < position[1] <  maze.shape[1])))
        return not ((-1 < position[0] <  self.maze.shape[0]) and (-1 < position[1] <  self.maze.shape[1]))

    def __is_a_wall(self,position):
        # TODO : cambiar por una tupla
        # TODO : Quitar el 1 hardcoded
        return (self.maze[position[0],position[1]] == self.wall_symbol)

    def get_valid_actions(self, position):
        valid_actions = []
        for act in self.actions:
            new_position = position + MAZE_ACTIONS_MAPPER[act]
            if not (self.__is_visited(new_position) or self.__is_out_of_bounds(new_position) or self.__is_a_wall(new_position)):
                valid_actions.append(act)
        # print(f"valid actions for {position} {np.array(valid_actions)}")
        return np.array(valid_actions)
    
    def show_env_state(self):
        print(f"agent_position {self.agent_position}")
        print(f"start_position {self.start_position}")
        print(f"end_position {self.end_position}")
        print(f"path {self.path}")

    def step(self, action : MazeActions):
        
        self.agent_position += MAZE_ACTIONS_MAPPER[action]

        if self.__is_visited(self.agent_position):
            self.show_env_state()
            raise Exception(f'step to {self.agent_position} not valid, path {self.path}')
        
        if self.__is_out_of_bounds(self.agent_position):
            self.show_env_state()
            raise Exception(f'step to {self.agent_position} out of bounds, action {action} prev position {self.agent_position - MAZE_ACTIONS_MAPPER[action]} valid_actions {self.get_valid_actions(self.agent_position - MAZE_ACTIONS_MAPPER[action])}')

        if self.__is_a_wall(self.agent_position):
            self.show_env_state()
            raise Exception(f'step to {self.agent_position} not valid, that position is a wall {self.maze[self.agent_position[0], self.agent_position[1]]}')


        # TODO Creo que si las coords los pongo como una tupla, podria hacer la indexacion mas facil            
        self.reward += self.reward_matrix[self.agent_position[0], self.agent_position[1]]
        self.path.append(self.agent_position.copy())
        return self.agent_position, self.reward, self.isDone()
    
    def reset(self):
        self.agent_position = self.start_position.copy()
        self.reward = 0
        self.path = [self.start_position.copy()]
        return self.agent_position.copy()