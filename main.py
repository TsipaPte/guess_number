"Главный файл - точка входа в приложение"

import click
import functions

def main() -> None:
    """Функция запускающая главную логику"""
    
    functions.run()

    click.pause("Нажмите любую клавишу для выхода ...")

if __name__ == "__main__":
    main()
