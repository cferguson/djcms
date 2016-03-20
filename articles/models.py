from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
	title = models.CharField(max_length=255, null=False, blank=False)
	slug = models.SlugField(max_length=255, null=False, blank=False)
	text = models.TextField(null=False, blank=False)
	created = models.DateTimeField(auto_now_add =True, null=False)
	modified = models.DateTimeField(auto_now=True, null=False)


class ArticleView(models.Model):
	article = models.ForeignKey(Article, null=False)
	created = models.DateTimeField(auto_now_add =True, null=False)
