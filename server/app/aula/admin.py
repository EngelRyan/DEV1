from django.contrib import admin
from .models.person import *
from .models.passport import *


admin.site.register(Person)
admin.site.register(Passport)
