from django.contrib import admin
# from .models import Plant
from .models import Item, ItemCat, Offer, Variant
# from django.contrib.auth.models import User
# Register your models here.


admin.site.register(Item)
admin.site.register(ItemCat)
admin.site.register(Offer)
admin.site.register(Variant)
# admin.site.register(User)
