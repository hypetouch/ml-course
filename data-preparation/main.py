import pandas as pd;
# import pdb;

def norm_arr(arr):
    if arr.dtype.kind != 'f':
      return arr
    mean = arr.mean()
    std = arr.std()

    normalized = (arr - mean) / std

    return normalized

def norm_df(df):
    result = df.copy()

    for feature in df.columns:
        result[feature] = norm_arr(result[feature])

    return result

dat = pd.read_csv('../titanic.csv')

df1 = dat[dat['Age'].notnull()]

print(norm_df(df1))
