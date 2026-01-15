from django.contrib import admin
from .models import (
    Subject, Course, Module, Text, ContentBase, OrderedContent,
    TextItem, File, Image, Video
)


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    search_fields = ['title', 'body']


@admin.register(ContentBase)
class ContentBaseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    search_fields = ['title']


@admin.register(OrderedContent)
class OrderedContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'created_delta']
    search_fields = ['title']
    # Note: OrderedContent is a proxy model, so it operates on the same
    # database table as ContentBase but with different ordering and methods


@admin.register(TextItem)
class TextItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created', 'updated']
    list_filter = ['created', 'updated']
    search_fields = ['title', 'content']
    raw_id_fields = ['owner']


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created', 'updated']
    list_filter = ['created', 'updated']
    search_fields = ['title']
    raw_id_fields = ['owner']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created', 'updated']
    list_filter = ['created', 'updated']
    search_fields = ['title']
    raw_id_fields = ['owner']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'url', 'created', 'updated']
    list_filter = ['created', 'updated']
    search_fields = ['title', 'url']
    raw_id_fields = ['owner']

