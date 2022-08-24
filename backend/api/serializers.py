from django.utils import timezone
from rest_framework.serializers import ModelSerializer
from .models import Location, Route, Student, Parent, Receipt, Bus, Trip




class BusSerializer(ModelSerializer):

    class Meta:
        model = Bus
        fields = '__all__'

class ParentSerializer(ModelSerializer):

    class Meta:
        model = Parent
        fields = '__all__'

class ReceiptSerializer(ModelSerializer):
    
    class Meta:
        model = Receipt
        fields = ['student', 'bus', 'location', 'active', 'issued']

class StudentSerializer(ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

class LocationSerializer(ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

class RouteSerializer(ModelSerializer):

    class Meta:
        model = Route
        fields = '__all__'

class TripSerializer(ModelSerializer):

    class Meta:
        model = Trip
        fields = '__all__'
