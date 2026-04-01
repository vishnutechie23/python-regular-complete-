import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt

st.title("📊 6️⃣ Charts and Visualizations in Streamlit")

# ------------------------------------------------------
st.header("🔹 Built-in Streamlit Charts")

# Create some dummy time series data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Product A', 'Product B', 'Product C']
)

# Line Chart
st.subheader("1️⃣ Line Chart")
st.line_chart(data)

# Bar Chart
st.subheader("2️⃣ Bar Chart")
st.bar_chart(data)

# Area Chart
st.subheader("3️⃣ Area Chart")
st.area_chart(data)

# ------------------------------------------------------
st.header("🔸 External Chart Libraries")

# Generate data for external plots
df_plot = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Value": [23, 45, 56, 78]
})

# ----------------------------------
st.subheader("4️⃣ Matplotlib Chart")

# Matplotlib bar chart
fig, ax = plt.subplots()
ax.bar(df_plot["Category"], df_plot["Value"], color='skyblue')
ax.set_title("Matplotlib Bar Chart")
st.pyplot(fig)

# ----------------------------------
st.subheader("5️⃣ Seaborn Chart")

# Seaborn boxplot
df_tips = sns.load_dataset("tips")
fig2, ax2 = plt.subplots()
sns.boxplot(x="day", y="total_bill", data=df_tips, ax=ax2)
ax2.set_title("Seaborn Box Plot")
st.pyplot(fig2)

# ----------------------------------
st.subheader("6️⃣ Plotly Chart")

# Plotly interactive scatter plot
df_plotly = px.data.iris()
fig3 = px.scatter(
    df_plotly, x="sepal_width", y="sepal_length",
    color="species", size="petal_length",
    title="Plotly Interactive Scatter Plot"
)
st.plotly_chart(fig3, use_container_width=True)

# ----------------------------------
st.subheader("7️⃣ Altair Chart")

# Altair chart
df_altair = pd.DataFrame({
    'x': list(range(10)),
    'y': np.random.randint(10, 100, 10)
})
chart = alt.Chart(df_altair).mark_line(point=True).encode(
    x='x',
    y='y'
).properties(title="Altair Line Chart")
st.altair_chart(chart, use_container_width=True)