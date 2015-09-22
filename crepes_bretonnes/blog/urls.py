from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^accueil$','home'),
    url(r'^article/(\d+)$','view_article'),
    url(r'^articles/(\d{4})/(\d{2})$','list_articles'),
)
