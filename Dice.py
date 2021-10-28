import random    
import plotly.express as px  
dice_results = []
count = []
for array in range(0, 100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_results.append(dice1 + dice2)
    #print(dice1,",",dice2)
    print(dice_results)
    count.append(array)
fig = px.bar(x = dice_results, y = count)
import plotly.figure_factory as ff
fig = ff.create_distplot([dice_results], ["result"], show_hist = False)
fig.show()