from django import template

register = template.Library()


@register.filter
def filter_multi(v1, v2):
    return v1 * v2

@register.simple_tag
def filter_simple_tag(x,y,z):
    return x+y+z

