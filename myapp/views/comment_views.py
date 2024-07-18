from django.http import HttpResponse

def get_comments(request):
    return HttpResponse("Hello from Response API")

