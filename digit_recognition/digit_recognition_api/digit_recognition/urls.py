from django.urls import path
from .views import predict_digit_api

urlpatterns = [
    path('predict_digit/', predict_digit_api, name='predict_digit_api'),
]