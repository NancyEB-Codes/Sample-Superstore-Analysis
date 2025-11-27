import streamlit as st 
import pandas as pd


df=pd.read_excel("C:\\Users\\buats\\Downloads\\anaconda file\\CODEPRACTICE101\\STREAMLIT\\read_file\\Clean_Superstore_Data.xlsx")


st.header('OVERVIEW OF DATA SET')
st.markdown(
'It simulates sales data for a fictional office supplies company called Superstore, operating across various U.S. regions. The dataset tracks customer orders and business performance over time.')




# Display the data in the app
st.write("Below is a preview of the Sample Superstore dataset:")
st.dataframe(df)

