import requests
from bs4 import BeautifulSoup
import pandas as pd

with open("Biology_Word_Glossary\\Biology_terms_Collins.html", "r", encoding="utf-8") as f:
    html_doc = f.read()

data =  []

soup = BeautifulSoup(html_doc, "html.parser")
# print(soup.prettify()) 

for link in soup.findAll(class_="ref"):
    # print(link.get_text())
    data.append([link.get_text()])

csv_file = 'Biology_terms_Collins.csv'
columns = ['Biology_Words']
df = pd.DataFrame(data, columns=columns)
df.to_csv(csv_file, index=False)
print("Data saved to", csv_file)