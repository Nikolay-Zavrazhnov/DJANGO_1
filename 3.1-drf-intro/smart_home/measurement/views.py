# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response


from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorInfoSerializer

#создание датчика(PATCH) а также получение инфрмации по датчикам(GET)
class SensorCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorInfoSerializer

# добавление измерения(POST)
class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

#Обновление (PATCH) а также получение информации по конкретному датчику(GET)
class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorInfoSerializer










