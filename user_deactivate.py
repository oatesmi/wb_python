import requests
import pandas as pd
from retry import retry
from requests.exceptions import Timeout

env = input("Which environment are you using? US=1, EU=2, MS=3:\n")

access_token = input("Data admin bearer token:\n")
bearer = "Bearer " + access_token 

file_name = input("File name:\n")
file = file_name + ".xlsx"
data = pd.read_excel(file)

ids = data["user_id"].to_list()

eu_api_url = 'https://www.myworkboard.eu/wb/apis/user/'
us_api_url = 'https://www.myworkboard.com/wb/apis/user/'

def call(url):
    id_count = 0

    for id in ids:
        headers = {
            'Authorization': bearer,
        }

        params = {
            'user_id': id,
            'action' : 'disable'
        }

        try:
            response = requests.patch(url, params=params, headers=headers, timeout=15)
        except Timeout:
            print("Timeout error has occurred.")
            
        id_count += 1

        print(
            id_count, " of ", len(ids), 
            "\tUser ID: ", id,
            "\t", response
            )

if env == "1": call(us_api_url)
elif env == "2": call(eu_api_url)
elif env == "3": call(us_api_url)
else: print("Invalid environment selection. Try again.\n")

