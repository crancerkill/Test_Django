from django.conf.urls import url

from blog import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^article/(?P<id_article>\d+)/$', views.view_article, name='view_article'), # Vue d'un article
	url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', views.list_articles, name='list_articles'), # Vue des articles d'un mois précis
]
