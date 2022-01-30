from django.urls import path

from bidding_app import views


app_name = 'bidding_app'

urlpatterns = [
	path('', views.get_bidding_list, name='get_bidding_list'),
	path('bid/<int:id>/', views.get_bidding_page, name='bid_page'),
	path('bid/bid_action/', views.bidding, name='bidding'),
	path('bid/admin/<int:id>', views.get_bidding_details, name='bidding-detail')
]
