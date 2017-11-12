import pymongo


class Mongo_Work(object):
	"""A class for working with mongodb"""

	def __init__(self):
		self.con = pymongo.Connection()

	def make_database(self, db_name):
		# self.db_name = db_name
		self.db = self.con.db_name

	def inser_data(self, data):
		self.db.insert(data)

	def quary_data(self, data_field):
		return self.db.find()
















if __name__ == "__main__":
	print('Inside the __main__')
