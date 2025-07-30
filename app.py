import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import date

# Page Config
st.set_page_config(page_title="Stock Market Dashboard", layout="wide")

# Title
st.title("Stock Market Dashboard")
st.write("Track stock prices and visualize data interactively!")

# Sidebar Inputs
st.sidebar.header("User Input Options")
ticker = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, TSLA):", "AAPL")
start_date = st.sidebar.date_input("Start Date", date(2023, 1, 1))
end_date = st.sidebar.date_input("End Date", date.today())

if start_date > end_date:
    st.error("Start Date cannot be after End Date.")
else:
    if ticker:
        try:
            data = yf.download(ticker, start=start_date, end=end_date)

            if not data.empty:
                # ✅ Fix MultiIndex columns (if present)
                if isinstance(data.columns, pd.MultiIndex):
                    data.columns = [col[0] for col in data.columns]

                # ✅ Check if 'Close' column exists
                if 'Close' in data.columns:
                    st.subheader(f"{ticker} Stock Data")
                    st.write(f"**Current Price:** ${round(data['Close'].iloc[-1], 2)}")

                    # Line Chart
                    fig = px.line(
                        data.reset_index(),
                        x='Date',
                        y='Close',
                        title=f"{ticker} Closing Price",
                        labels={'Close': 'Closing Price', 'Date': 'Date'}
                    )
                    st.plotly_chart(fig, use_container_width=True)

                    # Show Data Table
                    st.write("### Raw Data")
                    st.dataframe(data.tail(10))

                    # Download Button
                    csv = data.to_csv().encode('utf-8')
                    st.download_button(
                        label="📥 Download Data as CSV",
                        data=csv,
                        file_name=f"{ticker}_data.csv",
                        mime="text/csv"
                    )
                else:
                    st.warning("⚠ 'Close' column not found in data.")
            else:
                st.warning("⚠ No data found. Please check the ticker symbol.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
