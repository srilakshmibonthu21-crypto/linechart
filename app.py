import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📈 Line Chart Visualization App")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read data
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())

    columns = df.columns.tolist()

    # --- Line Chart 1 ---
    st.subheader("Line Chart 1")
    x_axis1 = st.selectbox("Select X-axis (Chart 1)", options=columns, key="lx1")
    y_axis1 = st.multiselect("Select Y-axis (Chart 1)", options=columns, key="ly1")

    if x_axis1 and y_axis1:
        fig1, ax1 = plt.subplots()
        for col in y_axis1:
            ax1.plot(df[x_axis1], df[col], label=col)
        ax1.set_xlabel(x_axis1)
        ax1.set_ylabel("Values")
        ax1.legend()
        st.pyplot(fig1)

    # --- Line Chart 2 ---
    st.subheader("Line Chart 2")
    x_axis2 = st.selectbox("Select X-axis (Chart 2)", options=columns, key="lx2")
    y_axis2 = st.multiselect("Select Y-axis (Chart 2)", options=columns, key="ly2")

    if x_axis2 and y_axis2:
        fig2, ax2 = plt.subplots()
        for col in y_axis2:
            ax2.plot(df[x_axis2], df[col], label=col)
        ax2.set_xlabel(x_axis2)
        ax2.set_ylabel("Values")
        ax2.legend()
        st.pyplot(fig2)
