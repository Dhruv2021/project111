import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("project.csv")
data=df["reading_time"].tolist()
mean=statistics.mean(data)
sd=statistics.stdev(data)

def randommean(numbers):
    dataset=[]
    for i in range (0,numbers):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

meanlist=[]
for i in range(0,1000):
    means=randommean(100)
    meanlist.append(means)

sd= statistics.stdev(meanlist)
mean1 = statistics.mean(meanlist)
print("mean of sampling distribution:- ",mean)
print("Standard deviation of sampling distribution:- ", sd)

z_score1=(mean1-mean)/sd
print("Z Score of mean =",z_score1)
