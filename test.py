import unittest

from app import db
from app import create_app
from config import config

class TestAPI(unittest.TestCase):

	def setUp(self):
		enviroment = config['test']
		self.app = create_app(enviroment)
		self.client = self.app.test_client()

		self.content_type = 'application/json'
		self.path = 'http://localhost:5000/api/v1/tasks'

	def tearDown(self):
		with self.app.app_context():
			db.drop_all()	

	def test_one_equals_one(self):
		self.assertEqual(1,1)

'''	def test_get_all_tasks(self):	
		response = self.client.get(path=self.path)
		self.assertEqual(response.status_code,200)
'''
if __name__ == '__main__':		
	unittest.main()