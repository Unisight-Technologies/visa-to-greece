"""Greece URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Greece_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Homepage.as_view(),name="index"),
    path('terms/', views.Terms.as_view(),name="terms"),
    path('disclaimer/', views.Disclaimer.as_view(),name="disclaimer"),
    path('privacy_policy/', views.Privacypolicy.as_view(),name="privacy_policy"),
    path('coming_soon/', views.Comingpage.as_view(),name="coming_soon"),\
    path('studentvisa/', views.Studentvisapage.as_view(),name="studentvisa"),
    path('aboutus/', views.Aboutuspage.as_view(),name="aboutus"),
    path('contactus/', views.Contactpage.as_view(),name="contactus"),
    path('workvisa/', views.Workvisapage.as_view(),name="workvisa"),
    path('goldenvisa/', views.Goldenvisapage.as_view(),name="golden_visa"),
    # path('shortvisa/', views.Shortvisapage.as_view(),name="shortvisa"),
    # path('longvisa/', views.Longvisapage.as_view(),name="longvisa"),
    # path('studentvisa/', views.Studentvisapage.as_view(),name="studentvisa"),
    # path('aboutus/', views.Aboutuspage.as_view(),name="aboutus"),
    # path('whyus/', views.Whyuspage.as_view(),name="whyus"),
    # path('contactus/', views.Contactpage.as_view(),name="contactus"),
    # path('coming_soon/', views.Comingpage.as_view(),name="coming_soon"),
    # path('terms/', views.Terms.as_view(),name="terms"),
    # path('disclaimer/', views.Disclaimer.as_view(),name="disclaimer"),
    # path('privacy_policy/', views.Privacypolicy.as_view(),name="privacy_policy"),
    # path('blogs/', views.Blog.as_view(), name="blogs"),
    # path('refresh/', views.refresh, name='refresh'),
]
