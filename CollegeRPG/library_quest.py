from colorama import init
import sys
import keyboard
import time
import ascii_magic
import os
import json
init()


with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)



def chosen_option(chosen: list):
    position = 0

    while True:

        for i in range(len(chosen)):
            if i == position:
                print(">", end = "")
            print(chosen[i])

        while True:
            event = keyboard.read_event(suppress=True)
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

def wall_of_slave(chosen: list):
    position = 0

    while True:

        for i in range(len(chosen)):
            if i == position:
                print(">", end = "")
            print(chosen[i]['name'])

        while True:
            event = keyboard.read_event(suppress=True)
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