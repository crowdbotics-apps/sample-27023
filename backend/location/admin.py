from django.contrib import admin
from .models import TaskerLocation, MapLocation, CustomerLocation, TaskLocation

admin.site.register(TaskLocation)
admin.site.register(MapLocation)
admin.site.register(CustomerLocation)
admin.site.register(TaskerLocation)

# Register your models here.
