
from django.shortcuts import render


def get_bidding_list(request):
	return render(request, 'index.html')
