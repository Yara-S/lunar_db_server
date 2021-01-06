import psycopg2
import os


class DatabaseHandler():
	def __init__(self):

		self.host = os.environ.get('DB_HOST')
		self.database = os.environ.get('DB_DATABASE')
		self.user = os.environ.get('DB_USER')
		self.pwd = os.environ.get('DB_PWD')


		try: 

			conn = psycopg2.connect(
			    host=self.host,
			    database=self.database,
			    user=self.user,
			    password=self.pwd
			)
			self.cur = conn.cursor()

		except Exception as e:
			raise Exception(e)

	def query(self, query):
		self.cur.execute(query)
		return self.cur.fetchall()

