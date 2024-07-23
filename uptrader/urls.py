from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin - admin
    path('admin/', admin.site.urls),
    # path('', include('menu.urls')),
]
