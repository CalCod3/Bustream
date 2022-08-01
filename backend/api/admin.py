from django.contrib import admin
from .models import Bus, Student, Parent, Receipt

# Register your models here.

admin.site.register(Bus)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Receipt)