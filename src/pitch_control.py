import numpy as np

MAX_SPEED = 5.5      # m/s
REACTION_TIME = 0.7 # seconds
LAMBDA = 4.3        # decay steepness

def team_control_vectorised(player_xy, grid_points):
    dx = player_xy[:, 0][:, None] - grid_points[:, 0][None, :]
    dy = player_xy[:, 1][:, None] - grid_points[:, 1][None, :]

    distances = np.sqrt(dx**2 + dy**2)
    arrival_times = REACTION_TIME + distances / MAX_SPEED
    influence = np.exp(-LAMBDA * arrival_times)

    return influence.sum(axis=0)
