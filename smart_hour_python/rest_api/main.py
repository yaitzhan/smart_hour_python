"""
Простой REST сервис

Смартчас "Знакомство с Python"

Еще про REST-сервисы:
    https://habr.com/ru/post/38730/
    https://habr.com/ru/post/483202/

"""
from flask import Flask
from flask import jsonify


# основное приложение
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # для кирллицы

# наша "БД"
local_data = {
        1: 'Grumpy cat',
        2: 'Чеширский кот',
        3: 'Кот Том, без Джери'
}


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/v1/cats', methods=['GET'])
def cats_json_handler():
    """
    Ф-ция обработчик запросов.

    :return: возвращает котиков
    """
    response = local_data

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
