import random    
import plotly.express as px  
import plotly.figure_factory as ff
import csv
import pandas as pd
df = pd.read_csv("StudentsPerformance.csv")
fig = ff.create_distplot([df["Height(Inches)"].tolist()],["height"],show_hist = False)
fig.show()