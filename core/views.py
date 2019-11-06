from django.shortcuts import render

from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import Cliente, Pedido
from .serializers import ClientSerializer, PedidoSerializer
from rest_framework.views import APIView

# Create your views here.
class ClientView(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClientSerializer    
     
class PedidoView(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

""" class PedidoView(APIView):
    def get(self, request, format=None):
        pedidos = Pedido.objects.all()
        serializer = PedidoSerializer(snippets, many=True)
        return Response(serializer.data)
 """
    