from flask import Flask
from flask import request
import json
import Levenshtein as lv
from data import db_session
from data.models import Hero, Spell, Build
app = Flask(__name__)
session = {}
count = 0

@app.route('/post', methods=['POST'])
def main():
    global count
    # счётчик для функции start
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    # получаем и сохраняем текст пользователя
    text = request.json['request']['original_utterance'].lower()
    # получаем и сохраняем id пользователя
    user_id = request.json['session']['user_id']
    if user_id in session:
        # если пользователь уже ведёт диалог с алисой
        if session[user_id] == "start" and count != -1:
            count += 1
            session[user_id] = 'choose'
            return start(response, text, user_id, count)
        elif session[user_id] == "choose":
            return choose(response, text, user_id, count)
    else:
        # если пользователь пишет алисе в первый раз
        response['response']['text'] = "Добро пожаловать в гайды от Алисы для новичков в Dota 2! Чтобы получить список персонажей с гайдами используйте фразу 'Хочу гайд'."
        session[user_id] = "start"

    return json.dumps(response)


def start(res, text, id, count):
    if lv.ratio(text, "хочу гайд") > 0.8:
        res['response']['text'] = "Вот доступный список персонажей: " \
                                  "Sniper, " \
                                  "Axe, " \
                                  "Ogre Magi, " \
                                  "Sven, " \
                                  "Lich, " \
                                  "Lion, " \
                                  "Phantom Assassin, " \
                                  "Папич." \
                                  " Выберите героя и напишите его имя"
        count = -1
    else:
        if count <= 2:
            res['response']['text'] = "Я не уверена, но на 'Хочу гайд' ваши слова не похожи"
        else:
            res['response']['text'] = "Я считаю что вам всё же следует использовать 'Хочу гайд', а не троллить меня"
    return json.dumps(res)


def choose(res, text, user_id, count):
    session = db_session.create_session()
    heroes = ["Sniper", "Axe", "Ogre Magi", "Sven", "Lich" "Lion", "Phantom Assassin"]
    if text in heroes:
        for i in heroes:
            if lv.ratio(text, i) > 0.95:
                hero = i
    result = session.query(Hero).filter(Hero.name == hero).first()

if __name__ == '__main__':
    app.run()
