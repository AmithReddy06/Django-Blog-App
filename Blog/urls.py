
from django.contrib import admin
from django.urls import path, include
from .import views
from articles import views as articleviews
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf.urls import include, re_path
from . import views
from django.conf.urls.static import static # tells where media url is and where document root is 
from django.conf import settings




urlpatterns = [
    path('admin/',admin.site.urls),
    path('',articleviews.article_list,name="home"),
    path('accounts/',include('accounts.urls')), # any request to the 'accounts/' route will be handled by the URL configuration defined in the 'accounts.urls' module. 
    path('about/',views.about),
    path('articles/',include('articles.urls')),
    path('comments/',include('comments.urls',namespace='comments'))

    
    ]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
































"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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