import requests
import pandas as pd
from retry import retry
from requests.exceptions import Timeout

env = input("Which environment are you using? US=1, EU=2, MS=3:\n")

access_token = input("Data admin bearer token:\n")
bearer = "Bearer " + access_token 

team_id = input("Team ID:\n")

file_name = input("File name:\n")
file = file_name + ".xlsx"
data = pd.read_excel(file).to_dict('records')

us_api_url = "https://www.myworkboard.com/wb/apis/team/"
eu_api_url = "https://www.myworkboard.eu/wb/apis/team/"

@retry()
def call(url):
    dict_size = 0

    for row in data:
        headers = {
            'Authorization': bearer,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
        }

        json = {"team_members": [{"email": row["email"]}]}
        
        try:
            response = requests.put(url + str(team_id), headers=headers, json=json, timeout=15)
        except Timeout:
            print("Timeout has occurred.")

        dict_size += 1
        
        print(
            dict_size, " of ", len(data), 
            "\tEmail: ", row['email'],
            "\t", response
        )

if env == "1": call(us_api_url)   
elif env == "2": call(eu_api_url)
elif env == "3": call(us_api_url)
else: print("Invalid environment. Try again.")