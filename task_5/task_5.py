#!/usr/bin/env python3
"""
– Написати ряд корисних функцій для роботи зі словниками:

    * операції, що трактують словник як множину (об'єднання словників, диз'юнкція словників, симетрична різниця словників та інші).
      Повний перелік операцій простіше всього побачити на діаграмах Вієна.

    * функцію для сортування словників

    * функцію для перегортання словників (міняє ключі та значення місцями, якщо це можливо,
      а в разі якщо неможливо – викидає виключення (raise ValueError(...))

– Подумати над аргументами функцій, щоб вони були продуманими, універсальними та зручними у використанні

– Потаймити реалізації. У разі якщо на думку спадає декілька реалізацій однієї з функцій – за результатами таймінгу вибрати найбільш оптимальну

– Задокументувати функції за допомогою docstring (інтерфейс), а де необхідно пояснити неочевидні з коду особливості реалізації – за допомогою коментарів

– Викласти в репозиторій, в окрему директорію два файли: один – модуль, в якому описані функції; а інший – з прикладом їх використання

– (extra) Встановити пакет wemake-python-styleguide та за допомогою утиліти flake8 перевірити код на відповідність coding style. Виправити помилки.
  (За основу нашого Coding Style беремо PEP8 з максимальною довжиною строки збільшеною до 100 символів)
"""
import time


def update_dict(dict1: dict, dict2: dict):
    """Обєднання словників"""
    start = time.time()
    dict1.update(dict2)
    end = time.time() - start
    return dict1, f"Function execution time: {end}"


def intersection_dict(dict1: dict, dict2: dict):
    """Спільні елемети словників"""
    start = time.time()
    dict1 = dict(dict1.items() & dict2.items())
    end = time.time() - start
    return dict1, f"Function execution time: {end}" 


def differense_dict(dict1: dict, dict2: dict):
    """Різниця  елеметів словників"""
    start = time.time()
    dict1 = dict(dict1.items() - dict2.items())
    end = time.time() - start
    return dict1, f"Function execution time: {end}" 


def symmetric_differense_dict(dict1: dict, dict2: dict):
    """Симетрична різниця  елеметів словників"""
    start = time.time()
    dict1 = dict(dict1.items() ^ dict2.items())
    end = time.time() - start
    return dict1, f"Function execution time: {end}" 


def sort_dict_key(dict1: dict):
    """сортування словника за ключем"""
    start = time.time()
    spisok_key = {k: dict1[k] for k in sorted(dict1, key=lambda x: x)}
    end = time.time() - start
    return spisok_key, f"Function execution time: {end}" 

def sort_dict_value(dict1: dict):
    """сортування словника за значенням"""
    start = time.time()
    spisok_value = {k: dict1[k] for k in sorted(dict1, key=lambda x: dict1[x])}
    end = time.time() - start
    return  spisok_value,  f"Function execution time: {end}" 


def change_k_v(dict1: dict):
    """заміна ключа на значення"""
    start = time.time()
    new_dict = {}
    for k, v in dict1.items():
        new_dict[v] = k
    end = time.time() - start
    return new_dict, f"Function execution time: {end}" 
