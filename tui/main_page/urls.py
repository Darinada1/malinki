from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60*15)(MainTui.as_view()), name="home"),
    path('about/', cache_page(60*60)(About.as_view()), name='about'),
    path('contacts/', cache_page(60*60)(Contacts.as_view()), name='contacts'),
    path('place/', cache_page(60*60)(Place.as_view()), name='place'),
    path('post/<slug:post_slug>/', cache_page(60*15)(posts), name='post'),
    path("category/<slug:cat_slug>", cache_page(60*15)(ShowCategory.as_view()), name='category'),
]

