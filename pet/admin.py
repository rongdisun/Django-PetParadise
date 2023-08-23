from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    exclude = ["adopt_status"]
    list_display = ['name', 'sex', 'neutered', 'address', 'birthday', 'brief_intro', 'avatar']


@admin.register(PetImage)
class PetImageAdmin(admin.ModelAdmin):
    list_display = ['photographer', 'pet', 'photograph_time']


@admin.register(AdoptPet)
class AdoptPetAdmin(admin.ModelAdmin):
    fields = ["apply_status"]
    list_display = ['adopter', 'pet', 'apply_time', 'apply_status']


@admin.register(PetGoods)
class PetGoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture', 'price', 'unit', 'stock', 'brief_intro']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['number', 'user', 'goods']
