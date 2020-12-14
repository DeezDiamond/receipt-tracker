from django.db import models
from users.models import User
from django.db.models.signals import post_save

# Create your models here.
class Receipt(models.Model):
    retailer = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    receipt_image = models.ImageField(upload_to="images/", default="receipt_holder.png")
    items = models.CharField(max_length=1000)

    user = models.ForeignKey(User, related_name='receipts', on_delete=models.CASCADE)