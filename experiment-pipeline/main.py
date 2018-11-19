import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

df = pd.read_csv('indians-diabetes.csv', names=names)

def stratified_split(y, proportion=0.8):
    y = np.array(y)

    train_inds = np.zeros(len(y), dtype=bool)
    test_inds = np.zeros(len(y), dtype=bool)

    values = np.unique(y)
    for value in values:
        value_inds = np.nonzero(y == value)[0]
        np.random.shuffle(value_inds)

        n = int(proportion * len(value_inds))

        train_inds[value_inds[:n]] = True
        test_inds[value_inds[n:]] = True

    return train_inds, test_inds

train, test = stratified_split(df['class'])

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

def accuracy(y_test, y_pred):
    return 1 - sum(abs(y_test - y_pred)/len(y_test))


def CV(df, classifier, nfold, norm=True):
    acc = []
    for i in range(nfold):
        y = df['class']
        train, test = stratified_split(y)

        if norm:
            X_train = norm_df(df.iloc[train, 0:8])
            X_test = norm_df(df.iloc[test, 0:8])
        else:
            X_train = df.iloc[train, 0:8]
            X_test = df.iloc[test, 0:8]

        y_train = y[train]
        y_test = y[test]

        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)

        acc.append(accuracy(y_test, y_pred)) # Homework - replace accuracy with BCR

    return acc
'''
X_train = norm_df(df.iloc[train, 0:8])
X_test = norm_df(df.iloc[test, 0:8])

y_train = df['class'][train]
y_test = df['class'][test]

logreg = LogisticRegression()

logreg.fit(X_train,y_train)

y_pred=logreg.predict(X_test)

print(accuracy(y_test, y_pred))
'''

'''
X_train = df.iloc[train, 0:8]
X_test = df.iloc[test, 0:8]

y_train = df['class'][train]
y_test = df['class'][test]

rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
print(accuracy(y_test, y_pred))
'''

'''
X_train = norm_df(df.iloc[train, 0:8])
X_test = norm_df(df.iloc[test, 0:8])

y_train = df['class'][train]
y_test = df['class'][test]

rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
print(accuracy(y_test, y_pred))
'''

logreg = LogisticRegression()
rf = RandomForestClassifier()

log_res = CV(df, logreg, 10)
rf_res = CV(df, rf, 10)

print(np.array(log_res).mean())
print(np.array(rf_res).mean())


log_res = CV(df, logreg, 10, norm=False)
rf_res = CV(df, rf, 10, norm=False)

print(np.array(log_res).mean())
print(np.array(rf_res).mean())

