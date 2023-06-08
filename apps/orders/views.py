from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *


@login_required
def previous_orders(request):
    user = request.user
    orders = Order.objects.filter(user_iduser=user).order_by('-order_date')
    return render(request, 'previous_orders.html', {'orders': orders})


def add_to_cart(request, book_id):
    cart = request.session.get('cart', [])

    cart.append({'book_id': book_id, 'quantity': 1})

    request.session['cart'] = cart

    return JsonResponse({'message': 'Book added to cart'})


def cart(request):
    # Retrieve the cart items from the session
    cart_items = request.session.get('cart', [])

    # Extract the book_ids from the cart_items
    book_ids = [item['book_id'] for item in cart_items]
    book_qnt = [item['quantity'] for item in cart_items]

    # Query the database to get all books with the matching book_ids
    books = Book.objects.filter(idbook__in=book_ids)

    # Combine books and book_qnt using zip
    book_data = zip(books, book_qnt)

    # Render the cart template with the book_data
    print(cart_items)
    return render(request, 'cart.html', {'book_data': book_data})


def remove_book(request, book_id):
    cart = request.session['cart']

    # Find the index of the book in the cart
    book_index = None
    for index, item in enumerate(cart):
        if item['book_id'] == book_id:
            book_index = index
            break

    if book_index is None:
        return JsonResponse({'message': 'Book not found in cart'})

    # Remove the book from the cart
    removed_book = cart.pop(book_index)
    request.session['cart'] = cart
    print(cart)
    return redirect('cart')


from django.http import JsonResponse


def update_quantity(request, book_id):
    cart = request.session.get('cart', [])

    # Find the book in the cart and update its quantity
    for item in cart:
        if item['book_id'] == book_id:
            # Get the new quantity from the request
            quantity = int(request.POST.get('quantity', 0))

            if quantity > 0:
                # Update the quantity if it's greater than 0
                item['quantity'] = quantity
                request.session['cart'] = cart
                return JsonResponse({'message': 'Quantity updated', 'cart': cart})
            else:
                # Remove the book from the cart if the quantity is 0
                cart.remove(item)
                request.session['cart'] = cart
                return JsonResponse({'message': 'Book removed from cart', 'cart': cart})
    print(cart)
    return JsonResponse({'message': 'Book not found in cart'})