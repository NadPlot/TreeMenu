from django.views.generic import TemplateView
from .models import Menu


class MenuPageView(TemplateView):
    template_name = 'menu.html'


class HeaderPageView(TemplateView):
    template_name = 'header.html'
