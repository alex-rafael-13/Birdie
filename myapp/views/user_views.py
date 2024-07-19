from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import RegisterSerializer

def get_user(request):
    return HttpResponse("Hello from Users API")

class RegisterView(APIView):
    '''
        View to register a new User
    '''

    def post(self, request):
        # Call in register serialize
        serializer = RegisterSerializer(data=request.data)

        # If successful request data, save to database and return with 201 
        if serializer.is_valid():
            serializer.save()           
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Return 400 error if unsuccesful
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





