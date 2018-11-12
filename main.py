import pandas as pd
my_series = pd.Series([5, 6, 7, 8, 9, 10])

#print(my_series)

#print(my_series.index)
#print(my_series.values)



my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])

#print(my_series2['f'])

#print(my_series2[['a', 'b', 'f']])



#print(my_series2[my_series2 > 0])
#print(my_series2[my_series2 > 0] * 2)


#test = my_series2[['a', 'b', 'f']] = 0
#print(test)

my_series3 = pd.Series({'a': 5, 'b': 6, 'c': 7, 'd': 8})

my_series3.name = 'numbers'
my_series3.index.name = 'letters'

#print(my_series3)


df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]
}, index=['KZ', 'RU', 'BY', 'UA'])

#print(type(df['country']))
#print(df.loc[['KZ', 'RU'], 'population'])

# df.index
# df.columns


#print(df.loc['KZ':'UA', :])

# print(df.iloc[:, 1:]) # filter columns

#print(df[df.population > 10][['country', 'square']])

df['destiny'] = df['population'] / df['square'] * 1000000
#print(df)


#df = df.drop(['destiny'], axis='columns')


#df = df.rename(index={'Country Code': 'country_code'})

df = pd.read_csv('titanic.csv', sep=',')

#print(df.shape)

#print(df.columns)

#print(df.iloc[:4])

#print(df.groupby(['Sex', 'Survived'])['PassengerID'].count())

#print(df.groupby(['PClass', 'Survived'])['PassengerID'].count())

titanic_df = pd.read_csv('titanic.csv')

pvt = titanic_df.pivot_table(index=['Sex', 'Survived'], columns=['PClass'], values='Name', aggfunc='count')

print(pvt)


print(pvt.loc['female', ['1st', '2nd', '3rd']])








