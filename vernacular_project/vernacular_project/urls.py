"""vernacular_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from myAppOne import views

urlpatterns = [
    path('', views.home_view, name='index'),
    path('admin/', admin.site.urls),
    path('roomform/', views.room_form_view, name='room_form'),
    path('roomrecord/', views.RoomRecordAPIView.as_view(), name='room_output'),
    path('ageform/', views.age_form_view, name='age_form'),
    path('agerecord/', views.AgeRecordAPIView.as_view(), name='age_output')
]
