from django.contrib import admin
from aplic.models import  Celular, Cliente, Endereco, Funcionario, Pedido








@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nome", 'cpf', ]


    
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', "salario"]

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ["data_pedido", 'data_entrega',"status_pedido", "cliente", ]


@admin.register(Celular)
class CelularAdmin(admin.ModelAdmin):
    list_display = ["nome"]




