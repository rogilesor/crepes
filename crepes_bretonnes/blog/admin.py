from django.contrib import admin
from blog.models import Categorie, Article

class ArticleAdmin(admin.ModelAdmin):
    list_display   = ('titre', 'categorie', 'auteur', 'date', 'apercu_contenu')
    list_filter    = ('auteur','categorie', )
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('titre', 'contenu')
    # fields = ('titre', 'slug', 'auteur', 'categorie', 'contenu')
    fieldsets = (
        ('Général',{
            'classes':['collapse',],
            'fields':('titre','slug','auteur','categorie')
            }),
        ('Contenu de l\'article',{
            'description':'Le formulaire accepte les balises HTML',
            'fields':('contenu',)
            }),
        )


    def apercu_contenu(self, article):
        text = article.contenu
        textReduit = article.contenu[0:40]
        if len(article.contenu) > 40:
            return '%s…' % textReduit
        else:
            return text
        # return text

    # En-tête de notre colonne
    apercu_contenu.short_description = 'Aperçu du contenu'
    prepopulated_fields = {'slug': ('titre', ), }


admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)