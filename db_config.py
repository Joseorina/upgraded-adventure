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