import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

import plotly.express as px
import numpy as np

# Sample data: a 10x10 matrix of random values
z_data = np.random.randint(255, 255)

# Create the heatmap
fig = px.imshow(    z_data, 
                    text_auto=True,
                    color_continuous_scale='Viridis',
                    aspect="auto",
                    title="Plotly Express Heatmap")


# Displaying using streamlit
st.plotly_chart(fig)

data = [["🟢", "🔴", "🟢"], ["🟢", "🟢", "🟢"], ["🔴", "🔴", "🟢"]]

st.image("./Temp/gabriel-spinning-plush.gif")