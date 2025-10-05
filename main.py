# Data analysis and Manipulation
import plotly.graph_objs as go
import plotly.io as pio
import plotly.express as px
import pandas as pd

# Data Visualization
import matplotlib.pyplot as plt

# Importing Plotly
import plotly.offline as py
#py.init_notebook_mode(connected=True)

# Initializing Plotly
pio.renderers.default = 'browser'

# Importing Dataset1
dataset1 = pd.read_csv("covid.csv")
dataset1.head()  # returns first 5 rows
# Returns tuple of shape (Rows, columns)
#print(dataset1.shape)

# Returns size of dataframe
#print(dataset1.size)

dataset1.info()

dataset2=pd.read_csv("covid_grouped.csv")
dataset2.head()

# Returns tuple of shape (Rows, columns)
#print(dataset2.shape)

# Returns size of dataframe
#print(dataset2.size)

# Information about Dataset2
dataset2.info()  # return concise summary of dataframe

# Columns labels of a Dataset1
dataset1.columns

dataset1.drop(['NewCases','NewDeaths','NewRecovered'],axis=1,inplace=True)
dataset1.sample(5)



#TO PLOT ALL THE DATA ON A TABLE FROM CSV 
from plotly.figure_factory import create_table

colorscale = [[0, '#4d004c'], [.5, '#f2e5ff'], [1, '#ffffff']]
table = create_table(dataset1.head(15), colorscale=colorscale)
#py.plot(table)


#BAR GRAPH
bar=px.bar(dataset1.head(15),x='Country/Region',y='TotalCases',color='TotalTests',orientation='v')
#bar.show()

#SCATTER PLOT
scat=px.scatter(dataset1, x='Country/Region',y='TotalCases', 
           
           color='TotalCases', size='TotalCases', size_max=80)
#scat.show()


#BUBBLE CHART 
scat2=px.scatter(dataset1.head(100),x='TotalCases',y='TotalDeaths',size='TotalDeaths',size_max=80,color='TotalDeaths',log_x=True)
#scat2.show()

#ADVANCED BAR CHART 

adv_bar=px.bar(dataset2,x='Date',y='Confirmed',color='Confirmed')
#adv_bar.show()

#SPECIFIC DATA VISUALIZATION

specific_data_vis=dataset2.loc[dataset2["Country/Region"]=="India"]
specific_data_vis_bar=px.bar(specific_data_vis,x="Date",y="Confirmed",color="Confirmed")
#specific_data_vis_bar.show()

#LINE PLOT

#line plot doesnt have any color in it 
specific_data_vis_line=px.line(specific_data_vis,x="Date",y="Deaths")
#specific_data_vis_line.show()











