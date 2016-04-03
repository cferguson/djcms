from django.contrib import admin
from models import Article, Comment, Channel


class ArticleAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


class ChannelAdmin(admin.ModelAdmin):
	readonly_fields = ('created_by',)

	def save_model(self, request, obj, form, change):
		obj.created_by = request.user
		obj.save()


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Channel, ChannelAdmin)