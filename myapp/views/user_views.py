from django.http import HttpResponse

def get_user(request):
    return HttpResponse("Hello from Users API")