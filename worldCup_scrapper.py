# Webscrapping program that stores the results of the any soccer World Cup
# Based on YT video by Frank Andrade | https://www.youtube.com/watch?v=XDIscigGpGI&ab_channel=FrankAndrade
# Sebastian Quirarte | sebastianquirajus@gmail.com | 24 Nov 22

from bs4 import BeautifulSoup
import requests
import pandas as pd
from IPython.display import display

years = [1930, 1934, 1938, 1950, 1954, 1958, 1962,
         1966, 1970, 1974, 1978, 1982, 1986, 1990,
         1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022]

def get_matches(year):
    # Gets and parses through website html
    url = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')

    # Finds all matches
    matches = soup.find_all('div', class_ = 'footballbox')

    home = []
    score = []
    away = []

    # Stores home team, score, and away team of every match
    for match in matches:
        home.append(match.find('th', class_ = 'fhome').get_text().strip())
        score.append(match.find('th', class_ = 'fscore').get_text().strip())
        away.append(match.find('th', class_ = 'faway').get_text().strip())

    # Creates dictionary of home teams, scores, and away teams
    dict_worldCup = {'home': home, 'score': score, 'away': away}
    # Creates dataframe
    df_worldCup = pd.DataFrame(dict_worldCup)
    df_worldCup['year'] = year
    return df_worldCup

# Asks user for world cup year and verifies valid year
while True:
    year = input("Year: ")
    if year == "":
        break
    # If year is valid, prints full df on terminal
    if int(year) in years:
        results = get_matches(year)
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(results)
            # Asks user if results of world cup should be saved as csv file
            save_WC = input("\nSave as csv file? (y/n): ")
            if save_WC == "y" or save_WC == "Y":
                # Saves results as csv file
                results.to_csv(f'WorldCupResults_{year}.csv', index = False)
                print("File created.")
            # Asks user if results of ALL world cups should be saved as csv file
            save_allWC = input("Save csv file of ALL world cups? (y/n): ")
            if save_allWC == "y" or save_allWC == "Y":
                allWC = [get_matches(year) for year in years]
                df_allWC = pd.concat(allWC, ignore_index = True)
                df_allWC.to_csv(f'WorldCupResults.csv', index = False)
                print("File created.")
                break
            else:
                break
    else:
        print("Invalid year.")
        print("Valid years: ", years)
