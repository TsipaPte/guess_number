"Файл хранящий основной код программы"

import random
import colorama

colorama.init(autoreset=True)

# Инициализируем переменные

HINT = colorama.Fore.BLUE
RED = colorama.Fore.RED
GREEN = colorama.Fore.CYAN
MAGENTA = colorama.Fore.MAGENTA
YELLOW = colorama.Fore.YELLOW

def run():
    """Запуск главного меню и создание игры
    
    :return: Функция ничего не возвращает
    :rtype: None
    """

    print("Добро пожаловать в угадыватель чисел!")
    print("Начните играть и настройте его под себя!")
    print("=" * 55)
    print(MAGENTA + "Version 1.0.1 Release")

    try:
        number_of_games = int(input(HINT + "Введите количество желаемых игр: "))
    except ValueError:
        print(RED + "Неизвестное число. Выбрано: 1")

        number_of_games = 1

    current_game_number = 0

    for _ in range(number_of_games):
        try:
            first_num = int(input(HINT + "Введите первое число. Загадать число от "))
            second_num = int(input(HINT + "Введите второе число. До "))
        except ValueError:
            print(RED + "Введены неправильные данные. Выставлены средние настройки (от 20 до 500)")

            current_game_number += 1
            start_game(20, 500, (current_game_number, number_of_games))
        else:
            current_game_number += 1
            start_game(first_num, second_num, (current_game_number, number_of_games))

def start_game(first_int: int, second_int: int, games_data: tuple) -> None:
    """Функция хранящая логику игры: угадывание числа
    
    :param first_int: Начало диапазона
    :type first_int: int
    :param second_int: Конец диапазона (включительно)
    :type second_int: int
    :return: Функция ничего не возвращает
    :rtype: None
    :raises ValueError: исключение, возникающие при попытке пользователя ввести не число, отлавливается через try/except
    """

    print(f"[Игра №{games_data[0]}/{games_data[1]}] Начата игра (от {first_int} до {second_int} включительно)")

    guessed_number = random.randint(first_int, second_int)
    attempts = 0

    while True:
        attempts += 1

        while True:
            try:
                user_guess = int(input(MAGENTA + f"[Попытка №{attempts}] Введите вашу догадку: "))
            except ValueError:
                print(RED + "Введите число!")
            else:
                break

        if user_guess > guessed_number:
            print(RED + f"Загаданное число ниже вашего ({user_guess})")
        elif user_guess < guessed_number:
            print(GREEN + f"Загаданное число выше вашего ({user_guess})")
        else:
            print(YELLOW + f"Вы выиграли за {attempts} попыток!")

            break
