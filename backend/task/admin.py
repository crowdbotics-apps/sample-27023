from django.contrib import admin
from .models import Message, Task, Rating, TaskTransaction

admin.site.register(Rating)
admin.site.register(Message)
admin.site.register(TaskTransaction)
admin.site.register(Task)

# Register your models here.
