import os
import re

def rename_items_in_directory(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):  # Обрабатываем файлы снизу вверх
        # Переименовываем папки
        for dirname in dirnames:
            new_name = rename_if_needed(dirname)
            if new_name and new_name != dirname:
                old_path = os.path.join(dirpath, dirname)
                new_path = os.path.join(dirpath, new_name)
                os.rename(old_path, new_path)
                print(f'Renamed directory: "{dirname}" -> "{new_name}"')

        # Переименовываем файлы
        for filename in filenames:
            new_name = rename_if_needed(filename)
            if new_name and new_name != filename:
                old_path = os.path.join(dirpath, filename)
                new_path = os.path.join(dirpath, new_name)
                os.rename(old_path, new_path)
                print(f'Renamed file: "{filename}" -> "{new_name}"')

def rename_if_needed(name):
    """ Добавляет ноль перед однозначными числами в начале имени """
    match = re.match(r'^(\d)(\D.*)?$', name)  # Ищем одиночную цифру в начале
    if match:
        return f'0{match.group(1)}{match.group(2) or ""}'
    return name  # Если изменений не требуется, возвращаем исходное имя

# Укажите путь к корневой папке
root_directory = "./data"
rename_items_in_directory(root_directory)