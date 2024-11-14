from typing import Any
from django import forms
from cars.models import Brand ,Car


class CarModelForm(forms.ModelForm):

    class Meta:
        model = Car # Um modelo pra o formulario se basear
        fields = "__all__"# isso significa que eu quero todos os campos da tabela Car
    
    def clean_value(self):
        value = self.cleaned_data.get("value")
        if value < 20000:
            self.add_error("value","Valor minimo pra inserir um carro tem que ser 20 pila")
        return value
    

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get("factory_year")
        if factory_year < 1975:
            self.add_error("factory_year","Ta de saca, Lata velha é no luciano huck , insira ai um acima do ano 1975")