![Python](https://img.shields.io/pypi/pyversions/scrapy?color=brightgreen&style=plastic)![Scrapy](https://img.shields.io/badge/scrapy-2.7.0-brightgreen>)

![Stars](https://img.shields.io/github/gist/stars/123?logoColor=yellow&style=social)
![Fork](https://img.shields.io/github/forks/ipatrushevsergey/scrapy_parser_pep?logoColor=green&style=social)

# Проект 19-го спринта "Асинхронный парсер PEP"

## Описание

В проекте реализована возможность:
- асинхронно, с помощью фреймворка **Scrapy**, парсить со страницы **https://peps.python.org/** ссылки на страницы документов **PEP**, переходить по данным ссылкам и собирать с **PEP** страниц информацию о порядковом номере, названии и статусе документа. Информация сохраняется в файл **pep_<%Y-%m-%dT%H-%M-%S>.csv** (в папку **results** в корне проекта);
- также по результатам парсинга создавать файл **status_summary_<%Y-%m-%d_%H-%M-%S>.csv**, в который сохранется количество **PEP** документов в зависимости от статуса и общее количество документов **PEP** (в папку **results** в корне проекта). 

## Технологии

- Python 3.7
- Scrapy 2.7.0

## Подготовка проекта

1. Необходимо сделать **Fork** репозитория:
```
https://github.com/iPatrushevSergey/scrapy_parser_pep.git
```
2. Далее нужно клонировать проект:
```
git clone git@github.com:<ваш_username>/scrapy_parser_pep.git
```
3. Создать и активировать виртуальное окружение:

- MacOS и Linux
```
python3 -m venv venv && . venv/bin/activate
```
- Windows
```
python -m venv venv && . venv/bin/activate
```
4. Установить зависимости:
```
pip install -r requirements.txt 
```

## Запуск проекта

```
scrapy crawl pep
```

Результаты парсинга сохраняются в директорию **results** в файлы:

1. **pep_<%Y-%m-%dT%H-%M-%S>.csv**
___
```
number,name,status
1,PEP Purpose and Guidelines,Active
42,Feature Requests,Withdrawn
100,Python Unicode Integration,Final
102,Doing Python Micro Releases,Superseded
160,Python 1.6 Release Schedule,Final
101,Doing Python Releases 101,Active
200,Python 2.0 Release Schedule,Final
103,Collecting information about git,Withdrawn
20,The Zen of Python,Active
8,Style Guide for Python Code,Active
10,Voting Guidelines,Active
13,Python Language Governance,Active
```
2. **status_summary_<%Y-%m-%d_%H-%M-%S>.csv**
___
```
"Статус","Количество"
"Active","37"
"Withdrawn","55"
"Final","264"
"Superseded","19"
"Accepted","40"
"Rejected","120"
"Deferred","36"
"Draft","30"
"April Fool!","1"
"Total","602"
```

+ **Author**: Patrushev Sergey
+ **Mail**: PatrushevSergeyVal@yandex.ru
+ **GitHub**: [iPatrushevSergey](https://github.com/iPatrushevSergey)
