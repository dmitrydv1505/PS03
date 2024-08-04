import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def get_english_words():
    url = "https://randomword.com"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def translate_to_russian(text):
    translator = Translator()
    try:
        result = translator.translate(text=text, dest="ru")
        return result.text
    except Exception as e:
        print(f"Не удалось перевести текст: {e}")
        return text

def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        if not word_dict:
            break

        word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")

        translated_word = translate_to_russian(word)
        translated_definition = translate_to_russian(word_definition)

        print(f"Значение слова - {translated_definition}")

        user = input("Что это за слово? ")
        if user.lower() == translated_word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано слово - {translated_word}")

        play_again = input("Хотите сыграть еще раз? y/n ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break

word_game()
