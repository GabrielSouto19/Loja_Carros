from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from cars.models import Car


def cars_view(request):
    cars_list = Car.objects.all()# Nesse caso não posso colocar o values se não começa a dar erro
    # carro = Car.objects.filter(brand__name="Fiat")# pesquisa pelo nome do carro . como isso é uma Fk
    # o __ indica que eu estou fazendo uma navegação entre tabelas
    # context = {"cars_list":cars_list}
    # carro = Car.objects.filter(model="Camaro")
    # carro = Car.objects.filter(model__contains="Camaro")# é como se fosse o %LIKE% do sql
    #carro = Car.objects.filter(model__icontains="camaro")#IGUAL O LIKE POREM ELE É CASE INSENCITIVE
    context = {"cars_list":cars_list}
    print(request)
    return render(request,'cars.html',context)
    