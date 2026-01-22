from django.contrib import admin

# Register your models here.

from django.utils.html import format_html
from .models import PromptTemplate


# I use "format_html" to display the actual preview image in the list view so i don't have to click into each one to see what it looks like.

@admin.register(PromptTemplate)
class PromptTemplateAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_preview', 'name', 'created_at')
    search_fields = ('name', 'prompt_text')

    def thumbnail_preview(self, obj):
        if obj.preview_image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />', obj.preview_image.url)
        return "No Image"
    
    thumbnail_preview.short_description = 'Preview'