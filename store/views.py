from django.shortcuts import render

def storeHandler(request):

	context = {}
	return render(request, 'store/store.html', context)

def cartHandler(request):
	return render(request, 'store/cart.html', )

def checkoutHandler(request):
	return render(request, 'store/checkout.html')

