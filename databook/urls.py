from django.contrib import admin
from django.urls import path, include   # ←, includeを追加

urlpatterns = [
    path('cms/', include('cms.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]