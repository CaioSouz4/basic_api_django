from django.db import models

# Create your models here.

class Pedido(models.Model):
    preço =  models.IntegerField()
    produto = models.CharField(max_length=50)    

    def preço(self):
        return self.preço    


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    endereço = models.CharField(max_length=50)
    cpf =  models.IntegerField()
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, blank=True, null=True)

    def __str__ (self):
        return self.pedido

