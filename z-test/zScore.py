import pandas as pd 
import statistics as st
import random as r
import csv 
import plotly.figure_factory as pf
import plotly.graph_objects as go
df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
mean = st.mean(data)
std = st.stdev(data)
#Code to find mean of 100 data points 1000 times
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = r.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean
    #Function to get the mean of 100 datasets
mean_list = []
for i in range(0,1000): 
    set_of_mean = random_set_of_mean(100)
    mean_list.append(set_of_mean)
#Calculating mean and standard deviation of sampling distribuition
std_deviation = st.stdev(mean_list)
meanofsampledistribuition = st.mean(mean_list)
print("Mean of Sampling Distribuition", meanofsampledistribuition)
print("Standard Deviation of Sampling Distribuition", std_deviation)
"""#Finding the Standard Deviation starting and ending values
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
#Finding mean of students who gave extra time in maths lab
df = pd.read_csv("School_1_Sample.csv")
data = df["Math_score"].tolist()
mean_of_Sample1 = st.mean(data)
print("Mean of Sample1", mean_of_Sample1)
fig = pf.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean_of_Sample1, mean_of_Sample1], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD MATH LABS"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

#Students who were enforced with registers
df = pd.read_csv("School_3_Sample.csv")
data = df["Math_score"].tolist()
mean_of_Sample3 = st.mean(data)
print("Mean of Sample3", mean_of_Sample3)
fig = pf.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean_of_Sample3, mean_of_Sample3], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD MATH LABS"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

#Students who used Maths Practice App
df = pd.read_csv("School_2_Sample.csv")
data = df["Math_score"].tolist()
mean_of_Sample2 = st.mean(data)
print("Mean of Sample2", mean_of_Sample2)
fig = pf.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean_of_Sample2, mean_of_Sample2], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD MATH LABS"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()
z_score1 = (mean - mean_of_Sample1)/std_deviation
z_score2 = (mean - mean_of_Sample2)/std_deviation
z_score3 = (mean - mean_of_Sample3)/std_deviation
print(z_score1)
print(z_score2)"""
z_score1 = (mean - meanofsampledistribuition)/std_deviation
print(z_score1)