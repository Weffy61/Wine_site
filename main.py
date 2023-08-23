import collections
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas as pd
from environs import Env


def get_age_name(age):
    num = age % 100
    if 4 < num < 21:
        return 'лет'
    num %= 10
    if num == 1:
        return 'год'
    if 1 < num < 5:
        return 'года'
    return 'лет'


def prepare_wine_categories(excel_base):
    wines = pd.read_excel(
        excel_base,
        na_values=None,
        keep_default_na=False).to_dict(orient='records')
    categories = collections.defaultdict(list)
    for category in wines:
        categories[category['Категория']].append(category)
    return categories


def main():
    env_environs = Env()
    env_environs.read_env()
    excel_base = env_environs.str('EXCEL_WINE_BASE')
    env_jinja = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    company_foundation_year = 1920
    template = env_jinja.get_template('template.html')
    company_age = datetime.datetime.now().year - company_foundation_year

    categories = prepare_wine_categories(excel_base)
    rendered_page = template.render(
        age=company_age,
        age_name=get_age_name(company_age),
        categories=categories
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
