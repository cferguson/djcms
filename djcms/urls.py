from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^articles/', include('articles.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
