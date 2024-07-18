from django.http import HttpResponse

def get_birds(request):
    return HttpResponse("Hello from Birds API")