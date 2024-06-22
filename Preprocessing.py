import Processing_Stanley_Cup_Playoffs
import Processing_Reg_Season
import json
from collections import defaultdict
import NHL_Playoff_Stats

#with open("Regular_Season.json", "r") as loading:
    #loaded_data = json.load(loading)

# Load regular season data from a JSON file
with open('Regular_Season.json', 'r') as f:
    regular_season_data = json.load(f)




def combine_team_stats(filename1, filename2):
    combined_data = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

    with open(filename1, "r") as file:
        data = json.load(file)  # Load the list of dictionaries directly

    for season in data:
        season_id = season["seasonID"]
        for team_name, stats in season.items():
            if team_name == "seasonID":
                continue  # Skip the seasonID entry
            for stat, value in stats.items():
                if "Percentage" in stat or "Pctg" in stat:
                    combined_data[team_name][season_id][stat] = value
                else:
                    combined_data[team_name][season_id][stat] += value
    
    with open(filename2, "r") as file:
        playoff_data = json.load(file)  # Load the list of dictionaries directly



 
 
    for season_index, playoffs in enumerate(playoff_data):
        season_year = ["20212022", "20222023", "20232024"][season_index]  # Adjust this according to your seasons
        for team, stats in playoffs.items():
            if team == "Stanley Cup Champions":
                continue  # Skip the Stanley Cup Champions entry
            else:
                if "Playoff History" not in combined_data[team]:
                    combined_data[team]["Playoff History"] = []

                playoff_record = {"season": season_year, **stats}
                combined_data[team]["Playoff History"].append(playoff_record)


    

    return combined_data

def defaultdict_to_dict(d):
    if isinstance(d, defaultdict):
        d = {k: defaultdict_to_dict(v) for k, v in d.items()}
    return d


def dictionary_to_list(data):
    records = [data]
    
    return records


preprocessed_data = defaultdict_to_dict(combine_team_stats("Regular_Season.json", "Stanley_Cup_Playoffs.json"))

training_data = dictionary_to_list(preprocessed_data)


