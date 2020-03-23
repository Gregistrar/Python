import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

data = pd.read_csv('C:/Users/ghodg/desktop/machine_learning_sample_data.csv',
                   encoding='utf-8')
data.head()
datacsv = pd.read_csv('C:/Users/ghodg/desktop/machine_learning_sample_datacsv.csv',
                      encoding='utf-8')

# Randomly split the data set into a train and test set by a percent
tr, ts = train_test_split(data, test_size=0.2)
tr.info()
ts.info()

plt.plot(data, linewidth='3')
plt.plot(100*datacsv, 'b--')
plt.xlabel('Xvalue')
plt.ylabel('Yvalue')


datacos = np.cos(data)
data.head()
datacos.head()

pltpanda = pd.plotting.boxplot(data)
pltpandascat = pd.plotting.scatter_matrix(data)






