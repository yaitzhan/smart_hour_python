"""
Простой REST сервис

Смартчас "Знакомство с Python"
"""
from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/v1/cats', methods=['GET'])
def cats_json_handler():
    response = {
        1: 'Grumpy cat',
        2: 'Чеширский кот',
        3: 'Кот Том, без Джери'
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run()
