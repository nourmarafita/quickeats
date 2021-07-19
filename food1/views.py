from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pizza, Burger, Order, Item
from rest_framework import serializers, viewsets
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignupForm
import random
import json
def randomOrderNumber(length):
    sample = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    number0 = ''.join((random.choice(sample) for i in range(length)))
    return number0
# Create your views here.

def index(request):
    request.session.set_expiry(0)
    ctx = {'active_link': 'index'}
    return render(request, 'food1/index.html', ctx)

def pizza(request):
    request.session.set_expiry(0)
    pizzas = Pizza.objects.all()
    ctx = {'pizzas': pizzas, 'active_link': 'pizza'}

    return render(request, 'food1/pizza.html', ctx)


def burgers(request):
    request.session.set_expiry(0)
    burgers = Burger.objects.all()
    ctx = {'burgers': burgers, 'active_link': 'burger'}

    return render(request, 'food1/burgers.html', ctx)

@csrf_exempt
def order(request):
    request.session.set_expiry(0)
    if request.is_ajax():
        request.session['note'] = request.POST.get('note')
        request.session['order'] = request.POST.get('orders')
        orders = json.loads(request.session['order'])
        request.session['bill'] = request.POST.get('bill')
        randomNum = randomOrderNumber(6)

        while Order.objects.filter(number=randomNum).count() > 0:
            randomNum = randomOrderNumber(6)

        if request.user.is_authenticated:
            order = Order(customer=request.user, 
                            number=randomNum, 
                            bill=float(request.session['bill']), 
                            note=request.session['note'])
            order.save()
            for article in orders:
                item = Item(
                    order = order,
                    name  = article[0],
                    price = float(article[2]),
                    size  = article[1]
                )
                item.save()
    ctx = {'active_link': 'order'}
    return render(request, 'food1/cart.html', ctx)

def success(request):
    order = request.session['order']
    ctx = {'order' : order}
    return render(request, 'food1/success.html', ctx)

def logIn(request):
    if request.POST:
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        account = authenticate(request, username=username, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'username and/or password are incorrect')
    ctx = {'active_link': 'login'}
    return render(request, "food1/login.html", ctx)

def logOut(request):
    logout(request)
    return redirect("index")


# Rest api pizza
class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('id', 'name', 'priceM', 'priceL', 'pImage',)

class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

