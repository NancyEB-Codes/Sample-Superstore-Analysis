import streamlit as st 
import pandas as pd
import plotly.express as px 


df = pd.read_excel("read_file/Clean_Superstore_Data.xlsx")


df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')


df_filtered = df[(df['Order_Date'].dt.year >= 2011) & (df['Order_Date'].dt.year <= 2014)]


most_ordered = (
    df_filtered.groupby('Product_Name')
    .size()
    .reset_index(name='Order_Count')
    .sort_values('Order_Count', ascending=False)
)
top_5_most_ordered= most_ordered.sort_values(by='Order_Count',ascending=False).head(5)


st.dataframe(top_5_most_ordered) 


fig=px.pie(
    top_5_most_ordered,
    names='Product_Name',
    values='Order_Count',
    title='Top 5 most ordered products (2011–2014)',
    labels={'Product_Name': 'Products', 'Order Count': 'Total Number Of orders'},
    )
st.plotly_chart(fig)     


df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')


df_filtered = df[(df['Order_Date'].dt.year >= 2011) & (df['Order_Date'].dt.year <= 2014)]


profit_analysis = (
    df_filtered.groupby('Product_Name')
    .agg(
        Order_Count=('Product_Name', 'size'),
        Total_Profit=('Profit', 'sum')
    )
    .reset_index()
    .sort_values('Order_Count', ascending=False)
)


top_products = profit_analysis.head(5)




fig = px.pie(
    top_products,
    names='Product_Name',
    values='Total_Profit',
    title='Most Ordered Products (2011–2014) with Profitability',
    labels={'Product_Name': "Product", "Total_Profit": "Profitability"}

)

st.plotly_chart(fig)


