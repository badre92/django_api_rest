from django.http                    import HttpResponse
from django.http                    import JsonResponse
from django.views.decorators.csrf   import csrf_exempt
from rest_framework.renderers       import JSONRenderer
from rest_framework.parsers         import JSONParser
from prediction.models              import House
from prediction.serializers         import HouseSerializer

def predict_medv(unscaled_data):
    from sklearn.externals import joblib
    colonnes        = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM",
                        "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B",
                        "LSTAT"]
    path_to_model   = "./ipynb/model_svr.pkl"
    path_for_scaler = "./ipynb/scaler.pkl"
    unscaled_data   = [unscaled_data[colonne] for colonne in colonnes]
    model           = joblib.load(path_to_model)
    scaler          = joblib.load(path_for_scaler)
    donnees_scalees = scaler.transform(unscaled_data)
    medv            = model.predict(donnees_scalees)
    return medv


@csrf_exempt
def predict(request):
    """
    Renvoie une house avec la MEDV completee
    (Attend une MEDV innexistante)
    """
    if request.method == 'GET':
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'POST':
        data        = JSONParser().parse(request)
        serializer  = HouseSerializer(data=data)
        if serializer.is_valid():
            data["MEDV"]        = predict_medv(data)
            serializer          = HouseSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data  , status=201)
        return     JsonResponse(serializer.errors, status=400)

@csrf_exempt
def house_list(request):
    """
    List all houses, or create a new house.
    """
    if request.method == 'GET':
        houses      = House.objects.all()
        serializer  = HouseSerializer(houses        , many=True)
        reponse     = JsonResponse(serializer.data  , safe=False)
        return reponse

    elif request.method == 'POST':
        data        = JSONParser().parse(request)
        serializer  = HouseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data  , status=201)
        return     JsonResponse(serializer.errors, status=400)

@csrf_exempt
def house_detail(request, pk):
    """
    Retrieve, update or delete a house.
    """
    try:
        house = House.objects.get(pk=pk)
    except House.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HouseSerializer(house)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = HouseSerializer(house, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        house.delete()
        return HttpResponse(status=204)