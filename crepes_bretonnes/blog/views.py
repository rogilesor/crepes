from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    """Exemple de page html, non valide pour que l'exemple soit concis"""
    text="""<h1>Bienvenue sur mon blog!</h1>
            <p>Les crêpes bretonnes ça tue des mouettes en plein vol!</p>"""
    return HttpResponse(text)

# Create your views here.
