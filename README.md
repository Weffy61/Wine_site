# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".
## Установка
```commandline
git clone https://github.com/Weffy61/wine_site
```
## Установка зависимостей
Переход в директорию с исполняемым файлом и установка
```commandline
cd wine_site
```
```commandline
pip install -r requirements.txt
```
## Настройка
В корне проекта необходимо создать файл `.env`. Открыть его любым текстовым редактором и внести 
данные вашей excel таблицы  
Пример:  

```djangourlpath
export EXCEL_WINE_BASE=wine_base.xlsx
``` 
Пример таблицы:  

|  Категория   |  Название  |      Сорт       | Цена |    Картинка     |        Акция         |
|:------------:|:----------:|:---------------:|:----:|:---------------:|:--------------------:|
|  Белые вина  | Белая леди | Дамский пальчик | 399  | belaya_ledi.png | Выгодное предложение |
| Красные вина | Хванчкара  |  Александраули  | 550  | hvanchkara.png  |                      |
|   Напитки    |    Чача    |                 | 299  |   chacha.png    |                      |
   
В корне проекта находится пробная таблица `wine_base.xlsx`
## Запуск
```commandline
python main.py
```
Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
