import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """reads the csv file into a DaaFrame"""
    if not os.path.exists(path):
        print(f"Path: {path} does not exist.")
        return
    if not os.access(path, os.R_OK):
        print(f"No permissions to read path: {path}.")
        return
    if os.path.isdir(path):
        print(f"Path: {path} is a directory.")
        return
    else:
        return pd.read_csv(path, index_col=0, header=0)
