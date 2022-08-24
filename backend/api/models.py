from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
import random
from threading import Timer
from datetime import datetime, timedelta
from django.utils.crypto import get_random_string

# Create your models here.

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
phone_number = RegexValidator(r'^\+?1?\d{9,15}$', "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

def qrcode_location(instance, filename):
    return '%s/qr_codes/%s/' % (instance.user.first_name, filename)

class Bus(models.Model):
    registration = models.CharField(max_length=20, blank=False, unique=True, validators=[alphanumeric])
    capacity = models.IntegerField()

    class Meta:
        managed = True
        verbose_name = 'Bus'
        verbose_name_plural = 'Buses'
    
    

    def __str__(self):
        return self.registration

    def __unicode__(self):
        return 

class Trip(models.Model):
    
    class TripType(models.TextChoices):
        MORNING = 'Morning'
        EVENING = 'Evening'

    trip_type = models.CharField(max_length=12, choices=TripType.choices)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)

    def __str__(self):
        return 

    def __unicode__(self):
        return 


class Location(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField(verbose_name='cost')
    

    def __str__(self):
        return self.name

class Route(models.Model):
    locations = models.ForeignKey(Location, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.id

    def __unicode__(self):
        return 



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    upi_no = models.CharField(max_length=20, blank=False, unique=True, validators=[alphanumeric])
    first_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    grade = models.CharField(max_length=20, blank=False, validators=[alphanumeric])
    stream = models.CharField(max_length=25)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.first_name

    def __unicode__(self):
        return 

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name="child", on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    phone = models.CharField(max_length=20, blank=False, validators=[phone_number])


    def __str__(self):
        return self.first_name

    def __unicode__(self):
        return 

class Receipt(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    active = models.BooleanField(verbose_name='Valid', default=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    issued = models.DateTimeField(editable=False, serialize=True)
    serial = models.CharField(max_length=8, blank=False, default=get_random_string(8))
    qr_code = models.ImageField(blank=True, upload_to='qrcode_location')
    
    class ReceiptType(models.TextChoices):
        WEEKLY = 'Weekly'
        MONTHLY = 'Monthly'
        QUARTERLY ='Quarterly'
        ANNUALY = 'Annual'

    receipt_type = models.CharField(max_length=12, choices=ReceiptType.choices)

    

    def __str__(self):
        return self.serial

    def __unicode__(self):
        return

    def save(self,*args,**kwargs):
      qrcode_img=qrcode.make(self.issued)
      canvas=Image.new("RGB", (310,310),"white")
      ImageDraw.Draw(canvas)
      canvas.paste(qrcode_img)
      buffer=BytesIO()
      canvas.save(buffer,"PNG")
      self.image.save(f'{self.student}-{self.issued}-{self.location}-{self.id}',File(buffer),save=False)
      canvas.close()
      super().save(*args,**kwargs)


    nextDay = datetime.now() + timedelta(days=1)
    dateString = nextDay.strftime('%d-%m-%Y') + " 01-00-00"
    newDate = nextDay.strptime(dateString,'%d-%m-%Y %H-%M-%S')
    delay = (newDate - datetime.now()).total_seconds()
    def set_active(self, *args, **kwargs):
        if self.receipt_type in ['weekly', 'WEEKLY', 'Weekly']:
            if self.issued-self.nextDay>=7:
                self.active=False
        if self.receipt_type in ['monthly', 'MONTHLY', 'Monthly']:
            if self.issued-self.nextDay>=30:
                self.active=False
        elif self.receipt_type in ['quarterly', 'QUARTERLY', 'Quarterly']:
            if self.issued-self.nextDay>=90:
                self.active=False
        else:
            if self.issued-self.nextDay>=366:
                self.active=False 

    Timer(delay, set_active,()).start()

