from django.db import models
from django.contrib.auth.models import User
from goodies.models import product

class Sale(models.Model):
	name = models.ForeignKey(User, on_delete=models.CASCADE)
	buyer = models.CharField(max_length= 100)
	buyercontact= models.IntegerField()
	clientemail = models.EmailField()
	item = models.ForeignKey(product, on_delete = models.CASCADE)
	quantity =models.PositiveIntegerField()
	date = models.DateTimeField(auto_now_add = True, auto_now= False)
