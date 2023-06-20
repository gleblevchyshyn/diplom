from django.contrib.admin.views.decorators import staff_member_required
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

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


@login_required
def make_order(request):
    if request.method == 'POST':
        # Retrieve form data
        payment_id = request.POST.get('payment')
        delivery_company_id = request.POST.get('delivery_company')
        branch_id = request.POST.get('branch')

        # Validate form data
        if not (payment_id and delivery_company_id and branch_id):
            return redirect('make_order')

        # Create the order
        try:
            branch = Branch.objects.get(idbranch=branch_id)
            delivery_company = Deliverycompany.objects.get(iddeliverycompany=delivery_company_id)
            payment = Payment.objects.get(idpayment=payment_id)

            # Create the order
            order = Order.objects.create(
                branch_idbranch=branch,
                orderstatus_idorderstatus_id=1,
                payment_idpayment=payment,
                order_date=timezone.now(),
                user_iduser=request.user
            )

            # Add items to the order
            cart = request.session.get('cart', [])
            for item in cart:
                book_id = item['book_id']
                quantity = item['quantity']
                book = Book.objects.get(idbook=book_id)

                Orderitem.objects.create(
                    order_idorder=order,
                    book_idbook=book,
                    amount=quantity,
                    is_recommended=0  # Assuming is_recommended is set to 0 initially
                )

            # Clear the cart
            request.session['cart'] = []

            return redirect('make_order')
        except (Branch.DoesNotExist, Deliverycompany.DoesNotExist, Payment.DoesNotExist, Book.DoesNotExist):
            return redirect('make_order')

    # Retrieve data for form dropdowns
    branches = Branch.objects.all()
    delivery_companies = Deliverycompany.objects.all()
    payments = Payment.objects.all()

    context = {
        'branches': branches,
        'delivery_companies': delivery_companies,
        'payments': payments
    }
    return render(request, 'order.html', context)


@staff_member_required
def admin_orders(request):
    orders = Order.objects.select_related('user_iduser', 'branch_idbranch', 'payment_idpayment', 'orderstatus_idorderstatus').all()
    order_statuses = Orderstatus.objects.all()

    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        status_id = request.POST.get('status')

        if order_id and status_id:
            try:
                order = Order.objects.get(idorder=order_id)
                status = Orderstatus.objects.get(idorderstatus=status_id)
                order.orderstatus_idorderstatus = status
                order.save()
                return redirect('admin_orders')
            except (Order.DoesNotExist, Orderstatus.DoesNotExist):
                pass

    context = {
        'orders': orders,
        'order_statuses': order_statuses,
    }
    return render(request, 'admin_orders.html', context)
