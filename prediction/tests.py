""" Python core """
import random

""" Django Framework"""
from django.core.urlresolvers   import resolve
from django.http                import HttpRequest
from django.utils.six           import BytesIO

""" DjangoRestFramework"""
from rest_framework.test        import APITestCase
from rest_framework.parsers     import JSONParser

""" Django specific """
from prediction.views           import house_list
from prediction.views           import house_detail
from prediction.models          import House
from prediction.serializers     import HouseSerializer
class Test_Houses_database(APITestCase):
    def setUp(self):
        for i in range(10):
            house = House(CRIM      =   0.02731 * (1 + random.random() ),
                          ZN        =   0.0     * (1 + random.random() ),
                          INDUS     =   7.07    * (1 + random.random() ),
                          CHAS      =   0.0     * (1 + random.random() ),
                          NOX       =   0.469   * (1 + random.random() ),
                          RM        =   6.421   * (1 + random.random() ),
                          AGE       =   78.9    * (1 + random.random() ),
                          DIS       =   4.9671  * (1 + random.random() ),
                          RAD       =   2.0     * (1 + random.random() ),
                          TAX       =   242.0   * (1 + random.random() ),
                          PTRATIO   =   17.8    * (1 + random.random() ),
                          B         =   396.9   * (1 + random.random() ),
                          LSTAT     =   9.14    * (1 + random.random() ),
                          )
            house.save()

    def test_url_pattern_for_houses_exists(self):
        found = resolve("/houses/")
        self.assertEqual(found.func, house_list)

    def test_url_pattern_for_one_specific_house_exists(self):
        found = resolve("/house/1/")
        self.assertEqual(found.func, house_detail)

    def test_houses_url_return_10_houses(self):
        request         = HttpRequest()
        request.method  = "GET"
        response        = house_list(request)
        stream          = BytesIO(response.content)
        data            = JSONParser().parse(stream)
        houses          = HouseSerializer(data=data, many=True)

        if houses.is_valid():
            assert 10 == len(houses.validated_data)



    def test_get_an_house(self):
        response    = self.client.get('/house/1/')
        stream      = BytesIO(response.content)
        data        = JSONParser().parse(stream)
        house       = HouseSerializer(data=data, many=True)

        if house.is_valid():
            assert 1 == len(house.validated_data)
