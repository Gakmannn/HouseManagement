from django.db import models

class House(models.Model):
  counryCode = models.CharField(max_length=3)
  city = models.CharField(max_length=50)
  street = models.CharField(max_length=50)
  house = models.CharField(max_length=15)
  def __str__(self):
    return f'{self.counryCode}, {self.city}, {self.street}, {self.house}'
    
class Apartment(models.Model):
  house = models.ForeignKey(House, on_delete=models.PROTECT)
  apartment = models.CharField(max_length=10)
  square = models.FloatField()
  def __str__(self):
    return f'{self.house.counryCode}, {self.house.city}, {self.house.street}, {self.house.house}, {self.apartment}'
    

