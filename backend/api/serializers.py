from django.utils import timezone
from rest_framework.serializers import ModelSerializer, StringRelatedField, DateTimeField, ImageField
from .models import Student, Parent, Receipt, Bus
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File



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
        fields = ['bus', 'active', 'student', 'issued']

class StudentSerializer(ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

