from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return str(self.name)

class VendorBidding(models.Model):
	user = models.ForeignKey(User, on_delete=models.RESTRICT)
	service = models.ForeignKey(Service, related_name='vendorbidding',
		                        on_delete=models.RESTRICT)
	value = models.PositiveIntegerField(default=0)
	is_bid = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.user.username}-{self.service}-{self.value}'
