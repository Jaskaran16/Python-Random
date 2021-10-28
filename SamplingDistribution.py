import pandas as pd 
import statistics as st
import random as r
import csv 
import plotly.figure_factory as pf
import plotly.graph_objects as go
df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = r.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean
def show_fig(mean_list):
    df = mean_list
    mean = st.mean(df)
    fig = pf.create_thisplot([df], ["reading_time"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean, mean], y = [0,1], mode = "lines", name = "mean"))
    fig.show()
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
    mean = st.mean(mean_list)
    print("mean_of_SamplingDistribution", mean)
setup()
population_mean = st.mean(data)
print(population_mean)
def standard_deviation():
    mean_list = []
    for i in range(0, 1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    std_deviation = st.stdev(mean_list)
    print(std_deviation)
standard_deviation()