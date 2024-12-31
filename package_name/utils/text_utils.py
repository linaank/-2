"""Вспомогательные функции для обработки текста."""

import re
from review_processor.exceptions import TextProcessingError

def clean_text(text):
    """Очистить текст от лишних символов, таких как пробелы, знаки препинания и спецсимволы.

    :param text: текст для очистки
    :type text: str

    :raises TextProcessingError: если текст не является строкой

    :rtype: str
    :return: очищенный текст
    """
    if not isinstance(text, str):
        raise TextProcessingError("Входные данные должны быть строкой.")
    return re.sub(r'[^\w\s]', '', text).strip()

def word_count(text):
    """Подсчитать количество слов в тексте.

    :param text: текст для подсчёта слов
    :type text: str

    :raises TextProcessingError: если текст не является строкой

    :rtype: int
    :return: количество слов
    """
    if not isinstance(text, str):
        raise TextProcessingError("Входные данные должны быть строкой.")
    return len(re.findall(r'\b\w+\b', text))

def char_count(text):
    """Подсчитать количество символов в тексте (без пробелов).

    :param text: текст для подсчёта символов
    :type text: str

    :raises TextProcessingError: если текст не является строкой

    :rtype: int
    :return: количество символов
    """
    if not isinstance(text, str):
        raise TextProcessingError("Входные данные должны быть строкой.")
    return len(text.replace(' ', ''))
