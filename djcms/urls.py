from django.conf.urls import patterns, include, url
from django.contrib import admin

from articles import views as article_views
from articles import api as article_api


api_urls = patterns('',

	# articles
    url(r'article/(?P<pk>\d+)$', article_api.ArticleDetail.as_view(), name='article-detail'),
    url(r'articles$', article_api.ArticleList.as_view(), name='article-list')
    
)

urlpatterns = patterns('',

	# homepage
	url(r'^$', article_views.IndexView.as_view(), name='index'),

	# api
	url(r'^api', include(api_urls)),
	
	# views
	url(r'^articles/', include('articles.urls', namespace='articles')),

	# admin
    url(r'^admin/', include(admin.site.urls)),

)
