import requests
import pandas as pd
import json


def grab_population_data(url = 'https://datausa.io//api//data?drilldowns=Nation&measures=Population'):
    resp = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
    data = resp.json()
    return data

def save_json_to_csv(data, filename):
    json_string = json.dumps(data)
    pythstr = str(json_string)
    return pythstr

def convert_json_to_csv(data, filename):
    json_load = json.load(data)
    json_dump = json.dumps(data)
    pythstr = str(json_string)
    return pythstr

def save_dataframe_to_csv(df,filename):
    df = pd.DataFrame(grab_population_data(url = 'https://datausa.io//api//data?drilldowns=Nation&measures=Population'))

    df.to_csv('df.csv', index=False)

def read_csv_to_dataframe(filename):



if __name__=='__main_':
    print("hi")