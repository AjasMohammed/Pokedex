from django import template

register = template.Library()

@register.filter
def get_val(item, key):
    val = item.get(key)
    return val 