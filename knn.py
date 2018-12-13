import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
iris = datasets.load_iris()

def main():
    '''main function'''

    #load data
    iris = datasets.load_iris()

    X = iris.data[:, :2]  # we only take the first two features.
    y = iris.target

    #split
    X_train,X_test, y_train,y_test=train_test_split(X,y, test_size = 1/3, random_state =2018)
    #declare model
    knn_model = KNeighborsClassifier()

    #train model

    knn_model.fit(X_train,y_train)

    #evaluation

    accuracy = knn_model.score(X_test,y_test)
    print('accuarcy:{:.2f}%'.format(accuracy*100))
    idx = 20
    test_sample_feat = [X_test[idx,:]]
    y_true = y_test[0]
    y_pred = knn_model.predict(test_sample_feat)
    print('true label{}, predict label{}'.format(y_true,y_pred))

if __name__ == '__main__':
    main()