from django.db import models
from goodies.models import product

class order(models.Model):
	buyer = models.CharField(max_length = 50)
	email = models.EmailField()
	phonenumber = models.PositiveIntegerField()
	product=models.ForeignKey(product, on_delete=models.CASCADE)
	dateordered  = models.DateTimeField(auto_now_add = True, auto_now= False)
	quantity = models.PositiveIntegerField()
