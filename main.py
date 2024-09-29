import json
import re
from collections import Counter

# Список стоп-слов (местоимения, союзы и т.д.)
stop_words = set([
    "я", "ты", "он", "она", "оно", "мы", "вы", "они",
    "это", "в", "на", "с", "и", "не", "что", "как", "а",
    "то", "или", "но", "да", "так", "за", "для",
    "по", "от", "о", "к", "бы", "чтобы",
    "сам", "который", "также", "можно",
    "да", "нет", "так", "всё", "у", "мне", "тебя",
    "меня", "ну", "может"
])




# Функция для обработки текста и подсчета слов
def count_words(messages):
    words = []
    for message in messages:
        # Проверяем наличие текста в сообщении
        if 'text' in message:
            # Если текст - строка, обрабатываем его
            if isinstance(message['text'], str):
                words.extend(re.findall(r'\b\w+\b', message['text'].lower()))
            # Если текст - список, обрабатываем каждый элемент
            elif isinstance(message['text'], list):
                for text in message['text']:
                    if isinstance(text, str):
                        words.extend(re.findall(r'\b\w+\b', text.lower()))

        # Если 'text_entities' присутствует, извлекаем текст из них
        if 'text_entities' in message:
            for entity in message['text_entities']:
                if 'text' in entity and isinstance(entity['text'], str):
                    words.extend(re.findall(r'\b\w+\b', entity['text'].lower()))
    return words


# Функция для получения топ-N самых частых слов
def get_top_words(words, n=100):
    word_counts = Counter(words)
    return word_counts.most_common(n)


# Загрузка переписки из JSON файла
def load_chat(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


# Запись результатов в текстовый файл
def save_to_txt(top_words, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for word, count in top_words:
            file.write(f"{word}: {count}\n")


# Основная функция
def main():
    # Загрузка переписки
    chat_data = load_chat('result.json')  # Укажите путь к вашему файлу JSON

    # Извлечение сообщений
    messages = chat_data.get('messages', [])

    # Подсчет всех слов
    words = count_words(messages)

    # Получение топ-100 слов без очищения
    top_words_without_cleaning = get_top_words(words, n=100)
    save_to_txt(top_words_without_cleaning, 'top_words_without_cleaning.txt')

    # Фильтрация стоп-слов
    filtered_words = [word for word in words if word not in stop_words and not word.isdigit()]

    # Получение топ-100 слов с очищением
    top_words_with_cleaning = get_top_words(filtered_words, n=100)
    save_to_txt(top_words_with_cleaning, 'top_words_with_cleaning.txt')


if __name__ == "__main__":
    main()
