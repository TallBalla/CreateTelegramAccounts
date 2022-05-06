import unittest
import json

import os
import sys
sys.path.append("..")

from src.FileHandler import FileHandler
from src.Account import Account

class FileHandlerTests(unittest.TestCase):
    def setUp(self):
        self.file_handler = FileHandler("test_file")

    def tearDown(self):
        self.file_handler = None
        os.remove("../test_file.json")

    def test_should_create_json_file(self):
        self.file_handler.create_json_file()
        self.assertTrue(os.path.isfile("../test_file.json"))

    def test_should_load_empty_account_list_when_file_created(self):
        self.file_handler.create_json_file()
        self.file_handler.load_accounts()
        self.assertEqual(self.file_handler.get_accounts(), [])

    def test_should_append_account_to_json_file(self):
        temp_account = Account("john", "dea", int(123), "0800838383")

        self.file_handler.create_json_file()
        self.file_handler.append_single_account_json_file(temp_account)
        self.file_handler.load_accounts()

        expected_json_string = [json.dumps(temp_account.__dict__)]
        actual_json_string = self.file_handler.get_accounts()

        self.assertEqual(expected_json_string, actual_json_string)

    def test_should_append_multiple_accounts_to_json_file(self):
        temp_account_1 = Account("john", "dear", int(123), "0800838383")
        temp_account_2 = Account("jane", "doe", int(456), "0800838383")
        temp_account_3 = Account("joe", "doe", int(789), "0800838383")

        self.file_handler.create_json_file()
        self.file_handler.append_multiple_account_json_file(temp_account_1,
                                                            temp_account_2,
                                                            temp_account_3)

        expected_json_strings = json.dumps([temp_account_1.__dict__,
                                            temp_account_2.__dict__,
                                            temp_account_3.__dict__])

        actual_json_strings = self.file_handler.get_accounts()

        self.assertEqual(expected_json_strings, actual_json_strings)


# if __name__ == '__main__':
#     unittest.main(verbosity=2)
