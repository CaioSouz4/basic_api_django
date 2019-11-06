
from django.contrib import admin
from django.urls import path, include
from core.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'clientes',ClientView)
router.register(r'pedidos',PedidoView)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))     
]




