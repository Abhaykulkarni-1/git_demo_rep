# COVID-19 Analysis and Visualization using Plotly Express

This project visualizes the global impact of COVID-19 using Python, Plotly Express, and Pandas.  
It explores patterns in confirmed cases, recoveries, deaths, and testing rates across countries through interactive data visualizations.

---

## Overview

The COVID-19 pandemic generated massive datasets that reveal how different regions responded and recovered.  
This project leverages data visualization to transform those raw numbers into insights — showing trends, hotspots, and testing efficiency using interactive charts.

---

## Features

- Interactive bar charts for total cases, deaths, and recoveries  
- Country-wise and continent-wise breakdowns  
- Custom color scales and hover interactions for better readability  
- Scatter plots to compare testing density versus total cases  
- Overview of the top affected regions  
- Easily extendable for additional metrics such as vaccination data

---

## Tech Stack

| Tool / Library | Purpose |
|-----------------|----------|
| Python 3.8+ | Core programming language |
| Pandas | Data loading and manipulation |
| Plotly Express | Interactive data visualization |
| Jupyter Notebook | Development and visualization environment |

---

## Dataset

The dataset includes:
- Country and continent information  
- Total confirmed cases, deaths, recoveries, and tests per million population  

You may use publicly available COVID-19 datasets such as:
- [COVID-19 Data Repository by Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19)
- [Our World in Data](https://ourworldindata.org/coronavirus-source-data)
- [Kaggle COVID-19 datasets](https://www.kaggle.com/datasets)

---

## Visualizations

Key visualizations in this project include:

- Top 15 countries by total cases  
- Scatter plot of tests per million versus total cases  
- Continent-wise comparisons  
- Bar charts for deaths and recoveries  
- Custom color scales for highlighting trends  

---

## Example Code Snippet

```python
import plotly.express as px
import pandas as pd

# Load dataset
dataset = pd.read_csv('covid_data.csv')

# Top 15 countries by total cases
fig = px.bar(dataset.head(15),
             x='Country/Region',
             y='TotalCases',
             color='TotalCases',
             title='Top 15 Countries by Total COVID-19 Cases')

fig.show()
