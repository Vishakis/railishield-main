import plotly.express as px
import pandas as pd


def get_data():
    # Read data
    df = pd.read_csv('data/data.csv')

    df['show'] = True
    df['reason'] = 'None'
    df.set_index('ID', drop=False, inplace=True)

    return df
