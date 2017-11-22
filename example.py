from prediction.models          import House
from prediction.serializers     import HouseSerializer
from rest_framework.parsers     import JSONParser
from rest_framework.renderers   import JSONRenderer

house = House(  CRIM     = 0.02731 ,
                ZN       = 0.0     ,
                INDUS    = 7.07    ,
                CHAS     = 0.0     ,
                NOX      = 0.469   ,
                RM       = 6.421   ,
                AGE      = 78.9    ,
                DIS      = 4.9671  ,
                RAD      = 2.0     ,
                TAX      = 242.0   ,
                PTRATIO  = 17.8    ,
                B        = 396.9   ,
                LSTAT    = 9.14    ,
                #MEDV     =
)
house.save()

serializer = HouseSerializer(house)
serializer.data

content = JSONRenderer().render(serializer.data)
content


from django.utils.six import BytesIO

stream = BytesIO(content)
data = JSONParser().parse(stream)


serializer = HouseSerializer(data=data)
serializer.save()


#house = HouseSerializer(data=data)
#print("Données pour créer la maison sont valide ? : %s "%(house.is_valid()))
#print("Données validées : %s"%(house.validated_data))
#house.save()#on enregistre la maison

house = HouseSerializer(data=data)
if house.is_valid():
    house.save()


