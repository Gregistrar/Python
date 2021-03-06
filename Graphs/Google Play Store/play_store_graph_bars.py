import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
plt.style.use('ggplot')
# After setting ggplot, these are the params we have started using as defaults
plt.rcParams['font.sans-serif'] = 'Helvetica'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['grid.color'] = 'grey'
plt.rcParams['grid.linewidth'] = 1
plt.rcParams['grid.alpha'] = 0.2
plt.rcParams["axes.edgecolor"] = "black"
from adjustText import adjust_text  # Used for scatterplots

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

def ratings_hist(df):
    # Histogram plot of Google Play Store Ratings
    plt.clf()
    plt.hist(df, 24, facecolor='green', edgecolor='gray')
    plt.ylabel('# of User Ratings')
    plt.xlabel('Google Play Store Rating')
    title = plt.title('Google Play Store Ratings', fontsize=16, fontweight='bold')
    title.set_position([.5, 1.02])
    plt.axis([0, 38, 0, 2250])
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)

    plt.xticks((0, 4.78, 9.5, 14.25, 19, 23.75, 28.5, 33.25, 38),
               ("1", "1.5", "2", "2.5", "3", "3.5", "4", "4.5", "5"))

    plt.savefig("\\Users\ghodg\Desktop\Projects\Python\Graphs\Google Play Store\Graph_outputs\\ratings_histogram.png")


# df for the Google Play Store categories
google_category = clean_data[['category']]
google_category.category.value_counts()
google_category['freq'] = google_category.groupby('category')['category'].transform('count')
df_category = google_category.drop_duplicates()
df_category = df_category.sort_values(['freq'], ascending=False)
df_category['category'] = df_category.category.str.replace('_', ' ')
df_category['category'] = df_category.category.str.title()
df_category.head()

def google_category(df_category):
    # Bar chart of Google Play Store Categories
    fig, ax1 = plt.subplots(figsize=(9, 7))
    fig.subplots_adjust(left=0.21, right=0.95)
    fig.canvas.set_window_title('Google Play Store Category (Bar)')

    list = df_category['category']
    y_pos = np.arange(len(list))

    rects = ax1.barh(y_pos, df_category['freq'],
                     align='center',
                     height=0.5, color='turquoise')
    plt.yticks(y_pos, list)
    ax1.set_xlim([0, 2000])
    title = ax1.set_title('Google Play Store: # of Apps by Category', fontsize=16, fontweight='bold')
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
    plt.xlabel('# of User Ratings')

    plt.savefig("\\Users\ghodg\Desktop\Projects\Python\Graphs\Google Play Store\Graph_outputs\\category_bar.png")


# df for the Google Play Store average rating categories
rating_category = clean_data[['category', 'rating']]
rating_category.rating.value_counts()
rating_average = rating_category.groupby('category')['rating'].mean().reset_index()
df_average = rating_average.sort_values(['rating'], ascending=False)
df_average['category'] = df_average.category.str.replace('_', ' ')
df_average['category'] = df_average.category.str.title()
df_average.head()


def average_category(df_average):
    # Bar chart of Google Play Store Categories
    fig, ax1 = plt.subplots(figsize=(9, 7))
    fig.subplots_adjust(left=0.21, right=0.95)
    fig.canvas.set_window_title('Google Play Store Average Category Rating')

    list = df_average['category']
    y_pos = np.arange(len(list))
    rects = ax1.barh(y_pos, df_average['rating'],
                     align='center',
                     height=0.5,
                     color='tomato')
    plt.yticks(y_pos, list)
    ax1.set_xlim([0, 5])
    title = ax1.set_title('Google Play Store: Average User Rating by Category', fontsize=16, fontweight='bold')
    title.set_position([.5, 1.02])
    ax1.xaxis.set_major_locator(MaxNLocator(12))
    ax1.xaxis.grid(True, linestyle='--', which='major',
                       color='grey', alpha=.25)

    labels = df_average['rating']
    for i, v in enumerate(labels):
        ax1.text(v+0.05, i-.25, str(round(v, 2)), color='black', size=8, fontweight='bold')
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.xlabel('Average User Rating')

    plt.savefig("\\Users\ghodg\Desktop\Projects\Python\Graphs\Google Play Store\Graph_outputs\\average_category_bar.png")


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


ratings_hist(google_ratings)
google_category(df_category)
type_stacked(clean_data)
content_stacked(clean_data)
average_category(df_average)
