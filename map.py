#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 23:32:55 2019

@author: abhijithneilabraham
"""

import folium
from folium import plugins
from folium.plugins import HeatMap


t_list = ["Stamen Terrain", "Stamen Toner", "Mapbox Bright"]
map_hooray = folium.Map(location=[51.5074, 0.1278],
                        tiles = "Stamen Terrain",
                        zoom_start = 12)
print(type(map_hooray))