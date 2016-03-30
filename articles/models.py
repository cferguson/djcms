from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Article(models.Model):
	title = models.CharField(max_length=100, null=False, blank=False)
	slug = models.SlugField(max_length=255, null=False, blank=False)
	teaser = models.CharField(max_length=255, null=False, blank=False)
	text = models.TextField(null=False, blank=False)
	author = models.ForeignKey(User, null=False, related_name='authored_articles')
	editor = models.ForeignKey(User, null=False, related_name='edited_articles')
	publish_date = models.DateTimeField(null=True)
	created = models.DateTimeField(auto_now_add =True, null=False)
	modified = models.DateTimeField(auto_now=True, null=False)

	class Meta:
		ordering = ['-publish_date']

	def __unicode__(self):
		return self.title

	def save(self):
		if not self.slug:
			obj.slug = slugify(self.title)
		if not self.teaser and self.text:
			self.teaser = self.text[:255]

		super(Article, self).save()


class ArticleView(models.Model):
	article = models.ForeignKey(Article, null=False)
	created = models.DateTimeField(auto_now_add =True, null=False)


class Comment(models.Model):
	article = models.ForeignKey(Article, null=False)
	user = models.ForeignKey(User, null=False)
	created = models.DateTimeField(auto_now_add =True, null=False)
	modified = models.DateTimeField(auto_now=True, null=False)
