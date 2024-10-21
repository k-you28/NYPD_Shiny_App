import pandas as pd

# Load the dataset (adjust the file path as needed)
df = pd.read_csv('NYPD_Arrests_Data_Reduced.csv')

# Print the first few rows to inspect the ARREST_DATE column
print(df['ARREST_DATE'].head())

# Handle missing or incorrect date formats by first inspecting unique date formats
# Convert the 'ARREST_DATE' column to datetime format, without specifying format first
df['ARREST_DATE'] = pd.to_datetime(df['ARREST_DATE'], errors='coerce')

# Check how many rows have valid dates and invalid dates
print("Number of rows with valid dates:", df['ARREST_DATE'].notnull().sum())
print("Number of rows with invalid dates:", df['ARREST_DATE'].isnull().sum())

# Filter the data to only include records from 2020 to 2023
filtered_df = df[(df['ARREST_DATE'].dt.year >= 2020) & (df['ARREST_DATE'].dt.year <= 2023)]

# Check the result of the filtering
print("Number of rows after filtering:", len(filtered_df))

# Save the filtered dataset to a new CSV file if there are valid results
if len(filtered_df) > 0:
    filtered_df.to_csv('NYPD_Arrests_Data_2020_to_2023.csv', index=False)
    print("The dataset has been filtered and saved to 'NYPD_Arrests_Data_2020_to_2023.csv'.")
else:
    print("No data available for the specified date range.")

