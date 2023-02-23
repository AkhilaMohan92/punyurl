"""urlshortner URL Configuration
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('punyurl/', include('punyurl.urls')),
    path('admin/', admin.site.urls),

]
