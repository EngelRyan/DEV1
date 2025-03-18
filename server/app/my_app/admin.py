from django.contrib import admin
from .models.tag import Tag
from .models.example import Example

admin.site.register(Tag)
admin.site.register(Example)
