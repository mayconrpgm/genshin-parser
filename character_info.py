# -*- coding: utf-8 -*-

class CharacterLevelInfo(object):
    level = '1'
    hp = 0
    base_atk = 0
    base_def = 0
    elemental_mastery = 0
    crit_rate = 0.0
    crit_dmg = 0.0
    atk_perc = 0.0
    def_perc = 0.0
    hp_perc = 0.0
    physical_dmg_bonus = 0.0
    elemental_dmg_bonus = 0.0
    healing_bonus = 0.0

    __LEVEL_KEY = 'lv'
    __BASE_HP_KEY = 'base hp'
    __BASE_ATK_KEY = 'base atk'
    __BASE_DEF_KEY = 'base def'
    __ELEMENTAL_MASTERY_KEY = 'elemental mastery'
    __CRIT_RATE_KEY = 'crit rate'
    __CRIT_DMG_KEY = 'crit dmg'
    __ATK_PERC_KEY = 'atk%'
    __DEF_PERC_KEY = 'def%'
    __HP_PERC_KEY = 'hp%'
    __PHYS_DMG_BONUS_KEY = 'phys dmg%'
    __PYRO_DMG_BONUS_KEY = 'pyro dmg%'
    __HYDRO_DMG_BONUS_KEY = 'hydro dmg%'
    __CRYO_DMG_BONUS_KEY = 'cryo dmg%'
    __ELECTRO_DMG_BONUS_KEY = 'electro dmg%'
    __ANEMO_DMG_BONUS_KEY = 'anemo dmg%'
    __GEO_DMG_BONUS_KEY = 'geo dmg%'
    __HEALING_BONUS_PERC_KEY = 'healing bonus%'

    def __init__(self, stats_dict):
        self.level = stats_dict[self.__LEVEL_KEY]
        self.hp = stats_dict[self.__BASE_HP_KEY]
        self.base_atk = stats_dict[self.__BASE_ATK_KEY]
        self.base_def = stats_dict[self.__BASE_DEF_KEY]
        self.elemental_mastery = int(
            stats_dict.get(self.__ELEMENTAL_MASTERY_KEY, '0'))
        self.crit_rate = float(
            stats_dict[self.__CRIT_RATE_KEY].replace('%', ''))
        self.crit_dmg = float(stats_dict[self.__CRIT_DMG_KEY].replace('%', ''))

        self.atk_perc = float(stats_dict.get(
            self.__ATK_PERC_KEY, '0.0').replace('%', ''))
        self.def_perc = float(stats_dict.get(
            self.__DEF_PERC_KEY, '0.0').replace('%', ''))
        self.hp_perc = float(stats_dict.get(
            self.__HP_PERC_KEY, '0.0').replace('%', ''))
        self.physical_dmg_bonus = float(stats_dict.get(
            self.__PHYS_DMG_BONUS_KEY, '0.0').replace('%', ''))

        if self.__PYRO_DMG_BONUS_KEY in stats_dict:
            self.elemental_dmg_bonus = float(
                stats_dict[self.__PYRO_DMG_BONUS_KEY].replace('%', ''))
        elif self.__HYDRO_DMG_BONUS_KEY in stats_dict:
            self.elemental_dmg_bonus = float(
                stats_dict[self.__HYDRO_DMG_BONUS_KEY].replace('%', ''))
        elif self.__CRYO_DMG_BONUS_KEY in stats_dict:
            self.elemental_dmg_bonus = float(
                stats_dict[self.__CRYO_DMG_BONUS_KEY].replace('%', ''))
        elif self.__ELECTRO_DMG_BONUS_KEY in stats_dict:
            self.elemental_dmg_bonus = float(
                stats_dict[self.__ELECTRO_DMG_BONUS_KEY].replace('%', ''))
        elif self.__ANEMO_DMG_BONUS_KEY in stats_dict:
            self.elemental_dmg_bonus = float(
                stats_dict[self.__ANEMO_DMG_BONUS_KEY].replace('%', ''))
        elif self.__GEO_DMG_BONUS_KEY in stats_dict:
            self.elemental_dmg_bonus = float(
                stats_dict[self.__GEO_DMG_BONUS_KEY].replace('%', ''))

        self.healing_bonus = float(stats_dict.get(
            self.__HEALING_BONUS_PERC_KEY, '0.0').replace('%', ''))


class Character(object):
    name = ''
    element = ''
    weapon_type = ''
    level_info = []

    def __init__(self, character_name, element, weapon_type, portrait_image_url, character_level_info: CharacterLevelInfo):
        self.name = character_name
        self.element = element
        self.weapon_type = weapon_type
        self.level_info = character_level_info

    def to_csv_format(self):
        string_reponse = ''

        for info in self.level_info:
            string_reponse += '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n'.format(
                self.name.capitalize(),
                self.element.capitalize(),
                self.weapon_type.capitalize(),
                info.level,
                info.hp,
                info.base_atk,
                info.base_def,
                info.elemental_mastery,
                info.crit_rate,
                info.crit_dmg,
                info.atk_perc,
                info.def_perc,
                info.hp_perc,
                info.physical_dmg_bonus,
                info.elemental_dmg_bonus,
                info.healing_bonus
            )

        return string_reponse

    def __str__(self):
        return self.to_csv_format()
        