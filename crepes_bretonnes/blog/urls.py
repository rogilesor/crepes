from django.conf.urls import patterns, url
from django.conf import settings


urlpatterns = patterns('blog.views',
    url(r'^$','accueil'),
    url(r'^article/(?P<id>\d+)-(?P<slug>.+)$','lire'),
#    url(r'^article/(\d+)$','view_article'),
    url(r'^article/(?P<id_article>\d+)$','view_article'),
#    url(r'^articles/(\d{4})/(\d{2})$','list_articles'),
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})$','list_articles'),
    url(r'^redirection$','view_redirection'),
    url(r'^date$','date_actuelle'),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$','addition'),
    url(r'^test$','affiche_temp'),
    url(r'^contact/$','nouveau_contact'),
    url(r'^Vcontact$','voir_contacts'),
    url(r'^Earticle/$','art_model'),
    # url(settings.MEDIA_URL,settings.MEDIA_ROOT),
)

# urlpatterns += ( settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
