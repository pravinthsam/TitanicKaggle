# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 09:52:49 2016

@author: Pravinth Samuel Vethanayagam
"""
import os
import pandas as pd

data1 = None

def load_titanic_dataset(folderpath=None):
    if folderpath is None:
        folderpath = os.getcwd()+'/data/'
        
    train_df = pd.read_csv(folderpath + 'train.csv')
    test_df = pd.read_csv(folderpath + 'test.csv')

    # Change Sex to 1 and 0
    train_df.Sex = (train_df.Sex=='male').astype(int)
    test_df.Sex = (test_df.Sex=='male').astype(int)
    
    return (train_df, test_df)
    
if __name__=="__main__":
    train_df, test_df = load_titanic_dataset()
    