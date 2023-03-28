from django import template

from ..models import Menu

register = template.Library()


@register.inclusion_tag('display_draw_menu.html', takes_context=True)
def draw_menu(context, name):

    # На отрисовку каждого меню требуется ровно 1 запрос к БД
    menu = Menu.objects.get(name=name).children.all()
    return {'menu': menu, 'request': context['request']}  # url пункта меню
