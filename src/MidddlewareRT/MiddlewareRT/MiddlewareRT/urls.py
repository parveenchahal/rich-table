"""MiddlewareRT URL Configuration

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
from django.urls import path
from hello.views import myView
from richtable.views import homePage
from richtable.views import menuPage
from richtable.views import aboutPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sayHello/', myView),
    path('', homePage),
    path('menu', menuPage),
    path('about', aboutPage),
]
