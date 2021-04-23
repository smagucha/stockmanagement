from django.db import models
from django.urls import reverse

class Catergory(models.Model):
	name = models.CharField(max_length = 50, unique = True)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length = 50)
	productcatergory = models.ForeignKey(Catergory, on_delete=models.CASCADE)
	weight = models.CharField(max_length = 50)
	quantity = models.PositiveIntegerField()
	date_created = models.DateTimeField(auto_now_add = True, auto_now= False)
	last_update = models.DateTimeField(auto_now_add = False, auto_now= True)


	def get_absolute_url(self):
		return reverse('product-detail', kwargs={'pk': self.pk})

	def __str__(self):
		return self.name
