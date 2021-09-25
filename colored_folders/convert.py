#!/usr/bin/python3

from os import listdir
from os.path import isfile, join

original_dir = "original"

green = {
    "#005ae1": "#64bd97",
    "#228be6": "#22dfe6",
    "#005ae1": "#64bd97",
    "#228be6": "#22dfe6",
    "#005ae1": "#64bd97",
    "#228be6": "#22dfe6",
    "#5e4aa6": "#477d7f",
    "#000000": "#1f5357"
}

purple = {
    "#005ae1": "#930077",
    "#228be6": "#7622e6",
    "#005ae1": "#930077",
    "#228be6": "#7622e6",
    "#005ae1": "#930077",
    "#228be6": "#7622e6",
    "#5e4aa6": "#3a0088",
    "#000000": "#e61c5d"
}

red = {
    "#005ae1": "#cb3b3b",
    "#228be6": "#e62256",
    "#005ae1": "#cb3b3b",
    "#228be6": "#e62256",
    "#005ae1": "#cb3b3b",
    "#228be6": "#e62256",
    "#5e4aa6": "#85203b",
    "#000000": "#e0c45c"
}

yellow = {
    "#005ae1": "#fff600",
    "#228be6": "#ffe343",
    "#005ae1": "#fff600",
    "#228be6": "#ffe343"
}

orange = {
    "#005ae1": "#ffc074",
    "#228be6": "#ffce36",
    "#005ae1": "#ffc074",
    "#228be6": "#ffce36"
}

pink = {
    "#005ae1": "#ff4fbc",
    "#228be6": "#ffabf3",
    "#005ae1": "#ff4fbc",
    "#228be6": "#ffabf3"
}

grey = {
    "#005ae1": "#565656",
    "#228be6": "#767fad",
    "#005ae1": "#565656",
    "#228be6": "#767fad"
}

aqua = {
    "#005ae1": "#00bce1",
    "#228be6": "#a4d7e1",
    "#005ae1": "#00bce1",
    "#228be6": "#a4d7e1"
}

color_mapping = {
    "green": green,
    "purple": purple,
    "red": red,
    "yellow": yellow,
    "orange": orange,
    "pink": pink,
    "grey": grey,
    "aqua": aqua
}

def change_color(blue_folder: str, color: str) -> str:
    mapping = color_mapping[color]
    color_folder = blue_folder
    for key, value in mapping.items():
        color_folder = color_folder.replace(key, value)
    return color_folder

def convert(color: str):
    with open('template.svg', 'r') as file:
        blue_folder = file.read()
    template = change_color(blue_folder, color)
    original_icons = [f for f in listdir(original_dir) if isfile(join(original_dir, f))]
    for icon in original_icons:
        with open(join(original_dir, icon), 'r') as file:
            txt = file.read()
            green_svg = txt.replace(blue_folder, template)
            with open("icons/" + color + "-" + icon, "w") as text_file:
                text_file.write(green_svg)

    with open('folder-open.svg', 'r') as file:
        folder_open = file.read()
        colored_folder_open = change_color(folder_open, color)
        with open("icons/" + color + "-folder-open.svg", "w") as text_file:
            text_file.write(colored_folder_open)

for color in color_mapping:
    convert(color)
