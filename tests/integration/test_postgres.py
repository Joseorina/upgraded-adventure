import os
from unittest import  TestCase
from db_config import PostgresConfig

TEST_DATABASE_URL = os.getenv('TEST_DATABASE_URL')
WRONG_TEST_DATABASE_URL = os.getenv('WRONG_TEST_DATABASE_URL')

class PostgresTestCase(TestCase):
	def setUp(self):
		self.postgres = PostgresConfig
		self.database_name = 'database_for_testing'
		self.query = """CREATE TABLE IF NOT EXISTS test_table_one (
				table_id serial PRIMARY KEY NOT NULL,
				table_number int NOT NULL,
				table_info character varying(1000),
				date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
				)"""
		self.table_name = 'test_table_one'

	def tearDown(self):
		self.postgres.drop_table(self.table_name, TEST_DATABASE_URL)
		self.postgres.drop_database(self.database_name)
