"""
Bekräftade fall i Sverige – daglig uppdatering
"""
import pandas as pd

publisher = "The Public Health Agency of Sweden"
uri = "https://www.arcgis.com/sharing/rest/content/items/b5e7488e117749c19881cce45db13f7e/data"

def get(uri=uri):
    return pd.read_excel(uri)