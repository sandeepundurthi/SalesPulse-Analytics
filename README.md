# SalesPulse Analytics Dashboard

Interactive business intelligence dashboard for analyzing retail sales, profitability, regional performance, and operational KPIs.

## Features
- Revenue & Profit KPI tracking
- Monthly sales trend analysis
- Regional sales performance
- Product category insights
- Discount vs profitability analysis
- Loss-making category detection
- Interactive dashboard filters

## Tech Stack
- Python
- Pandas
- Streamlit
- Plotly
- SQL
- Data Analytics

## Key Insights
- High discounts negatively impact profitability
- West region generates highest profit
- Phones and Chairs are top-performing categories
- Tables show high sales but negative profit margins

## Run Locally

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

## Project Structure

```text
SalesPulse-Analytics/
│
├── dashboard/
│   └── app.py
├── data/
│   └── superstore.csv
├── notebooks/
├── sql/
├── README.md
└── requirements.txt
```
