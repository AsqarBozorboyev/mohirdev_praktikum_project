from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Category, News
from .forms import ContactForm


class NewsListView(ListView):
    model = News.objects.filter(status=News.Status.Published)
    context_object_name = 'news_list'
    template_name = 'news_list.html'


class NewsDetailView(DetailView):
    model = News
    context_object_name = 'news'
    template_name = 'single_page.html'

    def get_queryset(self):
        news = News.published.all().filter()




# def homePageView(request):
#     news = News.published.all().order_by('-publish_time')[:5]
#     categories = Category.objects.all()
#     mahalliy = News.published.all().filter(category__name="O‘zbekiston")[:1]
#     mahalliy_news = News.published.all().filter(category__name="O‘zbekiston")[1:5]
#
#     context = {
#         'news_list': news,
#         'categories': categories,
#         'mahalliy_news': mahalliy_news,
#         'mahalliy': mahalliy
#     }
#     return render(request, 'home.html', context)


class HomePageView(ListView):
    model = News
    template_name = 'home.html'
    context_object_name = ('news')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = News.published.all().order_by('-publish_time')[:5]
        context['categories'] = Category.objects.all()
        context['mahalliy_news'] = News.published.all().filter(category__name="O‘zbekiston")[:5]
        context['jahon_news'] = News.published.all().filter(category__name="Jahon")[:5]
        context['sport_news'] = News.published.all().filter(category__name="Sport")[:5]
        context['fan_news'] = News.published.all().filter(category__name="Fan-texnika")[:5]
        return context


# def contactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'contact.html')
#

class ContactPageView(TemplateView):
    template_name = 'contact.html'
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context ={
            'form': form
        }

        return render(request, template_name='contact.html', context=context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2>Biz bilan bog'langaniz uchun raxmat</h2>")
        context = {
            'form': form
        }

        return render(request, template_name='contact.html', context=context)



class UzbekistanNewsView(ListView):
    model = News
    template_name = 'uzbekistan.html'
    context_object_name = 'uzbekistan_news'

    def get_queryset(self):
        news = News.published.all().filter(category__name="O‘zbekiston")
        return news

class JahonNewsView(ListView):
    model = News
    template_name = 'jahon.html'
    context_object_name = 'jahon_news'

    def get_queryset(self):
        news = News.published.all().filter(category__name='Jahon')
        return news

class SportNewsView(ListView):
    model = News
    template_name = 'sport.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        news = News.published.all().filter(category__name='Sport')
        return news


class TexnologyNewsView(ListView):
    model = News
    template_name = 'texnology.html'
    context_object_name = 'texnology_news'

    def get_queryset(self):
        news = News.published.all().filter(category__name='Fan-texnika')
        return news
