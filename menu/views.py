from django.views.generic import ListView
from .models import Menu


class MenuPageView(ListView):
    model = Menu
    template_name = 'menu.html'
    context_object_name = 'header'
