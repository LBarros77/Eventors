from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # AllAuth
    path('accounts/', include('allauth.urls')),
    # System
    path('', include('system.urls')),
    # Flow
    path('app/', include('system.flow.urls'))
]
