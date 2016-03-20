from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify


class Article(models.Model):
	title = models.CharField(max_length=255, null=False, blank=False)
	slug = models.SlugField(max_length=255, null=False, blank=False)
	text = models.TextField(null=False, blank=False)
	created = models.DateTimeField(auto_now_add =True, null=False)
	modified = models.DateTimeField(auto_now=True, null=False)

	def save(self):
		if not self.slug:
			obj.slug = slugify(self.title)
		super(Article, self).save()


class ArticleView(models.Model):
	article = models.ForeignKey(Article, null=False)
	created = models.DateTimeField(auto_now_add =True, null=False)
