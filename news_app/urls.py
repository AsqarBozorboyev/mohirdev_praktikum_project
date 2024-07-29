from django.urls import path
from .views import NewsListView, NewsDetailView, ContactPageView, HomePageView, UzbekistanNewsView, JahonNewsView, SportNewsView, TexnologyNewsView


urlpatterns = [
    path('all/', NewsListView.as_view(), name='news_list'),
    path('news/<slug>/', NewsDetailView.as_view(), name='news_detail'),
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('sports/', SportNewsView.as_view(), name='sports'),
    path('texnology/', TexnologyNewsView.as_view(), name='texnology'),
    path('uzbekistan/', UzbekistanNewsView.as_view(), name='uzbekistan'),
    path('jahon/', JahonNewsView.as_view(), name='jahon'),
]