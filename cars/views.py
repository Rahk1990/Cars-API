
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CarSerializer
from .models import Car



# Create your views here.

@api_view(['GET'])  
def car_list(request):

    cars = Car.objects.all() 

    serializers = CarSerializer(cars, many=True)

    return Response(serializers.data) 

    