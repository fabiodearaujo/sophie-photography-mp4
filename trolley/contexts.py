from django.conf import settings

def trolley_contents(request):

    trolley_items = []
    total = 0
    product_count = 0

    context = {
        'trolley_items': trolley_items,
        'total': total,
        'product_count': product_count,
    }

    return context
