from django.contrib import admin
from .models import Issue, Type, Status

# Register your models here.
admin.site.register(Issue)
admin.site.register(Type)
admin.site.register(Status)
