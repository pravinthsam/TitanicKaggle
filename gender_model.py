# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 09:51:39 2016

@author: Pravinth Samuel Vethanayagam
"""
import load_data
import numpy as np
import pandas as pd

def gender_model(tr_df, te_df):
    gender_model_df = te_df[["PassengerId", "Sex"]]
    gender_model_df.columns=['PassengerId', 'Survived']
    gender_model_df.Survived = 1 - gender_model_df.Survived
    
    return gender_model_df
    

if __name__ == '__main__':
    train_df, test_df = load_data.load_titanic_dataset()
    
    # Finding survival rate with gender
    num_male = np.sum(train_df.Sex==1)
    num_female = np.sum(train_df.Sex==0)
    num_survived = np.sum(train_df.Survived==1)
    male_survival_ratio = float(np.sum(train_df[train_df.Sex==1].Survived)) / num_male
    female_survival_ratio = float(np.sum(train_df[train_df.Sex==0].Survived)) / num_female
    total_survival_ratio = float(num_survived) / len(train_df)
    
    print 'Number of males onboard is {0} of which {1:.2f}% survived'.format(num_male, 100*male_survival_ratio)
    print 'Number of females onboard is {0} of which {1:.2f}% survived'.format(num_female, 100*female_survival_ratio)
    print 'Only {0:.2f}% out of {1} passengers survived'.format(total_survival_ratio*100, len(train_df))
    
    # gender based simple decision tree
    gender_model_df = gender_model(train_df, test_df)
    gender_model_df.to_csv('results/gender_model_results.csv', index=False)