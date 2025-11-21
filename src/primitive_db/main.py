#!/usr/bin/env python3
import prompt
from . import engine

def main():
    print("DB project is running!")
    engine.welcome()
    while True:
        match prompt.string("Введите строку: "):
            case 'help':
                engine.welcome()
            case 'exit':
                exit()


if __name__ == "__main__":
    main()
