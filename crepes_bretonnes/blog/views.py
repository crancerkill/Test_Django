from django.shortcuts import render

# Create your views here.
#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404

def home(request):
  text = """<h1>Bienvenue sur mon blog !</h1>
            <p>Les crèpes bretonnes ça tue des mouettes en plein vol !</p>"""
  return HttpResponse(text)

def view_article(request, id_article):
    # Vue qui affiche un article selon son identifiant (ou ID, ici un numéro). Son ID est le second paramètre de la fonction 
    #    (pour rappel, le premier paramètre est TOUJOURS la requête de l'utilisateur) 
    if int(id_article) > 100:
		raise Http404
	else
		text = "Vous avez demandé l'article n°{0} !".format(id_article)
		return HttpResponse(text)
def list_articles(request, month, year):
    # Liste des articles d'un mois précis. 

    text = "Vous avez demandé les articles de {0} {1}.".format(month, year)
    return HttpResponse(text)
