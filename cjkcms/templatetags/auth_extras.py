from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name="has_group")
def has_group(user, group_name):
    """Filter to check if current user belongs to specific group"""
    group = Group.objects.get(name=group_name)
    return group in user.groups.all()


@register.simple_tag
def define(val=None):
    return val
