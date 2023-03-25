from django.views.generic import ListView
from .models import Menu


class MenuPageView(ListView):
    model = Menu
    queryset = Menu.objects.get(name='Main')
    template_name = 'menu.html'
    context_object_name = 'menu'
