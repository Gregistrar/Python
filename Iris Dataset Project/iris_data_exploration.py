# https://archive.ics.uci.edu/ml/datasets/Iris
# https://www.slideshare.net/thoi_gian/iris-data-analysis-with-r
# https://www.marsja.se/pandas-python-descriptive-statistics/
import pandas as pd
import numpy as np
from scipy.stats import trim_mean, kurtosis
from scipy.stats.mstats import mode, gmean, hmean

iris = pd.read_csv('C:\\Users\\ghodg\\Desktop\\Projects\\Python\\Iris Dataset Project\\iris.data.txt',
                   names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
iris.info()
iris.head()

# Pandas will output summary statistics by using this method
iris.describe()

grouped_data = iris.groupby(['class'])
grouped_data['sepal_length', 'sepal_width', 'petal_length', 'petal_width'].describe()

# Pandas Mean, both are doing the same thing
grouped_data['sepal_length', 'sepal_width', 'petal_length', 'petal_width'].mean().reset_index()
grouped_data['sepal_length', 'sepal_width', 'petal_length', 'petal_width'].aggregate(np.mean).reset_index()


# Geometric & Harmonic mean

