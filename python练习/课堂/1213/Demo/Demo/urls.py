"""Demo URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from Demo import settings
from Book import views#后加as可改名

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('book_detail/<int:id>', views.detail),
    path('text2',views.Test2View.as_view())
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
router = DefaultRouter()
router.register('books', views.Testview)#'参数'要网址http://127.0.0.1:8000/+参数
urlpatterns += router.urls
