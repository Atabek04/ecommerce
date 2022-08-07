from django.urls import path
from . import views

urlpatterns = [
	path('', views.storeHandler, name='store'),
	path('cart/', views.cartHandler, name='cart'),
	path('checkout/', views.checkoutHandler, name='checkout'),
]