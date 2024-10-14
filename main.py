import json
import re
from collections import Counter
import pandas as pd

# Список стоп-слов
stop_words = set([
    "я", "ты", "он", "она", "оно", "мы", "вы", "они", "это", "в", "на", "с", "и", "не", 
    "что", "как", "а", "то", "или", "но", "да", "так", "за", "для", "по", "от", "о", 
    "к", "бы", "чтобы", "сам", "который", "также", "можно", "да", "нет", "так", "всё", 
    "у", "мне", "тебя", "меня", "ну", "может"
])

# Функция для подсчета слов
def count_words(messages):
    words = []
    for message in messages:
        if isinstance(message['text'], str):
            words.extend(re.findall(r'\b\w+\b', message['text'].lower()))
        elif isinstance(message['text'], list):
            for item in message['text']:
                if isinstance(item, str):
                    words.extend(re.findall(r'\b\w+\b', item.lower()))
    return words

# Функция для подсчета сообщений от пользователей
def count_messages_by_user(messages):
    user_message_count = Counter()
    for message in messages:
        if 'from' in message:
            user_message_count[message['from']] += 1
    return user_message_count

# Функция для получения списка всех пользователей с их никнеймами и ID
def get_users(messages):
    users = {}
    for message in messages:
        if 'from_id' in message and 'from' in message:
            user_id = message['from_id']
            username = message['from']
            if 'from_username' in message:  # Проверка на наличие никнейма
                username = f"@{message['from_username']}"
            users[user_id] = username
    return users

def main():
    # Чтение данных из файла
    with open('result.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    messages = data['messages']
    
    # Подсчет всех слов
    words = count_words(messages)
    word_counter = Counter(words)
    
    # Запись топ-100 слов без фильтрации
    with open('top_100_words_raw.txt', 'w', encoding='utf-8') as f:
        for word, count in word_counter.most_common(100):
            f.write(f"{word}: {count}\n")

    # Фильтрация слов по стоп-словам
    filtered_words = [word for word in words if word not in stop_words]
    filtered_word_counter = Counter(filtered_words)
    
    # Запись топ-100 отчищенных слов
    with open('top_100_words_cleaned.txt', 'w', encoding='utf-8') as f:
        for word, count in filtered_word_counter.most_common(100):
            f.write(f"{word}: {count}\n")

    # Подсчет количества сообщений от пользователей
    user_message_count = count_messages_by_user(messages)
    
    # Запись топ пользователей по количеству сообщений с никнеймами
    with open('top_users.txt', 'w', encoding='utf-8') as f:
        for user, count in user_message_count.most_common():
            f.write(f"{user}: {count} messages\n")
    
    # Получение списка всех пользователей с их ID и никнеймами
    users = get_users(messages)
    
    # Запись списка всех пользователей с их ID и никнеймами
    with open('users_list.txt', 'w', encoding='utf-8') as f:
        for user_id, username in users.items():
            f.write(f"User: {username}, ID: {user_id}\n")
        f.write(f"\nTotal users: {len(users)}")

if __name__ == "__main__":
    main()
