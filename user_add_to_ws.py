import requests
import pandas as pd
from retry import retry
from requests.exceptions import Timeout

env = input("Which environment are you using? US=1, EU=2, MS=3:\n")

access_token = input("Data admin bearer token:\n")
bearer = "Bearer " + access_token 

wsid = input("Workstream ID:\n")

file_name = input("File name:\n")
file = file_name + ".xlsx"
data = pd.read_excel(file)

ids = data["user_id"].to_list()

eu_api_url = 'https://www.myworkboard.eu/wb/apis/workstream/'
us_api_url = 'https://www.myworkboard.com/wb/apis/workstream/'

@retry()
def call(url):
    id_count = 0

    for id in ids:
        headers = {
            'Authorization': bearer,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
        }

        json = {
            #"ws_name": wsname,
            "ws_shared_with": [
                {
                "user_id": id
                }
            ]
        }

        try:
            response = requests.put(url + str(wsid), headers=headers, json=json, timeout=15)
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

