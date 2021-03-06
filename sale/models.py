from django.db import models
from django.contrib.auth.models import User
from goodies.models import Product
from django.urls import reverse

class Sale(models.Model):
	serverby = models.ForeignKey(User, on_delete=models.CASCADE)
	buyer = models.CharField(max_length= 100)
	buyercontact= models.IntegerField()
	clientemail = models.EmailField()
	item = models.ForeignKey(Product, on_delete = models.CASCADE)
	quantity =models.PositiveIntegerField()
	date = models.DateTimeField(auto_now_add = True, auto_now= False)

	def get_absolute_url(self):
		return reverse('sale-detail', kwargs={'pk': self.pk})

	def __str__(self):
		return str(self.serverby)
