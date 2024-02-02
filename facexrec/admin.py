from django.contrib import admin
from . import models
from django.utils.html import format_html,urlencode
from django.urls import reverse
from django.db.models.aggregates import Count
# Register your models here.

admin.site.register(models.Department)
admin.site.register(models.Year)
admin.site.register(models.Div)
admin.site.register(models.Student)
admin.site.register(models.Present)


