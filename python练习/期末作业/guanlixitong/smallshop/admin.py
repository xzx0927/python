from django.contrib import admin

from smallshop.models import place, user, shop


# Register your models here
@admin.register(place)
class placeAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'detail_place')


@admin.register(shop)
class shopAdmin(admin.ModelAdmin):
    list_display = ('name', 'msg', 'place', 'prime_cost', 'price', 'quantity', 'residual_quantity')
    search_fields = ('name', 'prime_cost', 'price', 'quantity', 'residual_quantity')  # 搜索


@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display = ('name', 'password', 'place')
    search_fields = ('name', 'password')
