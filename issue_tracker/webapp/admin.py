from django.contrib import admin
from .models import Issue, Type, Status


# Register your models here.
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'author', 'created_at']
#     list_filter = ['author']
#     search_fields = ['title', 'content']
#     fields = ['title', 'author', 'content', 'created_at', 'updated_at']
#     readonly_fields = ['created_at', 'updated_at']

class IssueAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'status', 'type']
    readonly_fields = ['create_at', 'update_at']
    # list_filter = ['summary']
    search_fields = ['summary']


admin.site.register(Issue, IssueAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Type, TypeAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Status, StatusAdmin)
