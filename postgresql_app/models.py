from django.db import models
# from django.contrib.postgres.fields import CICharField



class Club(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# one to many relationship
# one driver can have multiple cars
# but any car cannot have more than 1 driver
class Driver(models.Model):
    name = models.TextField()
    license = models.TextField()

class Car(models.Model):
    make = models.TextField()
    model = models.TextField()
    year = models.IntegerField()
    vin = models.TextField()
    owner = models.ForeignKey("Driver", on_delete=models.SET_NULL, null=True)
