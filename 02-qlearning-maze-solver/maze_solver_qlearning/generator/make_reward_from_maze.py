import numpy as np

def make_reward_from_maze(m : np.ndarray, m_start : np.ndarray, m_end : np.ndarray, no_round_walls_reward_mapper = lambda x : [-100,-1000,-10,100000][x]):

    def reward_mapper(maze : np.ndarray, start_position):

        reward = np.zeros(maze.shape, dtype=np.int64)
        # reward = np.copy(maze)
        factor = 2

        for i in range(maze.shape[0]):
            for j in range(maze.shape[1]):

                if ( maze[i,j] == 3 ) or ( maze[i,j] == 1 ):
                    reward[i,j] = no_round_walls_reward_mapper(maze[i,j])
                    continue
                cof =  no_round_walls_reward_mapper(maze[i,j])  / ( (1 / 20) * np.linalg.norm(np.array([i,j]) - start_position) + 0.1) 


                if ( maze[i,j] == 2 ):
                    reward[i,j] =  no_round_walls_reward_mapper(1)
                    continue
                
                coun_neighbors = 0
                if (maze[i - 1, j] == 1):
                    coun_neighbors +=1
                if (maze[i, j + 1] == 1):
                    coun_neighbors +=1
                if (maze[i + 1, j] == 1):
                    coun_neighbors +=1
                if (maze[i, j -1] == 1):
                    coun_neighbors +=1
                # Evaluamos si es una callejon sin salida
                if (coun_neighbors >= 3):
                    reward[i,j] = no_round_walls_reward_mapper(1) 
                    continue
                
                reward[i,j] = cof
        return reward

    reward = reward_mapper(m.copy(), m_start)
    return reward