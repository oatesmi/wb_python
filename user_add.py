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

us_api_url = "https://www.myworkboard.com/wb/apis/user"
eu_api_url = "https://www.myworkboard.eu/wb/apis/user"

@retry()
def call(url):
    dict_size = 0

    for row in data:
        headers = {
            'Authorization': bearer,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
        }

        json = {
                    'email':row['email'],
                    'first_name':row['first_name'],
                    'last_name':row['last_name'],
                    'profile':{'title':row['title']}
                }

        try:        
            response = requests.post(url, headers=headers, json=json, timeout=15)
        except Timeout:
            print("Timeout error has occurred.")
                            
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