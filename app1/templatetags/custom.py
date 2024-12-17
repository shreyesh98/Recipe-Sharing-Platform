from django import template

register = template.Library()

def upar(value):
    return value.title()

register.filter('up', upar)