from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at pools index")
