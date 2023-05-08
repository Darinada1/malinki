from .models import Tui, Category
from django.db import *
menu = [
    {'title': 'главная', 'url_name': 'home'},
    {'title': 'о нас', 'url_name': 'about'},
    {'title': 'контакты', 'url_name': 'contacts'},
    {'title': 'местоположение', 'url_name': 'place'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = '#'
        return context