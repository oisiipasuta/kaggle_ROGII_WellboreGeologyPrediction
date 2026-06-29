import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display

df = pd.read_csv(r"C:\Users\koyamaharuki\OneDrive\デスクトップ\vscode\kaggles\rogii\input\rogii-wellbore-geology-prediction\train\000d7d20__horizontal_well.csv")
df_typewell = pd.read_csv(r"C:\Users\koyamaharuki\OneDrive\デスクトップ\vscode\kaggles\rogii\input\rogii-wellbore-geology-prediction\train\000d7d20__typewell.csv")

display(df.head(-3))
display(df_typewell.head())

#探索的データ分析を行う

#sns.histplot(data=df, x='TVT', kde=True)
#plt.show()

#TVT１１７２０以下をカットして分布を確認
df_cut = df[df['TVT'] > 11720]
#sns.histplot(data=df_cut, x='TVT', kde=True)
#plt.show()

#GRの分布とTVTの関係を確認する
#sns.histplot(data=df_cut, x='GR', kde=True)
#plt.show()

#sns.scatterplot(data=df_cut, x='GR', y='TVT')
#plt.show()

#TVTinputの散布図とTVTの散布図を確認する
#sns.scatterplot(data=df_cut, x='TVT_input', y='TVT')
#plt.show()

#x, y, zとTVTの関係を見てみる。ただこれはこのファイルではこの関係なだけで、他のファイルでは違う可能性があるので注意する
sns.scatterplot(data=df, x='X', y='TVT')
plt.show()
sns.scatterplot(data=df, x='Y', y='TVT')
plt.show()
sns.scatterplot(data=df, x='Z', y='TVT')
plt.show()  
