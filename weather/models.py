from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30)
    # TODO
    # temperature = models.FloatField()
    # weather_icon = models.CharField()
    # date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Create your models here.
