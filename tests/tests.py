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

    def test_1(self):
        old_dir = directories.copy()
        remove_doc_from_shelf('10006')
        self.assertNotEqual(old_dir, directories)

    def test_2(self):
        old_dict = directories.copy()
        add_new_shelf('55555')
        self.assertNotEqual(old_dict, directories)

    @mock.patch('app.input', return_value='10006')
    def test_3(self, input):
        old_docs = documents.copy()
        delete_doc()
        i=documents
        self.assertNotEqual(old_docs,i)

    @mock.patch('app.input', return_value='10006')
    def test_4(self, input):
        resalt = get_doc_shelf()
        self.assertEqual('2',resalt)
