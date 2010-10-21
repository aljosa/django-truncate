from django import template
from django.utils.encoding import force_unicode
from django.utils.functional import allow_lazy

register = template.Library()

# based on http://code.djangoproject.com/ticket/5025

def truncate(s, limit): 
    s = force_unicode(s) 
    if len(s) <= limit: 
        return s 
    return '%s...' % s[:max(1, limit - 3)] 
truncate = allow_lazy(truncate, unicode) 
 
@register.filter(name="truncate")
def truncate_chars(value, limit):
    try: 
        limit = int(limit) 
    except ValueError: # invalid literal for int() 
        return value # Fail silently. 
    return truncate(value, limit) 
