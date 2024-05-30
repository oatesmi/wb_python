import requests
import pandas as pd
from retry import retry
from requests.exceptions import Timeout

env = input("Which environment are you using? US=1, EU=2, MS=3:\n")

access_token = input("Data admin bearer token:\n")
bearer = "Bearer " + access_token 

team_file_name = input("Team ID file:\n")
team_file = team_file_name + ".xlsx"
team_data = pd.read_excel(team_file)

file_name = input("User ID file:\n")
file = file_name + ".xlsx"
data = pd.read_excel(file)

team_list = team_data['team_id'].to_list()
user_list = data['user_id'].to_list()

us_api_url = "https://www.myworkboard.com/wb/apis/team/"
eu_api_url = "https://www.myworkboard.eu/wb/apis/team/"

team_count = 0

@retry()
def call(url,team_id):
    dict_size = 0
    print(url + str(team_id))

    for user in user_list:
        headers = {
            'Authorization': bearer,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
        }

        json = {
            "team_members": [
                {
                    "id": user, 
                    "team_access": "revoke"
                }
            ]
        }
        
        try:
            response = requests.put(url + str(team_id), headers=headers, json=json, timeout=15)
        except:
            print("Timeout error has occurred.")
            
        dict_size += 1
        
        print(
            dict_size, " of ", len(user_list), 
            "\tTeam ID: ", team_id,
            "\tUser ID: ", user,
            "\t", response
        )

for team in team_list:
    
    if env == "1": call(us_api_url,team)   
    elif env == "2": call(eu_api_url)
    elif env == "3": call(us_api_url)
    else: print("Invalid environment. Try again.")

    team_count += 1

    print(
        team_count, " of ", len(team_list),
        "\t-- ", team
    )