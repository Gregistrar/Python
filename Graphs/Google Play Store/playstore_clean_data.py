import pandas as pd
import numpy as np

google_data = pd.read_csv("\\Users\ghodg\Desktop\Projects\Python\Graphs\Google Play Store\googleplaystore.csv",
                   encoding='utf-8')


def clean_raw_data(df):
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = [x.lower() for x in df.columns]
    df = df[pd.notnull(df['type'])]
    print("Cleaning raw data......")
    return df

