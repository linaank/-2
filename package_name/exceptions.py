"""Пользовательские исключения для пакета review_processor."""

class InvalidReviewFormatException(Exception):
    """Исключение для некорректного формата отзыва.

    :param message: описание ошибки
    :type message: str
    """
    def __init__(self, message="Некорректный формат отзыва."):
        super().__init__(message)


class FileProcessingError(Exception):
    """Исключение для ошибок при обработке файлов.

    :param message: описание ошибки
    :type message: str
    """
    def __init__(self, message="Ошибка при обработке файла."):
        super().__init__(message)


class SentimentAnalysisError(Exception):
    """Исключение для ошибок анализа тональности.

    :param message: описание ошибки
    :type message: str
    """
    def __init__(self, message="Ошибка при анализе тональности."):
        super().__init__(message)


class VisualizationError(Exception):
    """Исключение для ошибок при визуализации данных.

    :param message: описание ошибки
    :type message: str
    """
    def __init__(self, message="Ошибка при визуализации данных."):
        super().__init__(message)


class DataAnalysisError(Exception):
    """Исключение для ошибок анализа данных.

    :param message: описание ошибки
    :type message: str
    """
    def __init__(self, message="Ошибка при анализе данных."):
        super().__init__(message)


class TextProcessingError(Exception):
    """Исключение для ошибок при обработке текстов.

    :param message: описание ошибки
    :type message: str
    """
    def __init__(self, message="Ошибка при обработке текста."):
        super().__init__(message)
