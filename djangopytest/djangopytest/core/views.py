from django.shortcuts import render, get_object_or_404
from core.models import Products
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def product_detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'product_detail.html', {'product': product})