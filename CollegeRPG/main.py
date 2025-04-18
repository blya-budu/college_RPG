import sys
import time
import ascii_magic
import os
import json
from library_quest import *

sraka = ascii_magic.from_image("art/sraka2.jpg")
dinero = ascii_magic.from_image("art/din.jpg")
nikita_static = ascii_magic.from_image("art/nikita_s.jpg")
nikita_good = ascii_magic.from_image("art/nikita_good.jpg")
babaev = ascii_magic.from_image("art/babaev.jpg")
room = ascii_magic.from_image("art/room.jpg")

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
                wall_of_slave()
                clear_console()
            case 3:
                break

def prologue():
    sraka.to_terminal(columns=150)
    str_welcome = """
            Привет вы попали в Рыбинский Авиационный коледж, это место полно тайных знаний, которые вы можете получить только у нас.
            Все другие коледжы по сравнению с нашим, так скажем не рентабельные, но как только вы получите силу диплома, вы познайте всю мощь.
            Надеюсь вы готовы вступить к нам и для начало, готовы ли вы вступить в наш колледж?
            """
    printR(str_welcome)
    if chosen_option(["Я ГОТОВ!!!", "Не я в полиграф в карты играть"]) == 1:
        clear_console()
        dinero.to_terminal(columns=100)
        printR("ТЫ ПОЖАЛЕЕШЬ ОБ ЭТОМ", 0.3)
        print("Получено достижение!")
        printR("...", 1)
        lose()
        return
    printR(r + "Тогда добро пожаловать, вы точно не разочируйтесь (зловещий смех)", 0.03)
    press_to_continue()
    clear_console()
    for i in range(len(achievement_data['prologue'])):
        nikita_static.to_terminal(columns=100)
        printR(achievement_data['prologue'][i]['question'])
        index = chosen_option(achievement_data['prologue'][i]['answers'])
        printR(achievement_data['prologue'][i]['replies'][index])
        press_to_continue()
        clear_console()

def lose():
    printR("ИГРА ОКОНЧЕНА", 0.3)
    return chosen_option(["Начать с последней контрольной точки", "Вернуться в главное меню"])

def home():
    room.to_terminal(columns=100)



menu()

