# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:29:25 2020

@author: ankuspat
"""

import pandas as pd
import numpy as np
import folium




state_wise_centroid = pd.read_csv(r"C:\Users\ankuspat\kpi\app\maps\datasets_7536_10717_district wise centroids.csv")
duplicateRowsDF = state_wise_centroid[state_wise_centroid.duplicated(["District","Latitude"])]


test=list(state_wise_centroid.District.unique())

center_lat = state_wise_centroid.mean().Latitude
center_long = state_wise_centroid.mean().Longitude



m = folium.Map(location=[center_lat, center_long], zoom_start=4.1)

for index, row in state_wise_centroid.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], 
                 popup=row['District'],
                  tooltip = str(row["District"]) + ", " + str(row["State"]),
                  icon = folium.Icon(color='red'),
                  legend_name='State and District level mapping'
                 ).add_to(m)
m




m.save(r"C:\Users\ankuspat\kpi\app\maps\mymap.html")

import webbrowser 
webbrowser.open(r"C:\Users\ankuspat\kpi\app\maps\mymap.html") 

