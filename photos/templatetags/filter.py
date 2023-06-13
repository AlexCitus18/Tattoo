from django import template

register = template.Library()


@register.filter
def service_blocks(value):
    if value % 2 == 0:
        return True
    return False
