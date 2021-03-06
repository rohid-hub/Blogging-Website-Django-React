from django.contrib import admin
from django.urls import path, include
from frontend.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api/', include("blogs.api.urls"))
]
