from django.shortcuts import render

from .models import Pizza

# Create your views here.
def index(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'index.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza':pizza, 'toppings':toppings}
    return render(request, 'pizza.html', context)