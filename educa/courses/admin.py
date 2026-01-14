from django.contrib import admin
from .models import Subject, Course, Module, Text


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

