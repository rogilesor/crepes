from django.conf.urls import patterns, url

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
    url(r'^contact/$','contact'),
    url(r'^Earticle/$','art_model'),
)
