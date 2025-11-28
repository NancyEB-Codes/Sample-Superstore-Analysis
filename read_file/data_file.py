import pandas as pd

def get_data():
    return pd.read_excel("C:\\Users\\buats\\OneDrive\\Documents\\STREAMLIT\\read_file\\Clean_Superstore_Data.xlsx", engine='openpyxl')
