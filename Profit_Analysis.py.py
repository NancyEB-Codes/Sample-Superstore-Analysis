import pandas as pd
import plotly.express as px
import streamlit as st


df = pd.read_excel("Clean_Superstore_Data.xlsx")
# Streamlit App Title
st.title("Superstore Profit Analysis")

# --- Top 10 Profitable Products ---
product_profit = (
    df.groupby("Product_Name", as_index=False)["Profit"]
      .sum()
      .sort_values(by="Profit", ascending=False)
      .head(10)
)

# Plot using Plotly
fig = px.bar(
    product_profit,
    x="Profit",
    y="Product_Name",
    orientation="h",
    title="Top 10 Most Profitable Products",
    labels={"Profit": "Total Profit", "Product_Name": "Product"},
)

# Keep highest profit product on top
fig.update_layout(yaxis={'categoryorder': 'total ascending'})

# Show chart in Streamlit
st.plotly_chart(fig, use_container_width=True)


import pandas as pd
import plotly.express as px
import streamlit as st
from read_file.data_file import get_data

df=get_data()

# --- Bottom 10 Least Profitable Products ---
least_profitable = (
    df.groupby("Product_Name", as_index=False)["Profit"]
      .sum()
      .sort_values(by="Profit", ascending=True)  # ascending → lowest first
      .head(10)
)

# Plot with Plotly Express
fig = px.bar(
    least_profitable,
    x="Profit",
    y="Product_Name",
    orientation="h",
    title="Bottom 10 Least Profitable Products",
    labels={"Profit": "Total Profit", "Product_Name": "Product"},
    color="Profit",  # color based on profit value
    color_continuous_scale="Reds"  # red = loss emphasis
)

# Keep least profitable at top
fig.update_layout(yaxis={'categoryorder': 'total ascending'})

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)



