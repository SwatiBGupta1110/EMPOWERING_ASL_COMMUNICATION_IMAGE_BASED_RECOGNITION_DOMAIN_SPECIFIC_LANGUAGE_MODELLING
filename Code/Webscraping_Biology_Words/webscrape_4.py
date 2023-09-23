import requests
from bs4 import BeautifulSoup
import pandas as pd

with open("Biology_Word_Glossary\\Understanding_difficult_biology_words.html", "r", encoding="utf-8") as f:
    html_doc = f.read()

data =  []

soup = BeautifulSoup(html_doc, "html.parser")
# print(soup.prettify()) 

for span in soup.findAll(class_="mntl-sc-block-subheading__text"):
    # print(span.get_text())
    data.append([span.get_text()])

csv_file = 'Understanding_difficult_biology_words.csv'
columns = ['Biology_Words']
df = pd.DataFrame(data, columns=columns)
df.to_csv(csv_file, index=False)
print("Data saved to", csv_file)