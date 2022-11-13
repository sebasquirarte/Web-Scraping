# Webscrapping program
# Based on YT video by Errodringer (2018) | https://www.youtube.com/watch?v=rhnMvvmfBFI&ab_channel=Errodringer
# Sebastian Quirarte | sebastianquirajus@gmail.com | 12 Nov 22

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

# TEAMS #

teams_html = soup.find_all('span', class_='nombre-equipo')

teams = list()
count = 0
for team in teams_html:
    # Checks that teams don't repeat
    if count < 20:
        teams.append(team.text)
    count += 1

#print(teams, len(teams))

# POINTS #

points_html = soup.find_all('td', class_='destacado')

points = list()
count = 0
for point in points_html:
    # Checks that points don't repeat
    if count < 20:
        points.append(point.text)
    count += 1

#print(points, len(points))

# DATAFRAME #

df = pd.DataFrame({'Team': teams, 'Points': points}, index = list(range(1,21)))
print(df)

df.to_csv('Clasficación.csv', index = False)
