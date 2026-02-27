import pandas as pd
import os

def load_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "data", "titanic.csv")
    return pd.read_csv(data_path)