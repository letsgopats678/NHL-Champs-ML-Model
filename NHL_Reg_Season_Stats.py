import requests
import json
import pandas as pd
from functools import reduce

#import seaborn as sns
#import matplotlib.pyplot as plt

def add_season_file(url_season, file_name): #function adds a season's data to a file
    url = url_season

    payload = ""
    headers = {"User-Agent": "insomnia/9.1.1"}

    response = requests.request("GET", url, data=payload, headers=headers)
    with open(file_name, 'w') as points: #creates a file and allows a write
        points.write(response.text)
        points.close() #closes the file

def process_teams(file_name):#function processes a team's data
    hockey_dict = {} #dictionary to contain the necessary vals for each team
    hockey_stack = []
    with open(file_name, "r") as team:#opens the file and reads the data
        team_data = json.load(team)
    for season in team_data["standings"]: #for each season for each team 
        #print(season["seasonId"])
        #set the key to be the team name to be the dict of the stats of that season
        hockey_dict["seasonID"] = season["seasonId"]
        hockey_dict[season["teamName"]["default"]] = {"points": season["points"], "wins" : season["wins"], "losses": season["losses"], "otLosses" : season["otLosses"], "goalsFor": season["goalFor"], "goalsAgainst": season["goalAgainst"], "winPercentage": season["winPctg"], "goalDifferential": season["goalDifferential"], "homeWins": season["homeWins"],  "homeLosses": season["homeLosses"], "regulationWins": season["regulationWins"], "roadLosses": season["roadLosses"], "roadPoints": season["roadPoints"], "roadWins": season["roadWins"], "last10gamesWins": season["l10Wins"], "last10gamesInPoints": season["l10Points"], "goalsForPctg": season["goalsForPctg"]}

    return hockey_dict




add_season_file("https://api-web.nhle.com/v1/standings/2024-04-18", "NHL_Team_Stats_2021_22.json")
#process_teams("NHL_Team_Stats_2021_22.json")

add_season_file("https://api-web.nhle.com/v1/standings/2023-04-14", "NHL_Team_Stats_2022_23.json")
#process_teams("NHL_Team_Stats_2022_23.json")


add_season_file("https://api-web.nhle.com/v1/standings/2022-04-30", "NHL_Team_Stats_2023_24.json")
#process_teams("NHL_Team_Stats_2023_24.json")







    



