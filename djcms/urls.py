from django.conf.urls import patterns, include, url
from django.contrib import admin

from articles import views as article_views


urlpatterns = patterns('',
	url(r'^$', article_views.IndexView.as_view(), name='index'),
	url(r'^articles/', include('articles.urls', namespace='articles')),
    url(r'^admin/', include(admin.site.urls)),
)
