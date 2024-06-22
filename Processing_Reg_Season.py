from NHL_Reg_Season_Stats import add_season_file, process_teams
import json
#import NHL_Reg_Season_Stats

seasons = [process_teams("NHL_Team_Stats_2021_22.json"), process_teams("NHL_Team_Stats_2022_23.json"), process_teams("NHL_Team_Stats_2023_24.json")]

#for season in seasons:

#seasons = [season_1, season_2, season_3]

combined_seasons = [season for season in seasons]


filename = 'Regular_Season.json'

# Open the file in write mode and write the combined season data to the file
with open(filename, 'w') as file:
    json.dump(combined_seasons, file, indent=4)