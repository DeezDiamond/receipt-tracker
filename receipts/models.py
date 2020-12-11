from django.db import models

# Create your models here.
class Receipt(models.Model):
    retailer = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    receipt_image = models.ImageField(upload_to="images/")
    items = models.CharField(max_length=1000)