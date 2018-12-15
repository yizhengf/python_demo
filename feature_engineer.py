'''
task : house price prediction

'''
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler


data_file = './data_ai/house_data.csv'

numeric_feat_cols = ['sqft_living','sqft_lot', 'sqft_above',	'sqft_basement', 'lat', 'long']

category_feat_col =['waterfront']


def prcess_features(X_train, X_test):
    '''feature pre processing'''
    #1. one-hot encoding on categorical feature

    encoder = OneHotEncoder(sparse=False)
    encoded_tr_feat =encoder.fit_transform(X_train[category_feat_col])
    encoded_te_feat = encoder.transform(X_test[category_feat_col])

    #2. min max normalization
    scaler = MinMaxScaler()
    scaled_tr_feat = scaler.fit_transform(X_train[numeric_feat_cols])
    scaled_te_feat=scaler.transform(X_test[numeric_feat_cols])

    #combine data
    X_train_proc = np.hstack((encoded_tr_feat, scaled_tr_feat))
    X_test_proc=np.hstack((encoded_te_feat,scaled_te_feat))

    return X_train_proc,X_test_proc




def main():
    '''main function'''

    house_data = pd.read_csv(data_file,usecols=numeric_feat_cols+category_feat_col+['price'])
    X = house_data[numeric_feat_cols+category_feat_col]
    y = house_data['price']

    #split into train/test

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=1/3, random_state=10)

    #build linear model

    linear_reg_model = LinearRegression()
    linear_reg_model.fit(X_train,y_train)
    #evalution

    r2_score = linear_reg_model.score(X_test,y_test)
    print('R2  for linear regression model is {:.2f}% '.format(r2_score*100))

    #data preprocessing

    X_train_proc,X_test_proc = prcess_features(X_train,X_test)

    # build linear model

    linear_reg_model2 = LinearRegression()
    linear_reg_model2.fit(X_train_proc, y_train)
    # evalution

    r2_score2 = linear_reg_model2.score(X_test_proc, y_test)
    print('R2  for linear regression model after feature engineering is {:.2f}% '.format(r2_score2 * 100))

    print('model improvement{:.2f}'.format((r2_score2 - r2_score)/r2_score))
if __name__ == '__main__':
    main()
