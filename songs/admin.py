from django.contrib import admin
from .models import Category, Song, Album

# Register your models here.
admin.site.register(Category)
admin.site.register(Song)
admin.site.register(Album)
