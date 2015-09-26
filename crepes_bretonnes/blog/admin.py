from django.contrib import admin
from blog.models import Categorie, Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre','categorie','auteur','date')
    list_filter  = ('auteur','categorie',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre','contenu')

admin.site.register(Categorie)
admin.site.register(Article,ArticleAdmin)
