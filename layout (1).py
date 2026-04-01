import streamlit as st

st.title("🧱 7️⃣ Layouts and UI Control in Streamlit")

# ================================================
# 1️⃣ Sidebar – Widgets on the side panel
st.sidebar.header("🎛️ Sidebar Widgets")

# Add sidebar widgets (like filters or navigation)
sidebar_name = st.sidebar.text_input("Enter your name:")
sidebar_slider = st.sidebar.slider("Select a value", 0, 100, 50)

if sidebar_name:
    st.sidebar.write(f"Hello, {sidebar_name} 👋")
st.sidebar.write(f"Slider value is: {sidebar_slider}")

st.markdown("---")

# ================================================
# 2️⃣ Columns – Create responsive multi-column layout
st.subheader("2️⃣ Responsive Columns Layout")

# Create 3 equal-width columns
col1, col2, col3 = st.columns(3)

with col1:
    st.write("🧊 Column 1")
    st.button("Click A")

with col2:
    st.write("🧊 Column 2")
    st.checkbox("Check me")

with col3:
    st.write("🧊 Column 3")
    st.radio("Pick one", ["X", "Y", "Z"])

st.markdown("---")

# ================================================
# 3️⃣ Expander – Collapsible section
st.subheader("3️⃣ Collapsible Sections using st.expander")

with st.expander("📦 Click to expand this section"):
    st.write("This content is hidden until you expand.")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=150)
    st.success("Thanks for expanding!")

st.markdown("---")

# ================================================
# 4️⃣ Container – Group multiple elements together
st.subheader("4️⃣ Grouped Content with st.container")

with st.container():
    st.write("This is inside a container.")
    st.line_chart({"data": [1, 5, 2, 6, 3]})
    st.text("All elements above are grouped.")

# Outside container
st.write("This is outside the container.")