from django.views import generic
from articles import models


class IndexView(generic.ListView):
	template_name = 'article/index.html'

	def get_queryset(self):
		return models.Article.objects.order_by('-id')[:25]


class DetailView(generic.DetailView):
	model = models.Article
	template_name = 'article/detail.html'
	
	query_pk_and_slug = True
	slug_url_kwarg = 'slug'

	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		context['comments'] = models.Comment.objects.filter(article=self.get_object())

		return context
