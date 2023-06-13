from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Photography, Consultation


class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'communication_method', 'get_html_photo')

    def get_html_photo(self, object):
        if object.file:
            return mark_safe(f"<img src='{object.file.url}' width=50>")

    get_html_photo.short_description = 'image'


class PhotographyAdmin(admin.ModelAdmin):
    list_display = ("category", "get_html_photo")

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_html_photo.short_description = 'image'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Photography, PhotographyAdmin)
admin.site.register(Consultation, ConsultationAdmin)
