"""Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from config.views import DashboardView
from core.homepage.views.homepage.views import IndexView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', include('core.login.urls')),
    path('Api/', include('core.inventario.urls')),
    path('Api/', include('core.facturacion.urls')),
    path('api/', include('core.notificaciones.urls')),
    path('personal/', include('core.personal.urls')),
    path('user/', include('core.user.urls')),
    path('electronicos/', include('core.electronicos.urls')),

    # home
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # Revista
    path('Revista/', include('core.Repositorio.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
