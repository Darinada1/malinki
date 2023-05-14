from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView
from .utils import *
category = Category.objects.all()


class About(DataMixin, ListView):
    model = Tui
    template_name = 'main_page/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='О нас')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class Contacts(DataMixin, ListView):
    model = Tui
    template_name = 'main_page/contacts.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Контакты')
        context = dict(list(c_def.items()) + list(context.items()))
        return context


class Place(DataMixin, ListView):
    model = Tui
    template_name = 'main_page/place.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Наше местоположение')
        context = dict(list(c_def.items()) + list(context.items()))
        return context


def posts(request, post_slug):
    post = get_object_or_404(Tui, slug=post_slug)
    category = Category.objects.all()
    tui = Tui.objects.all()
    context = {
        'cats': category,
        'tui': tui,
        "menu": menu,
        'post': post,
        'cat_selected': post.thuja_cat_id
    }
    return render(request, 'main_page/posts.html', context=context)


class MainTui(DataMixin, ListView):
    paginate_by = 10
    model = Tui
    template_name = 'main_page/index.html'
    context_object_name = 'tui'
    category = Category.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница', cat_selected=0)
        context = dict(list(c_def.items()) + list(context.items()))
        return context


class ShowCategory(DataMixin, ListView):
    paginate_by = 10
    model = Tui
    template_name = 'main_page/index.html'
    context_object_name = 'tui'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='категория ' + str(context['tui'][0].choice),
                                      cat_selected=context['tui'][0].thuja_cat_id)
        context = dict(list(c_def.items()) + list(context.items()))
        return context

    def get_queryset(self):
        return Tui.objects.filter(thuja_cat__slug=self.kwargs['cat_slug'])
