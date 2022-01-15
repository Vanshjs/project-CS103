import pandas as pd
import plotly.exprees as px

df=pd.read_csv("data2.csv")
fig=px.scatter(df,x="date",y="cases",color="country")
fig.show()