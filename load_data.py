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

def extractInfoFromCabin(cabin):
    info = [re.search('\A(\w)', c, re.M|re.I).group(1) if c==c else None for c in cabin]
    return info


    
def convertToNumerical(incol1, incol2, extractFunc = lambda x:x):
    allVals = set(extractFunc(incol1)).union(set(extractFunc(incol2)))
    valMapping = {s[1]:s[0] for s in enumerate(allVals)}
    return ([valMapping[s] for s in extractFunc(incol1)], [valMapping[s] for s in extractFunc(incol2)])
    
    
    

def load_titanic_dataset(folderpath=None):
    if folderpath is None:
        folderpath = os.getcwd()+'/data/'
        
    train_df = pd.read_csv(folderpath + 'train.csv')
    test_df = pd.read_csv(folderpath + 'test.csv')

    # Change Sex to 1 and 0
    train_df.Sex = train_df.Sex.map( {'female': 0, 'male': 1} ).astype(int)
    test_df.Sex = test_df.Sex.map( {'female': 0, 'male': 1} ).astype(int)
    
    # Change embarked to numeric
    train_df['Embarked2'], test_df['Embarked2'] = convertToNumerical(train_df.Embarked, test_df.Embarked)
    
    # Fill unavailable age values
    meanAge, train_df.Age = fillWithAverage(train_df.Age)
    _, test_df.Age = fillWithAverage(test_df.Age, meanAge)
    
    # Fill any rows with null fares
    meanFare, train_df.Fare = fillWithAverage(train_df.Fare)
    _, test_df.Fare = fillWithAverage(test_df.Fare, meanFare)
    
    # Extract honorary from name
    train_df['Honorary'], test_df['Honorary'] = convertToNumerical(train_df.Name, test_df.Name, extractInfoFromName)
    
    #Extract cabin info
    train_df['Cabin2'], test_df['Cabin2'] = convertToNumerical(train_df.Cabin, test_df.Cabin, extractInfoFromCabin)
    
    return (train_df, test_df)
    
if __name__=="__main__":
    train_df, test_df = load_titanic_dataset()
    