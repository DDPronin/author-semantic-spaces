Скачано автоматически (без изменения ноутбуков)

Файл: word2vec-ruscorpora-300.gz
Источник: GitHub release репозитория gensim-data (модель "word2vec-ruscorpora-300")
Описание: word2vec Skip-gram вектора, обученные на Национальном корпусе русского языка (НКРЯ), ~250M слов, 300d.

Ссылка на релиз:
https://github.com/piskvorky/gensim-data/releases/tag/word2vec-ruscorpora-300

Прямая ссылка на скачивание:
https://github.com/piskvorky/gensim-data/releases/download/word2vec-ruscorpora-300/word2vec-ruscorpora-300.gz

Как загрузить (пример):
1) распакуйте .gz, получите файл в формате word2vec
2) в python:
   from gensim.models import KeyedVectors
   kv = KeyedVectors.load_word2vec_format("word2vec-ruscorpora-300", binary=False)  # если текстовый формат
   # или binary=True, если внутри бинарный word2vec

