"""Функции для проверки структуры данных."""

from review_processor.exceptions import InvalidReviewFormatException
from review_processor.decorators import log_execution_time

def validate_review(review):
    """Проверить корректность структуры одного отзыва.

    :param review: отзыв
    :type review: dict

    :raises InvalidReviewFormatException: если структура отзыва некорректна
    """
    required_keys = {"text", "rating"}
    if not isinstance(review, dict):
        raise InvalidReviewFormatException("Отзыв должен быть словарём.")

    missing_keys = required_keys - review.keys()
    if missing_keys:
        raise InvalidReviewFormatException(
            f"В отзыве отсутствуют обязательные поля: {', '.join(missing_keys)}"
        )

    if not isinstance(review["text"], str):
        raise InvalidReviewFormatException("Поле 'text' должно быть строкой.")

    if not isinstance(review["rating"], (int, float)):
        raise InvalidReviewFormatException("Поле 'rating' должно быть числом.")

@log_execution_time
def validate_reviews(reviews):
    """Проверить корректность структуры списка отзывов.

    :param reviews: список отзывов
    :type reviews: list[dict]

    :raises InvalidReviewFormatException: если хотя бы один отзыв некорректен
    """
    if not isinstance(reviews, list):
        raise InvalidReviewFormatException("Отзывы должны быть списком.")

    for review in reviews:
        validate_review(review)
