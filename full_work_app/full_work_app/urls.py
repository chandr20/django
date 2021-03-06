"""full_work_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from restaurants.views import (
    RestaurantListview,
    RestaurantDetailedView,
    RestaurantCreateView )


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',TemplateView.as_view(template_name='home.html'),name='home'),
    url(r'^restaurants/', include('restaurants.urls',namespace='restaurants')),
    url(r'^u/', include('profiles.urls',namespace='profiles')),
    url(r'^menus/', include('menus.urls',namespace='menus')),
    url(r'^About/$',TemplateView.as_view(template_name='About.html'),name='about'),
    url(r'^Contact/$',TemplateView.as_view(template_name='contact.html'),name='contact'),
    url(r'^login/$',LoginView.as_view(),name='login')


]
