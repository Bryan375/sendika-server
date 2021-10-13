from django.contrib import admin
from .models import MLModel

class MLAdmin(admin.ModelAdmin):
    list_display = ('smile_name', 'result')

# Register your models here.
admin.site.register(MLModel, MLAdmin)