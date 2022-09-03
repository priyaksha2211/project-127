from bs4 import BeautifulSoup
import requests
import pandas as pd

startUrl = (
    "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
)
browser = requests.get(startUrl)
soup = BeautifulSoup(browser.text, "html.parser")
temp_list = []
for tr in soup.find("table").find_all("tr"):
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

NAME = []
DISTANCE = []
MASS = []
RADIUS = []

for i in range(1, len(temp_list)):
    NAME.append(temp_list[i][1])
    DISTANCE.append(temp_list[i][3])
    MASS.append(temp_list[i][5])
    RADIUS.append(temp_list[i][6])

df = pd.DataFrame(
    list(zip(NAME, DISTANCE, MASS, RADIUS)),
    columns=["Star_name", "Distance", "Mass", "Radius"],
)
df.to_csv("star_data.csv")