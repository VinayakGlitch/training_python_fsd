
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
# views
def user_detail(request):
    # return render(request, <filename>)
    # return HttpResponse("<h1>Hello ji</h            1>")
    return JsonResponse({"name":"rohan","age":45})


def homepage(request):
    return  HttpResponse("<h1>Welcome to my application</h1>")
urlpatterns = [
    path('', homepage),
    path('admin/', admin.site.urls),
    path('user/', user_detail)
    
]
