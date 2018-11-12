import pandas as pd;

def norm_arr(arr):
    mean = arr.mean()
    std = arr.std()

    normalized = (arr - mean) / std

    return normalized

def norm_df(df):
    result = df.copy()

    for feature in df.columns:
        result[feature] = norm_arr(result[feature])

    return result

df = pd.read_csv('../titanic.csv')

df1 = df[df['Age'].notnull()]

print(norm_arr(df1['Age']))
