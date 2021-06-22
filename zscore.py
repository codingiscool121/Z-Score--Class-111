import pandas as pd
import statistics as st
import plotly_express as pe
import plotly.figure_factory as pf
import random as rand
import plotly.graph_objects as pg
data1= pd.read_csv("original.csv")
read= data1["Math_score"].tolist()
graph= pf.create_distplot([read],["Math Scores Month 1"], show_hist=False)
graph.show()
mean = st.mean(read)
sd = st.stdev(read)
print("The mean of the original data is", mean)
print("The standard deviation of the original data is", sd)
meanlist=[]

def sampling():
    list=[]
    for i in range(0, 25):
        r=rand.randint(0,len(read)-1)
        list.append(read[r])
    return(st.mean(list))

def samplingdistrubution():
    for i in range(0,500):
        meanlist.append(sampling())
        
samplingdistrubution()

newmean = st.mean(meanlist)
newsd = st.stdev(meanlist)
print("The new mean(after sampling) is", newmean)
print("The new standard deviation(after sampling) is", newsd)
newgraph = pf.create_distplot([meanlist], ["Math Scores Month 1(Better)"], show_hist=False)

firstsdstart, firstsdend = newmean - newsd, newmean+newsd
secondsdstart, secondsdend = newmean-2*newsd, newmean+2*newsd
thirdsdstart, thirdsdend= newmean-3*newsd, newmean+3*newsd
#after first intervention
data2 = pd.read_csv("intervention1.csv")
read1= data1["Math_score"].tolist()
meaninter1 = st.mean(read1)
#after second intervention
data3 = pd.read_csv("intervention2.csv")
read2= data3["Math_score"].tolist()
meaninter2 = st.mean(read2)
#after third intervention
data4 = pd.read_csv("intervention3.csv")
read3 = data4["Math_score"].tolist()
meaninter3 = st.mean(read3)

newgraph.add_trace(pg.Scatter(x=[firstsdstart, firstsdstart], y=[0,0.5], mode="lines", name="First Region Start"))
newgraph.add_trace(pg.Scatter(x=[firstsdend, firstsdend], y=[0, 0.5], mode="lines", name="First Region End"))
newgraph.add_trace(pg.Scatter(x=[secondsdstart, secondsdstart], y=[0, 0.5], mode="lines", name="Second Region Start"))
newgraph.add_trace(pg.Scatter(x=[secondsdend, secondsdend], y=[0, 0.5], mode="lines", name="Second Region End"))
newgraph.add_trace(pg.Scatter(x=[thirdsdstart, thirdsdstart], y=[0, 0.5], mode="lines", name="Third Region Start"))
newgraph.add_trace(pg.Scatter(x=[thirdsdend, thirdsdend], y=[0, 0.5], mode="lines", name="Third Region End"))
newgraph.add_trace(pg.Scatter(x=[newmean, newmean], y=[0,0.5], mode="lines", name="Mean"))
newgraph.add_trace(pg.Scatter(x=[meaninter1, meaninter1], y=[0,0.5], mode="lines", name="Mean Inter 1"))
newgraph.add_trace(pg.Scatter(x=[meaninter2, meaninter2], y=[0,0.5], mode="lines", name="Mean Inter 2"))
newgraph.add_trace(pg.Scatter(x=[meaninter3, meaninter3], y=[0,0.5], mode="lines", name="Mean Inter 3"))
newgraph.show()

#zscore for samples 1,2,3
zs1=(newmean-meaninter1)/newsd
zs2=(newmean-meaninter2)/newsd
zs3=(newmean-meaninter3)/newsd

print("Z score for sample 1: ", zs1)
print("Z score for sample 2:", zs2)
print("Z score for sample 3", zs3)

