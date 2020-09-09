from django.contrib import admin
from .models import FavoriteGroup
from .models import Favorite
from .models import TodoGroup
from .models import Todo

# Register your models here.
@admin.register(FavoriteGroup)
class FavoriteGroupAdmin(admin.ModelAdmin):
    pass

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    pass

@admin.register(TodoGroup)
class TodoGroupAdmin(admin.ModelAdmin):
    pass

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass