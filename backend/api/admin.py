from django.contrib import admin
from .models import Bus, Location, Route, Student, Parent, Receipt, Trip

# Register your models here.

admin.site.register(Bus)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Receipt)
admin.site.register(Location)
admin.site.register(Route)
admin.site.register(Trip)