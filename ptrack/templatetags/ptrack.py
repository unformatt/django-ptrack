"""Ptrack Template Tag"""
import logging

from django import template
from django.utils.html import mark_safe

logger = logging.getLogger(__name__)
register = template.Library()


@register.simple_tag
def ptrack(*args, **kwargs):
    """Generate a tracking pixel html img element."""
    from ptrack import create_img
    img = create_img(*args, **kwargs)
    return mark_safe(img)
