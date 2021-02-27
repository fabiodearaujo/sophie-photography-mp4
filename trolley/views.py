from django.shortcuts import (get_object_or_404, render,
                              redirect, reverse, HttpResponse)
from django.contrib import messages
from products.models import Product


def view_trolley(request):
    """ View to connect and return the shopping trolley page """
    return render(request, 'trolley/trolley.html')


def add_to_trolley(request, item_id):
    """ Add a quantity of the specified product to the shopping trolley """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    trolley = request.session.get('trolley', {})

    if item_id in list(trolley.keys()):
        trolley[item_id] += quantity
    else:
        trolley[item_id] = quantity
        messages.success(request, f'Added {product.name} to the Trolley')

    request.session['trolley'] = trolley
    return redirect(redirect_url)


def adjust_trolley(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    trolley = request.session.get('trolley', {})

    if quantity > 0:
        if quantity < 100:
            trolley[item_id] = quantity
            messages.success(request,
                             f'Quantity and Subtotal \
                                 updated for {product.name}')
        else:
            trolley[item_id] = 99
            messages.warning(request,
                             'Quantity cannot be higher than 99 items')
    else:
        trolley.pop(item_id)
        messages.error(request,
                       'Item removed as the quantity was lower than 1 item')

    request.session['trolley'] = trolley
    return redirect(reverse('view_trolley'))


def remove_from_trolley(request, item_id):
    """Remove the item from the shopping trolley"""

    try:
        trolley = request.session.get('trolley', {})
        trolley.pop(item_id)
        messages.success(request, 'The item was removed from your Trolley')
        request.session['trolley'] = trolley
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item {e}')
        return HttpResponse(status=500)
