 # %% Imports
 # --------------------

import pandas as pd
import numpy as np
import os

os.getcwd()
# %% 
# --------------------
# read tcx file
from tcxparser import TCXParser


# %%

# read a csv from file raw/Activities_Garmint.csv
garmin_raw = pd.read_csv('activities/raw/Activities_Garmin.csv')


# %%
garmin_processed = garmin_raw.copy()

# rename Date to Datetime
garmin_processed.rename(columns={'Date': 'Datetime'}, inplace=True)
# separate the date and time
garmin_processed['Date'] = pd.to_datetime(garmin_processed['Datetime'], format='%Y-%m-%d %H:%M:%S').dt.date
garmin_processed['Time'] = pd.to_datetime(garmin_processed['Datetime'], format='%Y-%m-%d %H:%M:%S').dt.time
garmin_processed['Avg Pace'] = pd.to_datetime(garmin_processed['Avg Pace'], format='%M:%S').dt.time

garmin_processed.drop(columns=[
    "Favorite",
    'Datetime',
    "Avg Vertical Ratio",
    "Avg Vertical Oscillation",
    "Avg Ground Contact Time",
    "Avg GCT Balance",
    "Training Stress Score®",
    "Avg Power",
    "Max Power",
    "Grit",
    "Flow",
    "Avg. Swolf",
    "Avg Stroke Rate",
    "Total Reps",
    "Dive Time",
    "Min Temp",
    "Surface Interval",
    "Decompression",
    "Max Temp",
    ], inplace=True)

garmin_processed.to_csv('activities/processed/Activities_Garmin.csv', index=False)
    # %%


