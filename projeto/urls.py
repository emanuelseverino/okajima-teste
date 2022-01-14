"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from core.api.viewsets import AppLoginViewSet, AppSamuraicupomViewSet, ShowMetaViewSet
from usuario.api.viewsets import CriarUsuarioViewSet, UsuarioViewSet
from usuario.views import criar_usuario

router = routers.DefaultRouter()
router.register(r'applogin', AppLoginViewSet)
router.register(r'appsamuraicupom', AppSamuraicupomViewSet)
router.register(r'showmeta', ShowMetaViewSet)
router.register(r'perfil', UsuarioViewSet)
router.register(r'usuario', CriarUsuarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('applogin/', criar_usuario),
    path('api/login/', obtain_auth_token),
    path('api/', include(router.urls)),
]
