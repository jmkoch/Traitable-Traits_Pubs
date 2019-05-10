"""Traitable2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from Traits.views import TraitAutocomplete
from Pubs.views import CitekeyAutocomplete

urlpatterns = [
    path('admin/', admin.site.urls),
    url(
    	'trait-autocomplete/$',
    	TraitAutocomplete.as_view(create_field='name'),
    	name='trait-autocomplete',
    ),
    path('', include('Traits.urls')),
    url(
    	'citekey-autocomplete/$',
    	CitekeyAutocomplete.as_view(create_field='name'),
    	name='citekey-autocomplete',
    ),
]
