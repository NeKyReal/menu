from django import template
from ..models import Menu, MenuItem
register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
        items = menu.items.select_related('parent').all()
        current_url = context['request'].path
        return {'menu_items': items, 'current_url': current_url}
    except Menu.DoesNotExist:
        return {'menu_items': []}
