import os
import unittest
import json
from app import remove_doc_from_shelf,  add_new_shelf, delete_doc,  get_doc_shelf, show_document_info
import mock



class CaseTests (unittest.TestCase):

    def setUp(self):
        current_path = os.getcwd()
        f_directories = os.path.join(current_path, 'fixtures\directories.json')
        f_documents = os.path.join(current_path, 'fixtures\documents.json')
        with open (f_directories, 'r', encoding='utf-8') as  out_dir:
            self.directories = json.load(out_dir)
        with open (f_documents, 'r', encoding='utf-8') as  out_doc:
            self.documents = json.load(out_doc)

    @mock.patch('app.directories')
    def test(self, directories):
        directories.return_value = self.directories
        self.assertEqual(self.directories['2'],['10006'])
        print(self.directories)
        remove_doc_from_shelf('10006')
        print(self.directories)
    #

    @mock.patch('app.directories')
    def test_1(self, directories):
        directories.return_value = self.directories
        old_dir = directories.copy()
        remove_doc_from_shelf('10006')
        self.assertNotEqual(old_dir, directories)

    @mock.patch('app.directories')
    def test_1(self, directories):
        directories.return_value = self.directories
        old_dict = directories.copy()
        add_new_shelf('55555')
        self.assertNotEqual(old_dict, directories)

    @mock.patch('app.input', return_value='10006')
    def test_3(self, input):
        old_docs = self.documents.copy()
        with mock.patch('app.documents', self.documents):
            delete_doc()
        i=self.documents
        self.assertNotEqual(old_docs,i)

    @mock.patch('app.input', return_value='10006')
    def test_4(self, input):
        with mock.patch('app.directories', self.directories):
            resalt = get_doc_shelf()
        self.assertEqual('2',resalt)









