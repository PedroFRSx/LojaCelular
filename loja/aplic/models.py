import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from stdimage.models import StdImageField



class Pessoa(models.Model):   
    nome = models.CharField(_("Nome"), blank=False, max_length=50,)
    cpf = models.CharField(_("cpf"), blank=False, max_length=11, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    

   
    def __str__(self):
        return self.nome 





class Funcionario(Pessoa):
    
    salario = models.DecimalField(_("Salario"), null=True, blank=False, max_digits=8, decimal_places=2)


    class Meta:
        verbose_name = _('Funcionario')
        verbose_name_plural = _('Funcionarios')

    def __str__(self):
        return f"{self.nome} / {self.cargo}"
    
class Cliente(Pessoa):
   
    
    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')

    def __str__(self):
        return f"{self.nome}"
    
    

class Celular(models.Model):
    nome = models.CharField( max_length=300,) 
    fabricante = models.CharField(  max_length=300,) 
    sistema_operacional = models.CharField()
    ram =models.IntegerField() 
    armazenamento = models.IntegerField()
    preco = models.DecimalField( blank=False, decimal_places=2, max_digits=10) 
    imagem = models.ImageField(upload_to='imagem_celular/')


    class Meta:
        verbose_name = _('Celular')
        verbose_name_plural = _('Celulares')

    def __str__(self):
        return f"{self.nome} {self.preco}"

class Pedido(models.Model):
    data_pedido = models.DateTimeField(_("Data pedido",))
    data_entrega = models.DateTimeField(_("Data entrega",))
    status_pedido = models.BooleanField(_("Finalizado"))  
    cliente = models.ForeignKey(Cliente, null=True, on_delete= models.SET_NULL)

    class Meta:
        verbose_name = _('Pedido')
        verbose_name_plural = _('Pedidos')
    
    def __str__(self):
        return f"{self.cliente} {self.status_pedido}"

    
class Endereco(models.Model):
    cidade = models.CharField(_("Cidade"), blank=False, max_length=50,)
    bairro = models.CharField(_("Bairro"), blank=False, max_length=50,)
    rua = models.CharField(_("Rua"), blank=False, max_length=50,)
    numero = models.CharField(_("Numero"), blank=False, max_length=50,)
    complemento = models.CharField(_("Complemento"), blank=False, max_length=50,)
   

    class Meta:   
        verbose_name = _('Endereço')
        verbose_name_plural = _('Endereços')

    def __str__(self):
        return f"Cidade:{self.cidade} Bairro:{self.bairro}"