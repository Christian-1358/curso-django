
from django.contrib import admin
from django.urls import path, include




# HTTP request handler <- HTTP response


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
]