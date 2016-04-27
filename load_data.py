# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 09:52:49 2016

@author: Pravinth Samuel Vethanayagam
"""
import os
import pandas as pd
import re

data1 = None

def fillWithAverage(age, meanAge = None):
    if meanAge is None:
        meanAge = age.mean()
    
    newAges = age.map(lambda a: a if ~pd.isnull(a) else meanAge )
    return meanAge, newAges
    
def extractInfoFromName(name):
    info = [re.search(',\ ([\w\ ]*)\.', n, re.M|re.I).group(1) for n in name]
    return info

def load_titanic_dataset(folderpath=None):
    if folderpath is None:
        folderpath = os.getcwd()+'/data/'
        
    train_df = pd.read_csv(folderpath + 'train.csv')
    test_df = pd.read_csv(folderpath + 'test.csv')

    # Change Sex to 1 and 0
    train_df.Sex = train_df.Sex.map( {'female': 0, 'male': 1} ).astype(int)
    test_df.Sex = test_df.Sex.map( {'female': 0, 'male': 1} ).astype(int)
    
    # Change embarked to numeric
    train_df.Embarked = train_df.Embarked.map({s[1]:s[0] for s in enumerate(train_df.Embarked.unique())}).astype(int)
    test_df.Embarked = test_df.Embarked.map({s[1]:s[0] for s in enumerate(test_df.Embarked.unique())}).astype(int)
    
    # Fill unavailable age values
    meanAge, train_df.Age = fillWithAverage(train_df.Age)
    _, test_df.Age = fillWithAverage(test_df.Age, meanAge)
    
    # Fill any rows with null fares
    meanFare, train_df.Fare = fillWithAverage(train_df.Fare)
    _, test_df.Fare = fillWithAverage(test_df.Fare, meanFare)
    
    # Extract honorary from name
    allHonorary = set(extractInfoFromName(train_df.Name)).union(set(extractInfoFromName(test_df.Name)))
    honoraryMapping = {s[1]:s[0] for s in enumerate(allHonorary)}
    train_df['Honorary'] = [honoraryMapping[s] for s in extractInfoFromName(train_df.Name)]
    test_df['Honorary'] = [honoraryMapping[s] for s in extractInfoFromName(test_df.Name)]
    
    return (train_df, test_df)
    
if __name__=="__main__":
    train_df, test_df = load_titanic_dataset()
    