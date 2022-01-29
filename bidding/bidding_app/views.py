
from django.shortcuts import render, redirect

from bidding_app import services


def get_bidding_list(request):

	data = services.get_bidding_item_list()
	return render(request, 'index.html', data)


def get_bidding_page(request, id):
	data = services.get_bidding_service(id)
	context = {'service': data}
	return render(request, 'bidding_page.html', context)


def bidding(request):
	user = request.user
	parameter_dict = request.data
	response = services.user_bidding(user, parameter_dict)
	return redirect('/')
