import streamlit as st
import pandas as pd 
import plotly.express as px



df=pd.read_excel("C:\\Users\\buats\\Downloads\\anaconda file\\CODEPRACTICE101\\STREAMLIT\\read_file\\Clean_Superstore_Data.xlsx")

df['Total Sales'] = df['Sales'] * df['Quantity']
# Calculate Total Sales per row

# Filter for years 2011 to 2014
df_filtered = df[(df['Order_Year'] >= 2011) & (df['Order_Year'] <= 2014)]

# Group by Customer and sum Total Sales
customer_sales = df_filtered.groupby('Customer_Name')['Total Sales'].sum().reset_index()

# Sort (optional)
customer_sales = customer_sales.sort_values(by='Total Sales', ascending=False)

top_5_customers = customer_sales.sort_values(by='Total Sales', ascending=False).head(5)

# Display in Streamlit
st.dataframe(top_5_customers)

fig = px.bar(
    top_5_customers,
    x='Customer_Name',
    y='Total Sales',
    color='Customer_Name',  # This creates a legend
    title='Top 5 Customers by Total Sales (2011–2014)',
    labels={'Customer_Name': 'Customer', 'Total Sales': 'Total Sales'},
)

# Show figure
st.plotly_chart(fig)


# Filter for years 2011 to 2014
df_filtered = df[(df['Order_Year'] >= 2011) & (df['Order_Year'] <= 2014)]

# Group by Customer and sum Total Sales
customer_profits= df_filtered.groupby('Customer_Name')['Profit'].sum().reset_index()

# Sort (optional)
customer_profits= customer_profits.sort_values(by='Profit', ascending=False)

top_5_customers = customer_profits.sort_values(by='Profit', ascending=False).head(5)

# Display in Streamlit
st.dataframe(top_5_customers)

fig = px.bar(
    top_5_customers,
    x='Customer_Name',
    y='Profit',
    color='Customer_Name',  # This creates a legend
    title='Top 5 Customers by Total Profits (2011–2014)',
    labels={'Customer_Name': 'Customer', 'Profit': 'Profit'},
)

# Show figure
st.plotly_chart(fig)


