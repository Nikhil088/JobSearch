from django.shortcuts import render

def orders_page(request):
    context = {}
    return render(request, "orders.html",context)

# Create your views here.
