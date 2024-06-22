import requests
import json
import pandas as pd


def add_playoffs_file(url_year, file_name):

    url = url_year


    payload = ""
    headers = {"User-Agent": "insomnia/9.1.1"}

    response = requests.request("GET", url, data=payload, headers=headers)

    #print(response.text)
    with open(file_name, 'w') as playoff: #opens a file, and allows writing of data
        playoff.write(response.text) #writes to the file 
        playoff.close() #closes the file
    #print(response.text)
#def process_prev_playoffs(file_name):
   # playoffs_dict = {}
   # playoffs_stack = []
   # with open(file_name, "r") as playoff_team:
    #    playoff_team_data = json.load(playoff_team)
    #for season in team_data["standings"]:
       # if season["teamName"]["default"] == "Vegas Golden Knights":
       #     won_lord_stanley = True
       # else:
       #     won_lord_stanley = False
        
        #hockey_dict[season["teamName"]["default"]] = {"points": season["points"], "wins" : season["wins"], "losses": season["losses"], "otLosses" : season["otLosses"], "goalsFor": season["goalFor"], "goalsAgainst": season["goalAgainst"], "winPercentage": season["winPctg"], "stanleyCupChamp": won_lord_stanley}

    #return hockey_dict



"""
Opens a file and reads the data.
"""
def process_and_fetch_stanley_cup_playoff_data(file_name):
    
    with open(file_name, "r") as playoff_team:
            playoff_team_data = json.load(playoff_team)
    #print(playoff_team_data)
    


    #abbreviations and team names
    full_team_names = {
        "ANA": "Anaheim Ducks",
        "BOS": "Boston Bruins",
        "BUF": "Buffalo Sabres",
        "CAR": "Carolina Hurricanes",
        "CBJ": "Columbus Blue Jackets",
        "CGY": "Calgary Flames",
        "CHI": "Chicago Blackhawks",
        "COL": "Colorado Avalanche",
        "DAL": "Dallas Stars",
        "DET": "Detroit Red Wings",
        "EDM": "Edmonton Oilers",
        "FLA": "Florida Panthers",
        "LAK": "Los Angeles Kings",
        "MIN": "Minnesota Wild",
        "MTL": "Montreal Canadiens",
        "NJD": "New Jersey Devils",
        "NSH": "Nashville Predators",
        "NYI": "New York Islanders",
        "NYR": "New York Rangers",
        "OTT": "Ottawa Senators",
        "PHI": "Philadelphia Flyers",
        "PIT": "Pittsburgh Penguins",
        "SEA": "Seattle Kraken",
        "SJS": "San Jose Sharks",
        "STL": "St. Louis Blues",
        "TBL": "Tampa Bay Lightning",
        "TOR": "Toronto Maple Leafs",
        "UTA": "Utah NHL team",
        "VAN": "Vancouver Canucks",
        "VGK": "Vegas Golden Knights",
        "WPG": "Winnipeg Jets",
        "WSH": "Washington Capitals" 
        }

    playoff_dict = {} #holds data of playoff games and teams
    series_end_num = 4 #number of wins needed to win a series



    

    
    for series in playoff_team_data["rounds"]: #for each series within each round in the playoffs
        
        #print(series["roundNumber"])
        for team in series["series"]: #for each (or either) team in the series
        
            top_team_abbrev = team["topSeed"]["abbrev"] #set the top seeded team abbreviation to the top seeded value
            bottom_team_abbrev = team["bottomSeed"]["abbrev"] #set the lower seeded team abbreviation to the lower seeded value

            top_team_name = full_team_names[top_team_abbrev] #sets the top seeded team name to the full name of the team thru the full team name dictionary
            bottom_team_name = full_team_names[bottom_team_abbrev] #sets the lower seeded team name to the full name of the team thru the full team name dictionary

            # Initialize the dictionary for each team if not already present
            if top_team_name not in playoff_dict:
                playoff_dict[top_team_name] = {"wins": 0, "rounds_won": 0, "Stanley Cup Champion": "NO"}
            if bottom_team_name not in playoff_dict:
                playoff_dict[bottom_team_name] = {"wins": 0, "rounds_won": 0, "Stanley Cup Champion": "NO"}
            

            # Update wins
            playoff_dict[top_team_name]["wins"] += team["topSeed"]["wins"]
            playoff_dict[bottom_team_name]["wins"] += team["bottomSeed"]["wins"]

            # Update rounds won for the winner
            if team["topSeed"]["wins"] == series_end_num:
                playoff_dict[top_team_name]["rounds_won"] += 1
            elif team["bottomSeed"]["wins"] == series_end_num:
                playoff_dict[bottom_team_name]["rounds_won"] += 1
            
            #sets team as stanley cup champions if the total number of wins is 16, regardless of seeding
           
            
                
            if playoff_dict[top_team_name]["wins"]== 16:
                playoff_dict[top_team_name]["Stanley Cup Champion"] = "YES" 
                            
            elif playoff_dict[bottom_team_name]["wins"] == 16:
                playoff_dict[bottom_team_name]["Stanley Cup Champion"] = "YES"

            elif playoff_dict[top_team_name]["wins"] != 16:
                playoff_dict[top_team_name]["Stanley Cup Champion"] = "NO"

            elif playoff_dict[bottom_team_name]["wins"] != 16:
                playoff_dict[bottom_team_name]["Stanley Cup Champion"] = "NO"

           

       
    return playoff_dict
    

add_playoffs_file("https://api-web.nhle.com/v1/playoff-series/carousel/20232024/", "Playoff_Stats_2023_24.json")

add_playoffs_file("https://api-web.nhle.com/v1/playoff-series/carousel/20222023/", "Playoff_Stats_2022_23.json")



add_playoffs_file("https://api-web.nhle.com/v1/playoff-series/carousel/20212022/", "Playoff_Stats_2021_22.json")




"""
test = "https://api-web.nhle.com/v1/playoff-series/carousel/20212022/"
final = []
for i in range(len(test)):
    final.append(test[i])
playoff_year = " ".join(final[52:-1])
#print(final[52:-1])
print(playoff_year)
"""