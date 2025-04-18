import sys
import time
import ascii_magic

def printR(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def while_to_dialog(questions, count_good, count_bad, count_abc):
    for q in questions:
            while True:  
                printR(q["question"])
                for i, ans in enumerate(q["answers"], 1):
                    print(f"{i} - {ans}")
                choice = input("Ваш ответ: ")
                if choice in ['1', '2', '3']:
                    idx = int(choice) - 1
                    printR(q["replies"][idx])
                    match q["counts"][idx]:
                        case 1:
                            count_good += 1
                        
                        case 2:
                            count_bad += 1
                            
                        case 3:
                            count_abc += 1
                            
                    break  
                else:
                    return print("❌ Введи только 1, 2 или 3. Попробуй ещё раз.")
    return count_good, count_bad, count_abc

count_bad = 0 
count_good = 0 
count_abc = 0

sraka = ascii_magic.from_image_file("art/sraka2.jpg", columns=150)
dinero = ascii_magic.from_image_file("art/din.jpg", columns=100)
nikita_static = ascii_magic.from_image_file("art/nikita_s.jpg", columns=100)
nikita_good = ascii_magic.from_image_file("art/nikita_good.jpg", columns=100)
babaev = ascii_magic.from_image_file("art/babaev.jpg", columns=100)

achievements = []

# menu
menu = """
  Главное меню
1 - Начать игру
2 - Посмотреть достижение
3 - выход
"""
r = '       '
questions = [
    # 1
    {
        "question": "Привет, меня зовут Мистер Н, как тебе это место?",
        "answers": [
            "Не очень, здесь противно",
            "Мне все нравится, побыстрее бы приступить к учебе",
            "А ты как думаешь?"
        ],
        "replies": [
            "Слушай меня тоже это место смущает, выглядит все очень потрепано",
            "... Ну да ... Типо мне тоже",
            "Честно даже не знаю, думаю скорее всего это ничем хорошим не закончится"
        ],
        "counts": [1, 2, 3]  # можно: 1 - good, 2 - bad, 3 - abc
    },
    #2
    {
        "question": "\nЧто расскажешь про себя, кто ты и как оказался здесь?",
        "answers": [
            "Меня зовут ??? честно даже не знал куда мне податся, попал сюда по случайности (правда)",
            "Меня зовут ??? я давно хотел попасть в этот коледж (ложь)",
            "Я не хочу раскрывать свое имя"
        ],
        "replies": [
            "Я тоже попал случайности, мой отец здесь работал какое-то время, так получилось что и квартира есть",
            "Ого, неожиданно. Но а я, куда сказали туда и пошел",
            "Окей..."
        ],
        "counts": [1, 2, 3]  # можно: 1 - good, 2 - bad, 3 - abc
    },
    {
        "question": "\nВообщем я рад с тобой познокомится, было приятно пообщатся",
        "answers": [
            "И мне тоже",
            "Да... как скажешь",
            "Все лучше чем тухнуть здесь одному"
        ],
        "replies": [
            "Супер! Пойду прогуляюсь",
            "Пожалуй я пойду",
            "И не говори"
        ],
        "counts": [1, 2, 3]  # можно: 1 - good, 2 - bad, 3 - abc
    },
    
]

while True:
    print(menu)
    inp = input("Ваш ответ: ")
    # game
    if (inp == '1'):
        ascii_magic.to_terminal(sraka)
        str_welcome = """
        Привет вы попали в Рыбинский Авиационный коледж, это место полно тайных знаний, которые вы можете получить только у нас.
        Все другие коледжы по сравнению с нашим, так скажем не рентабельные, но как только вы получите силу диплома, вы познайте всю мощь.
        Надеюсь вы готовы вступить к нам и для начало, готовы ли вы вступить в наш колледж?
        """

        #введение 
        printR(str_welcome)
        print("Если вы согласны, то введите 1, если нет, то 0")
        inp = input("Ваш ответ: ")

        if (inp == '0'):
            ascii_magic.to_terminal(dinero)
            printR("ТЫ ПОЖАЛЕЕШЬ ОБ ЭТОМ", 0.3)
            achievements.append("Думай головой!")
            print("Получено достижение!")
            printR("...", 1)
            continue

        if (inp == "1"):
            printR(r + "Тогда добро пожаловать, вы точно не разочируйтесь (зловещий смех)", 0.03)

            # Глава первая 1 курс
            printR(r + "ГЛАВА 1. Первый курс", 0.01)

            ascii_magic.to_terminal(nikita_static)
            # основной блок вопрос-ответ
            count_good, count_bad, count_abc = while_to_dialog(questions, count_good, count_bad, count_abc)
            ascii_magic.to_terminal(nikita_good)
            printR("Мистер.Н довольно интересный человек, возможно в будущем он мне поможет в решении моих проблем")
            printR("(услышав неряшливый звук) Я повернулся назад и увидел перед собой некого человека, его туповатый взгляд пристольно наблюдал за мной, пришлось ответить")
            ascii_magic.to_terminal(babaev)
            
                                    




    # achievements
    if (inp == '2'):
        print(f"Ваши достижения {len(achievements)}/10:")
        for i, el in enumerate(achievements):
            print(i+1, " - ", el)

        printR("...", 1)
        continue

    if (inp == '3'):
        break