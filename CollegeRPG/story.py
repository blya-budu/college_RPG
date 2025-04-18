import sys
import time
import ascii_magic
import os
import json
from library_quest import *

sraka = ascii_magic.from_image_file("art/sraka2.jpg", columns=150)
dinero = ascii_magic.from_image_file("art/din.jpg", columns=100)
nikita_static = ascii_magic.from_image_file("art/nikita_s.jpg", columns=100)
nikita_good = ascii_magic.from_image_file("art/nikita_good.jpg", columns=100)
babaev = ascii_magic.from_image_file("art/babaev.jpg", columns=100)
room = ascii_magic.from_image_file("art/room.jpg", columns=100)
r = '   '

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


def menu():
    while True:
        match chosen_option(["Новая игра", "Продолжить", "Достижения", "Выход"]):
            case 0:
                prologue()
                clear_console()
            case 1:
                print("continue")
            case 2:
                print("achievements")
            case 3:
                break

def prologue():
    ascii_magic.to_terminal(sraka)
    str_welcome = """
            Привет вы попали в Рыбинский Авиационный коледж, это место полно тайных знаний, которые вы можете получить только у нас.
            Все другие коледжы по сравнению с нашим, так скажем не рентабельные, но как только вы получите силу диплома, вы познайте всю мощь.
            Надеюсь вы готовы вступить к нам и для начало, готовы ли вы вступить в наш колледж?
            """
    printR(str_welcome)
    if chosen_option(["Я ГОТОВ!!!", "Не я в полиграф в карты играть"]) == 1:
        clear_console()
        ascii_magic.to_terminal(dinero)
        printR("ТЫ ПОЖАЛЕЕШЬ ОБ ЭТОМ", 0.3)
        print("Получено достижение!")
        printR("...", 1)
        lose()
        return
    printR(r + "Тогда добро пожаловать, вы точно не разочируйтесь (зловещий смех)", 0.03)
    press_to_continue()
    clear_console()
    for i in range(len(data['prologue'])):
        ascii_magic.to_terminal(nikita_static)
        printR(data['prologue'][i]['question'])
        index = chosen_option(data['prologue'][i]['answers'])
        printR(data['prologue'][i]['replies'][index])
        press_to_continue()
        clear_console()

def lose():
    printR("ИГРА ОКОНЧЕНА", 0.3)
    return chosen_option(["Начать с последней контрольной точки", "Вернуться в главное меню"])

def home():
    ascii_magic.to_terminal(room)



menu()

