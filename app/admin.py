from django.contrib import admin

from app.models import Content


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_published', 'title', 'author', )
    list_display_links = ('title', )
    list_editable = ('is_published', )
    list_filter = ('title', )
    list_per_page = 10
    prepopulated_fields = {"slug": ('title', )}
