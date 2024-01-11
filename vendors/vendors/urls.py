from django.contrib import admin
from django.urls import path, include
from Metrics.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", admin.site.urls),
    path('', dashboard_view, name='dashboard'),
    path("api/", include('Metrics.urls')),
    path("access-token/",TokenObtainPairView.as_view(), name='jwt_token'),
    path("refresh-token",TokenRefreshView.as_view(), name='jwt_token'),
]
