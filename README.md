
# Stock Market Dashboard

A simple and interactive **Stock Market Dashboard** built using **Streamlit**, **YFinance**, **Plotly**, and **Pandas**. This application allows users to:

✅ Fetch historical stock price data
✅ Visualize closing prices with interactive charts
✅ Download the stock data as a CSV file

---

## Features

* Enter any stock ticker symbol (e.g., `AAPL`, `TSLA`, `GOOG`)
* Choose a **start date** and **end date** for historical data
* Interactive **line chart** for closing prices
* Display latest stock price
* Download stock data as a CSV file

---

## Tech Stack

* **Python 3.9+**
* [Streamlit](https://streamlit.io/) – For web interface
* [YFinance](https://pypi.org/project/yfinance/) – For stock data
* [Plotly](https://plotly.com/python/) – For interactive charts
* [Pandas](https://pandas.pydata.org/) – For data manipulation
* [Prophet](https://facebook.github.io/prophet/) *(optional for future forecasting)*

---

## 📂 Project Structure

```
📦 Stock-Market-Dashboard
├── app.py                 # Main Streamlit app
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/stock-market-dashboard.git
cd stock-market-dashboard
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run the App

```bash
streamlit run app.py
```

Then open the URL shown in the terminal (usually `http://localhost:8501`).

---

## 📦 requirements.txt

```
streamlit
yfinance
pandas
plotly
prophet
```

---

