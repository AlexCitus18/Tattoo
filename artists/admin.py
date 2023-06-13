from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Artist


class ArtistAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "get_html_photo", "description")

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_html_photo.short_description = 'image'


admin.site.register(Artist, ArtistAdmin)
