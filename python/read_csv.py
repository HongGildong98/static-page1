#-*- coding: utf-8 -*-
import csv
import pandas as pd

def read_csv_by_pd(fname):

    df = pd.read_csv(fname,engine='python',names=['이름', '전화번호'], header=None,index_col='이름')
    return df

def read_csv_by_csvreader(fname):
    with open(fname, 'r') as csvfile:
        file = csv.reader(csvfile)
        for data in file:
            print(data)
    


#main code block
df = read_csv_by_pd("name_phone_sort_by_name.csv")
#f = read_csv_by_csvreader("name_phone_sort_by_name.csv")
print(df)

df.to_csv('name_phone_changed.csv',encoding='cp949', header=True)
