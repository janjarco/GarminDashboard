# %% imports
# --------------------

import pandas as pd
import numpy as np

import os

# %% Import data
# --------------------

# read a csv from file raw/Activities_Garmint.csv
garmin_df = pd.read_csv('../data/activities/processed/Activities_Garmin.csv')
# %%
# plot a scatterplot in plotly with Avg HR vs Avg Pace
import plotly.express as px
fig = px.scatter(garmin_df, x="Avg HR", y="Avg Pace", color="Activity Type")

fig.show()


# %%
