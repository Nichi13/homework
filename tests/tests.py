import os
import unittest
import json
from app import remove_doc_from_shelf, directories, add_new_shelf, delete_doc, documents, get_doc_shelf, show_document_info
import mock
import requests


class CaseTests (unittest.TestCase):

    # def setUp(self):
    #     current_path = os.getcwd()
    #     f_directories = os.path.join(current_path, 'fixtures\directories.json')
    #     f_documents = os.path.join(current_path, 'fixtures\documents.json')
    #     with open (f_directories, 'r', encoding='utf-8') as  out_dir:
    #         self.directories = json.load(out_dir)
    #     with open (f_documents, 'r', encoding='utf-8') as  out_doc:
    #         self.documents = json.load(out_doc)

    # @mock.patch('app.directories')
    # def test(self, directories):
    #     directories.return_value = self.directories
    #     self.assertEqual(self.directories['2'],['10006'])
    #     print(self.directories)
    #     remove_doc_from_shelf('10006')
    #     print(self.directories)
    #
    # Хотел сделать через fixtures,  он даже подгружал, однако при print-e все равно полки были все на месте,
    # как я понял он просто заново подгружал целый файл со всеми полками.
    def test_1(self):
        self.assertEqual(directories['2'],['10006'])
        print(directories)
        remove_doc_from_shelf('10006')
        print(directories)

    def test_2(self):
        print(directories.keys())
        add_new_shelf('55555')
        print(directories.keys())

    def test_3(self):
        l=documents
        print(l)
        delete_doc()
        i=documents
        print(i)
        self.assertEqual(l,i)
        #  мне кажется или в данном случае self.assertEqual не работает

    def test_4(self):
        print(directories['2'])
        print(get_doc_shelf())
        self.assertEqual('2',get_doc_shelf())

#     Честно - очень сложно придумать примеры, тем более код написан так, что не подкопаться

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
        print( response.status_code)
        self.assertEqual(response.status_code, 200, 'Не соответствует код запроса')
        t = response.json()
        s =t['text'][0]
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
        print( 'Доступ к яндекс запрещен, проверь API_KEY ',response.status_code)
        self.assertEqual(response.status_code, 403)





