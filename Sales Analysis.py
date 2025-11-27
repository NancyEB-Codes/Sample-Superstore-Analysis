
import streamlit as st
import pandas as pd
import plotly.express as px


# Load dataset
df=pd.read_excel("Clean_Superstore_Data.xlsx")

# Convert Order_Date
  
# Convert Order Date
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Year'] = df['Order_Date'].dt.year


# Group by Year
yearly_sales = df.groupby('Year')['Sales'].sum().reset_index()

st.title("Superstore Total Yearly Sales (2011 - 2014)")

# Interactive plot
fig = px.bar(yearly_sales, 
             x="Year", 
             y="Sales", 
             text="Sales",
             color="Sales", 
             color_continuous_scale="Blues",
             title="Total Sales by Year (2011–2014)")

fig.update_traces(texttemplate='%{text:,.0f}', textposition="outside")
fig.update_layout(yaxis_title="Total Sales", xaxis_title="Year")

st.plotly_chart(fig, use_container_width=True)

# Show data table
st.dataframe(yearly_sales)



import streamlit as st
import pandas as pd
import plotly.express as px


# Load dataset
df=pd.read_excel("Clean_Superstore_Data.xlsx")

# Convert Order Date to datetime
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Extract Year and Quarter
df['Year'] = df['Order_Date'].dt.year
df['Quarter'] = df['Order_Date'].dt.to_period('Q').astype(str)

# Group by Quarter
quarterly_sales = df.groupby('Quarter')['Sales'].sum().reset_index()

# Identify the best quarter
best_quarter = quarterly_sales.loc[quarterly_sales['Sales'].idxmax()]

st.title(" Best Performing Quarter Analysis")

# Show best quarter
st.success(f"🏆 Best Performing Quarter: {best_quarter['Quarter']} with Sales of ${best_quarter['Sales']:,.2f}")

# ---- Visualization ----
fig = px.bar(
    quarterly_sales,
    x="Quarter",
    y="Sales",
    text="Sales",
    color="Sales",
    color_continuous_scale="Blues",
    title="Quarter Sales Performance"
)

fig.update_traces(texttemplate='%{text:,.0f}', textposition="outside")
fig.update_layout(xaxis_title="Quarter", yaxis_title="Total Sales")

st.plotly_chart(fig, use_container_width=True)

# Show data table
st.dataframe(quarterly_sales)



