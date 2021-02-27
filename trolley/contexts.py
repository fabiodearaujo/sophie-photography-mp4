from django.shortcuts import get_object_or_404
from products.models import Product


def trolley_contents(request):

    trolley_items = []
    total = 0
    product_count = 0
    trolley_dic = request.session.get('trolley', {})
    print(trolley_dic)

    for item_id, quantity in trolley_dic.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        trolley_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'trolley_items': trolley_items,
        'total': total,
        'product_count': product_count,
    }

    return context
