"""main URL Configuration

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
from django.urls import path
from webapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('status/<int:pk>/', guestbook_view, name='guestbook_view'),
    path('status/add/', guestbook_create_view, name='guestbook_add'),
    path('guestbook/<int:pk>/edit/', guestbook_update_view, name='guestbook_update'),
    path('guestbook/<int:pk>/delete/', guestbook_delete_view, name='guestbook_delete'),
    # path('task/<str:description>/search/', guestbook_seacrh, name='guestbook_seacrh')
]

