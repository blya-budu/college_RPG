from colorama import init
import sys
import keyboard
import time
import ascii_magic
import os
import json
from PIL import Image
init()


with open('achievements.json', 'r', encoding='utf-8') as f:
    achievement_data = json.load(f)



def chosen_option(chosen: list):
    position = 0

    while True:

        for i in range(len(chosen)):
            if i == position:
                print(">", end = "")
            print(chosen[i])

        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                break

        if event.name == 'up' and position > 0:
            position -= 1
        elif event.name == 'down' and position < len(chosen) - 1:
            position += 1
        for _ in range(len(chosen)):
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
        if event.name == 'enter':
            break
    return position

def wall_of_slave():
    img = Image.open("art/unknow.jpg")
    img = img.resize((90, 160))
    achievements_post = ascii_magic.from_pillow_image(img)
    position = 0

    while True:
        if position != len(achievement_data['all']) - 1:
            if achievement_data['all'][position]['check']:
                img = Image.open(achievement_data['all'][position]['path'])
                img = img.resize((90, 160))
                achievements_post = ascii_magic.from_pillow_image(img)
            else:
                img = Image.open("art/unknow.jpg")
                img = img.resize((90, 160))
                achievements_post = ascii_magic.from_pillow_image(img)
        achievements_post.to_terminal(columns=60)
        for i in range(len(achievement_data['all'])):
            if i == len(achievement_data['all']) - 1:
                print("\n\n")
            if i == position:
                print(">", end = "")
            if achievement_data['all'][i]['check']:
                print(achievement_data['all'][i]['name'])
            else:
                print('...')

        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                break

        if event.name == 'up' and position > 0:
            position -= 1
        elif event.name == 'down' and position < len(achievement_data['all']) - 1:
            position += 1
        clear_console()
        if event.name == 'enter' and position == len(achievement_data['all']) - 1:
            break



def printR(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def press_to_continue():
    event = keyboard.read_event(suppress=True)