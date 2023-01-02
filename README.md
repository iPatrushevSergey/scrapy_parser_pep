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

+ **Author**: Patrushev Sergey
+ **Mail**: PatrushevSergeyVal@yandex.ru
+ **GitHub**: https://github.com/iPatrushevSergey
