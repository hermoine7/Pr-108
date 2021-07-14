  
import plotly.figure_factory as ff
import pandas as pd

df=pd.read_csv("data.csv")

graph=ff.create_distplot([df["Avg Rating"].tolist()], ["Average Rating"], show_hist=False)
graph.show()