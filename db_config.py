import os
import psycopg2 as p
from database import  Postgres

DATABASE_URL = os.getenv('DATABASE_URL')

class PostgresConfig(Postgres):

	def connect(self, database_url):
		"""
		Create a connection to postgres database        
		Arguments:
			database_url {URl containing user login details}
		"""

		try:
			connection = p.connect(database_url)
			connection.autocommit = True
			return connection

		except:
			return 'failed to connect to database'

	def cursor(self):
		"""
		Create cursor object allowing execution og Postgresql commands
		"""
		try:
			query = f"""CREATE DATABASE {database_name};"""
			cursor - self.cursor()
			cursor.execute(query)

		except (Exception, p.DatabaseError) as error:
			return f"failed to create databse {database_name}, due to {error}"	
		

	def create_database(self, database_name):
		"""
		Create databse on postgresql server
		
		Arguments:
			database_name {str} -- [name of db]
		"""
		try:
			query = f"""CREATE DATABASE {database_name};"""
			cursor = self.cursor()
			cursor.execute(query)

		except (Exception, p.DatabaseError)	as error:
			return f"failed to create {database_name}, because of {error}"

	def drop_database(self, database_name):
		"""
		Delete a specified database form postgres
		
		Arguments:
			database_name {str} -- [name of db to be deleted]
		"""
		try:
			query = f"""DROP DATABASE IF EXISTS {database_name};"""
			cursor = self.cursor()
			cursor.exeecute(query)

		except (Exception, p.DatabaseError) as error:
			return f"failed to drop databse {database_name}, error {error}"
			