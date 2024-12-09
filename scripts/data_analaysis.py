import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# List of cleaned files
file_paths = ["cleaned_data_1.csv", 
              "cleaned_data_2.csv", 
              "cleaned_data_3.csv"]

# Initialize a dictionary to store data from each file
data_frames = {}

# Process each file
for file_path in file_paths:
    # Load data
    df = pd.read_csv(file_path)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df.set_index('Timestamp', inplace=True)
    
    # Store in dictionary
    data_frames[file_path] = df
    
    # Time Series Plot
    plt.figure(figsize=(12, 6))
    df[['GHI', 'DNI', 'DHI']].plot()
    plt.title(f"Solar Radiation Components Over Time - {file_path.split('/')[-1]}")
    plt.xlabel("Time")
    plt.ylabel("Radiation (W/m²)")
    plt.legend(["GHI", "DNI", "DHI"])
    plt.grid()
    plt.show()

    # Correlation Matrix
    corr = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title(f"Correlation Matrix - {file_path.split('/')[-1]}")
    plt.show()

# Optional: Combine all data for a unified analysis
combined_df = pd.concat(data_frames.values())
combined_df = combined_df.sort_index()

# Combined Time Series Plot
plt.figure(figsize=(12, 6))
combined_df[['GHI', 'DNI', 'DHI']].plot()
plt.title("Combined Solar Radiation Components Over Time")
plt.xlabel("Time")
plt.ylabel("Radiation (W/m²)")
plt.legend(["GHI", "DNI", "DHI"])
plt.grid()
plt.show()

# Combined Correlation Matrix
combined_corr = combined_df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(combined_corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Combined Correlation Matrix")
plt.show()
