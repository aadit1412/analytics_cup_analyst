import numpy as np

MAX_SPEED = 5.5
REACTION_TIME = 0.7
LAMBDA = 4.3

def pressure_from_players(players, ball_xy):
    player_xy = players[["x", "y"]].values
    distances = np.linalg.norm(player_xy - ball_xy, axis=1)
    arrival_times = REACTION_TIME + distances / MAX_SPEED
    return np.exp(-LAMBDA * arrival_times).sum()
