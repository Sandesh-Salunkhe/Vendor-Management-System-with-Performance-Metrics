from django.contrib import admin
from django.urls import path, include
from Metrics.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", admin.site.urls),
    path('', dashboard_view, name='dashboard'),
    path("api/", include('Metrics.urls')),
]
