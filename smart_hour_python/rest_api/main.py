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

# наша "БД"
local_data = {
        1: 'Grumpy cat',
        2: 'Чеширский кот',
        3: 'Кот Том, без Джери'
}


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/v1/cats/<int:cat_id>', methods=['GET'])
@app.route('/api/v1/cats', methods=['GET'], defaults={'cat_id': 0})
def cats_json_handler(cat_id):
    """
    Ф-ция обработчик запросов.

    :param cat_id: id котика
    :return: возвращает всех котиков или определенного
    """
    if cat_id:
        response = local_data.get(cat_id)  # возращаем определенного котика
    else:
        response = local_data  # возращаем всех котиков
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
