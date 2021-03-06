from django.conf.urls import url
from articles import views


urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[a-zA-Z0-9-]+)/$', views.DetailView.as_view(), name='detail'),
]