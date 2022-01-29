
from bidding_app.models import ServiceName, VendorBidding


def get_bidding_item_list():
	items = ServiceName.objects.all()
	bidding_items = {'service_items': items}
	return bidding_items
