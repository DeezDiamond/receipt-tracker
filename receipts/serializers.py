from rest_framework import serializers
from .models import Receipt

class ReceiptSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = "user.email")
    class Meta:
        model = Receipt
        fields = ("id", "retailer", "date", "amount", "receipt_image", "items", "user")