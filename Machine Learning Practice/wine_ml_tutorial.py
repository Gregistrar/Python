"""
Wine Predicting with Scikit-Learn
=================================
1. Set up your environment.
2. Import libraries and modules.
3. Load red wine data.
4. Split data into training and test sets.
5. Declare data preprocessing steps.
6. Declare hyperparameters to tune.
7. Tune model using cross-validation pipeline.
8. Refit on the entire training set.
9. Evaluate model pipeline on test data.
10. Save model for further use.

https://elitedatascience.com/python-machine-learning-tutorial-scikit-learn
"""

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
# For cross validation
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
# Evaluate performance
from sklearn.metrics import mean_squared_error, r2_score
# Persist the model for future use
from sklearn.externals import joblib

dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(dataset_url, sep=';')
data.head()

data.describe()
# All of the features are numeric, but have very different scales. We should standardize the data

# Create train and test sets, the stratify makes sure your training set looks similar to the test set
y = data.quality
X = data.drop('quality', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123, stratify=y)

# Standardization, most algorithms assume all features are centered around zero w. the same variance
X_train_scaled = preprocessing.scale(X_train)
# We wont use this method, because it won't work on the test set
scaler = preprocessing.StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

pipeline = make_pipeline(preprocessing.StandardScaler(), RandomForestRegressor(n_estimators=100))

# Tuning hyperparameters
pipeline.get_params()
hyperparameters = {'randomforestregressor__max_features': ['auto', 'sqrt', 'log2'],
                   'randomforestregressor__max_depth': [None, 5, 3, 1]}

# Tune using a cross-validation pipeline
clf = GridSearchCV(pipeline, hyperparameters, cv=10)
clf.fit(X_train, y_train)
clf.best_params_
clf.refit

# Evaluate the model pipeline on test data
y_pred = clf.predict(X_test)
r2_score(y_test, y_pred)
mean_squared_error(y_test, y_pred)

# Save the model for future use
joblib.dump(clf, 'wine_regressor.pkl')
clf2 = joblib.load('wine_regressor.pkl')
clf2.predict(X_test)








