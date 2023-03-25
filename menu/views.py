from django.views.generic import DetailView
from .models import Menu


class MenuPageView(DetailView):
    model = Menu
    template_name = 'menu.html'
    context_object_name = 'menu'
