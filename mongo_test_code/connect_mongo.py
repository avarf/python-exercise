# from pymongo import Connection
from pymongo import MongoClient

"""
class Mongo_Work(object):
"""
"""A class for working with mongodb"""
"""
	def __init__(self):
		self.con = pymongo.Connection()

	def make_database(self, db_name):
		# self.db_name = db_name
		self.db = self.con.db_name

	def show_all_databases(self):
		self.con.showdbs()

	def inser_data(self, data):
		self.db.insert(data)

	def quary_data(self, data_field):
		return self.db.find()
"""




if __name__ == "__main__":
	print('Inside the __main__')

	# con = Connection()
	con = MongoClient()
	# creating database
	db = con.test_db
	# creating dataset
	# collection = db.ds_test

	# members is a collection
	# result = db.members.insert_one({
	# 	'name': 'Ali',
	# 	'family':'varfan',
	# 	'sex':'male',
	# 	'mem_id': '1'
	# 	})
	# result2 = db.members.insert_one({
	# 	'name': 'Selale',
	# 	'family':'Ozbay',
	# 	'sex':'female',
	# 	'id':'2'
	# 	})
	# print(result2)
	docs = db.members.find()
	for d in docs:
		print(docs)


	# db.insert({
	# 	'name': 'Ali',
	# 	'family':'varfan',
	# 	'sex':'male'
	# 	})

	# db.insert({
	# 	'name': 'Selale',
	# 	'family':'Ozbay',
	# 	'sex':'female'
	# 	})

	# records = db.find()

	# print('Records in db:')
	# for rec in records:
	# 	print(rec)

	print('Finished')
