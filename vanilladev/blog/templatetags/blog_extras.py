from django import template

register = template.Library()


def previous(value):
    return value-1

def next(value):
    return value+1

register.filter('previous', previous)
register.filter('next', next)