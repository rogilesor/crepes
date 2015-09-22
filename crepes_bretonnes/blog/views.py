from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect



def home(request):
    """Exemple de page html, non valide pour que l'exemple soit concis"""
    text="""<h1>Bienvenue sur mon blog!</h1>
            <p>Les crêpes bretonnes ça tue des mouettes en plein vol!</p>"""
    return HttpResponse(text)

# Create your views here.

# def view_article(request, id_article):
#     """Vue qui affiche un article selon son identifiant (ou ID, ici un numero)
#        Son ID est le second parametre de la fonction (pour rappel, le premier parametre est toujours la requete de l'utilisateur)"""
#     text = "Vous avez demande l'article #{2} !".format(id_article)
#     return HttpResponse(text)

def view_article(request, id_article):
    #si l'ID est superieur à 100 nous considerons que l'article n'existe pas
    if int(id_article) > 100:
        raise Http404
    return redirect(view_redirection)

def view_redirection(request):
    return HttpResponse("vous avez été redirigé")

# def list_articles(request, month, year):
#     """Liste des articles d'un mois précis"""
#     text = "Vous avez demandé les articles de {0} {1}".format(month,year)
#     return HttpResponse(text)

def list_articles(request, month, year):
    """Liste des articles d'un mois précis"""
    return redirect("https://www.djangoproject.com")