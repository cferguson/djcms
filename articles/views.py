from django.views import generic
from articles import models


class IndexView(generic.ListView):
	template_name = 'article/index.html'

	def get_queryset(self):
		return models.Article.objects.order_by('-id')[:5]


class DetailView(generic.DetailView):
	model = models.Article
	template_name = 'article/detail.html'
