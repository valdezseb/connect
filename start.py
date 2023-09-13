import numpy as np
import pandas as pd


import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1da3hg3H0oSdii7zMxXL21jHVkKL2TByo4WJpk_MOyp8/edit?usp=sharing"

conn = st.experimental_connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols=[0, 5])
st.dataframe(data)
