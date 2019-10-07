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

	def create_table(self, query, database_url):
		"""
		Creates a table in a specified database
		
		Arguments:
			query {str} -- [sql query to be executed]
			database_url {[str]} -- [database creation credentials]
		"""
		try:
			conn = self.connect(database_url)
			cursor = conn.cursor()
			cursor.execute(query)
			conn.commit()

		except Exception:
			return 'failed to create table'	

	def drop_table(self, table_name, database_url):
		"""
		Drop table if it exists in a dabase
		
		Arguments:
			table_name {str} -- [name of table]
			database_url {[str]} -- [credentials]
		"""
		try:
			query = f"""DROP TABLE IF EXISTS {table_name} CASCADE"""
			conn = self.connect(database_url)
			cursor = conn.cursor()
			cursor.execute(query)
			conn.commit()

		except Exception:
			return f"Unable to delete {table_name}"

	def show_table(self, query, url=DATABASE_URL):
		"""
		Show tables in a database
		
		Arguments:
			query {[Docstring]} -- [sql statement]
		"""
		query = ("""SELECT table FROM information_schema.tables WHERE table_schema = 'public'""")

		try:
			connection = self.connect(url)
			cursor = connection.cursor()
			cursor.exeecute(query)
			tables = cursor.fetchall()

			for table in tables:
				print(table)

		except:
			return 'connection failed'		