
from bidding_app.models import Service, VendorBidding


def get_bidding_item_list():
    items = Service.objects.all()
    bidding_items = {'service_items': items}
    return bidding_items


def get_bidding_service(id):
    service_obj = Service.objects.get(id=id)
    return service_obj


def user_bidding(user, parameter_dict):

    service_id = parameter_dict.get('service_name')
    bid_value = parameter_dict.get('bid_value')

    vendor, _ = VendorBidding.objects.get_or_create(
             user=user, service=service_id)
    if not vendor.is_bid:
        vendor.is_bid = True
        vendor.value = bid_value
        vendor.save()


def get_service_bidding_details(service_obj):
    all_vendors = service_obj.vendorbidding.filter(is_bid=True).order_by('value')
    return all_vendors


def user_done_bidding(user, id):
    service_obj = get_bidding_service(id)
    vendor, _ = VendorBidding.objects.get_or_create(
                user=user, service=service_obj)
    result = {'value': vendor.value, 'is_bid': vendor.is_bid,
              'service_name': service_obj.name,
              'service_id': service_obj.id}
    return result


def get_lowest_bid(data):
    ans = ''



def get_highest_bid(data):
    pass
