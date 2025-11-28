import streamlit as st



st.set_page_config(page_title="SAMPLE SUPERSTORE DATA ANALYSIS DASHBOARD",layout='wide')


def set_background_url(url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background (optional, comment out if not needed)
set_background_url("https://png.pngtree.com/thumb_back/fh260/background/20240418/pngtree-overtime-binder-data-finance-report-business-with-graph-analysis-in-office-image_15659721.jpg")

# Intro message
st.markdown("""
    <div style='background-color: rgba(0,0,0,0.6); padding: 2rem; border-radius: 30px; text-align: center;'>
        <h1 style='color: white;'>🧠 Welcome to the Sample Superstore Data Insights Dashboard</h1>
        <p style='color: yellow; font-size: 20px;'>
            This project presents a detailed analysis of <b>📦Orders</b>, <b>👥Customers</b>, <b>🏷️Sales</b>, and <b>💰Profits</b> 
            of the sample superstore dataset to help uncover key trends, identify performance gaps, and guide business decisions.
        </p>
        <p style='color: white; font-size: 17px;'>
            Navigate through the sidebar to explore specific pages and gain actionable insights into each area of the business.
        </p>
        <p style='color: white; font-size: 17px;'>
            Created with ❤️ using Streamlit.
        </p>
    </div>
""", unsafe_allow_html=True)

