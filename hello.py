from flask import Flask, render_template, request
import json
import logging

app = Flask(__name__)
logging.basicConfig(filename="logs/flask.log", level=logging.INFO)


class GetJson():
    '''дессериализуем наш json'''
    @staticmethod
    def get_api1():
        with open('api1.json', 'r') as jsonnable:
            return json.load(jsonnable)

    @staticmethod
    def get_api2():
        with open('api2.json', 'r') as jsonnable:
            return json.load(jsonnable)


def logger(string):
    logging.info(string)


@app.route('/')
def hello()->str:  # тестовая кнопки
    return render_template('html.html')


@app.route('/api1', methods=['GET', 'POST'])
def api1():
    if request.method == 'GET':
        logger(request.args)
        return GetJson.get_api1()
    else:  # тут 2 варианта, можно неявно указать, что метод работает только при GET или же сделать это явно
        return 'ONLY GET'


@app.route('/api2', methods=['GET', 'POST'])
def api2():
    if request.method == 'POST':
        logger(request.form.to_dict())
        return GetJson.get_api2()
    else: # аналогично
        return 'ONLY POST'
