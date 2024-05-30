import requests
import pandas as pd
from retry import retry
from requests.exceptions import Timeout

env = input("Which environment are you using? US=1, EU=2, MS=3:\n")

access_token = input("Data admin bearer token:\n")
bearer = "Bearer " + access_token 

wsfile = input("Workstream ID file:\n")
wsfile = wsfile + ".xlsx"
wsdata = pd.read_excel(wsfile)

file_name = input("User ID file:\n")
file = file_name + ".xlsx"
data = pd.read_excel(file)

ids = data["user_id"].to_list()
wsids = wsdata["ws_id"].to_list()

eu_api_url = 'https://www.myworkboard.eu/wb/apis/workstream/'
us_api_url = 'https://www.myworkboard.com/wb/apis/workstream/'

ws_count = 0

@retry()
def call(url,wsid):
    id_count = 0
    print(url + str(wsid))

    for id in ids:
        headers = {
            'Authorization': bearer,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
        }

        json = {
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
            "\tWS ID: ", wsid,
            "\tUser ID: ", id,
            "\t", response
            )
            
for ws_id in wsids:

    if env == "1": call(us_api_url,ws_id)
    elif env == "2": call(eu_api_url,ws_id)
    elif env == "3": call(us_api_url,ws_id)
    else: print("Invalid environment selection. Try again.\n")

    ws_count += 1

    print(
        ws_count, " of ", len(wsids),
        "\t-- ", ws_id
    )



