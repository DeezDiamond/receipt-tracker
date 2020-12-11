from rest_framework import serializers
from .models import Receipt

class ReceiptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receipt
        field = ("retailer", "date", "amount", "receipt_image", "items")