from django.contrib import admin
from .models import Apartment, Category, Selling, Rent, Apartment_info, Community, Selling_Comment, Rent_Comment, \
    Apartment_info_Comment, Community_Comment, Image

# Register your models here.
admin.site.register(Apartment)
admin.site.register(Category)
admin.site.register(Selling)
admin.site.register(Rent)
admin.site.register(Apartment_info)
admin.site.register(Community)
admin.site.register(Selling_Comment)
admin.site.register(Rent_Comment)
admin.site.register(Apartment_info_Comment)
admin.site.register(Community_Comment)
admin.site.register(Image)



