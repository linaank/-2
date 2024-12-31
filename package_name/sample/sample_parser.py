"""Парсер отзывов из локального HTML-файла."""

import json
from bs4 import BeautifulSoup

def parse_reviews(file_path, output_path="sample_reviews.json"):
    """Парсить отзывы из HTML-файла и сохранять их в JSON.

    :param file_path: путь к HTML-файлу
    :type file_path: str
    :param output_path: путь для сохранения результата в JSON
    :type output_path: str
    """
    print(f"Загрузка файла: {file_path}")
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    reviews_data = {
        "pros": [],
        "cons": [],
        "comms": []
    }

    review_blocks = soup.find_all(class_="feedback__content")
    print(f"Найдено блоков отзывов: {len(review_blocks)}")

    for block in review_blocks:
        pros = block.find(class_="feedback__text--item-pro")
        cons = block.find(class_="feedback__text--item-con")
        comm = block.find(class_="feedback__text--item")

        rating_tag = block.find_next(class_="feedback__rating-wrap")
        rating = None
        if rating_tag:
            stars_class = rating_tag.find(class_="stars-line")
            if stars_class:
                for cls in stars_class.get("class", []):
                    if cls.startswith("star") and cls[4:].isdigit():
                        try:
                            rating = int(cls[4:])  # Извлекаем число после "star"
                            break
                        except ValueError:
                            print(f"Ошибка преобразования рейтинга: {stars_class.get('class')}")
                            rating = None

        # Удаляем ключевые слова в начале текста
        def clean_text(text):
            keywords = ["Достоинства:", "Недостатки:", "Комментарий:"]
            for keyword in keywords:
                if text.startswith(keyword):
                    return text[len(keyword):].strip()
            return text

        # Удаляем записи с пустым текстом
        if pros and pros.text.strip():
            cleaned_text = clean_text(pros.text.strip())
            reviews_data["pros"].append({"text": cleaned_text, "rating": rating})
        if cons and cons.text.strip():
            cleaned_text = clean_text(cons.text.strip())
            reviews_data["cons"].append({"text": cleaned_text, "rating": rating})
        if comm and comm.text.strip():
            cleaned_text = clean_text(comm.text.strip())
            reviews_data["comms"].append({"text": cleaned_text, "rating": rating})

        # Выводим информацию о некорректных данных
        if rating is None or not isinstance(rating, int):
            print(f"Некорректный блок: {{'pros': {pros.text.strip() if pros else None}, 'cons': {cons.text.strip() if cons else None}, 'comm': {comm.text.strip() if comm else None}, 'rating_tag': {rating_tag}}}")

    for category in ["pros", "cons", "comms"]:
        reviews_data[category] = [review for review in reviews_data[category] if isinstance(review.get("rating"), int)]

    # Сохраняем данные в файл
    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(reviews_data, json_file, ensure_ascii=False, indent=4)

    print(f"Отзывы успешно сохранены в {output_path}")
