import requests
import pandas as pd

data = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
datausa = data.text

for key in datausa:
    print(key, end=" ")

with open("C:\\Users\\13173\\PycharmProjects\\bootcamp\\practice.txt", "w") as f:
    mystringdict = repr(datausa)
    f.write(mystringdict)
    f.close()

csvfile = pd.read_csv (r'C:\Users\13173\PycharmProjects\bootcamp\practice.txt')
csvfile.to_csv ('C:\\Users\\13173\\PycharmProjects\\bootcamp\\practice.csv', index=None )