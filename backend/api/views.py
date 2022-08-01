from .serializers import *
from .models import *
from rest_framework import generics, viewsets, permissions


class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StudentSerializer

    
class ParentViewset(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ParentSerializer


class BusViewset(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BusSerializer


class ReceiptViewset(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReceiptSerializer