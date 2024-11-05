from django.contrib import admin
from cars.models import Car,Brand


class CarAdmin(admin.ModelAdmin):
    list_display = ("model","brand","factory_year","model_year","value")#estou definindo quais campos vão estar visiveis na minha tela de admin
    search_fields = ("model","brand")#Me permite buscar o filtrar a busca pelos seguintes campos
    
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)#estou definindo quais campos vão estar visiveis na minha tela de admin
    search_fields = ("name",)#Me permite buscar o filtrar a busca pelos seguintes campos


admin.site.register(Car,CarAdmin)
admin.site.register(Brand,BrandAdmin)