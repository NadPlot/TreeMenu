from django.urls import path

from .views import HeaderPageView, MenuPageView

urlpatterns = [
    path('menu/', MenuPageView.as_view(), name='menu'),
    path('menu/<slug:slug>/', HeaderPageView.as_view(), name='header'),
]
