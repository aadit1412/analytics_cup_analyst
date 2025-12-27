
def possession_loss_within_window(frame, team, change_events, window):
    future = change_events[
        (change_events["frame"] > frame) &
        (change_events["frame"] <= frame + window)]
    # loss only if possession moves away from the current team
    return int(any(future["team_ffill"] == team))
