from unittest import TestCase

from chicago import ZIP_CODES


class ZipCodeTestCase(TestCase):
    def test_get_by_zip(self):
        zip_code = ZIP_CODES.get_by_zip('60651')
        self.assertEqual(zip_code.zip, '60651')

    def test_get_by_zip_number(self):
        zip_code = ZIP_CODES.get_by_zip(60651)
        self.assertEqual(zip_code.zip, '60651')

    def test_is_chicago(self):
        self.assertEqual(ZIP_CODES.is_chicago('60651'), True)
        self.assertEqual(ZIP_CODES.is_chicago('61201'), False)
