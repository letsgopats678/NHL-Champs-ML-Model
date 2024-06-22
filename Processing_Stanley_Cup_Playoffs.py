from NHL_Playoff_Stats import process_and_fetch_stanley_cup_playoff_data, add_playoffs_file
import json





stanley_cup_playoffs = [process_and_fetch_stanley_cup_playoff_data("Playoff_Stats_2021_22.json"), process_and_fetch_stanley_cup_playoff_data("Playoff_Stats_2022_23.json"), process_and_fetch_stanley_cup_playoff_data("Playoff_Stats_2023_24.json")]


combined_playoffs = [playoff_year for playoff_year in stanley_cup_playoffs]


filename = 'Stanley_Cup_Playoffs.json'

# Open the file in write mode and write the combined season data to the file
with open(filename, 'w') as file:
    json.dump(combined_playoffs, file, indent=4)

