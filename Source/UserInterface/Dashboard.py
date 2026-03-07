import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

import plotly.express as px
import numpy as np

from Main import Main

# Running main
results: dict = Main.run_tests()["Results"]

names_data = [[]]
z_data = [[]]
for i in range(len(results)):
    if len(z_data[-1]) < 4:
        z_data[-1].append(results[i])
        names_data[-1].append(i)
    else:
        z_data.append([results[i]])
        names_data.append([i])

while len(z_data[-1]) < 4:
    z_data[-1].append(-1)

# Create the heatmap
fig = px.imshow(
    z_data,
    color_continuous_scale=[
        [0.0, "#03FF81"],
        [0.1, "#03FF81"],
        [0.2, "#FF0000"],
        [1.0, "#FF0000"],
    ],
    aspect="auto",
    title="Test results",
)

fig.update_traces(text=names_data, texttemplate="%{text}", textfont={"size": 14})

# Hide the colorbar
fig.update_coloraxes(showscale=False)

fig.update_xaxes(tickmode="array", tickvals=[], ticktext=[])

fig.update_yaxes(tickmode="array", tickvals=[], ticktext=[])

# Displaying using streamlit
st.plotly_chart(fig)

# Data frame
status_names = {0: "Ok", 1: "Error", 2: "Error", 3: "Error", 4: "Error"}

error_names = {0: "None", 1: "Bug 1", 2: "Bug 2", 3: "Bug 3", 4: "Unknown Error"}

data_frame_data = pd.DataFrame(
    {
        "Register IDs": results.keys(),
        "Status": [status_names[results[i]] for i in results],
        "Error Type": [error_names[results[i]] for i in results],
    }
)


def color_row(row):
    if row["Status"] == "Ok":
        return [""] * len(row)
    elif row["Status"] == "Error":
        return ["background-color: #FF0000"] * len(row)
    return [""] * len(row)


styled_df = data_frame_data.style.apply(color_row, axis=1)

st.dataframe(
    styled_df,
    hide_index=True,
)

# st.image("./Temp/gabriel-spinning-plush.gif")
# st.image("./Megumin.png")
