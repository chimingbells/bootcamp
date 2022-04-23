import csv
import json
import requests
import pandas as pd
import pprint as pp

def grab_population_data(url='https://datausa.io//api//data?drilldowns=Nation&measures=Population'):
    """
    This function grabs population date from the datausa.io api.
    :param url: str that represents api endpoint to pull data from.
    :return: data: dict containing api response.
    """
    resp = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
    data = resp.json()
    #  json.dump(data, open('data/population_data.json', 'w'))

    return data

def save_json_to_csv(data, filename):
    """
    Saves data to a csv formatted file.

    :param data: dict object containing data from api endpoint
    :param filename: str representing filename to save to.
    :return: None
    """
    """
    hint:
        Don't use repr, instead use the json.load() and json.dumps() library (you will also need to use str(data))
        
        id_nation,id_year,nation,population,slug_nation,year
        01000US,2018,United States,327167439,united-states,2018
        ...
        
    """

    # Format Dict -> List[Lists] in CSV format.
    csv_data = convert_json_to_csv(data)

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in csv_data:
            writer.writerow(row)



def convert_json_to_csv(api_resp: dict):
    """Takes a dict and formats it into a list of lists to be used with csv.csvwriter"""
    filedata = [
        ['id_nation','id_year','nation','population','slug_nation','year']
    ]

    for d in api_resp['data']:
        row = [d['ID Nation'], d['ID Year'], d['Nation'], d['Population'], d['Slug Nation'], d['Year']]
        filedata.append(row)

    return filedata

#
# def save_df_to_csv(df, filename):
#     return df.to_csv(filename, index=False)
#
#
# def read_csv_to_df(filename):
#     # hint: pd.read_csv()
#     pass


if __name__ == '__main__':
    data = grab_population_data()
    filename = "data/population_data.csv"
    save_json_to_csv(data, filename)
    # Read the filename using pd.read_csv()
    # Then print the contents here

    # Bonus: Add a row the the dataframe before saving.

    # Save the file again, after printing
    # and this time use the pd.DataFrame().to_csv() function (hint: df.to_csv(Filename, index=false))