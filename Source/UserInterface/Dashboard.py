import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

import plotly.express as px
import numpy as np

import Source.Main as Main

# Running main
results = Main.run_tests()["Results"]

z_data = [[]]
for i in range(len(results)):
    if len(z_data[-1]) < 3:
        z_data[-1].append(results[i])
    else:
        z_data.append([results[i]])
        
while len(z_data[-1]) < 3:
    z_data[-1].append(-1)

# Create the heatmap
fig = px.imshow(    z_data, 
                    text_auto=True,
                    color_continuous_scale=[[0.0, "#000000"], 
                                            [0.2, "#03FF81"], 
                                            [0.4, "#FF0000"],
                                            [1.0, "#FF0000"]],
                    aspect="auto",
                    title="Test results")

# Displaying using streamlit
st.plotly_chart(fig)

st.image("./Temp/gabriel-spinning-plush.gif")