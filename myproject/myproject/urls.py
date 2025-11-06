"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from basic.views import sample
from basic.views import jsonresponse
from basic.views import dynamicresponse
from basic.views import dynamicresponse1
from basic.views import add
from basic.views import sub
from basic.views import mult
from basic.views import div
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sai/',sample),
    path('mohan/',jsonresponse),
    path('teja/',dynamicresponse),
    path('salaar/',dynamicresponse1),
    path('m1/',add),
    path('m2/',sub),
    path('m3/',mult),
    path('m4/',div),
]
