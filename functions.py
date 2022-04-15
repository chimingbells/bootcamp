import requests
import pandas as pd


def grab_population_data(url):
    """
    This function calls the datausa api endpoint, and returns the response as a dictionary.

    :param url: url is a str representing an api endpoint from datausa
    :return: response: dict containing api response from the given api
    """

    """
       
    hint: 
        resp = request.get(url)
        data = resp.json()
        return data
    """
    # TODO(chimingbells) Write Code Below
    pass


def save_json_to_csv(data, filename):
    """
    Saves a file to csv locally using the given filename.
    :param data: dict object containing data from api endpoint
    :return: None
    """
    """
    hint:
        Don't use repr, instead use the json.dumps() library (you will also need to use str(data)) 
    """
    # TODO(chimingbells) Write Code Below
    pass


def save_dataframe_to_csv(df, filename):
    """
    Saves a pandas dataframe to a csv file locally given the filename.
    :param df: pandas dataframe containing data
    :param filename:  name of the file you want to save the data to.
    :return: None
    """
    # TODO(chimingbells) Write Code Below
    pass


def read_csv_to_dataframe(filename):
    """
    Reads a csv file and returns a pandas dataframe.
    :param filename: str represnting csv file to laod.
    :return: df: dataframe containing data in the csv file
    """
    # TODO(chimingbells) Write Code Below
    pass


if __name__=='__main__':
    print('hi')