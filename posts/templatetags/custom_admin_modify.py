from django import template
from django.contrib.admin.templatetags.admin_modify import submit_row
from django.contrib.admin.templatetags.base import InclusionAdminNode

register = template.Library()


@register.tag(name='custom_submit_row')
def submit_row_tag(parser, token):
    return InclusionAdminNode(parser, token, func=submit_row, template_name='custom_submit_line.html')


@register.tag(name='exam_submit_row')
def submit_row_tag(parser, token):
    return InclusionAdminNode(parser, token, func=submit_row, template_name='exam_submit_line.html')


@register.tag(name='exam100_submit_row')
def submit_row_tag(parser, token):
    return InclusionAdminNode(parser, token, func=submit_row, template_name='exam_submit_line.html')
