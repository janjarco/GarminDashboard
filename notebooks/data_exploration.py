# %% imports
# --------------------

import pandas as pd|
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
# show a histogram of Avg HR by date of run
# use plotly express
fig = px.histogram(garmin_df, x="Date", y="Avg HR", color="Activity Type", marginal="rug")
fig.show()

# :)))))
# %%


# Lambda meeting update :-)