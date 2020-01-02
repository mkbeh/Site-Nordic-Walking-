import re

from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter(name='cutimages')
@stringfilter
def cut_images(value):
    """
    Filter which cut `img` tags.
    """
    pattern = re.compile(r'<p><img .*</p>')
    return re.sub(pattern, '', value)


@register.filter(name='cutiframes')
@stringfilter
def cut_iframes(value):
    """
    Filter which cut <iframe> tags.
    """
    pattern = re.compile(r'<p><iframe .*</iframe></p>')
    return re.sub(pattern, '', value)
