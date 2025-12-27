import pandas as pd

def build_pressure_curve(df, q=10):
    df = df.copy()

    df["pressure_bin"] = pd.qcut(
        df["pressure_z"],
        q=q,
        duplicates="drop")

    curve_df = (
        df
        .groupby("pressure_bin")
        .agg(
            mean_pressure_z=("pressure_z", "mean"),
            disruption_rate=("disruption", "mean"),
            n_frames=("disruption", "size"))
        .reset_index())

    return df, curve_df
