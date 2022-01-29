
from bidding_app.models import ServiceName, VendorBidding


def get_bidding_item_list():
	items = ServiceName.objects.all()
	bidding_items = {'service_items': items}
	return bidding_items


def get_bidding_service(id):
	service_name = ServiceName.objects.get(id=id)
	return service_name


def user_bidding(user, parameter_dict):

	service_id = parameter_dict.get('service_name')
	bid_value = parameter_dict.get('bid_value')

	service_obj = get_bidding_service(service_id)
	vendor = VendorBidding.objects.create(user=user,
		     service_name=service_obj, value=bid_value)
	vendor.save()
