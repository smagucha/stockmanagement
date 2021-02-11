from django import template
from sale.models import Sale
from goodies.models import product
from django.db.models import Sum
register = template.Library()


@register.simple_tag
def somefilter():
    queryset=product.objects.values('name','productcatergory','weight').annotate(Sum('quantity'))
    # for x in queryset:
    #     print (x, '\n')
    queryset1=Sale.objects.values('item').annotate(Sum('quantity'))
    for x in queryset1:
        print (x, '\n')
    return (queryset, queryset1)
