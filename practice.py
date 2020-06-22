# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 08:28:02 2020

@author: prani
"""
import pandas as pd
import numpy as np


'''given_list = [6,7,8,9,2,3,4,5]
pseries = pd.Series(given_list)

pseries_sq = pseries.apply(lambda x: x**2)

print(pseries_sq)
##

df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
print(df.describe())
print(df.columns)
print(df.shape)
print(df.head())

##

input_num = int(input())
s_squared = pd.Series([x**2 for x in range(1,(input_num+1))], index = range(1, input_num+1))
print(s_squared)

##

df2 = df.sort_values(['month', 'day'], ascending = True)
print(df2.head(20))
print(df[2::2].head(20))
print(df[['month', 'day','temp', 'area']].head(20))

df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
print(df[(df['area'] > 0 )& (df['wind'] > 1) & (df['temp'] > 15)])

##
df_1 = pd.read_csv('https://query.data.world/s/vv3snq28bp0TJq2ggCdxGOghEQKPZo')
df_2 = pd.read_csv('https://query.data.world/s/9wVKjNT0yiRc3YbVJaiI8a6HGl2d74')
new_df = pd.merge(df_1, df_2, how= 'inner', on = 'unique_id' )
app_df = df_1.append(df_2)
print(app_df.head(20))

##
gold = pd.DataFrame({'Country': ['USA', 'France', 'Russia'],
                         'Medals': [15, 13, 9]}
                    )
silver = pd.DataFrame({'Country': ['USA', 'Germany', 'Russia'],
                        'Medals': [29, 20, 16]}
                    )
bronze = pd.DataFrame({'Country': ['France', 'USA', 'UK'],
                        'Medals': [40, 28, 27]}
                    )

print(pd.concat([gold, silver]))

gold.set_index('Country', inplace = True)
silver.set_index('Country', inplace = True)
bronze.set_index('Country', inplace = True)


master_df = (gold.add(silver, fill_value = 0)).add(bronze, fill_value = 0)
print(master_df.sort_values('Medals', ascending = 0))

##
df_by_mon = df.groupby(['month', 'day'])
print(df_by_mon['rain', 'wind'].mean())


df_1 = df[['rain','wind','month','day']].groupby(['month','day']).mean()
print(df_1.head(20))

##
df['XY'] = df['X']*df['Y']
'''

df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')

by_mon_day = df.pivot_table(values = ['wind', 'rain'], index = ['month', 'day'], aggfunc = np.mean)


print(by_mon_day)








