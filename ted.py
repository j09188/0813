import pandas as pd
df=pd.read_csv("ted_main.csv", encoding="utf-8")

#Dataframe表格 Series單行或單列
#行操作: [ ["標1","標2", ...] ], 翻轉: T
#df[["comments","description"]]
df.T.to_csv("ted_transpose.csv", encoding="utf-8")