from django import template

register = template.Library()


@register.inclusion_tag('display_draw_menu.html')
def draw_menu(menu):
    menu = menu.all()
    return {'menu': menu}
