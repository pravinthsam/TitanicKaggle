# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:44:33 2016

@author: Pravinth Samuel Vethanayagam
"""
import load_data
import numpy as np
from sklearn.ensemble import RandomForestClassifier


class random_forest_model:
    
    forest = None
    
    def __init__(self, num_trees = 20):
        print 'Initializing model...'
        self.forest = RandomForestClassifier(n_estimators = num_trees)
        
    def fit(self, tr_df):
        print 'Fitting the model...'
        y = tr_df.Survived
        X = tr_df.drop('Survived', 1)
        self.forest = self.forest.fit(X, y)
        
    def predict(self, te_df):
        rf_model_df = te_df[["PassengerId", "Sex"]]
        rf_model_df.columns=['PassengerId', 'Survived']
        
        if 'Survived' in te_df.columns:
            te_df = te_df.drop('Survived', 1)
            
        rf_model_df['Survived'] = self.forest.predict(te_df)
        
        return rf_model_df
    
if __name__ == '__main__':
    train_df, test_df = load_data.load_titanic_dataset()
    train_df.drop('Name', 1, inplace=True)
    train_df.drop('Ticket', 1, inplace=True)
    train_df.drop('Cabin', 1, inplace=True)
    
    test_df.drop('Name', 1, inplace=True)
    test_df.drop('Ticket', 1, inplace=True)
    test_df.drop('Cabin', 1, inplace=True)
    
    rf_model = random_forest_model()
    rf_model.fit(train_df)
    
    train_results = rf_model.predict(train_df)
    test_results = rf_model.predict(test_df)
    
    '''
    # check training data error
    train_error = np.sum(rf_model.predict(train_df).Survived == train_df.Survived)
    print 'Training error is {0:.2f}%'.format(float(train_error*100)/len(train_df))
    
    rf_model.predict(test_df).to_csv('results/random_forest_results.csv')
    '''