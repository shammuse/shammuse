import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load and Cache Data
@st.cache
def load_data(file_path):
    df = pd.read_csv(file_path)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df.set_index('Timestamp', inplace=True)
    return df

st.title("Solar Farm Data Analysis")
uploaded_file = st.file_uploader("Upload Dataset", type="csv")

if uploaded_file:
    df = load_data(uploaded_file)
    st.write(df.head())

    # Correlation Matrix
    st.subheader("Correlation Matrix")
    corr = df.corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # Time Series Plot
    st.subheader("Solar Radiation Over Time")
    fig, ax = plt.subplots(figsize=(10, 6))
    df[['GHI', 'DNI', 'DHI']].plot(ax=ax)
    st.pyplot(fig)
