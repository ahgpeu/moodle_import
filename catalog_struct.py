import os

def process_folder(path):
    names = []
    topics = []
    files_dict = {}

    # Перебираем все папки в корневом каталоге
    for folder in sorted(os.listdir(path)):
        if folder.startswith("."):  # Пропускаем скрытые папки
            continue
        folder_path = os.path.join(path, folder)
        if os.path.isdir(folder_path):  # Проверяем, что это папка
            names.append(folder)  # Добавляем в список names

            # Перебираем подпапки
            for subfolder in sorted(os.listdir(folder_path)):
                subfolder_path = os.path.join(folder_path, subfolder)
                if os.path.isdir(subfolder_path):  # Проверяем, что это подпапка
                    topics.append(subfolder)  # Добавляем в список topics

                    # Получаем файлы в подпапке
                    files = sorted(f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f)))
                    files_dict[subfolder] = files  # Записываем файлы в словарь

    return names, topics, files_dict

# Пример использования
path = "./data"
names, topics, files_dict = process_folder(path)

print("Names:", names)
print("Topics:", topics)
print("Files Dictionary:", files_dict)
