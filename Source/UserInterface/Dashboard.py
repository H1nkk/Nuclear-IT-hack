import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

import plotly.express as px
import numpy as np

import Source.Main as Main

# Running main
z_data = Main.run_tests()["Results"]

# Sample data: a 10x10 matrix of random values

# Create the heatmap
fig = px.imshow(    z_data, 
                    text_auto=True,
                    color_continuous_scale=[[0.0, "#03FF81"], 
                                            [0.2, "#FF0000"],
                                            [1.0, "#FF0000"]],
                    aspect="auto",
                    title="Plotly Express Heatmap")


# Displaying using streamlit
st.plotly_chart(fig)

st.image("./Temp/gabriel-spinning-plush.gif")