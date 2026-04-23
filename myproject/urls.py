# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from api.views import health  # root -> health to avoid 404 on /

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", health, name="root_health"),
    path("api/", include("api.urls")),
]
