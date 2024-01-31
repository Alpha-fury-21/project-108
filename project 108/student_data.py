import pandas as Pd
import plotly.figure_factory as ff
import csv

df=pd.read_csv("student_data.csv")
fig=ff.create_distplot([df["Marks In Percentage(Pounds)"].tolist()],["Days Present"])
fig.show()