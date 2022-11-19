# from django.forms import modelformset_factory, formset_factory
# from django.shortcuts import render, redirect
# from blog.forms import CommentForm
# from shop.forms import  Order, postform, OrderAddToCartForm
# from .models import Product, Order, PostInfo, Invoice
# from blog.models import Category, Comment
# from user_auth.models import User
# from django.utils import timezone
# from django.contrib.auth.decorators import login_required
# from shop.decorators import just_owner, not_owner
# from PIL import Image
# from persian_tools import digits
# from django.urls import reverse
# from django.db.models import Sum


# def all_views_navbar_utils(request):
#     order_count = Order.objects.filter(buyer=request.user).filter(paid=False).count()
#     same_context = {
#         "order_count" : order_count
#     }
#     return same_context


# def shop(request):
#     all_categories = Category.objects.all()
#     product_list1 = Product.objects.filter(home_list='First')
#     product_list2 = Product.objects.filter(home_list='Second')
#     product_list3 = Product.objects.filter(home_list='Third')
#     product_list4 = Product.objects.filter(home_list='Forth')
#     if request.method == "POST":
#         slug_product = request.POST['action']
#         single_product = Product.objects.filter(slug=slug_product).first()
#         my_order = Order.objects.create(buyer=request.user, product=single_product, quantity=1)
#         my_order.save()

#     context_same = all_views_navbar_utils(request)
#     context = {
#                 "product_list1": product_list1,
#                 "product_list2": product_list2,
#                 "product_list3": product_list3,
#                 "product_list4": product_list4,
#     }
#     context.update(context_same)
#     return render(request, 'shop1/shop.html', context)


# def single_product(request, slug):  
#     single_product = Product.objects.filter(slug=slug).first()
#     if request.method == 'POST':
#         if request.POST['action'] == 'add_cart':
#             form2 = OrderAddToCartForm(request.POST)
#             if form2.is_valid():
#                 obj = form2.save(commit=False)
#                 obj.buyer = request.user
#                 obj.product = single_product 
#                 obj.save()
#             return redirect('single-product', slug)
#     else:
#         form2 = OrderAddToCartForm()
#     ip_address = request.user.ip_address
#     single_product = Product.objects.filter(slug=slug).first()
#     related_products = Product.objects.filter(category=single_product.category)[0:10]
#     context = {
#                 'now': timezone.now,
#                 'product': single_product ,
#                 'related_products': related_products,
#                 'form2': form2,
#                 'single_product': single_product,
#     }
#     context_sample = all_views_navbar_utils(request)
#     context.update(context_sample)

#     return render(request, 'shop1/single-product.html', context)


# @login_required(login_url='register')
# def cart(request):
#     my_orders = Order.objects.filter(buyer=request.user).filter(paid=False)
#     total_price_checkout = my_orders.aggregate(Sum('total_price'))
#     if total_price_checkout['total_price__sum']==None:
#         total_price_checkout['total_price__sum'] = 0
#     context = {
#         'order_list': my_orders,
#         'total_price': total_price_checkout['total_price__sum'],
#     }
#     if request.method == "POST":
#         action = request.POST["action"]
#         if action=="create":
#             my_invoice = Invoice.objects.create()
#             my_invoice.orders.set(my_orders)
#             my_invoice.save()
#         else:
#             pk_product = action
#             Order.objects.get(pk=pk_product).delete()
#     return render(request, 'shop1/cart.html', context)

    
# @login_required(login_url='register')
# def checkout(request):
#     my_orders = Order.objects.filter(buyer=request.user).filter(paid=False)
#     total_price_checkout = my_orders.aggregate(Sum('total_price'))
#     post_m = PostInfo.objects.filter(user=request.user).order_by('-time_add').first()
#     if request.method == 'POST':
#         form = postform(request.POST, instance=post_m)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = request.user
#             obj.save()
#             return redirect('go-to-shop')
#     else:
#         form = postform(instance=post_m)
#     # context = {
#     #     'form': form,
#     # }
#     context = {
#         'form': form,
#         'order_list': my_orders,
#         'total_price': total_price_checkout['total_price__sum'],
#     }

#     context_sample = all_views_navbar_utils(request)
#     context.update(context_sample)
#     return render(request, 'shop1/checkout.html', context)


# def page_404(request, exception):
#     return render(request, '404.html', status=404)


# def page_403(request, exception):
#     return render(request, '403.html', status=403)


# def page_500(request, exception):
#     return render(request, '500.html', status=500)


# def page_400(request, exception):
#     return render(request, '400.html', status=400)