"""
Linear Regression
- Relation between two continuous variables
- Fits the equation to the data: Y = aX + b
- Best fitting the straight line is called a regression line

Uses
- Mainly for binary classification
- Gives the probability that the variable belongs to a class
"""

import sklearn
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = datasets.load_iris()
dat = pd.DataFrame(data.data[:, 0:4])
dat.columns = ['a', 'b', 'c', 'd']
tar = pd.DataFrame(data.target)

mdln = linear_model.LinearRegression()
mdlnfit = mdln.fit(dat, tar)
predict = mdln.predict([[1, 1, 1, 1]])
print(predict)
print(mdln.coef_)









