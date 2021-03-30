from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from order.models import order
from .models import product

@receiver(pre_save, sender =order)
def subtract_quantity(sender, instance, **kwargs):
	bought =instance.quantity
	# obj = product.objects.get(product)
	# print(obj)
	
	#print(obj)
	#if instance.product ==

	
	
