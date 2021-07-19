from django.urls import path, include
from rest_framework import routers
from . import views
from .views import PizzaViewSet

app_name = 'fastfood'
router = routers.SimpleRouter()
router.register(r'', PizzaViewSet)

urlpatterns = [
    path('pizza', views.pizza, name='pizza'),
    path('burgers', views.burgers, name='burgers'),
    path('order', views.order, name='order'),
    path('success', views.success, name='success'),
    path('login', views.logIn, name='login'),
    path('logout', views.logOut, name='logout'),
    path('', include(router.urls,)),
]