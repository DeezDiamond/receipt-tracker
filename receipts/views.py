from django.shortcuts import render
from rest_framework import viewsets 
from .models import Receipt
from .serializers import ReceiptSerializer

# Create your views here.
class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer