from django import template
from ..models import Menu

register = template.Library()


@register.inclusion_tag('display_draw_menu.html')
def draw_menu(name):
    menus = Menu.objects.get(name=name).children.all()
    #menus = menu.children.all()
    return {'menus': menus}
