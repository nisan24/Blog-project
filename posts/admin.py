from django.contrib import admin
from .models import PostModel

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    search_fields = ('title', 'author__username', 'author__email')

admin.site.register(PostModel, PostAdmin)
# admin.site.register(PostModel)