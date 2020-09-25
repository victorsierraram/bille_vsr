"""billie_pr URL Configuration
"""
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'compras', views.CompraViewSet)
router.register(r'facturas', views.FacturaViewSet)
router.register(r'earnings/(?P<month>.+)/(?P<year>.+)$', views.EarningsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]