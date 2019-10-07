import os
from unittest import  TestCase
from db_config import PostgresConfig

TEST_DATABASE_URL = os.getenv('TEST_DATABASE_URL')
WRONG_TEST_DATABASE_URL = os.getenv('WRONG_TEST_DATABASE_URL')

class PostgresTestCase(TestCase):
    def setUp(self):
        pass