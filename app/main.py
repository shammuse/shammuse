import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cache Data Loading Function
@st.cache
def load_data(file_path):
    df = pd.read_csv(file_path)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df.set_index('Timestamp', inplace=True)
    return df

# Streamlit App
st.title("Solar Farm Data Analysis")

# File Uploader
file_path = "cleaned_data_1.csv"  # Local dataset
df = load_data(file_path)

# Display Data
st.write("### Dataset Preview")
st.write(df.head())

# Correlation Matrix
st.subheader("Correlation Matrix")
corr = df.corr()
fig_corr, ax_corr = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax_corr)
st.pyplot(fig_corr)

# Time Series Plot
st.subheader("Solar Radiation Over Time")
fig_ts, ax_ts = plt.subplots(figsize=(10, 6))
df[['GHI', 'DNI', 'DHI']].plot(ax=ax_ts)
st.pyplot(fig_ts)

