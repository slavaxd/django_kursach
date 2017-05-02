from django.contrib import admin

from .models import *


admin.site.register(Team)
admin.site.register(Bike)
admin.site.register(Participant)
admin.site.register(Coach)
admin.site.register(Organizator)
admin.site.register(Competition)


# Register your models here.
