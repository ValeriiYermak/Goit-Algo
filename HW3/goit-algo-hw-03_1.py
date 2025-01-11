"""
Завдання 1

Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії, переміщає їх до нової директорії та
сортує в піддиректорії, назви яких базуються на розширенні файлів.
Також візьміть до уваги наступні умови:

1. Парсинг аргументів. Скрипт має приймати два аргументи командного рядка: шлях до вихідної директорії та шлях до директорії
призначення (за замовчуванням, якщо тека призначення не була передана, вона повинна бути з назвою dist).

2. Рекурсивне читання директорій:
Має бути написана функція, яка приймає шлях до директорії як аргумент.
Функція має перебирати всі елементи у директорії.
Якщо елемент є директорією, функція повинна викликати саму себе рекурсивно для цієї директорії.
Якщо елемент є файлом, він має бути доступним для копіювання.

3. Копіювання файлів:
Для кожного типу файлів має бути створений новий шлях у вихідній директорії, використовуючи розширення файлу для назви піддиректорії.
Файл з відповідним типом має бути скопійований у відповідну піддиректорію.

4. Обробка винятків. Код має правильно обробляти винятки, наприклад, помилки доступу до файлів або директорій.
"""
import os
import shutil
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Copy and sort files based on their extensions.')
    parser.add_argument('source_dir', type=str, help='Path to the source directory.')
    parser.add_argument('destination_dir', type=str, nargs='?', default='dist',
                        help='Path to the destination directory (default:dist).')
    return parser.parse_args()


def create_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as error:
        print(f'Error creating directory {path}: {error}')
        raise


def copy_and_sort_files(source_dir, destination_dir):
    try:
        for entry in os.scandir(source_dir):
            if entry.is_dir():
                copy_and_sort_files(entry.path, destination_dir)
            elif entry.is_file():
                file_extension = os.path.splitext(entry.name)[1].lower()
                if file_extension:
                    target_dir = os.path.join(destination_dir, file_extension[1:])
                else:
                    target_dir = os.path.join(destination_dir, 'no extension')
                create_directory(target_dir)

                try:
                    shutil.copy2(entry.path, target_dir)
                    print(f'Copied {entry.path} to {target_dir}')
                except IOError as error:
                    print(f'Error copying file {entry.path} to {target_dir}: {error}')
    except Exception as error:
        print(f'Error processing directory {source_dir}: {error}')
        raise


def main():
    args = parse_arguments()
    source_dir = args.source_dir
    destination_dir = args.destination_dir

    if not os.path.exists(source_dir):
        print(f'Source directory {source_dir} does not exist.')
        return
    create_directory(destination_dir)
    copy_and_sort_files(source_dir, destination_dir)


if __name__ == '__main__':
    main()
