"""
DIGG Folkhälsomyndigheten
"""

import pandas as pd

publisher = "The Public Health Agency of Sweden"

# Datasets on the spread of COVID-19 from The Public Health Agency of Sweden.
files = {
    "Antal fall av covid-19 i Sverige per åldersgrupp":
        'https://free.entryscape.com/store/360/resource/25',
    "Antal fall av covid-19 i Sverige per dag och region":
        'https://free.entryscape.com/store/360/resource/15',
    "Antal fall av covid-19 i Sverige per region":
        'https://free.entryscape.com/store/360/resource/4',
    "Antal fall av covid-19 i Sverige per kön":
        'https://free.entryscape.com/store/360/resource/20',
}

def get(files=files):
    for set, uri in files.items():
        yield set, pd.read_csv(uri)