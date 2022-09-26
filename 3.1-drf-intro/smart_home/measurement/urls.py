from django.urls import path

from measurement.views import SensorCreateView, MeasurementCreateView, SensorView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorCreateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),

]
