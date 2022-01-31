import scipy
import csv
import pandas as pd
import plotly.figure_factory as ff



DataFrame = pd.read_csv("bellCurve.csv")
figure = ff.create_distplot([DataFrame["Avg Rating"].tolist()], ["Mobile Brand"])
figure.show()