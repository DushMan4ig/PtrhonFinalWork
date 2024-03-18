#Задание №6
#Напишите код, который запускается из командной строки и получает на вход
#путь до директории на ПК.
#Соберите информацию о содержимом в виде объектов namedtuple.
#Каждый объект хранит:
#○ имя файла без расширения или название каталога,
#○ расширение, если это файл,
#○ флаг каталога,
#○ название родительского каталога.
#В процессе сбора сохраните данные в текстовый файл используя
#логирование.

import os
import sys
import logging
from collections import namedtuple

logging.basicConfig(filename='file_info.log', level=logging.INFO)

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def get_file_info(file_path):
    name, extension = os.path.splitext(os.path.basename(file_path))
    parent_directory = os.path.basename(os.path.dirname(file_path))
    is_directory = os.path.isdir(file_path)
    return FileInfo(name=name, extension=extension if not is_directory else '', 
                    is_directory=is_directory, parent_directory=parent_directory)

def main(directory_path):
    logging.info(f"Collecting file information from directory: {directory_path}")
    try:
        with open('file_info.txt', 'w') as file:
            for item in os.listdir(directory_path):
                file_path = os.path.join(directory_path, item)
                file_info = get_file_info(file_path)
                logging.info(f"Processed: {file_path}")
                file.write(f"Name: {file_info.name}, Extension: {file_info.extension}, "
                           f"Is Directory: {file_info.is_directory}, Parent Directory: {file_info.parent_directory}\n")
        logging.info("File information collected successfully.")
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py directory_path")
        sys.exit(1)
    directory_path = sys.argv[1]
    main(directory_path)
    
    # Запускать код будет команда "python script.py /path/to/directory"