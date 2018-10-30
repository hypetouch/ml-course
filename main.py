import pandas as pd;
import numpy as np;

s = pd.Series([1,3,5,np.nan,6,8]);

s1 = pd.Series({'kirill': 1})

df = pd.DataFrame({
    'country': ['Ukraine', 'USA'],
    'locations': [32121321, 321312321]
}, index=['UA', 'US'])

#print(s1);
#print(s);
#print(df);
print(df['country'])
print(df.loc['UA'])
