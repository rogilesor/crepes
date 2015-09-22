from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    """Exemple de page html, non valide pour que l'exemple soit concis"""
    text="""<h1>Bienvenue sur mon blog!</h1>
            <p>Les crêpes bretonnes ça tue des mouettes en plein vol!</p>"""
    return HttpResponse(text)

# Create your views here.

def view_article(request, id_article):
    """Vue qui affiche un article selon son identifiant (ou ID, ici un numero)
       Son ID est le second parametre de la fonction (pour rappel, le premier parametre est toujours la requete de l'utilisateur)"""
    text = "Vous avez demande l'article #{0} !".format(id_article)
    return HttpResponse(text)
