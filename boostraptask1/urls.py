"""boostraptask1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from testapp import views
from django.conf import settings
from django.conf.urls.static import static
from testapp import views as v1
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hom/',v1.home_view,name ='homepage'),
    path('testapp/',include('testapp.urls')),
    path('login/',auth_view.LoginView.as_view(template_name = 'testapp/login.html')),
    path('logout/',auth_view.LogoutView.as_view(template_name = 'testapp/success.html')),
    path('userreg/',v1.user_registration),

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
