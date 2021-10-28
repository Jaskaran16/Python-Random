import random    
import plotly.express as px  
import statistics as s
import plotly.figure_factory as ff
import plotly.graph_objects as go
dice_results = []
count = []
for array in range(0, 1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_results.append(dice1 + dice2)
mean = s.mean(dice_results)
mode = s.mode(dice_results)
median= s.median(dice_results)
print("mean:", mean)
print("mode:", mode)
print("median:", median)
std_deviation = s.stdev(dice_results)
print(std_deviation)
#Finding One Standard Deviation
first_std_deviation_start, first_standard_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_standard_end = mean - 2*std_deviation, mean + 2*std_deviation
third_std_deviation_start, third_standard_end = mean - 3*std_deviation, mean + 3*std_deviation
#Plotting the Chart
fig = ff.create_distplot([dice_results], ["result"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0, 0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [first_std_deviation_start, first_std_deviation_start], y = [0, 0.17], mode = "lines", name = "standardDeviation1"))
fig.add_trace(go.Scatter(x = [first_standard_end, first_standard_end], y = [0, 0.17], mode = "lines", name = "standardDeviation1"))
fig.add_trace(go.Scatter(x = [second_std_deviation_start, second_std_deviation_start], y = [0, 0.17], mode = "lines", name = "standardDeviation1"))
fig.add_trace(go.Scatter(x = [second_standard_end, second_standard_end], y = [0, 0.17], mode = "lines", name = "standardDeviation1"))
fig.show()
#Printing the Findings
list_of_data_within_1_std= [result for result in dice_results if result >first_std_deviation_start and result < first_standard_end ]
list_of_data_within_2_std= [result for result in dice_results if result >second_std_deviation_start and result < second_standard_end ]
list_of_data_within_3_std= [result for result in dice_results if result >third_std_deviation_start and result < third_standard_end ]
print("{}% of data lies within one standard deviation".format(len(list_of_data_within_1_std)*100.0/len(dice_results)))
print("{}% of data lies within second standard deviation".format(len(list_of_data_within_2_std)*100.0/len(dice_results))
)
print("{}% of data lies within third standard deviation".format(len(list_of_data_within_3_std)*100.0/len(dice_results)))