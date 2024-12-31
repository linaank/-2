"""Пример использования парсера для обработки отзывов."""

import json
from sample.sample_parser import parse_reviews
from review_processor.visualization import generate_word_cloud

def main():
    """Основной пример использования проекта."""
    file_path = "sample_page.htm"
    parsed_reviews_path = "sample_reviews.json"

    print("Парсинг отзывов из локального файла...")
    parse_reviews(file_path, parsed_reviews_path)

    print("Анализ данных...")
    with open(parsed_reviews_path, 'r', encoding='utf-8') as file:
        reviews_data = json.load(file)

    for category in ["pros", "cons", "comms"]:
        print(f"Создание визуализаций для категории: {category}...")
        generate_word_cloud(
            [item["text"] for item in reviews_data[category]], output_path=f"{category}_word_cloud.png"
        )

    print("Анализ завершён.")

if __name__ == "__main__":
    main()
