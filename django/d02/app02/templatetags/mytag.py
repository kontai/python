from django import template

register = template.Library()


# @register.filter(name='myAdd')
# def add(v1, v2):
#     return v1 + v2

@register.filter(name='myAdd')
def add(v1, v2):
    return v1 + v2


@register.simple_tag(name='plus')
def index(a, b, c, d):
    return "%s-%s-%s-%s" % (a, b, c, d)

@register.inclusion_tag('left_menu.html')
def left(n):
    data=['第{}項'.format(i) for i in range(n)]

    # return {'data':data}
    return locals()