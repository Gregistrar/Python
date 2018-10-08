import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib.ticker import FormatStrFormatter
plt.style.use('ggplot')
# After setting ggplot, these are the params we have started using as defaults
plt.rcParams['font.sans-serif'] = 'Helvetica'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['grid.color'] = 'grey'
plt.rcParams['grid.linewidth'] = 1
plt.rcParams['grid.alpha'] = 0.2
plt.rcParams["axes.edgecolor"] = "black"
from adjustText import adjust_text

google_data = pd.read_csv("\\Users\ghodg\Desktop\Projects\Python\Graphs\Google Play Store\googleplaystore.csv",
                   encoding='utf-8')
google_data.head()
google_data.info()

def clean_columns(df):
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = [x.lower() for x in df.columns]
    print("Cleaning raw data......")
    return df

clean_data = clean_columns(google_data)
clean_data.info()

# Take just the ratings column for a histogram plot
ratings = clean_data[['rating']]
ratings = ratings.dropna()
ratings.rating.value_counts()
google_ratings = ratings[ratings['rating'] <= 5.0]
x = ratings[ratings['rating'] > 5]

def ratings_hist(df):
    # Histogram plot of Google Play Store Ratings
    plt.clf()
    plt.hist(df, 24, facecolor='green', edgecolor='gray')
    plt.ylabel('# of User Ratings')
    plt.xlabel('Google Play Store Rating')
    title = plt.title('Google Play Store Ratings (Histogram)', fontsize=16, fontweight='bold')
    title.set_position([.5, 1.02])
    plt.axis([0, 38, 0, 2250])
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)

    plt.xticks((0, 4.78, 9.5, 14.25, 19, 23.75, 28.5, 33.25, 38),
               ("1", "1.5", "2", "2.5", "3", "3.5", "4", "4.5", "5"))

    plt.savefig("\\Users\ghodg\Desktop\Projects\Python\Graphs\Google Play Store\Graph_outputs\\ratings_histogram.png")


ratings_hist(google_ratings)


google_category = clean_data[['category']]
google_category.category.value_counts()
google_category['freq'] = google_category.groupby('category')['category'].transform('count')
df_category = google_category.drop_duplicates()
df_category = df_category.sort_values(['freq'], ascending=False)
df_category['category'] = df_category.category.str.replace('_', ' ')
df_category['category'] = df_category.category.str.title()
df_category.head()
df_category

# Bar chart of Google Play Store Categories
plt.clf()
list = df_category['category']
y_pos = np.arange(len(list))

plt.bar(y_pos, df_category['freq'])
plt.xticks(y_pos, list, rotation=65)









