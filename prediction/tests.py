from django.test                import TestCase
from prediction.views           import house_list
from django.core.urlresolvers   import resolve
# Create your tests here.
class Test_Houses_database(TestCase):

    def test_url_houses_exists(self):
        found = resolve("/houses/")
        self.assertEqual(found.func, house_list)




