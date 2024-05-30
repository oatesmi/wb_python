import requests
import pandas as pd
from retry import retry
from requests.exceptions import Timeout

env = input("Which environment are you using? US=1, EU=2, MS=3:\n")

access_token = input("Data admin bearer token:\n")
bearer = "Bearer " + access_token 

file_name = input("File name:\n")
file = file_name + ".xlsx"
data = pd.read_excel(file).to_dict('records')

us_api_url = "https://www.myworkboard.com/wb/apis/metric/"
eu_api_url = "https://www.myworkboard.eu/wb/apis/metric/"

@retry()
def call(url):
    dict_size = 0

    for row in data:
        headers = {'Authorization': bearer}
        json = {"metric_data" : row['update_value']}

        try:
            response = requests.put(url + str(row['kr_id']), headers=headers, json=json, timeout=15)
        except Timeout:
            print("Timeout error has occurred.")

        
        print(
            "\tKR ID: ", row['kr_id'],
            "\tUpdate Value: ", row['update_value'],
            "\t", response,
            url + str(row['kr_id'])
        )

if env == "1": call(us_api_url)
elif env == "2": call(eu_api_url)
elif env == "3": call(us_api_url)
else: print("Invalid environment selection. Try again.\n")

