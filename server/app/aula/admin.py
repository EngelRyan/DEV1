from django.contrib import admin
from .models.person import *
from .models.passport import *
from .models.reporter import *
from .models.article import *
from .models.magazine import *


admin.site.register(Person)
admin.site.register(Passport)
admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Magazine)
