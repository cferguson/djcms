from rest_framework import routers, serializers

from django.contrib.auth.models import User
from articles.models import Article


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username')


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    editor = UserSerializer(required=False)

    class Meta:
        model = Article
        fields = (
        	'title', 'slug', 'teaser', 'text',
        	'author', 'editor', 'publish_date',
        )