from django.db import models
from goodies.models import product
from django.urls import reverse

class order(models.Model):
	buyer = models.CharField(max_length = 50)
	email = models.EmailField()
	phonenumber = models.PositiveIntegerField()
	product=models.ForeignKey(product, on_delete=models.CASCADE)
	dateordered  = models.DateTimeField(auto_now_add = True, auto_now= False)
	quantity = models.PositiveIntegerField()

	def get_absolute_url(self):
		return reverse('order-detail', kwargs={'pk': self.pk})

	def __str__(self):
		return self.buyer
