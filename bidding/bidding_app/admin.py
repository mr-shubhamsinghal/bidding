from django.contrib import admin

from bidding_app.models import ServiceName, VendorBidding


admin.site.register(ServiceName)
admin.site.register(VendorBidding)

