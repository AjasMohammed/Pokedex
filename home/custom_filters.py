from django import template
import json

register = template.Library()

@register.filter
def get_val(item, key):
    val = item.get(key)
    return val 

@register.filter
def img_path(path, name):
    src = path + str(name) + '.svg'
    return src
