import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

google_data = pd.read_csv("\\Users\ghodg\Desktop\Projects\Python\Graphs\Google Play Store\googleplaystore.csv",
                   encoding='utf-8')
google_data.head()
google_data.info()

def clean_columns(df):
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = [x.lower() for x in df.columns]
    df = df[pd.notnull(df['type'])]
    print("Cleaning raw data......")
    return df

clean_data = clean_columns(google_data)
clean_data.info()











