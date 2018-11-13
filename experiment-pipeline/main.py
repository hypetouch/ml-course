import pandas as pd
import matplotlib.pyplot as plt
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

df = pd.read_csv('indians-diabetes.csv', names=names)

df.groupby('class').plas.hist(alpha=0.4)

plt.show()
