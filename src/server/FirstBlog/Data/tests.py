from django.test import TestCase
from Data.models import data

class dataTestCase(TestCase):
	def setUp(self):
		data.objects.create(name='unitTest1', sex='M', age='29',active='true', tags='hello, this is unit test1!')
		data.objects.create(name='unitTest2', sex='F', age='29',active='false', tags='hello, this is unit test2!')

	def test_data_can_be_made(self):
		"""test data model is working right"""
		print("\nTest 1")
		datas = data.objects.all()
		self.assertEqual(2, len(datas) )
		print("OK...data model can be created\n")

	def test_data_can_insert_into_db(self):
		print("Test 2")
		test_case3 = data.objects.create(name='unitTest3', sex='F', age='19',active='true', tags='hello, this is unit test3!')
		test_case3.save();
		self.assertEqual(3, data.objects.count())
		print("OK...data model can be saved into database\n")

	def test_invalid_data(self):
		print("Test 3")
		test_case4 = data.objects.create(name='unitTest3', sex='F', age='19',active='xxx', tags='hello, this is unit test3!')
		test_case4.save();
		self.assertEqual(3, data.objects.count())
		print("OK...invalid input will not be saved into database\n")

	def test_empty_dababase(self):
		print("Test 4")
		data.objects.all().delete()
		self.assertEqual(0, data.objects.count())
		print("OK...Empty databse successful\n")