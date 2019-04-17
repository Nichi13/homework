import unittest
import requests

#  я бы вынес в def setUp(self): запрос, но он различается у тестов

class CaseTests (unittest.TestCase):

    def test_yandex(self):
        API_KEY = 'trnsl.1.1.20190228T195305Z.0e420ab62864e7bd.999563fd55628362f83666c9741638399a300113'
        URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        text_str = 'привет'
        params = {
            'key': API_KEY,
            'id': '0689baea.5c7838be.cf87f84b-1-0',
            'lang': 'ru-en',
            'reason': 'auto',
            'srv': 'tr-text'}

        i = {'text': text_str}
        response = requests.post(URL, params=params, data=i)
        print(response.status_code)
        self.assertEqual(response.status_code, 200, 'Не соответствует код запроса')
        t = response.json()
        s = t['text'][0]
        self.assertEqual(s, 'hi', 'Неверный перевод')
        print(s)


    def test_yandex2(self):
        API_KEY = 'trnsl.1.1.20190228T195305Z.0e420ab62864e7bd.999563fd55628362f83666c9741638399a300113'
        URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        text_str = 'привет'
        params = {
            'key': API_KEY,
            'id': '0689baea.5c7838be.cf87f84b-1-0',
            'reason': 'auto',
            'srv': 'tr-text'}

        i = {'text': text_str}
        response = requests.post(URL, params=params, data=i)
        print('Bad Request', response.status_code)
        self.assertEqual(response.status_code, 400)
        t = response.json()

    def test_yandex(self):
        API_KEY = 'trnsl.1.1.20190228T195305Z.0e420ab62864e7bd.999563fd55628362f83666c9741638399a30011'
        URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        text_str = 'привет'
        params = {
            'key': API_KEY,
            'id': '0689baea.5c7838be.cf87f84b-1-0',
            'lang': 'ru-en',
            'reason': 'auto',
            'srv': 'tr-text'}

        i = {'text': text_str}
        response = requests.post(URL, params=params, data=i)
        print('Доступ к яндекс запрещен, проверь API_KEY ', response.status_code)
        self.assertEqual(response.status_code, 403)
