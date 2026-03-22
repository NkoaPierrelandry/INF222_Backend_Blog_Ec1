from django.contrib import admin
from .models import Article

# Register your models here.

class AdminArticle(admin.ModelAdmin):
    list_display = ('name','title','contenu','autor','date','category','date')

admin.site.register(Article,AdminArticle)
