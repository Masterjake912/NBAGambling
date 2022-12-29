import pandas
import requests
from bs4 import BeautifulSoup

# Only gets starters lineup
url = "https://www.rotowire.com/basketball/nba-lineups.php"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

#print(soup)

lineups = soup.find_all(class_='is-pct-play-100')
positions = [x.find('div').text for x in lineups]
names = [x.find('a')['title'] for x in lineups]
teams = sum([[x.text] * 5 for x in soup.find_all(class_='lineup__abbr')], [])

df = pandas.DataFrame(zip(names, teams, positions))
#print(df.to_string())


# Trying to get all players (starters and bench)
url = "https://rotogrinders.com/lineups/nba"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

print(soup)

#lineups = soup.find_all()
