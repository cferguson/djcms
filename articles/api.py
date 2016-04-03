from rest_framework import generics, permissions

from articles.models import Article
from articles.serializers import ArticleSerializer


class ArticleList(generics.ListCreateAPIView):
    model = Article
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [
    	permissions.AllowAny
    ]


class ArticleDetail(generics.RetrieveAPIView):
	model = Article
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	lookup_field = 'pk'
