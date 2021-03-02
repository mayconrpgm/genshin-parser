# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def get_data_for_character(character):
    base_url = "https://genshin.honeyhunterworld.com/db/char/"
    final_url = base_url + character

    req = requests.get(final_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    
    live_data = soup.find(id="live_data") #ignores content from beta version

    character_stats = parse_character_stats(live_data.find(id="scroll_stat").next_sibling)

    print(character_stats)

    

def parse_character_stats(stats_table):
    first_row = True
    character_stats = []
    header = []
    i = 0

    rows = stats_table.find_all('tr')

    for row in rows:
        if first_row:
            cols = row.find_all('td')
            header = [ele.text.strip() for ele in cols]
            first_row = False
        else:
            i = 0
            stats = {}

            cols = row.find_all('td')
            
            for item in header:
                if item.lower() == "ascension":
                    continue

                stats[item] = cols[i].text.strip()
                i += 1

            character_stats.append(stats)

    return character_stats


def main():
    characters = ['diluc', 'razor', 'xiangling']

    for character in characters:
        get_data_for_character(character)

if __name__ == '__main__':
    main()