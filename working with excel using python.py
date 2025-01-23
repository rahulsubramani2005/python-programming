import pandas as pd

# File paths
input_file_path = 'RCB.xlsx'  # Path to the input Excel file
output_file_path = 'Team1.xlsx'  # Path to save the ordered output file

# Read the Excel file
df = pd.read_excel(input_file_path)


df['Cntry'] = df['Cntry'].str.strip().str.capitalize()

# Define the countries of interest
countries = ['India', 'England', 'Australia', 'West Indies','Newzland']

# Filter the data to include only the countries of interest
df_filtered = df[df['Cntry'].isin(countries)]

# Define the desired column order for the final DataFrame
final_columns = ['India', 'England', 'Australia', 'West Indies','Newzland', 'Role', 'Bidding price', 'Batting Position', 'Batting Type', 'Bowling Type']

# Initialize lists to hold data for each column
india_players = []
england_players = []
australia_players = []
west_indies_players = []
New_zland_players=[]
roles = []
bidding_prices = []
batting_positions = []
batting_types = []
bowling_types = []

# Loop through each player and add them to the respective country column
for index, row in df_filtered.iterrows():
    player_name = row['NAME']
    role = row['ROLE']
    bidding_price = row['Bidding price']
    batting_position = row['Batting Position']
    batting_type = row['Batting Type']
    bowling_type = row['Bowling Type']
    country = row['Cntry']

    # Add player names under their respective country column
    india_players.append(player_name if country == 'India' else '-')
    england_players.append(player_name if country == 'England' else '-')
    australia_players.append(player_name if country == 'Australia' else '-')
    west_indies_players.append(player_name if country == 'West Indies' else '-')
    New_zland_players.append(player_name if country == 'Newzland' else '-')
    # Add the player data for the other columns
    roles.append(role)
    bidding_prices.append(bidding_price)
    batting_positions.append(batting_position)
    batting_types.append(batting_type)
    bowling_types.append(bowling_type)

# Create the final DataFrame
final_df = pd.DataFrame({
    'India': india_players,
    'England': england_players,
    'Australia': australia_players,
    'West Indies': west_indies_players,
    'Newzland': New_zland_players,
    'Role': roles,
    'Bidding price': bidding_prices,
    'Batting Position': batting_positions,
    'Batting Type': batting_types,
    'Bowling Type': bowling_types
})

# Save the result to an Excel file
final_df.to_excel(output_file_path, index=False)

print(f"Filtered and organized data has been saved to {output_file_path}")
