"""Функции для визуализации данных."""

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from review_processor.decorators import log_execution_time
from review_processor.exceptions import VisualizationError


@log_execution_time
def generate_word_cloud(reviews, output_path="word_cloud.png"):
    """Создать облако слов из текстов отзывов.

    :param reviews: список отзывов
    :type reviews: list[dict]
    :param output_path: путь для сохранения облака слов
    :type output_path: str

    :raises VisualizationError: если данные некорректны или облако слов не удалось сохранить
    """
    if not isinstance(reviews, list):
        raise VisualizationError("Отзывы должны быть списком.")

    if not isinstance(output_path, str):
        raise VisualizationError("Путь для сохранения облака слов должен быть строкой.")

    try:
        combined_text = " ".join(
            review.get("text", "") if isinstance(review, dict) else review
            for review in reviews
        ).strip()

        if not combined_text:
            print("Данные для облака слов пусты. Генерация пропущена.")
            return

        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(combined_text)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.savefig(output_path)
        plt.close()

        print(f"Облако слов сохранено в {output_path}")
    except Exception as e:
        raise VisualizationError(f"Ошибка при создании или сохранении облака слов: {e}")
