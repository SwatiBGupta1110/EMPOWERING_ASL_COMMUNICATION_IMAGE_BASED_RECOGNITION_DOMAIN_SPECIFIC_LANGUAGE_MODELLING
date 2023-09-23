import requests
from bs4 import BeautifulSoup
import pandas as pd

with open("Biology_Word_Glossary\\Glossary_Biology_words_Wikipedia.html", "r", encoding="utf-8") as f:
    html_doc = f.read()

data =  []

soup = BeautifulSoup(html_doc, "html.parser")
# print(soup.prettify()) 
# print(soup.dfn)
# print("To get 1st div element",soup.findAll("dfn")[0])

for link in soup.findAll("dfn"):
    # print(link.get_text())
    data.append([link.get_text()])

csv_file = 'Glossary_Biology_words_Wikipedia.csv'
columns = ['Biology_Words']
df = pd.DataFrame(data, columns=columns)
df.to_csv(csv_file, index=False)
print("Data saved to", csv_file)