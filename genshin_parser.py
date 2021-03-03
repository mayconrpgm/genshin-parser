# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from character_info import *


__HEADER = 'name, element, weapon type, lv, base hp, base atk, base def, elemental mastery, crit rate, crit dmg, atk %, def %, hp %, phys dmg %, elem dmg %, healing bonus\n'


def get_data_for_character(character):
    base_url = "https://genshin.honeyhunterworld.com/"
    character_path = "db/char/"
    img_path = "img/char/"
    char_stats_url = base_url + character_path + character
    char_img_url = base_url + img_path + character

    req = requests.get(char_stats_url)
    soup = BeautifulSoup(req.content, 'html.parser')

    live_data = soup.find(id="live_data")  # ignores content from beta version

    character_weapon_type = live_data.find(
        'td', text='Weapon Type').next_sibling.find('a').text
    character_element = parse_character_element(live_data.find(
        'td', text='Element').next_sibling.find('img')['src'])

    character_stats = parse_character_level_stats(
        live_data.find(id="scroll_stat").next_sibling)

    character = Character(character, character_element,
                          character_weapon_type, char_img_url, character_stats)

    print(__HEADER)
    print(character)

    return character


def parse_character_element(element_image_path):
    element_image_path = element_image_path.lower()

    if 'pyro' in element_image_path:
        return 'pyro'
    elif 'hydro' in element_image_path:
        return 'hydro'
    elif 'cryo' in element_image_path:
        return 'cryo'
    elif 'electro' in element_image_path:
        return 'electro'
    elif 'anemo' in element_image_path:
        return 'anemo'
    elif 'geo' in element_image_path:
        return 'geo'


def parse_character_level_stats(stats_table):
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

                stats[normalize_stat_name(item)] = cols[i].text.strip()
                i += 1

            character_stats.append(CharacterLevelInfo(stats))

    return character_stats


def normalize_stat_name(stat_name):
    stat_name = stat_name.lower()

    if stat_name == 'crit rate%':
        stat_name = 'crit rate'
    elif stat_name == 'crit dmg%':
        stat_name = 'crit dmg'

    return stat_name


def main():
    characters = ['diluc', 'razor', 'xiangling']

    with open('character_level_info.csv', 'w') as writer:
        writer.write(__HEADER)

        for character in characters:
            character_data = get_data_for_character(character)
            
            writer.write(character_data.to_csv_format())



if __name__ == '__main__':
    main()
