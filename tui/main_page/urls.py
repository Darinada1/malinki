from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', MainTui.as_view(), name="home"),
    path('about/', About.as_view(), name='about'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('place/', Place.as_view(), name='place'),
    path('post/<slug:post_slug>/', posts, name='post'),
    path("category/<slug:cat_slug>", ShowCategory.as_view(), name='category'),
]

