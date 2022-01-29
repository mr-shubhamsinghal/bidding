
from django.shortcuts import render

from bidding_app import services


def get_bidding_list(request):

	data = services.get_bidding_item_list()
	return render(request, 'index.html', data)
