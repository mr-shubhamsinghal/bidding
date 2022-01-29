from django.db import models
from django.contrib.auth.models import User


class ServiceName(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return str(self.name)

class VendorBidding(models.Model):
	user = models.ForeignKey(User, on_delete=models.RESTRICT)
	service_name = models.ForeignKey(ServiceName, on_delete=models.RESTRICT)
	value = models.PositiveIntegerField()
	is_bid = models.BooleanField(default=False)

	def __str__(self):
		return f'{user}-{service_name}-{value}'
