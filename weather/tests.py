from unittest import mock
from defer import return_value
from django.test import TestCase
from more_itertools import side_effect

from weather.models import City

# Create your tests here.
class viewsTest(TestCase):

    @mock.patch("weather.views.request_weather", return_value={
        "main": {
            "temp": 12.1,
        },
        "weather": [
            {"icon": "test_icon"},
        ]
    })
    def test_simple(self, request_weather_mock):
        City.objects.create(name="Санкт-Петербург")
        resp = self.client.get("/")
        print(resp.context["all_info"])
    
    @mock.patch("weather.views.request_weather", side_effect=Exception())
    def test_service_error(self):
        # TODO: проверить ответ в случае ошибки ответа сервиса погоды
        pass

    def test_user_post_city(self):
        # TODO: проверить кейс, когда пользователь отправляет город
        pass