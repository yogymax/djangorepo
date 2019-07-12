from django.db import models

# Create your models here.

class Ven(models.Model):
   name = models.CharField(max_length = 50)
   address = models.CharField(max_length = 50)

   class Meta:
      db_table = "ven_info"



class RainySeason(models.Model):
   name = models.CharField(max_length = 50)
   barcode = models.CharField(max_length = 50)
   model = models.CharField(max_length = 50)
   price = models.FloatField()
   qty = models.IntegerField()
   active = models.BooleanField()
   vendor = models.ForeignKey(Ven, on_delete=models.CASCADE)

   class Meta:
      db_table = "cloths_info"


