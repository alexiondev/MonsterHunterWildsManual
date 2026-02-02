#!/usr/bin/env python3

ITEMS_FILE_PATH = "mhwilds_roulette/data/items.json"
ITEMS_FILE_HEADER = """{
    "$schema": "https://github.com/ManualForArchipelago/Manual/raw/main/schemas/Manual.items.schema.json",
    "data": ["""
ITEMS_FILE_FOOTER = """\t]
}"""

LOCATIONS_FILE_PATH = "mhwilds_roulette/data/locations.json"
LOCATIONS_FILE_HEADER = """{
	"$schema": "https://github.com/ManualForArchipelago/Manual/raw/main/schemas/Manual.locations.schema.json",
    "data": ["""
LOCATIONS_FILE_FOOTER = """\t]
}"""

REGIONS_FILE_PATH = "mhwilds_roulette/data/regions.json"
REGIONS_FILE_HEADER = """{
    "$schema": "https://github.com/ManualForArchipelago/Manual/raw/main/schemas/Manual.regions.schema.json",
"""
REGIONS_FILE_FOOTER = """}"""

MAPS = [
    "Windward Plains",
    "Scarlet Forest",
    "Oilwell Basin",
    "Iceshard Cliffs",
    "Ruins of Wyveria",
    "Wounded Hollow",
]

MONSTERS = [
    "Ajarakan",
    "Arkveld",
    "Balahara",
    "Blangonga",
    "Chatacabra",
    "Congalala",
    "Doshaguma",
    "G. Doshaguma",
    "G. Ebony Odogaron",
    "G. Fulgur Anjanath",
    "G. Rathalos",
    "Gogmazios",
    "Gore Magala",
    "Gravios",
    "Gypceros",
    "Hirabami",
    "Jin Dahaad",
    "Lagiacrus",
    "Lala Barina",
    "Mizutsune",
    "Nerscylla",
    "Nu Udra",
    "Omega Planetes",
    "Quematrice",
    "Rathalos",
    "Rathian",
    "Rey Dau",
    "Rompopolo",
    "Seregios",
    "Uth Duna",
    "Xu Wu",
    "Yian Kut-Ku",
    "Zoh Shia",
]

WEAPONS = [
    "Great Sword",
    "Long Sword",
    "Sword and Shield",
    "Dual Blades",
    "Hammer",
    "Hunting Horn",
    "Lance",
    "Gunlance",
    "Switch Axe",
    "Charge Blade",
    "Insect Glaive",
    "Light Bowgun",
    "Heavy Bowgun",
    "Bow",
]

ELEMENTS = [
    "Fire",
    "Water",
    "Thunder",
    "Ice",
    "Dragon",
    "Raw",
]

MONSTER_PER_MAP = {
    "Windward Plains": {
        "Arkveld",
        "Balahara",
        "Chatacabra",
        "Doshaguma",
        "Gypceros",
        "Quematrice",
        "Rathian",
        "Rey Dau",
        "Seregios",
    },
    "Scarlet Forest": {
        "Arkveld",
        "Congalala",
        "Doshaguma",
        "Lagiacrus",
        "Lala Barina",
        "Mizutsune",
        "Rathian",
        "Rathalos",
        "Uth Duna",
        "Yian Kut-Ku",
    },
    "Oilwell Basin": {
        "Ajarakan",
        "Arkveld",
        "Gogmazios",
        "Gravios",
        "Gypceros",
        "Nerscylla",
        "Nu Udra",
        "Rathian",
        "Rathalos",
        "Rompopolo",
    },
    "Iceshard Cliffs": {
        "Arkveld",
        "Blangonga",
        "Gore Magala",
        "Gypceros",
        "Hirabami",
        "Jin Dahaad",
        "Nerscylla",
        "Omega Planetes",
        "Yian Kut-Ku",
    },
    "Ruins of Wyveria": {
       "Ajarakan",
       "Arkveld",
       "Congalala",
       "Doshaguma",
       "G. Doshaguma",
       "Gore Magala",
       "Gravios",
       "G. Ebony Odogaron",
       "G. Fulgur Anjanath",
       "Gypceros",
       "Hirabami",
       "Lala Barina",
       "Mizutsune",
       "Nerscylla",
       "Quematrice",
       "Rathalos",
       "G. Rathalos",
       "Seregios",
       "Xu Wu",
       "Zoh Shia",
    },
    "Wounded Hollow": {
        "Ajarakan",
        "Arkveld",
        "Balahara",
        "Blangonga",
        "Chatacabra",
        "Congalala",
        "Doshaguma",
        "Gore Magala",
        "Gravios",
        "Gypceros",
        "Hirabami",
        "Lagiacrus",
        "Lala Barina",
        "Mizutsune",
        "Nerscylla",
        "Nu Udra",
        "Quematrice",
        "Rathalos",
        "Rathian",
        "Rey Dau",
        "Rompopolo",
        "Seregios",
        "Xu Wu",
        "Yian Kut-Ku",
    },
}

def access_pass(map_name):
    return f'{map_name} Access'

def permit(monster):
    return f'{monster} Permit'

def weapon_element(weapon, element):
    return f'{weapon} {element}'

def generate_items():
    output = [ITEMS_FILE_HEADER]

    for map_name in MAPS:
        output.append("\t\t{")
        output.append(f'\t\t\t"name": "{access_pass(map_name)}",')
        output.append(f'\t\t\t"progression": true,')
        output.append(f'\t\t\t"count": 1,')
        output.append(f'\t\t\t"category": ["Map"]')
        output.append("\t\t},")

    for monster in MONSTERS:
        output.append("\t\t{")
        output.append(f'\t\t\t"name": "{permit(monster)}",')
        output.append(f'\t\t\t"progression": true,')
        output.append(f'\t\t\t"count": 1,')
        output.append(f'\t\t\t"category": ["Monster"]')
        output.append("\t\t},")
    
    for weapon in WEAPONS:
        for element in ELEMENTS:
            output.append("\t\t{")
            output.append(f'\t\t\t"name": "{weapon_element(weapon, element)}",')
            output.append(f'\t\t\t"progression": true,')
            output.append(f'\t\t\t"count": 1,')
            output.append(f'\t\t\t"category": ["Weapon"]')
            output.append("\t\t},")

    output[-1] = output[-1].replace(",", "")
    output.append(ITEMS_FILE_FOOTER)
    with open(ITEMS_FILE_PATH, "w") as items_file:
        items_file.write("\n".join(output))


def generate_locations():
    output = [LOCATIONS_FILE_HEADER]

    for weapon in WEAPONS:
        elements = [f'|{weapon_element(weapon, element)}|' for element in ELEMENTS]

        for monster in MONSTERS:
            zones = [f'|{access_pass(zone)}|' for zone in MONSTER_PER_MAP if monster in MONSTER_PER_MAP[zone]]
            output.append("\t\t{")
            output.append(f'\t\t\t"name": "{monster} - {weapon}",')
            output.append(f'\t\t\t"requires": "|{permit(monster)}| and ({" or ".join(elements)}) and ({" or ".join(zones)})"')
            output.append("\t\t},")


    output[-1] = output[-1].replace(",", "")
    output.append(LOCATIONS_FILE_FOOTER)
    with open(LOCATIONS_FILE_PATH, "w") as locations_file:
        locations_file.write("\n".join(output))

if __name__ == "__main__":
    generate_items()
    generate_locations()