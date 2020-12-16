from django.shortcuts import render
from rest_framework import viewsets, permissions 
from .models import Receipt
from .serializers import ReceiptSerializer
from .permissions import IsOwner

# Create your views here.
class ReceiptViewSet(viewsets.ModelViewSet):
    serializer_class = ReceiptSerializer
    permission_classes = [IsOwner]

    def get_queryset(self, *args, **kwargs): 
        return Receipt.objects.all().filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def patch(self, request, pk):
        receipt = self.get_object(pk)
        serializer = ReceiptSerializer(receipt, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(code=201, data=serializer.data)
        return JsonResponse(code=400, data="wrong parameters")