from django.http import HttpResponse
from django.shortcuts import render


menu = [
    {'title': 'Главная', 'url_name': 'index'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Блог', 'url_name': 'blog'},
    {'title': 'Контакты', 'url_name': 'contact'}
]


def index(request):
    template = 'blog/index.html'
    context = {
        'menu': menu,
        'title': 'Главная страница сайта'
    }
    return render(request, template, context=context)


def news_blog(request):
    template = 'blog/blog.html'
    context = {
        'menu': menu,
        'title': 'Блог про птиц'
    }
    return render(request, template, context=context)


def single(request):
    template = 'blog/single.html'
    context = {
        'menu': menu,
        'title': 'Статья про птиц'
    }
    return render(request, template, context=context)


def about(request):
    pass


def contact(request):
    pass
