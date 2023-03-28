from django.views.generic import TemplateView

from .models import Menu


class MenuPageView(TemplateView):
    """"
    Renders a template with one or more menu
    """
    template_name = 'menu.html'


class HeaderPageView(TemplateView):
    """"
    Renders a template with selected header of menu
    """
    template_name = 'header.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = context.get('slug')
        context['header'] = Menu.objects.get(url=url)
        return context
