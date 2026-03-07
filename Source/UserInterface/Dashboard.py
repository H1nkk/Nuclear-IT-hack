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
    if len(z_data[-1]) < 4:
        z_data[-1].append(results[i])
    else:
        z_data.append([results[i]])

while len(z_data[-1]) < 4:
    z_data[-1].append(-1)

# Create the heatmap
fig = px.imshow(
    z_data,
    text_auto=True,
    color_continuous_scale=[
        [0.0, "#03FF81"],
        [0.1, "#03FF81"],
        [0.2, "#FF0000"],
        [1.0, "#FF0000"],
    ],
    aspect="auto",
    title="Test results",
)

# Displaying using streamlit
st.plotly_chart(fig)

# Data frame
status_names = {
    0 : "Ok",
    1 : "Error",
    2 : "Error",
    3 : "Error"
}

error_names = {
    0 : "None",
    1 : "Bug 1",
    2 : "Bug 2",
    3 : "Bug 3"
}

data_frame_data = pd.DataFrame(
    {
        "Register IDs": range(16),
        "Status" : [status_names[i] for i in results],
        "Error Type": [error_names[i] for i in results]
    }
)

st.dataframe(
    data_frame_data,
    column_config={
        "Register IDs": "Register IDs",
        "Status": "Status",
        "Error Type": "Error Type"
    },
    hide_index=True,
)

# st.image("./Temp/gabriel-spinning-plush.gif")
# st.image("./Megumin.png")
