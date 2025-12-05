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
from basic.views import health
from basic.views import addStudent
from basic.views import addStudent_age_20, orderbyname
from basic.views import job1
from basic.views import job2
from basic.views import signUp
from basic.views import check
from basic.views import login,passwordchange,getallusers,home

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
    path('health/',health),
    path('add/',addStudent),
    path('addStudent_age_20/',addStudent_age_20),
    path('orderby/',orderbyname),
    path('job1/',job1),
    path('job2/',job2),
    path('signup/',signUp),
    path('check/',check),
    path('login/',login),
    path('passwordchange/',passwordchange),
    path('users/',getallusers),
    path('home/',home)

]
