from django.contrib import admin
from .models import Studendts
from .models import scores

# Register your models here.
@admin.register(Studendts)
class StudendtsAdmin(admin.ModelAdmin):
    pass

@admin.register(scores)
class scoresAdmin(admin.ModelAdmin):
    pass