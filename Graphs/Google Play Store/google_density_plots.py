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
import seaborn as sns
sns.set(style="ticks")

# Read in Google Play Store data
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


# line density plots of top 5 categories by # of apps
def single_line_density(clean_data):
    categories = ['Family', 'Game', 'Tools', 'Medical', 'Business']
    google_top_category = clean_data[['category', 'rating']]
    google_top_category = google_top_category.dropna()
    google_top_category['category'] = google_top_category.category.str.replace('_', ' ')
    google_top_category['category'] = google_top_category.category.str.title()

    for genre in categories:
        subset = google_top_category[google_top_category['category'] == genre]
        g = sns.distplot(subset['rating'],
                         hist=False,
                         kde=True,
                         kde_kws={'linewidth': 1.5},
                         label=genre)

    # Plot formatting
    plt.legend(prop={'size': 10}, title='Categories')
    g.set(xlim=(1, None))
    plt.title('Top 5 Categories by # of Apps', fontsize=14,
              fontweight='bold')
    plt.xlabel('Google Play Store Ratings')
    plt.ylabel('Density')
    plt.savefig("\\Users\ghodg\Desktop\Projects\Python\Graphs\Google Play Store\Graph_outputs\\genre_top5_distplot.png")


# line density plots of top 5 categories by average rating
def single_line_density_rating(clean_data):
    categories = ['Events', 'Education', 'Art And Design', 'Books And Reference', 'Personalization']
    google_rating_category = clean_data[['category', 'rating']]
    google_rating_category = google_rating_category.dropna()
    google_rating_category['category'] = google_rating_category.category.str.replace('_', ' ')
    google_rating_category['category'] = google_rating_category.category.str.title()

    for genre in categories:
        subset = google_rating_category[google_rating_category['category'] == genre]
        g = sns.distplot(subset['rating'],
                         hist=False,
                         kde=True,
                         kde_kws={'linewidth': 1.5},
                         label=genre)

    # Plot formatting
    plt.legend(prop={'size': 10}, title='Categories', loc='upper left')
    g.set(xlim=(1, None))
    plt.title('Top 5 Categories by Average Rating', fontsize=14,
              fontweight='bold')
    plt.xlabel('Google Play Store Ratings')
    plt.ylabel('Density')
    sns.set(rc={'figure.figsize': (11.7, 8.27)})
    plt.savefig("\\Users\ghodg\Desktop\Projects\Python\Graphs\Google Play Store\Graph_outputs\\genre_top5rating_distplot.png")


def multi_line_density(clean_data):
    categories = ['Family', 'Game', 'Tools', 'Medical', 'Business']
    google_den_category = clean_data[['category', 'rating']]
    google_den_category = google_den_category.dropna()
    google_den_category['category'] = google_den_category.category.str.replace('_', ' ')
    google_den_category['category'] = google_den_category.category.str.title()
    density_df = google_den_category.loc[google_den_category['category'].isin(categories)]

    d = {'color': ['blue', 'orange', 'green', 'red', 'purple']}
    g = sns.FacetGrid(density_df,
                      row="category",
                      height=1.4,
                      aspect=6,
                      hue_kws=d,
                      hue='category')
    g.map(sns.distplot, "rating",
          hist=True,
          rug=False)
    g.set(xlim=(1, None))
    axes = g.axes.flatten()
    axes[0].set_title('Business Apps')
    axes[1].set_title('Game Apps')
    axes[2].set_title('Family Apps')
    axes[3].set_title('Medical Apps')
    axes[4].set_title('Tools Apps')
    axes = g.axes.flatten()
    for ax in axes:
        ax.set_ylabel("Density")
    plt.subplots_adjust(top=0.9)
    g.fig.suptitle('Top 5 Categories by # of Apps',
                   fontweight='bold')
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    plt.xlabel('Google Play Store Ratings')

    plt.savefig("\\Users\ghodg\Desktop\Projects\Python\Graphs\Google Play Store\Graph_outputs\\genre_top5_density_plot.png")


def multi_line_density_rating(clean_data):
    categories = ['Events', 'Education', 'Art And Design', 'Books And Reference', 'Personalization']
    google_den_category = clean_data[['category', 'rating']]
    google_den_category = google_den_category.dropna()
    google_den_category['category'] = google_den_category.category.str.replace('_', ' ')
    google_den_category['category'] = google_den_category.category.str.title()
    density_df = google_den_category.loc[google_den_category['category'].isin(categories)]

    d = {'color': ['blue', 'orange', 'green', 'red', 'purple']}
    g = sns.FacetGrid(density_df,
                      row="category",
                      height=1.4,
                      aspect=6,
                      hue_kws=d,
                      hue='category')
    g.map(sns.distplot, "rating",
          hist=True,
          rug=False)
    g.set(xlim=(1, None))
    axes = g.axes.flatten()
    axes[0].set_title('Events Apps')
    axes[1].set_title('Education Apps')
    axes[2].set_title('Art And Design Apps')
    axes[3].set_title('Books And Reference Apps')
    axes[4].set_title('Personalization Apps')
    axes = g.axes.flatten()
    for ax in axes:
        ax.set_ylabel("Density")
    plt.subplots_adjust(top=0.9)
    g.fig.suptitle('Top 5 Categories by User Ratings', fontweight='bold')
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    plt.xlabel('Google Play Store Ratings')

    plt.savefig("\\Users\ghodg\Desktop\Projects\Python\Graphs\Google Play Store\Graph_outputs\\genre_top5rating_density_plot.png")


single_line_density(clean_data)
single_line_density_rating(clean_data)
multi_line_density(clean_data)
multi_line_density_rating(clean_data)
