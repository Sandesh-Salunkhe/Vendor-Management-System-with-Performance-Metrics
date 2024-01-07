from django.contrib import admin
from django.urls import path, include
from Metrics.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", admin.site.urls),
    path('', dashboard_view, name='dashboard'),
    path('faqs/', faqs_view, name='faqs'),
    path('about/', about_view, name='about'),
    path('login/', login_view, name='login'),
    path('sign-up/', signup_view, name='signup'),
    path("api/", include('Metrics.urls')),
]
