from django.urls import path
from .views import cal_distance_view

app_name = 'state'

urlpatterns = [
    path('', cal_distance_view, name='calculate_view'),
]
