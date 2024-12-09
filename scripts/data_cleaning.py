import pandas as pd
import numpy as np

def clean_and_save_data(url, output_file):
    try:
        # Load data from Google Drive link
        print(f"Processing file: {url}")
        df = pd.read_csv(url)

        # Ensure Timestamp column is parsed as datetime
        if 'Timestamp' in df.columns:
            df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
        else:
            raise ValueError("Timestamp column missing in the dataset.")

        # Drop rows with invalid timestamps
        df = df.dropna(subset=['Timestamp'])

        # Drop duplicate rows
        df = df.drop_duplicates()

        # Convert all applicable columns to numeric, ignoring errors
        numeric_cols = df.select_dtypes(include=['object', 'float64', 'int64']).columns
        df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

        # Fill missing numeric values with the median
        df = df.fillna(df.median(numeric_only=True))

        # Remove rows with invalid GHI, DNI, or DHI values
        df = df[(df['GHI'] >= 0) & (df['DNI'] >= 0) & (df['DHI'] >= 0)]

        # Save cleaned data
        df.to_csv(output_file, index=False)
        print(f"Cleaned data saved to {output_file}")
    except Exception as e:
        print(f"Error processing {url}: {e}")

if __name__ == "__main__":
    # List of Google Drive file links
    file_links = [
        "https://drive.google.com/uc?id=1zhIuSM7Im5YqJN1AGGe_yqej8F2O40lw",
        "https://drive.google.com/uc?id=1z8ow-PPe3oVDKFpk0e_uVP0Lm4HALYrh",
        "https://drive.google.com/uc?id=1Ds6SIIl7DvSMWOUGM5qCPnPAF1zNZSfo"
    ]

    # Corresponding output file names
    output_files = [
        "cleaned_data_1.csv",
        "cleaned_data_2.csv",
        "cleaned_data_3.csv"
    ]

    # Process each file
    for url, output in zip(file_links, output_files):
        clean_and_save_data(url, output)

