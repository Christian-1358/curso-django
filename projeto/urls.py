
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# HTTP request handler <- HTTP response
def my_view(request):
    return HttpResponse("Teste")
    


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/',  my_view),
]
