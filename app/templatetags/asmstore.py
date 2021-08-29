from django import template
register=template.Library()
from ..models import ShopByDepartment,User
@register.simple_tag
def shoppbydepartments():
    return ShopByDepartment.objects.all().order_by("name")

@register.simple_tag(takes_context=True)
def myinfos(context):
    user=context['user']
    infos=[
        ('First_name',user.first_name),
        ('Last_name', user.last_name),
        ('Username',user.username),
        ('Email', user.email),
        ('Birthday', user.birthday),
    ]
    return infos

@register.filter(name="remove_dunder")
def remove_dunder(value):
    return value.replace("_"," ")