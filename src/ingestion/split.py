import pandas as pd


def temporal_split(df):

    df = df.sort_values("timestamp")

    train_end = int(len(df) * 0.8)

    val_end = int(len(df) * 0.9)

    train = df.iloc[:train_end]

    validation = df.iloc[train_end:val_end]

    test = df.iloc[val_end:]

    return train, validation, test