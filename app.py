<<<<<<< HEAD
import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Restaurant Tips Dashboard",
    page_icon="🍽️",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background-color:#F5F7FA;
}

h1{
    color:#1F3A93;
    font-weight:700;
}

[data-testid="stMetric"]{
    background:linear-gradient(135deg,#4F46E5,#2563EB);
    color:white;
    border-radius:15px;
    padding:20px;
    text-align:center;
    box-shadow:0 6px 15px rgba(0,0,0,0.15);
}

[data-testid="stMetricLabel"]{
    color:white;
    font-size:18px;
    font-weight:bold;
}

[data-testid="stMetricValue"]{
    color:white;
    font-size:30px;
}

.sidebar .sidebar-content{
    background:#F8FAFC;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("data/tips.csv")

USD_TO_INR = 83.5

df["total_bill_inr"] = df["total_bill"] * USD_TO_INR
df["tip_inr"] = df["tip"] * USD_TO_INR

# -----------------------------
# TITLE
# -----------------------------
st.title("🍽 Restaurant Tips Analysis Dashboard")


# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.header("🔎 Filters")

days = ["Mon","Tues","Wed","Thur","Fri","Sat","Sun"]

selected_day = st.sidebar.multiselect(
    "Select Day",
    options=days,
    default=days
)

selected_gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

selected_time = st.sidebar.multiselect(
    "Select Time",
    options=df["time"].unique(),
    default=df["time"].unique()
)

filtered_df = df[
    (df["day"].isin(selected_day)) &
    (df["Gender"].isin(selected_gender)) &
    (df["time"].isin(selected_time))
]

# -----------------------------
# KPI CARDS
# -----------------------------
col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "💰 Total Revenue",
    f"₹{filtered_df['total_bill_inr'].sum():,.0f}"
)

col2.metric(
    "💵 Total Tips",
    f"₹{filtered_df['tip_inr'].sum():,.0f}"
)

col3.metric(
    "🧾 Average Bill",
    f"₹{filtered_df['total_bill_inr'].mean():,.0f}"
)

col4.metric(
    "🎁 Average Tip",
    f"₹{filtered_df['tip_inr'].mean():,.0f}"
)

st.divider()

# -----------------------------
# CHARTS
# -----------------------------
left,right = st.columns(2)

with left:

    fig1 = px.scatter(
        filtered_df,
        x="total_bill_inr",
        y="tip_inr",
        color="Gender",
        size="size",
        hover_data=["day"],
        title="Total Bill vs Tip"
    )

    fig1.update_layout(
        template="plotly_white"
    )

    st.plotly_chart(fig1,use_container_width=True)

with right:

    avg_tip = filtered_df.groupby("day",as_index=False)["tip_inr"].mean()

    fig2 = px.bar(
        avg_tip,
        x="day",
        y="tip_inr",
        color="day",
        text_auto=".0f",
        title="Average Tip by Day"
    )

    fig2.update_layout(
        template="plotly_white",
        showlegend=False
    )

    st.plotly_chart(fig2,use_container_width=True)

left,right = st.columns(2)

with left:

    fig3 = px.pie(
        filtered_df,
        names="Gender",
        hole=0.6,
        color_discrete_sequence=px.colors.qualitative.Bold,
        title="Gender Distribution"
    )

    st.plotly_chart(fig3,use_container_width=True)

with right:

    fig4 = px.histogram(
        filtered_df,
        x="total_bill_inr",
        nbins=20,
        color_discrete_sequence=["#2563EB"],
        title="Bill Distribution"
    )

    st.plotly_chart(fig4,use_container_width=True)

st.divider()

# -----------------------------
# DATA TABLE
# -----------------------------
st.subheader("📋 Restaurant Dataset")

st.dataframe(filtered_df,use_container_width=True)

# -----------------------------
# DOWNLOAD BUTTON
# -----------------------------
csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Download Filtered Data",
    csv,
    "restaurant_data.csv",
    "text/csv"
=======
import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Restaurant Tips Dashboard",
    page_icon="🍽️",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background-color:#F5F7FA;
}

h1{
    color:#1F3A93;
    font-weight:700;
}

[data-testid="stMetric"]{
    background:linear-gradient(135deg,#4F46E5,#2563EB);
    color:white;
    border-radius:15px;
    padding:20px;
    text-align:center;
    box-shadow:0 6px 15px rgba(0,0,0,0.15);
}

[data-testid="stMetricLabel"]{
    color:white;
    font-size:18px;
    font-weight:bold;
}

[data-testid="stMetricValue"]{
    color:white;
    font-size:30px;
}

.sidebar .sidebar-content{
    background:#F8FAFC;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("data/tips.csv")

USD_TO_INR = 83.5

df["total_bill_inr"] = df["total_bill"] * USD_TO_INR
df["tip_inr"] = df["tip"] * USD_TO_INR

# -----------------------------
# TITLE
# -----------------------------
st.title("🍽 Restaurant Tips Analysis Dashboard")


# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.header("🔎 Filters")

days = ["Mon","Tues","Wed","Thur","Fri","Sat","Sun"]

selected_day = st.sidebar.multiselect(
    "Select Day",
    options=days,
    default=days
)

selected_gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

selected_time = st.sidebar.multiselect(
    "Select Time",
    options=df["time"].unique(),
    default=df["time"].unique()
)

filtered_df = df[
    (df["day"].isin(selected_day)) &
    (df["Gender"].isin(selected_gender)) &
    (df["time"].isin(selected_time))
]

# -----------------------------
# KPI CARDS
# -----------------------------
col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "💰 Total Revenue",
    f"₹{filtered_df['total_bill_inr'].sum():,.0f}"
)

col2.metric(
    "💵 Total Tips",
    f"₹{filtered_df['tip_inr'].sum():,.0f}"
)

col3.metric(
    "🧾 Average Bill",
    f"₹{filtered_df['total_bill_inr'].mean():,.0f}"
)

col4.metric(
    "🎁 Average Tip",
    f"₹{filtered_df['tip_inr'].mean():,.0f}"
)

st.divider()

# -----------------------------
# CHARTS
# -----------------------------
left,right = st.columns(2)

with left:

    fig1 = px.scatter(
        filtered_df,
        x="total_bill_inr",
        y="tip_inr",
        color="Gender",
        size="size",
        hover_data=["day"],
        title="Total Bill vs Tip"
    )

    fig1.update_layout(
        template="plotly_white"
    )

    st.plotly_chart(fig1,use_container_width=True)

with right:

    avg_tip = filtered_df.groupby("day",as_index=False)["tip_inr"].mean()

    fig2 = px.bar(
        avg_tip,
        x="day",
        y="tip_inr",
        color="day",
        text_auto=".0f",
        title="Average Tip by Day"
    )

    fig2.update_layout(
        template="plotly_white",
        showlegend=False
    )

    st.plotly_chart(fig2,use_container_width=True)

left,right = st.columns(2)

with left:

    fig3 = px.pie(
        filtered_df,
        names="Gender",
        hole=0.6,
        color_discrete_sequence=px.colors.qualitative.Bold,
        title="Gender Distribution"
    )

    st.plotly_chart(fig3,use_container_width=True)

with right:

    fig4 = px.histogram(
        filtered_df,
        x="total_bill_inr",
        nbins=20,
        color_discrete_sequence=["#2563EB"],
        title="Bill Distribution"
    )

    st.plotly_chart(fig4,use_container_width=True)

st.divider()

# -----------------------------
# DATA TABLE
# -----------------------------
st.subheader("📋 Restaurant Dataset")

st.dataframe(filtered_df,use_container_width=True)

# -----------------------------
# DOWNLOAD BUTTON
# -----------------------------
csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Download Filtered Data",
    csv,
    "restaurant_data.csv",
    "text/csv"
>>>>>>> 949a3b605e5da5ea6cba195082ef529b87c5cf63
)