from django.urls import path, include
import weather.views as views

urlpatterns = [
    path('', views.index, name="weather_index"),
]