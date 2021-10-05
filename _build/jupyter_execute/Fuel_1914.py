#!/usr/bin/env python
# coding: utf-8

# # Using data from fossil-fuel CO2 emissions

# ## 1. Introduction

# In this Jupyter Notebook we follow the same procedure as before but with data on $CO_2$. The dataset used shows the per Country $CO_2$ Emissions from fossil-fuels annually since 1751 till 2014. Data comes from the Carbon Dioxide Information Analysis Center (CDIAC). 
# 
# In order to make a comparison I've taken data from 1914 and 2014. 
# 
# * Year 1914 shows a wanting of data: a total of 46 countries, which compared to 219 countries' data available in 2014, is rather short.

# ## 2. Code

# ### 2.1. Import libraries

# In[1]:


import pandas as pd
import geopandas
import folium


# ### 2.2. Read data from CSV file

# In[2]:


# Read csv file
df_co2 = pd.read_csv('Data/fossil-fuel.csv')


# ### 2.3. Construct the arrays of interest

# Here we'll take only the data available in 1914 and the last data available: 2014. 

# In[3]:


# Select the data that I want
df_1 = df_co2[df_co2['Year'] == 1914]
df_2 = df_co2[df_co2['Year'] == 2014]


# In[4]:


df_1_good = pd.read_excel('Data/df_1.xls')
df_2_good = pd.read_excel('Data/df_2.xls')
df_1_good = df_1_good[df_1_good['Total']>=100]


# In[5]:


df_1_good.to_excel(r'df_1_good.xlsx')


# ### 2.4. Read GeoPandas dataset and create the map for year 1914

# In[6]:


# Read the geopandas dataset
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

df_1_good = world.merge(df_1_good, how="left", left_on=['name'], right_on=['Country'])

# Drop NaN values in dataset
df_1_good = df_1_good.dropna(subset=['Total'])
df_1_good = df_1_good.dropna(subset=['Solid Fuel'])

# Create a map
my_map = folium.Map()


# In[7]:


# Add the data for first Worldmap (1914)
folium.Choropleth(
    geo_data=df_1_good,
    name='choropleth',
    data=df_1_good,
    columns=['Country', 'Total'],
    key_on='feature.properties.name',
    fill_color='OrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Total amount of fossil-fuel CO2 emissions in 1914'
).add_to(my_map)
my_map.save('co2_1914.html')


# ### 2.5. Read GeoPandas dataset and create the map for year 2014

# In[8]:


# Read the geopandas dataset and add data from 2014
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

df_2_good = world.merge(df_2_good, how="left", left_on=['name'], right_on=['Country'])

# Drop NaN values in dataset
#df_2 = df_2.dropna(subset=['Total'])
#df_2= df_2.dropna(subset=['Solid Fuel'])

# Create a map
my_map = folium.Map()


# In[9]:


# Add the data for SECOND worldmap (2014)
folium.Choropleth(
    geo_data=df_2_good,
    name='choropleth',
    data=df_2_good,
    columns=['Country', 'Total'],
    key_on='feature.properties.name',
    fill_color='OrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Total amount of fossil-fuel CO2 emissions in 2014'
).add_to(my_map)
my_map.save('co2_2014.html')

