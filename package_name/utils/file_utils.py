"""Утилиты для работы с JSON-файлами."""

import json
from review_processor.exceptions import FileProcessingError
from review_processor.decorators import log_execution_time

@log_execution_time
def load_json(filepath):
    """Загрузить данные из JSON-файла.

    :param filepath: путь к файлу
    :type filepath: str

    :raises FileProcessingError: если файл не найден или повреждён

    :rtype: dict | list
    :return: данные из JSON-файла
    """
    if not isinstance(filepath, str):
        raise FileProcessingError("Путь к файлу должен быть строкой.")

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise FileProcessingError(f"Ошибка при чтении файла {filepath}: {e}")

@log_execution_time
def save_json(data, filepath):
    """Сохранить данные в JSON-файл.

    :param data: данные для сохранения
    :type data: dict | list
    :param filepath: путь к файлу
    :type filepath: str

    :raises FileProcessingError: если запись в файл завершилась ошибкой
    """
    if not isinstance(filepath, str):
        raise FileProcessingError("Путь к файлу должен быть строкой.")

    if not isinstance(data, (dict, list)):
        raise FileProcessingError("Данные должны быть словарём или списком.")

    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        raise FileProcessingError(f"Ошибка при записи в файл {filepath}: {e}")
