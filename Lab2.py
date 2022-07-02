# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 18:36:45 2021

@author: FREE
"""

import pandas as pd

df = pd.read_table('score.txt', sep=' ', header=None, names=['ID', 'midterm', 'final'])


df['total'] = 0.4*df['midterm']+ 0.6*df['final']



grades = []
for row in df['total']:
    if row >= 90:
        grades.append('(A)')
    elif row >=80:
        grades.append('(B)')
    elif row >=70:
        grades.append('(C)')
    elif row >=60:
        grades.append('(D)')
    else :
        grades.append('(F)')
        
df['grade'] = grades


df['total'] = df['total'].astype(str)

df['last']  = df['total'] + df['grade']


df=df.drop(columns=['total', 'grade'], axis=1)


df.to_csv('report.txt', header=None, index=False, sep = ' ')



