from django.shortcuts import render, reverse
from django.views.generic import *
from . models import *
from.forms import *
from django.db.models import Q

# Create your views here.

class Shop(ListView):
    model = Product
    template_name = 'shop/shop.html'
    paginate_by = 9
    ordering = ['-created_at']

class Search(ListView):
    model = Product
    template_name = 'shop/shop.html'
    paginate_by = 100
    ordering = ['-created_at']

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        if query:
            q_list = Product.objects.filter(
                Q(name__icontains=query) | Q(id__icontains=query) | Q(created_at__icontains=query)
            ).order_by('-created_at')
            return q_list
        return Product.objects.all().order_by('-created_at')

class CreateProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'shop/create_product.html'

    def get_success_url(self):
        return reverse("shop:shop")

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {
            'get_cart_items': 0,
            'get_cart_total': 0
        }
    context = {'items': items, 'order': order}
    return render(request, 'shop/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {
            'get_cart_items': 0,
            'get_cart_total': 0
        }
    context = {'items': items, 'order': order}
    return render(request, 'shop/checkout.html', context)
