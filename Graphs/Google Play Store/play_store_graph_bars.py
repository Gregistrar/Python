import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import MaxNLocator
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
    df = df[pd.notnull(df['type'])]
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


# df for the Google Play Store categories
google_category = clean_data[['category']]
google_category.category.value_counts()
google_category['freq'] = google_category.groupby('category')['category'].transform('count')
df_category = google_category.drop_duplicates()
df_category = df_category.sort_values(['freq'], ascending=False)
df_category['category'] = df_category.category.str.replace('_', ' ')
df_category['category'] = df_category.category.str.title()
df_category.head()
df_category

def google_category(df_category):
    # Bar chart of Google Play Store Categories
    fig, ax1 = plt.subplots(figsize=(9, 7))
    fig.subplots_adjust(left=0.21, right=0.95)
    fig.canvas.set_window_title('Google Play Store Category (Bar)')

    list = df_category['category']
    y_pos = np.arange(len(list))

    rects = ax1.barh(y_pos, df_category['freq'],
                     align='center',
                     height=0.5, color='darkturquoise')
    plt.yticks(y_pos, list)
    ax1.set_xlim([0, 2000])
    title = ax1.set_title('Google Play Store Category (Bar)', fontsize=16, fontweight='bold')
    title.set_position([.5, 1.02])
    ax1.xaxis.set_major_locator(MaxNLocator(12))
    ax1.xaxis.grid(True, linestyle='--', which='major',
                       color='grey', alpha=.25)

    # Plot a solid vertical gridline to highlight the median position
    ax1.axvline(1000, color='grey', alpha=0.75)

    labels = df_category['freq']
    for i, v in enumerate(labels):
        ax1.text(v+4, i-.25, str(v), color='black', size=8)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)

    plt.savefig("\\Users\ghodg\Desktop\Projects\Python\Graphs\Google Play Store\Graph_outputs\\category_bar.png")


google_category(df_category)

def type_stacked(clean_data):
    # df for the Google Play Store content ratings vs. paid/free
    google_content = clean_data[['type', 'content_rating']]
    google_content.type.value_counts()
    google_content = google_content[~(google_content['content_rating'].isin(['Unrated', 'Adults only 18+']))]
    google_content.info()

    free_content = google_content[google_content['type'] == 'Free']['content_rating'].value_counts()
    paid_content = google_content[google_content['type'] == 'Paid']['content_rating'].value_counts()
    df = pd.DataFrame([free_content, paid_content])
    df.index = ['Free', 'Paid']
    df.plot(kind='bar', stacked=True, figsize=(9, 7))
    plt.savefig("\\Users\ghodg\Desktop\Projects\Python\Graphs\Google Play Store\Graph_outputs\\type_stacked_bar.png")


def content_stacked(clean_data):
    google_content = clean_data[['type', 'content_rating']]
    everyone_content = google_content[google_content['content_rating'] == 'Everyone']['type'].value_counts()
    teen_content = google_content[google_content['content_rating'] == 'Teen']['type'].value_counts()
    mature_content = google_content[google_content['content_rating'] == 'Mature 17+']['type'].value_counts()
    tenplus_content = google_content[google_content['content_rating'] == 'Everyone 10+']['type'].value_counts()

    df_content = pd.DataFrame([everyone_content, teen_content, mature_content, tenplus_content])
    df_content.index = ['Everyone', 'Teen', 'Mature 17+', 'Everyone 10+']
    df_content.plot(kind='bar', stacked=True, figsize=(9, 7), rot=45)
    plt.ylabel('# of Apps')
    plt.xlabel('Content Rating Type')
    title = plt.title('Google Play Store Content Ratings (Stacked Bar)', fontsize=16, fontweight='bold')
    title.set_position([.5, 1.02])
    plt.subplots_adjust(left=0.11, right=0.95, bottom=0.16)
    plt.savefig("\\Users\ghodg\Desktop\Projects\Python\Graphs\Google Play Store\Graph_outputs\\content_stacked_bar.png")

type_stacked(clean_data)
content_stacked(clean_data)

# Attempt at some line density plots of category and rating
import seaborn as sns
sns.set(style="ticks")

categories = ['Family', 'Game', 'Tools', 'Medical', 'Business']
google_top_category = clean_data[['category', 'rating']]
google_top_category = google_top_category.dropna()
google_top_category['category'] = google_top_category.category.str.replace('_', ' ')
google_top_category['category'] = google_top_category.category.str.title()

for genre in categories:
    subset = google_top_category[google_top_category['category'] == genre]
    sns.distplot(subset['rating'], hist=False, kde=True,
                 kde_kws={'linewidth': 1.5},
                 label=genre)

# Plot formatting
plt.legend(prop={'size': 10}, title='Categories')
plt.title('Density Plot of Top 5 Categories', fontsize=14,
          fontweight='bold')
plt.xlabel('Google Play Store Ratings')
plt.ylabel('Density')
plt.savefig("\\Users\ghodg\Desktop\Projects\Python\Graphs\Google Play Store\Graph_outputs\\genre_top5_distplot.png")


# Other density plots, top 5 categories visualized differently
categories = ['Family', 'Game', 'Tools', 'Medical', 'Business']
google_den_category = clean_data[['category', 'rating']]
google_den_category = google_den_category.dropna()
google_den_category['category'] = google_den_category.category.str.replace('_', ' ')
google_den_category['category'] = google_den_category.category.str.title()
density_df = google_den_category.loc[google_den_category['category'].isin(categories)]

g = sns.FacetGrid(density_df, row="category",
                  height=1.7, aspect=4,)
g.map(sns.distplot, "rating", hist=False, rug=True)

