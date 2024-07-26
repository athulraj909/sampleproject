"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('reg',views.registration,name='reg'),
    path('login',views.Login,name='login'),
    path('logout',views.logout,name='logout'),

    path('userhome',views.userhome,name='userhome'),
    path('userprofile',views.userprofile,name='userprofile'),
    path('useredit/<int:id>',views.useredit,name='useredit'),
    path('deposite',views.deposite,name='deposite'),
    path('withdraw',views.withdraw,name='withdraw'),
    path('userhistory',views.userhistory,name='userhistory'),


    path('bankhome',views.bankhome,name='bankhome'),
    path('bankprofileedit',views.bankprofileedit,name='bankprofileedit'),
    path('viewusers',views.viewusers,name='viewusers'),
    path('viewuserdetails/<int:id>',views.viewuserdetails,name='viewuserdetails'),
    path('bankuserhistory/<int:id>',views.bankuserhistory,name='bankuserhistory')
]

if settings.DEBUG:
    
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
