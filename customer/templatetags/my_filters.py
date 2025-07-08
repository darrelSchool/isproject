from django import template

register = template.Library()


@register.filter(name="sub")
def sub(val1, val2):
    return val1 - val2


@register.filter(name="get_range")
def get_range(val):
    return range(val)
