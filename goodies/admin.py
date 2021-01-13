from django.contrib import admin
from goodies.models import catergory, product

#admin.site.register(catergory)
#admin.site.register(product)

@admin.register(catergory)
class catergoryAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
    list_display = ['name', ]
    list_filter = ['name',]

@admin.register(product)
class productAdmin(admin.ModelAdmin):
	search_fields = ['name','productcatergory','date_created', ]
	list_display = ['name', 'productcatergory','weight','quantity','date_created','last_update',]
	list_filter = ['name','productcatergory','date_created',]



   
