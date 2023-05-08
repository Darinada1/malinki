from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class TuiAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'availability', 'amount', 'get_photo')
    list_display_links = ('availability', 'price', 'amount')
    search_fields = ('title', 'amount')
    prepopulated_fields = {'slug': ('title',)}

    def get_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=75>")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('choice_thuja',)
    prepopulated_fields = {'slug': ('choice_thuja',)}


admin.site.register(Tui, TuiAdmin)
admin.site.register(Category, CategoryAdmin)
