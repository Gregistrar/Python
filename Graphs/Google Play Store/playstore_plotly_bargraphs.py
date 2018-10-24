# https://plot.ly/python/bar-charts/
import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='Gregistrar', api_key='4siWzJbBAA3lJ1NDaDlv')

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

free_categories = (clean_data[clean_data['type'] == 'Free']
                   .groupby('category')['app']
                   .count().reset_index()
                   .rename(columns={'app': 'free_count'})
                   )
free_categories['category'] = (free_categories.category.str.title()
                               .str.replace('_', ' ')
                               )
paid_categories = (clean_data[clean_data['type'] == 'Paid']
                   .groupby('category')['app']
                   .count().reset_index()
                   .rename(columns={'app': 'paid_count'})
                   )
paid_categories['category'] = (paid_categories.category.str.title()
                               .str.replace('_', ' ')
                               )

data = [go.Bar(x=free_categories['category'],
               y=free_categories['free_count'])
]

py.plot(data, filename='basic-bar')






