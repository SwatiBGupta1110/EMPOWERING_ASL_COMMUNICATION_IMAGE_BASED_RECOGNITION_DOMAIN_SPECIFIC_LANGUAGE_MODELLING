import requests
from bs4 import BeautifulSoup
import pandas as pd

with open("Biology_Word_Glossary\\Complete_list_biology_terms_Biology_Dictionary.html", "r", encoding="utf-8") as f:
    html_doc = f.read()

data =  []

soup = BeautifulSoup(html_doc, "html.parser")
# print(soup.prettify()) 

for link in soup.findAll(class_="wpg-list-item-title"):
    # print(link.get_text())
    data.append([link.get_text()])

csv_file = 'Complete_list_biology_terms_Biology_Dictionary.csv'
columns = ['Biology_Words']
df = pd.DataFrame(data, columns=columns)
df.to_csv(csv_file, index=False)
print("Data saved to", csv_file)