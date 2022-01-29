from django.urls import path

from bidding_app import views


app_name = 'bidding_app'


urlpatterns = [
	path('', views.get_bidding_list, name='get_bidding_list')
]
