import numpy as np
import pandas as pd
df = pd.read_csv('D:/coding/data/seoul_park.csv')
import seaborn as sns
import matplotlib.pyplot as plt

df_2016 = df[df["연"] == 2016]
ax = sns.boxplot(data=df_2016, x="월", y="어른")
ax.set_title("2016년 성인 입장객 수")
plt.show()
