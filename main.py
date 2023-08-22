import collections
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas as pd


def check_age_name(age):
    num = age % 100
    if 4 < num < 21:
        return 'лет'
    num %= 10
    if num == 1:
        return 'год'
    if 1 < num < 5:
        return 'года'
    return 'лет'


def prepare_wine_categories():
    wines = pd.read_excel('wine3.xlsx', na_values=None, keep_default_na=False).to_dict(orient='records')
    categories = collections.defaultdict(list)
    for category in wines:
        categories[category['Категория']].append(category)
    return categories


def generate_wine_page():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    company_age = datetime.datetime.now().year - 1920

    categories = prepare_wine_categories()
    rendered_page = template.render(
        age=company_age,
        age_name=check_age_name(company_age),
        categories=categories
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


def main():
    generate_wine_page()


if __name__ == '__main__':
    main()
