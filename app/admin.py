from django.contrib import admin
from app.models import CCBZ
from django.apps import apps

# Register your models here.



class CCBZ_admin(admin.ModelAdmin):
    modelobj = apps.get_model("app","CCBZ")
    filed = modelobj._meta.fields
    list_display = [f.name for f in filed][1:]

admin.site.register(CCBZ,CCBZ_admin)