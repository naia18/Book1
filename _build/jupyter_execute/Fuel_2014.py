#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import geopandas
import folium


# In[2]:


# Read csv file
df_co2 = pd.read_csv('Data/fossil-fuel.csv')


# In[3]:


# Select the data that I want
df_1 = df_co2[df_co2['Year'] == 1914]
df_2 = df_co2[df_co2['Year'] == 2014]


# In[4]:


df_2_good = pd.read_excel('Data/df_2.xls')


# In[49]:


#df_2 = df_2[df_2['Total']>=100]
#df_1_good['Total'] = df_1_good['Total'].astype(str)
#df_1_good['Solid Fuel'] = df_1_good['Solid Fuel'].astype(str)


# In[50]:


# Read the geopandas dataset
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

df_2_good = world.merge(df_2_good, how="left", left_on=['name'], right_on=['Country'])

# Drop NaN values in dataset
#df_2 = df_2.dropna(subset=['Total'])
#df_2= df_2.dropna(subset=['Solid Fuel'])

# Create a map
my_map = folium.Map()


# In[51]:


# Add the data
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


# In[ ]:




