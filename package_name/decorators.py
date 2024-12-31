"""Декораторы для улучшения функциональности."""

import time
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def log_execution_time(func):
    """Логировать время выполнения функции.

    :param func: функция, время выполнения которой нужно логировать
    :type func: function

    :rtype: function
    :return: обёрнутая функция
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Функция '{func.__name__}' выполнена за {execution_time:.4f} секунд.")
        return result

    return wrapper
