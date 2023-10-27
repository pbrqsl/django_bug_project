from django.contrib import admin
from .models import Project, User, Bug

# Register your models here.
admin.site.register([Project, User, Bug])
