from django.contrib import admin
from .models import usuarios,Room,Message
# Register your models here.


admin.site.register(usuarios)
admin.site.register(Room)
admin.site.register(Message)