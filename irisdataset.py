# -*- coding: utf-8 -*-
"""IrisDataSet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IxpWOqrc9_igHBOpMh4PfK9tZB2K9U1L
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from google.colab import files
uploaded = files.upload()

import io
df = pd.read_csv(io.BytesIO(uploaded['Iris.csv']))
# Dataset is now stored in a Pandas Dataframe

df.head()



print(df.shape)

print(df['Species'].unique())

print(df.groupby('Species').size())

#Here we just visualize how the data has been distributed wrt diff SPECIES.
import seaborn as sns
sns.countplot(df['Species'],label="Count")
plt.show()

X = df.iloc[:,:-1].values
Y = df.iloc[: , 5].values

plt.scatter(df.Id , df.Species,marker = '*',color = 'red')

# importing train_test_split
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X, Y, random_state=0)



from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train , Y_train)
y_pred=logreg.predict(X_test)

print('Accuracy of Logistic regression classifier on training set: {:.2f}'
     .format(logreg.score(X_train, Y_train)))
print('Accuracy of Logistic regression classifier on test set: {:.2f}'
     .format(logreg.score(X_test, Y_test)))

#Here Applying Multinomial Logistic Regression
from sklearn.linear_model import LogisticRegression
mlr = LogisticRegression(multi_class='multinomial',solver ='newton-cg').fit(X_train,Y_train)
mlr.fit(X_train , Y_train)
y_pred=mlr.predict(X_test)

print('Accuracy of Multinomial Logistic regression classifier on training set: {:.2f}'
     .format(mlr.score(X_train, Y_train)))
print('Accuracy of Multinomial Logistic regression classifier on test set: {:.2f}'
     .format(mlr.score(X_test, Y_test)))

#HERE we are applying decision tree
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier().fit(X_train, Y_train)
print('Accuracy of Decision Tree classifier on training set: {:.2f}'
     .format(clf.score(X_train, Y_train)))
print('Accuracy of Decision Tree classifier on test set: {:.2f}'
     .format(clf.score(X_test, Y_test)))

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
print('Accuracy of K-NN classifier on training set: {:.2f}'
     .format(knn.score(X_train, Y_train)))
print('Accuracy of K-NN classifier on test set: {:.2f}'
     .format(knn.score(X_test, Y_test)))

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train, Y_train)
print('Accuracy of GNB classifier on training set: {:.2f}'
     .format(gnb.score(X_train, Y_train)))
print('Accuracy of GNB classifier on test set: {:.2f}'
     .format(gnb.score(X_test, Y_test)))



