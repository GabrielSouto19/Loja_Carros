from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from cars.models import Car


def cars_view(request):
    nome_carro = request.GET.get("search")
    if nome_carro:
        print(nome_carro)
        carro = Car.objects.filter(model__icontains = nome_carro)#filtrando por modelo
        context = {"cars_list":carro}
    else:
        cars_list = Car.objects.all().order_by("model")# Nesse caso não posso colocar o values se não começa a dar erro,order_by ordena minha consulta pelo campo destacado
        context = {"cars_list":cars_list}
        
    # carro = Car.objects.filter(brand__name = nome_carro)#filtrando por marca
    # carro = Car.objects.filter(brand__name="Fiat")# pesquisa pelo nome do carro . como isso é uma Fk
    # o __ indica que eu estou fazendo uma navegação entre tabelas
    # context = {"cars_list":cars_list}
    # carro = Car.objects.filter(model="Camaro")
    # carro = Car.objects.filter(model__contains="Camaro")# é como se fosse o %LIKE% do sql
    #carro = Car.objects.filter(model__icontains="camaro")#IGUAL O LIKE POREM ELE É CASE INSENCITIVE
    # context = {"cars_list":carro}
    return render(request,'cars.html',context)
    
