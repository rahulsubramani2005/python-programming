import pandas as pd

# Step 1: Read the data from the Excel file
input_file = 'RCB.xlsx'  # Replace with your input Excel file path
df = pd.read_excel(input_file)

# Step 2: Transpose the data
df_transposed = df.transpose()

# Step 3: Write the transposed data to a new Excel file
output_file = 'Team2.xlsx'  
df_transposed.to_excel(output_file, index=True, header=False)

print(f"Data has been transposed and saved to {output_file}")
