from django.contrib import admin
from .models import Post, Tecnologia

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'titulo', 'autor',


@admin.register(Tecnologia)
class TecnlogiaAdmin(admin.ModelAdmin):
    list_display = 'nome', 