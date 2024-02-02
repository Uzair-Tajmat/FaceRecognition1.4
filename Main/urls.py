"""TYProject URL Configuration

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
from django.contrib import admin
from django.urls import path
from facexrec import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage, name='home'),
    path('home/registration/',views.SignUp,name='signup'),
    path('home/login/',views.Login,name='login'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('download/',views.download,name='download'),
    path('first/',views.first,name='first'),
    path('imageregister/',views.imageregister,name='imageregister'),
    path('TYCMA/',views.TYCMA,name='TYCMA'),
    path('studenttable/',views.student_table,name='studenttable'),
    path('mark/',views.mark,name='mark'),
    path('addAttendance/',views.addAttendance,name='addAttendance'),
    path('reportissue/',views.reportissue,name='reportissue'),
    path('downloadAttendance/',views.downloadAttendance,name='downloadAttendance'),
    path('Logout/',views.Logout,name='Logout'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    