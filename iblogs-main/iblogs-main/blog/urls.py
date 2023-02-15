"""iblogs URL Configuration

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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home, post, category, about, add_blog

from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('home/'), name='home'),
    path('home/', home),
    path('about/', about),  # add this line
    path('blog/<slug:url>', post),
    path('add_blog/', add_blog, name='add_blog'),
    path('category/<slug:url>', category)
]

# the rest of the file remains the same


