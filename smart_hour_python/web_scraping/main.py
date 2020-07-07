"""
Веб-скрапинг

Смартчас "Знакомство с Python"

"""
import requests
from bs4 import BeautifulSoup

# сервис для тестирования веб-скрапинга
url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones'


def parse_site():
    """
    Функция парсит тестовый сайт и собирает инф-ию продукта:
        1. наименование
        2. цена
    """
    response = requests.get(url)
    print(response.status_code)

    soup = BeautifulSoup(response.content, "html.parser")

    # поиск всех контейнеров с информацией
    containers = soup.find_all("div", {"class": "caption"})
    # print(containers)

    for each in containers:
        title = each.find("a", {"class": "title"}).text
        price = each.find("h4", {"class": "price"}).text
        print(f'{title}: {price}')


if __name__ == '__main__':
    parse_site()