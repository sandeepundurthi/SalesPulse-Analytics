import streamlit as st
import pandas as pd
import plotly.express as px

# ======================
# PAGE CONFIG
# ======================

st.set_page_config(
    page_title="SalesPulse Analytics Dashboard",
    layout="wide"
)

# ======================
# LOAD DATA
# ======================

df = pd.read_csv("../data/superstore.csv", encoding="latin1")

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month_name()
df["Year-Month"] = df["Order Date"].dt.to_period("M").astype(str)

# ======================
# SIDEBAR FILTERS
# ======================

st.sidebar.header("Dashboard Filters")

selected_region = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

selected_category = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

filtered_df = df[
    (df["Region"].isin(selected_region)) &
    (df["Category"].isin(selected_category))
]

# ======================
# TITLE
# ======================

st.title("SalesPulse Analytics Dashboard")
st.markdown("Business Intelligence Dashboard for Sales & Revenue Analytics")

# ======================
# KPI CALCULATIONS
# ======================

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()

profit_margin = (total_profit / total_sales) * 100 if total_sales != 0 else 0

# ======================
# KPI CARDS
# ======================

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Total Orders", total_orders)
col4.metric("Profit Margin", f"{profit_margin:.2f}%")

# ======================
# MONTHLY SALES TREND
# ======================

monthly_sales = (
    filtered_df.groupby("Year-Month")["Sales"]
    .sum()
    .reset_index()
)

fig1 = px.line(
    monthly_sales,
    x="Year-Month",
    y="Sales",
    title="Monthly Sales Trend",
    markers=True
)

st.plotly_chart(fig1, use_container_width=True)

# ======================
# REGION ANALYSIS
# ======================

region_sales = (
    filtered_df.groupby("Region")[["Sales", "Profit"]]
    .sum()
    .reset_index()
)

fig2 = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    color="Profit",
    title="Sales by Region",
    text_auto=".2s"
)

st.plotly_chart(fig2, use_container_width=True)

# ======================
# TOP PRODUCT CATEGORIES
# ======================

top_products = (
    filtered_df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig3 = px.bar(
    top_products,
    x="Sub-Category",
    y="Sales",
    title="Top Product Categories",
    text_auto=".2s"
)

st.plotly_chart(fig3, use_container_width=True)

# ======================
# DISCOUNT VS PROFIT
# ======================

fig4 = px.scatter(
    filtered_df,
    x="Discount",
    y="Profit",
    title="Discount vs Profitability",
    opacity=0.6,
    hover_data=["Product Name", "Category", "Sub-Category", "Region"]
)

st.plotly_chart(fig4, use_container_width=True)

# ======================
# TOP LOSS-MAKING CATEGORIES
# ======================

loss_products = (
    filtered_df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values()
    .head(5)
    .reset_index()
)

fig5 = px.bar(
    loss_products,
    x="Sub-Category",
    y="Profit",
    title="Top Loss-Making Categories",
    text_auto=".2s"
)

st.plotly_chart(fig5, use_container_width=True)

# ======================
# BUSINESS INSIGHTS
# ======================

st.subheader("Key Business Insights")

st.markdown("""
- High discounts between 50% and 80% are strongly associated with negative profitability.
- The West region generates the highest overall revenue and profit.
- Phones and Chairs are the top-performing product sub-categories by sales.
- Tables generate strong sales volume but show negative profit performance.
- Discount strategy should be reviewed for low-margin categories to improve profitability.
""")
