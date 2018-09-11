from django.template import Library


register = Library()


@register.filter
def md(values):
    return values